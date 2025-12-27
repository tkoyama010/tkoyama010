#!/usr/bin/env python3
"""Run OpenFOAM circuitBoardCooling tutorial using Docker and visualize with PyVista."""

from __future__ import annotations

import argparse
import io
import os
import shutil
import sys
import tarfile
import tempfile
from pathlib import Path

import docker
import numpy as np
import pyvista as pv

# Constants
DEFAULT_OPENFOAM_IMAGE = "openfoam/openfoam11-paraview510"
NUMPY_DIM_2D = 2
NUMPY_DIM_3D = 3
MIN_STREAMLINE_POINTS = 100


def run_openfoam_case(
    case_dir: Path,
    openfoam_image: str = DEFAULT_OPENFOAM_IMAGE,
) -> None:
    """Run OpenFOAM case using Docker.

    Args:
        case_dir: Path to the OpenFOAM case directory.
        openfoam_image: Docker image to use for running OpenFOAM.

    """
    client = docker.from_env()

    # Pull the image if not available
    try:
        client.images.get(openfoam_image)
    except docker.errors.ImageNotFound:
        client.images.pull(openfoam_image)

    # Run Allmesh script (for circuit board cooling)
    client.containers.run(
        openfoam_image,
        command="bash -c './Allmesh-extrudeFromInternalFaces'",
        volumes={str(case_dir.absolute()): {"bind": "/case", "mode": "rw"}},
        working_dir="/case",
        remove=True,
        stdout=True,
        stderr=True,
    )

    # Run chtMultiRegionFoam
    client.containers.run(
        openfoam_image,
        command="chtMultiRegionFoam",
        volumes={str(case_dir.absolute()): {"bind": "/case", "mode": "rw"}},
        working_dir="/case",
        remove=True,
        stdout=True,
        stderr=True,
    )


def convert_to_vtk(case_dir: Path) -> None:
    """Convert OpenFOAM results to VTK format.

    Args:
        case_dir: Path to the OpenFOAM case directory.

    """
    client = docker.from_env()
    openfoam_image = DEFAULT_OPENFOAM_IMAGE

    client.containers.run(
        openfoam_image,
        command="bash -c 'foamToVTK -allRegions'",
        volumes={str(case_dir.absolute()): {"bind": "/case", "mode": "rw"}},
        working_dir="/case",
        remove=True,
        stdout=True,
        stderr=True,
    )


def visualize_results(case_dir: Path) -> None:
    """Visualize OpenFOAM results using PyVista.

    Args:
        case_dir: Path to the OpenFOAM case directory.

    """
    vtk_dir = case_dir / "VTK"

    if not vtk_dir.exists():
        convert_to_vtk(case_dir)

    # Find the latest time directory in VTK
    vtk_folders = sorted([d for d in vtk_dir.iterdir() if d.is_dir()])
    if not vtk_folders:
        return

    latest_vtk = vtk_folders[-1]

    # Find all region directories (multiRegion case)
    region_dirs = [d for d in latest_vtk.iterdir() if d.is_dir()]

    if region_dirs:
        # MultiRegion case - visualize all regions
        visualize_multiregion(region_dirs)
    else:
        # Single region case
        visualize_single_region(latest_vtk)


def _add_temperature_subplot(
    plotter: pv.Plotter,
    all_meshes: list[tuple[str, pv.DataSet]],
) -> None:
    """Add temperature subplot to plotter.

    Args:
        plotter: PyVista plotter instance.
        all_meshes: List of tuples containing region name and mesh.

    """
    plotter.subplot(0, 0)
    plotter.add_text("Temperature Distribution", font_size=12)

    for region_name, mesh in all_meshes:
        if "T" in mesh.array_names:
            plotter.add_mesh(
                mesh,
                scalars="T",
                cmap="hot",
                opacity=0.9,
                show_edges=False,
                scalar_bar_args={
                    "title": "Temperature (K)",
                    "vertical": True,
                    "position_x": 0.85,
                    "position_y": 0.1,
                },
            )
        else:
            # Show region without temperature field
            plotter.add_mesh(
                mesh,
                color="lightblue",
                opacity=0.5,
                show_edges=True,
                label=region_name,
            )

    plotter.add_axes()
    plotter.camera_position = "iso"


