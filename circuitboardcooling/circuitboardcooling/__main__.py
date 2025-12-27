#!/usr/bin/env python3
"""Run OpenFOAM circuitBoardCooling tutorial using Docker and visualize with PyVista."""

from __future__ import annotations

import argparse
import io
import logging
import os
import platform
import shutil
import subprocess
import sys
import tarfile
import tempfile
import time
from pathlib import Path

import docker
import numpy as np
import pyvista as pv

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger(__name__)

# Constants
DEFAULT_OPENFOAM_IMAGE = "openfoam/openfoam11-paraview510"
NUMPY_DIM_2D = 2
NUMPY_DIM_3D = 3
MIN_STREAMLINE_POINTS = 100
DOCKER_STARTUP_TIMEOUT = 60


def start_docker() -> bool:
    """Start Docker (Colima) if not running.

    Returns:
        True if Docker is running or successfully started, False otherwise.

    """
    # Set DOCKER_HOST if not already set (for Colima)
    if "DOCKER_HOST" not in os.environ:
        docker_sock = Path.home() / ".colima" / "default" / "docker.sock"
        if docker_sock.exists():
            os.environ["DOCKER_HOST"] = f"unix://{docker_sock}"
            logger.debug(f"DOCKER_HOST set to: {os.environ['DOCKER_HOST']}")
    
    try:
        client = docker.from_env()
        client.ping()
        logger.info("Docker/Colima is already running")
        return True
    except Exception:
        pass

    # Docker is not running, try to start it
    system = platform.system()
    
    if system == "Darwin":  # macOS
        # Check if Colima is installed
        colima_check = subprocess.run(["which", "colima"], capture_output=True)
        if colima_check.returncode == 0:
            # Use Colima (preferred for licensing reasons)
            logger.info("Starting Colima...")
            try:
                # Check Colima status
                status_result = subprocess.run(
                    ["colima", "status"],
                    capture_output=True,
                    text=True,
                )
                
                if status_result.returncode != 0:
                    # Colima is not running, start it
                    subprocess.run(
                        ["colima", "start", "--cpu", "4", "--memory", "8"],
                        check=True,
                    )
                    logger.info("Colima started successfully")
                    
                    # Set DOCKER_HOST for this session
                    docker_sock = Path.home() / ".colima" / "default" / "docker.sock"
                    os.environ["DOCKER_HOST"] = f"unix://{docker_sock}"
                    logger.info(f"DOCKER_HOST set to: {os.environ['DOCKER_HOST']}")
                else:
                    logger.info("Colima is already running")
                    
            except subprocess.CalledProcessError as e:
                logger.error(f"Failed to start Colima: {e}")
                return False
        else:
            # Colima not installed
            logger.error(
                "Colima not found. Please install Colima: "
                "brew install docker colima"
            )
            return False
        
    elif system == "Linux":
        logger.info("Starting Docker daemon...")
        try:
            subprocess.run(["sudo", "systemctl", "start", "docker"], check=True, capture_output=True)
            logger.info("Docker daemon started")
        except subprocess.CalledProcessError:
            logger.error(
                "Failed to start Docker. Please start Docker manually: "
                "sudo systemctl start docker"
            )
            return False
            
    elif system == "Windows":
        logger.error(
            "Windows is not supported. Please use Colima or Docker on Linux/macOS."
        )
        return False
    else:
        logger.error(f"Unsupported platform: {system}")
        return False

    # Wait for Docker to start
    logger.info("Waiting for Docker to start...")
    for i in range(DOCKER_STARTUP_TIMEOUT):
        try:
            client = docker.from_env()
            client.ping()
            logger.info("Docker started successfully!")
            return True
        except Exception:
            if i % 5 == 0:
                logger.debug(f"Still waiting... ({i}/{DOCKER_STARTUP_TIMEOUT}s)")
            time.sleep(1)
    
    logger.error("Docker failed to start within timeout. Please start Docker manually.")
    return False