def _add_velocity_subplot(
    plotter: pv.Plotter,
    all_meshes: list[tuple[str, pv.DataSet]],
) -> None:
    """Add velocity subplot to plotter.

    Args:
        plotter: PyVista plotter instance.
        all_meshes: List of tuples containing region name and mesh.

    """
    plotter.subplot(0, 1)
    plotter.add_text("Velocity Field", font_size=12)

    for _region_name, mesh in all_meshes:
        if "U" in mesh.array_names:
            # Calculate velocity magnitude
            velocity_data = mesh["U"]
            if velocity_data.ndim == NUMPY_DIM_2D and velocity_data.shape[1] == NUMPY_DIM_3D:
                velocity_mag = np.linalg.norm(velocity_data, axis=1)
                mesh["velocity_magnitude"] = velocity_mag

                plotter.add_mesh(
                    mesh,
                    scalars="velocity_magnitude",
                    cmap="coolwarm",
                    opacity=0.7,
                    show_edges=False,
                    scalar_bar_args={
                        "title": "Velocity (m/s)",
                        "vertical": True,
                        "position_x": 0.85,
                        "position_y": 0.1,
                    },
                )

                # Add streamlines if possible
                if mesh.n_points > MIN_STREAMLINE_POINTS:
                    _add_streamlines(plotter, mesh)
        else:
            # Show solid regions
            plotter.add_mesh(
                mesh,
                color="gray",
                opacity=0.3,
                show_edges=True,
            )

    plotter.add_axes()
    plotter.camera_position = "iso"


def _add_streamlines(plotter: pv.Plotter, mesh: pv.DataSet) -> None:
    """Add streamlines to plotter.

    Args:
        plotter: PyVista plotter instance.
        mesh: Mesh data with velocity field.

    """
    try:
        # Create seed points for streamlines
        bounds = mesh.bounds
        seed = pv.Line(
            [
                bounds[0],
                (bounds[2] + bounds[3]) / 2,
                (bounds[4] + bounds[5]) / 2,
            ],
            [
                bounds[1],
                (bounds[2] + bounds[3]) / 2,
                (bounds[4] + bounds[5]) / 2,
            ],
            resolution=20,
        )
        streamlines = mesh.streamlines_from_source(
            seed,
            vectors="U",
            max_time=100.0,
        )
        plotter.add_mesh(streamlines, color="black", line_width=2)
    except (ValueError, RuntimeError, AttributeError) as e:
        # Streamline generation may fail for various reasons:
        # - Empty mesh or insufficient points
        # - Invalid vector field
        # - Numerical issues in integration
        sys.stderr.write(f"Streamline generation failed: {e}\n")


def visualize_multiregion(region_dirs: list[Path]) -> None:
    """Visualize multiRegion case with all regions.

    Args:
        region_dirs: List of region directories.

    """
    # Create plotter with multiple subplots
    plotter = pv.Plotter(shape=(1, 2), window_size=[1600, 800])

    all_meshes = []

    # Load all regions
    for region_dir in region_dirs:
        region_name = region_dir.name
        internal_vtk = region_dir / "internal.vtk"

        if internal_vtk.exists():
            mesh = pv.read(str(internal_vtk))
            mesh["region"] = region_name  # Tag with region name
            all_meshes.append((region_name, mesh))

    if not all_meshes:
        return

    # Left subplot: Temperature visualization
    _add_temperature_subplot(plotter, all_meshes)

    # Right subplot: Velocity/Streamlines (if available)
    _add_velocity_subplot(plotter, all_meshes)

    # Link cameras
    plotter.link_views()

    plotter.show()


def visualize_single_region(vtk_dir: Path) -> None:
    """Visualize single region case.

    Args:
        vtk_dir: Path to VTK time directory.

    """
    # Find VTK files
    vtk_files = list(vtk_dir.glob("*.vtk"))
    if not vtk_files:
        return

    # Load the internal mesh
    internal_vtk = vtk_dir / "internal.vtk"
    if not internal_vtk.exists():
        return

    mesh = pv.read(str(internal_vtk))

    # Create plotter
    plotter = pv.Plotter()

    # Check available fields
    if "T" in mesh.array_names:
        # Plot temperature field
        plotter.add_mesh(
            mesh,
            scalars="T",
            cmap="hot",
            opacity=0.8,
            show_edges=False,
        )
        plotter.add_scalar_bar(title="Temperature (K)")
    elif "U" in mesh.array_names:
        # Plot velocity magnitude
        plotter.add_mesh(
            mesh,
            scalars="U",
            cmap="viridis",
            opacity=0.8,
            show_edges=False,
        )
        plotter.add_scalar_bar(title="Velocity Magnitude (m/s)")
    else:
        # Just show the mesh
        plotter.add_mesh(mesh, show_edges=True)

    # Add boundary meshes if available
    for vtk_file in vtk_files:
        if vtk_file.name != "internal.vtk":
            boundary_mesh = pv.read(str(vtk_file))
            plotter.add_mesh(boundary_mesh, color="lightgray", opacity=0.3)

    plotter.add_axes()
    plotter.show_grid()
    plotter.camera_position = "iso"

    plotter.show()