def run_openfoam_case(
    case_dir: Path,
    openfoam_image: str = DEFAULT_OPENFOAM_IMAGE,
) -> None:
    """Run OpenFOAM case using Docker.

    Args:
        case_dir: Path to the OpenFOAM case directory.
        openfoam_image: Docker image to use for running OpenFOAM.

    """
    if not start_docker():
        msg = "Docker is not available and could not be started automatically."
        raise RuntimeError(msg)
    
    client = docker.from_env()

    # Pull the image if not available
    try:
        client.images.get(openfoam_image)
        logger.info(f"Using OpenFOAM image: {openfoam_image}")
    except docker.errors.ImageNotFound:
        logger.info(f"Pulling OpenFOAM image: {openfoam_image}")
        client.images.pull(openfoam_image)

    # Run Allmesh script (for circuit board cooling)
    logger.info("Running mesh generation (Allmesh-extrudeFromInternalFaces)...")
    try:
        output = client.containers.run(
            openfoam_image,
            command="/bin/bash -c 'source /opt/openfoam11/etc/bashrc && ./Allmesh-extrudeFromInternalFaces'",
            volumes={str(case_dir.absolute()): {"bind": "/case", "mode": "rw"}},
            working_dir="/case",
            remove=True,
            stdout=True,
            stderr=True,
        )
        if output:
            output_str = output.decode('utf-8')
            # Filter out welcome message
            lines = [l for l in output_str.split('\n') if 'Welcome to' not in l and 'Further Resources' not in l and '* ' not in l and 'Contributors' not in l]
            filtered_output = '\n'.join(lines).strip()
            if filtered_output:
                logger.info(f"Mesh generation output:\n{filtered_output}")
        logger.info("Mesh generation completed")
    except docker.errors.ContainerError as e:
        logger.error(f"Mesh generation failed: {e.stderr.decode('utf-8')}")
        raise

    # Run chtMultiRegionFoam
    logger.info("Running chtMultiRegionFoam solver...")
    try:
        output = client.containers.run(
            openfoam_image,
            command="/bin/bash -c 'source /opt/openfoam11/etc/bashrc && chtMultiRegionFoam'",
            volumes={str(case_dir.absolute()): {"bind": "/case", "mode": "rw"}},
            working_dir="/case",
            remove=True,
            stdout=True,
            stderr=True,
        )
        if output:
            output_str = output.decode('utf-8')
            lines = [l for l in output_str.split('\n') if 'Welcome to' not in l and 'Further Resources' not in l and '* ' not in l and 'Contributors' not in l]
            filtered_output = '\n'.join(lines).strip()
            if filtered_output:
                logger.info(f"Solver output:\n{filtered_output}")
        logger.info("Simulation completed")
    except docker.errors.ContainerError as e:
        logger.error(f"Simulation failed: {e.stderr.decode('utf-8')}")
        raise


def convert_to_vtk(case_dir: Path) -> None:
    """Convert OpenFOAM results to VTK format.

    Args:
        case_dir: Path to the OpenFOAM case directory.

    """
    if not start_docker():
        msg = "Docker is not available and could not be started automatically."
        raise RuntimeError(msg)
    
    client = docker.from_env()
    openfoam_image = DEFAULT_OPENFOAM_IMAGE

    logger.info("Converting OpenFOAM results to VTK format...")
    try:
        output = client.containers.run(
            openfoam_image,
            command="/bin/bash -c 'source /opt/openfoam11/etc/bashrc && foamToVTK -allRegions'",
            volumes={str(case_dir.absolute()): {"bind": "/case", "mode": "rw"}},
            working_dir="/case",
            remove=True,
            stdout=True,
            stderr=True,
        )
        if output:
            output_str = output.decode('utf-8')
            lines = [l for l in output_str.split('\n') if 'Welcome to' not in l and 'Further Resources' not in l and '* ' not in l and 'Contributors' not in l]
            filtered_output = '\n'.join(lines).strip()
            if filtered_output:
                logger.info(f"VTK conversion output:\n{filtered_output}")
        logger.info("VTK conversion completed")
    except docker.errors.ContainerError as e:
        logger.error(f"VTK conversion failed: {e.stderr.decode('utf-8')}")
        raise


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
        logger.warning("No VTK folders found")
        return

    latest_vtk = vtk_folders[-1]
    logger.info(f"Visualizing results from: {latest_vtk.name}")

    # Find all region directories (multiRegion case)
    region_dirs = [d for d in latest_vtk.iterdir() if d.is_dir()]

    if region_dirs:
        # MultiRegion case - visualize all regions
        logger.info(f"Found {len(region_dirs)} regions to visualize")
        visualize_multiregion(region_dirs)
    else:
        # Single region case
        logger.info("Visualizing single region case")
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
    plotter.camera.parallel_projection = True


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
            if (
                velocity_data.ndim == NUMPY_DIM_2D
                and velocity_data.shape[1] == NUMPY_DIM_3D
            ):
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
    plotter.camera.parallel_projection = True