def setup_case(
    tutorial_path: str | None = None,
    openfoam_image: str = DEFAULT_OPENFOAM_IMAGE,
) -> Path:
    """Set up the OpenFOAM case directory.

    Args:
        tutorial_path: Path to the tutorial case (if None, uses temp directory).
        openfoam_image: Docker image to use for extracting tutorial.

    Returns:
        Path to the case directory.

    """
    if tutorial_path:
        case_dir = Path(tutorial_path)
        if not case_dir.exists():
            msg = f"Tutorial path not found: {tutorial_path}"
            raise FileNotFoundError(msg)
        return case_dir

    # Copy from $FOAM_TUTORIALS if available
    foam_tutorials = os.environ.get("FOAM_TUTORIALS")
    if foam_tutorials:
        tutorial_src = (
            Path(foam_tutorials)
            / "heatTransfer"
            / "buoyantSimpleFoam"
            / "circuitBoardCooling"
        )
        if tutorial_src.exists():
            temp_dir = Path(tempfile.mkdtemp(prefix="circuitboard_"))
            case_dir = temp_dir / "circuitBoardCooling"
            shutil.copytree(tutorial_src, case_dir)
            return case_dir

    # Extract from Docker container
    try:
        client = docker.from_env()
    except Exception as e:
        msg = (
            "Docker is not available. Please install and start Docker:\n"
            "  macOS: https://docs.docker.com/desktop/install/mac-install/\n"
            "  Linux: https://docs.docker.com/engine/install/\n"
            "  Windows: https://docs.docker.com/desktop/install/windows-install/\n"
            f"Error: {e}"
        )
        raise RuntimeError(msg) from e

    # Pull the image if not available
    try:
        client.images.get(openfoam_image)
    except docker.errors.ImageNotFound:
        client.images.pull(openfoam_image)

    temp_dir = Path(tempfile.mkdtemp(prefix="circuitboard_"))
    case_dir = temp_dir / "circuitBoardCooling"

    # Create a container and copy the tutorial files
    container = client.containers.create(openfoam_image, command="bash")
    try:
        # Get the tutorial path from the container
        tutorial_archive, _ = container.get_archive(
            "/opt/openfoam11/tutorials/multiRegion/CHT/circuitBoardCooling",
        )

        # Extract the archive
        tar_stream = io.BytesIO()
        for chunk in tutorial_archive:
            tar_stream.write(chunk)
        tar_stream.seek(0)

        with tarfile.open(fileobj=tar_stream) as tar:
            tar.extractall(temp_dir, filter="data")

    finally:
        container.remove()

    return case_dir


def main() -> int:
    """Run the circuitBoardCooling simulation and visualization."""
    parser = argparse.ArgumentParser(
        description="Run OpenFOAM circuitBoardCooling tutorial with Docker and visualize",
    )
    parser.add_argument(
        "--case-dir",
        type=str,
        help="Path to OpenFOAM case directory (default: uses $FOAM_TUTORIALS)",
    )
    parser.add_argument(
        "--skip-run",
        action="store_true",
        help="Skip running simulation, only visualize existing results",
    )
    parser.add_argument(
        "--no-viz",
        action="store_true",
        help="Skip visualization after running simulation",
    )
    parser.add_argument(
        "--image",
        type=str,
        default=DEFAULT_OPENFOAM_IMAGE,
        help=f"Docker image to use (default: {DEFAULT_OPENFOAM_IMAGE})",
    )

    args = parser.parse_args()

    try:
        # Setup case directory
        case_dir = setup_case(args.case_dir, openfoam_image=args.image)

        # Run simulation
        if not args.skip_run:
            run_openfoam_case(case_dir, openfoam_image=args.image)

        # Visualize results
        if not args.no_viz:
            visualize_results(case_dir)

    except (FileNotFoundError, RuntimeError, docker.errors.DockerException) as e:
        sys.stderr.write(f"Error: {e}\n")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
if __name__ == "__main__":
    sys.exit(main())