def _add_streamlines(plotter: pv.Plotter, mesh: pv.DataSet) -> None:
    """Add streamlines to plotter.

    Args:
        plotter: PyVista plotter instance.
        mesh: Mesh data with velocity field.

    """
    try:
        bounds = mesh.bounds
        x_mid = (bounds[0] + bounds[1]) / 2
        y_range = bounds[3] - bounds[2]
        z_range = bounds[5] - bounds[4]
        
        # Create multiple seed points for better flow visualization
        seed_points = []
        n_seeds = 15
        
        # Create seeds along the inlet (x-direction)
        for i in range(n_seeds):
            y_pos = bounds[2] + (i + 1) * y_range / (n_seeds + 1)
            for j in range(n_seeds):
                z_pos = bounds[4] + (j + 1) * z_range / (n_seeds + 1)
                seed_points.append([bounds[0], y_pos, z_pos])
        
        # Also add seeds in the middle of the domain
        for i in range(n_seeds // 2):
            y_pos = bounds[2] + (i + 1) * y_range / (n_seeds // 2 + 1)
            for j in range(n_seeds // 2):
                z_pos = bounds[4] + (j + 1) * z_range / (n_seeds // 2 + 1)
                seed_points.append([x_mid, y_pos, z_pos])
        
        seed = pv.PolyData(np.array(seed_points))
        
        streamlines = mesh.streamlines_from_source(
            seed,
            vectors="U",
            max_time=200.0,
            integration_direction="forward",
        )
        
        if streamlines.n_points > 0:
            # Calculate velocity magnitude for coloring streamlines
            velocity_data = streamlines["U"]
            if velocity_data.ndim == NUMPY_DIM_2D and velocity_data.shape[1] == NUMPY_DIM_3D:
                velocity_mag = np.linalg.norm(velocity_data, axis=1)
                streamlines["velocity_magnitude"] = velocity_mag
                
                plotter.add_mesh(
                    streamlines,
                    scalars="velocity_magnitude",
                    cmap="jet",
                    line_width=3,
                    render_lines_as_tubes=True,
                    opacity=0.8,
                )
    except (ValueError, RuntimeError, AttributeError) as e:
        logger.warning(f"Streamline generation failed: {e}")


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
    plotter.camera.parallel_projection = True

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
    if not start_docker():
        msg = "Docker is not available and could not be started automatically."
        raise RuntimeError(msg)
    
    client = docker.from_env()

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
        logger.info("Setting up OpenFOAM case directory...")
        case_dir = setup_case(args.case_dir, openfoam_image=args.image)
        logger.info(f"Case directory: {case_dir}")

        # Run simulation
        if not args.skip_run:
            logger.info("Starting OpenFOAM simulation...")
            run_openfoam_case(case_dir, openfoam_image=args.image)
        else:
            logger.info("Skipping simulation (--skip-run)")

        # Visualize results
        if not args.no_viz:
            logger.info("Preparing visualization...")
            visualize_results(case_dir)
        else:
            logger.info("Skipping visualization (--no-viz)")

        logger.info("All tasks completed successfully!")

    except (FileNotFoundError, RuntimeError, docker.errors.DockerException) as e:
        logger.error(f"Error: {e}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
if __name__ == "__main__":
    sys.exit(main())
