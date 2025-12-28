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
VECTOR_SUBSAMPLE_THRESHOLD = 100
VECTOR_SUBSAMPLE_TARGET = 100


def filter_openfoam_output(output_bytes: bytes) -> str:
    """Filter out OpenFOAM welcome messages from command output.

    Args:
        output_bytes: Raw output from OpenFOAM command.

    Returns:
        Filtered output string with welcome messages removed.

    """
    output_str = output_bytes.decode("utf-8")
    lines = [
        line
        for line in output_str.split("\n")
        if "Welcome to" not in line
        and "Further Resources" not in line
        and "* " not in line
        and "Contributors" not in line
    ]
    return "\n".join(lines).strip()


def _set_docker_host_if_needed() -> None:
    """Set DOCKER_HOST environment variable if not already set (for Colima)."""
    if "DOCKER_HOST" not in os.environ:
        docker_sock = Path.home() / ".colima" / "default" / "docker.sock"
        if docker_sock.exists():
            os.environ["DOCKER_HOST"] = f"unix://{docker_sock}"
            logger.debug("DOCKER_HOST set to: %s", os.environ["DOCKER_HOST"])


def _is_docker_running() -> bool:
    """Check if Docker is currently running."""
    try:
        client = docker.from_env()
        client.ping()
    except docker.errors.DockerException:
        return False
    else:
        logger.info("Docker/Colima is already running")
        return True


def _start_colima() -> bool:
    """Start Colima on macOS."""
    colima_path = shutil.which("colima")
    if not colima_path:
        logger.error(
            "Colima not found. Please install Colima: brew install docker colima",
        )
        return False

    logger.info("Starting Colima...")
    try:
        # Check Colima status
        status_result = subprocess.run(  # noqa: S603
            [colima_path, "status"],
            check=False,
            capture_output=True,
            text=True,
        )

        if status_result.returncode != 0:
            # Colima is not running, start it
            subprocess.run(  # noqa: S603
                [colima_path, "start", "--cpu", "4", "--memory", "8"],
                check=True,
            )
            logger.info("Colima started successfully")

            # Set DOCKER_HOST for this session
            docker_sock = Path.home() / ".colima" / "default" / "docker.sock"
            os.environ["DOCKER_HOST"] = f"unix://{docker_sock}"
            logger.info("DOCKER_HOST set to: %s", os.environ["DOCKER_HOST"])
        else:
            logger.info("Colima is already running")
    except subprocess.CalledProcessError:
        logger.exception("Failed to start Colima")
        return False
    else:
        return True


def _start_docker_linux() -> bool:
    """Start Docker daemon on Linux."""
    logger.info("Starting Docker daemon...")
    try:
        subprocess.run(
            ["sudo", "systemctl", "start", "docker"],  # noqa: S607
            check=True,
            capture_output=True,
        )
        logger.info("Docker daemon started")
    except subprocess.CalledProcessError:
        logger.exception(
            "Failed to start Docker. Please start Docker manually: sudo systemctl start docker",
        )
        return False
    else:
        return True


def _wait_for_docker() -> bool:
    """Wait for Docker to become available."""
    logger.info("Waiting for Docker to start...")
    for i in range(DOCKER_STARTUP_TIMEOUT):
        if _check_docker_ping():
            logger.info("Docker started successfully!")
            return True
        if i % 5 == 0:
            logger.debug("Still waiting... (%s/%ss)", i, DOCKER_STARTUP_TIMEOUT)
        time.sleep(1)

    logger.error("Docker failed to start within timeout. Please start Docker manually.")
    return False


def _check_docker_ping() -> bool:
    """Check if Docker responds to ping."""
    try:
        client = docker.from_env()
        client.ping()
    except docker.errors.DockerException:
        return False
    else:
        return True


def start_docker() -> bool:
    """Start Docker (Colima) if not running.

    Returns:
        True if Docker is running or successfully started, False otherwise.

    """
    _set_docker_host_if_needed()

    if _is_docker_running():
        return True

    # Docker is not running, try to start it
    system = platform.system()

    if system == "Darwin":  # macOS
        if not _start_colima():
            return False
    elif system == "Linux":
        if not _start_docker_linux():
            return False
    elif system == "Windows":
        logger.error(
            "Windows is not supported. Please use Colima or Docker on Linux/macOS.",
        )
        return False
    else:
        logger.error("Unsupported platform: %s", system)
        return False

    return _wait_for_docker()


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
        logger.info("Using OpenFOAM image: %s", openfoam_image)
    except docker.errors.ImageNotFound:
        logger.info("Pulling OpenFOAM image: %s", openfoam_image)
        client.images.pull(openfoam_image)

    # Run Allmesh script (for circuit board cooling)
    logger.info("Running mesh generation (Allmesh-extrudeFromInternalFaces)...")
    try:
        output = client.containers.run(
            openfoam_image,
            command=(
                "/bin/bash -c 'source /opt/openfoam11/etc/bashrc && "
                "./Allmesh-extrudeFromInternalFaces'"
            ),
            volumes={str(case_dir.absolute()): {"bind": "/case", "mode": "rw"}},
            working_dir="/case",
            remove=True,
            stdout=True,
            stderr=True,
            entrypoint="",
        )
        if output:
            filtered_output = filter_openfoam_output(output)
            if filtered_output:
                logger.info("Mesh generation output:\n%s", filtered_output)
        logger.info("Mesh generation completed")
    except docker.errors.ContainerError as e:
        logger.exception("Mesh generation failed: %s", e.stderr.decode("utf-8"))
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
            entrypoint="",
        )
        if output:
            filtered_output = filter_openfoam_output(output)
            if filtered_output:
                logger.info("Solver output:\n%s", filtered_output)
        logger.info("Simulation completed")
    except docker.errors.ContainerError as e:
        logger.exception("Simulation failed: %s", e.stderr.decode("utf-8"))
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
        # For multiRegion cases, foamToVTK must be run for each region
        # First check if it's a multiRegion case
        system_dir = case_dir / "system"
        regions = [
            d.name
            for d in system_dir.iterdir()
            if d.is_dir() and d.name not in ["include"]
        ]

        if regions:
            # MultiRegion case - convert each region
            logger.info("Converting %s regions: %s", len(regions), ", ".join(regions))
            for region in regions:
                output = client.containers.run(
                    openfoam_image,
                    command=(
                        f"/bin/bash -c 'source /opt/openfoam11/etc/bashrc && "
                        f"foamToVTK -region {region}'"
                    ),
                    volumes={str(case_dir.absolute()): {"bind": "/case", "mode": "rw"}},
                    working_dir="/case",
                    remove=True,
                    stdout=True,
                    stderr=True,
                    entrypoint="",
                )
                if output:
                    output_str = output.decode("utf-8")
                    if "error" in output_str.lower() or "fatal" in output_str.lower():
                        logger.warning(
                            "VTK conversion for region %s:\n%s",
                            region,
                            output_str,
                        )
        else:
            # Single region case
            output = client.containers.run(
                openfoam_image,
                command="/bin/bash -c 'source /opt/openfoam11/etc/bashrc && foamToVTK'",
                volumes={str(case_dir.absolute()): {"bind": "/case", "mode": "rw"}},
                working_dir="/case",
                remove=True,
                stdout=True,
                stderr=True,
                entrypoint="",
            )
            if output:
                filtered_output = filter_openfoam_output(output)
                if filtered_output:
                    logger.info("VTK conversion output:\n%s", filtered_output)
        logger.info("VTK conversion completed")
    except docker.errors.ContainerError as e:
        logger.exception("VTK conversion failed: %s", e.stderr.decode("utf-8"))
        raise


def visualize_results(case_dir: Path) -> None:
    """Visualize OpenFOAM results using PyVista.

    Args:
        case_dir: Path to the OpenFOAM case directory.

    """
    vtk_dir = case_dir / "VTK"

    if not vtk_dir.exists():
        convert_to_vtk(case_dir)

    # Check for region directories directly in VTK folder (multiRegion case)
    region_dirs = [d for d in vtk_dir.iterdir() if d.is_dir()]

    if region_dirs and all(
        d.name in ["baffle3D", "fluid"]
        for d in region_dirs
        if not d.name.startswith(".")
    ):
        # MultiRegion case with region folders directly in VTK
        logger.info("Found %s regions to visualize", len(region_dirs))

        # Get VTK files from each region (latest time)
        region_time_dirs = []
        for region_dir in region_dirs:
            # Find latest time directory in each region
            time_files = sorted(region_dir.glob("case_*.vtk"))
            if time_files:
                # Use the region directory itself, we'll read files directly
                region_time_dirs.append(region_dir)

        if region_time_dirs:
            visualize_multiregion(region_time_dirs)
            visualize_cross_section(region_time_dirs)
        return

    # Find the latest time directory in VTK (old structure)
    vtk_folders = sorted([d for d in vtk_dir.iterdir() if d.is_dir()])
    if not vtk_folders:
        logger.warning("No VTK folders found")
        return

    latest_vtk = vtk_folders[-1]
    logger.info("Visualizing results from: %s", latest_vtk.name)

    # Find all region directories (multiRegion case)
    region_dirs = [d for d in latest_vtk.iterdir() if d.is_dir()]

    if region_dirs:
        # MultiRegion case - visualize all regions
        logger.info("Found %s regions to visualize", len(region_dirs))
        visualize_multiregion(region_dirs)
        visualize_cross_section(region_dirs)
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
            if (
                velocity_data.ndim == NUMPY_DIM_2D
                and velocity_data.shape[1] == NUMPY_DIM_3D
            ):
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
        logger.warning("Streamline generation failed: %s", e)


def _load_region_meshes(region_dirs: list[Path]) -> list[tuple[str, pv.Mesh]]:
    """Load all region meshes from VTK files."""
    all_meshes = []
    for region_dir in region_dirs:
        region_name = region_dir.name
        case_vtk_files = sorted(region_dir.glob("case_*.vtk"))
        if case_vtk_files:
            latest_vtk = case_vtk_files[-1]
            mesh = pv.read(str(latest_vtk))
            mesh["region"] = region_name
            all_meshes.append((region_name, mesh))
            logger.debug("Loaded %s: %s points", region_name, mesh.n_points)
    return all_meshes


def _find_baffle_center(all_meshes: list[tuple[str, pv.Mesh]]) -> float | None:
    """Find the X-coordinate of the baffle center."""
    for region_name, mesh in all_meshes:
        if "baffle" in region_name.lower():
            bounds = mesh.bounds
            return (bounds[0] + bounds[1]) / 2
    return None


def _add_fluid_slice(
    plotter: pv.Plotter,
    slice_mesh: pv.Mesh,
) -> None:
    """Add fluid region slice with temperature and velocity to plotter."""
    if "T" not in slice_mesh.array_names:
        return

    # Convert temperature to Celsius
    t_celsius = slice_mesh["T"] - 273.15
    slice_mesh["t_celsius"] = t_celsius

    # Add temperature contour (semi-transparent to see baffle behind)
    plotter.add_mesh(
        slice_mesh,
        scalars="t_celsius",
        cmap="hot",
        show_edges=False,
        opacity=0.7,  # Semi-transparent
        scalar_bar_args={
            "title": "Temperature (°C)",
            "vertical": True,
            "position_x": 0.85,
            "position_y": 0.1,
            "n_labels": 8,
            "fmt": "%.1f",
        },
    )

    # Add velocity vectors/streamlines on the slice
    if "U" in slice_mesh.array_names:
        _add_velocity_arrows(plotter, slice_mesh)


def _add_velocity_arrows(plotter: pv.Plotter, slice_mesh: pv.Mesh) -> None:
    """Add velocity arrows to the plotter."""
    # Subsample for cleaner vector display
    subsample = slice_mesh.extract_geometry()
    if subsample.n_points > VECTOR_SUBSAMPLE_THRESHOLD:
        # Reduce point density for vectors
        every_n = max(1, subsample.n_points // VECTOR_SUBSAMPLE_TARGET)
        indices = np.arange(0, subsample.n_points, every_n)
        subsample = subsample.extract_points(indices)

    # Add velocity vectors
    arrows = subsample.glyph(
        orient="U",
        scale=False,
        factor=0.005,
        geom=pv.Arrow(),
    )

    # Calculate velocity magnitude for arrows
    if arrows.n_points > 0:
        plotter.add_mesh(
            arrows,
            color="black",
            opacity=0.7,
        )


def _add_baffle_slice(
    plotter: pv.Plotter,
    slice_mesh: pv.Mesh,
) -> None:
    """Add baffle region slice to plotter."""
    if "T" not in slice_mesh.array_names:
        logger.warning("Baffle slice has no temperature data")
        return

    # Convert temperature to Celsius for baffle
    t_celsius = slice_mesh["T"] - 273.15
    slice_mesh["t_celsius"] = t_celsius

    logger.info(
        "Adding baffle slice: %d points, T range: %.1f to %.1f °C",
        slice_mesh.n_points,
        t_celsius.min(),
        t_celsius.max(),
    )

    # Add baffle with red fill and cyan edges for high visibility
    plotter.add_mesh(
        slice_mesh,
        color="red",
        show_edges=True,
        edge_color="cyan",
        line_width=10,
        opacity=1.0,
    )

    # Add points as yellow spheres for maximum visibility
    plotter.add_points(
        slice_mesh.points,
        color="yellow",
        point_size=15,
        render_points_as_spheres=True,
    )


def _setup_cross_section_view(
    plotter: pv.Plotter,
    x_center: float,
) -> None:
    """Set up camera and labels for cross-section view."""
    plotter.add_text(
        (
            f"YZ-Plane Cross-Section at X = {x_center:.4f} m (Baffle Center)\n"
            "Temperature: °C, Velocity: Arrows"
        ),
        font_size=12,
        position="upper_edge",
    )

    # Set camera to view YZ plane
    plotter.view_yz()
    plotter.camera.parallel_projection = True

    # Add axis labels for YZ plane view
    plotter.show_bounds(
        xtitle="Z (m)",  # Vertical axis
        ytitle="Y (m)",  # Horizontal axis
        ztitle="X (m)",  # Out of plane
        grid="back",
        location="outer",
        all_edges=True,
        font_size=12,
    )

    plotter.add_axes()


def visualize_cross_section(
    region_dirs: list[Path],
) -> None:
    """Visualize X-direction cross-section at baffle center.

    Shows temperature contour and velocity lines with isometric view.

    Args:
        region_dirs: List of region directories containing VTK files.

    """
    # Use multi-panel plotter: left = isometric, right = cross-section
    plotter = pv.Plotter(shape=(1, 2), window_size=[2000, 1000], off_screen=True)

    all_meshes = _load_region_meshes(region_dirs)
    if not all_meshes:
        logger.warning("No meshes found for cross-section visualization")
        return

    x_center = _find_baffle_center(all_meshes)
    if x_center is None:
        logger.warning("Baffle region not found for cross-section")
        return

    logger.info("Creating cross-section at X = %.4f m (baffle center)", x_center)

    # Left panel: Isometric view showing the cut plane location
    plotter.subplot(0, 0)
    plotter.add_text(
        "Isometric View\n(showing cut plane location)",
        font_size=12,
        position="upper_edge",
    )

    # Add semi-transparent geometry outlines
    for region_name, mesh in all_meshes:
        if "fluid" in region_name.lower():
            # Show fluid domain outline
            outline = mesh.extract_geometry().extract_surface()
            plotter.add_mesh(
                outline,
                color="lightblue",
                opacity=0.2,
                show_edges=True,
                edge_color="blue",
            )
        elif "baffle" in region_name.lower():
            # Show baffle location
            plotter.add_mesh(
                mesh,
                color="red",
                opacity=0.5,
            )

    # Add cutting plane visualization
    bounds = all_meshes[0][1].bounds
    y_range = [bounds[2], bounds[3]]
    z_range = [bounds[4], bounds[5]]

    # Create plane mesh at x_center
    plane = pv.Plane(
        center=[x_center, (y_range[0] + y_range[1]) / 2, (z_range[0] + z_range[1]) / 2],
        direction=[1, 0, 0],
        i_size=y_range[1] - y_range[0],
        j_size=z_range[1] - z_range[0],
    )
    plotter.add_mesh(
        plane,
        color="yellow",
        opacity=0.5,
        show_edges=True,
        edge_color="orange",
        line_width=3,
    )

    # Set isometric view
    plotter.view_isometric()
    plotter.add_axes()
    plotter.show_bounds(
        grid="back",
        location="outer",
        font_size=10,
    )

    # Right panel: Cross-section view
    plotter.subplot(0, 1)

    # Create slice at baffle center
    for region_name, mesh in all_meshes:
        slice_mesh = mesh.slice(normal="x", origin=[x_center, 0, 0])

        if slice_mesh.n_points == 0:
            continue

        if "fluid" in region_name.lower():
            _add_fluid_slice(plotter, slice_mesh)
        elif "baffle" in region_name.lower():
            _add_baffle_slice(plotter, slice_mesh)

    _setup_cross_section_view(plotter, x_center)

    # Save screenshot
    screenshot_path = Path.cwd() / "cross_section_yz.png"
    plotter.screenshot(str(screenshot_path))
    logger.info("Cross-section screenshot saved to: %s", screenshot_path)


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

    # Show cross-section view
    visualize_cross_section(list(region_dirs))


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
            temp_dir = Path(tempfile.mkdtemp(prefix="circuitboard_", dir=Path.home()))
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

    # Create temp directory in $HOME for Colima compatibility
    temp_dir = Path(tempfile.mkdtemp(prefix="circuitboard_", dir=Path.home()))
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


def _add_demo_geometry(
    plotter: pv.Plotter,
    bounds: tuple[float, float, float, float, float, float],
    x_center: float,
) -> None:
    """Add geometry to isometric view for demo."""
    x_min, x_max, y_min, y_max, z_min, z_max = bounds

    # Fluid domain box
    fluid_box = pv.Box(bounds=[x_min, x_max, y_min, y_max, z_min, z_max])
    plotter.add_mesh(
        fluid_box,
        color="lightblue",
        opacity=0.2,
        show_edges=True,
        edge_color="blue",
    )

    # Baffle
    baffle_thickness = 0.002
    baffle = pv.Box(
        bounds=[
            x_center - baffle_thickness / 2,
            x_center + baffle_thickness / 2,
            y_min + 0.01,
            y_max - 0.01,
            z_min,
            z_max,
        ],
    )
    plotter.add_mesh(baffle, color="red", opacity=0.5)

    # Cutting plane
    plane = pv.Plane(
        center=[x_center, (y_min + y_max) / 2, (z_min + z_max) / 2],
        direction=[1, 0, 0],
        i_size=y_max - y_min,
        j_size=z_max - z_min,
    )
    plotter.add_mesh(
        plane,
        color="yellow",
        opacity=0.5,
        show_edges=True,
        edge_color="orange",
        line_width=3,
    )


def _add_demo_cross_section(
    plotter: pv.Plotter,
    bounds: tuple[float, float, float, float, float, float],
    x_center: float,
) -> None:
    """Add cross-section to demo visualization."""
    _x_min, _x_max, y_min, y_max, z_min, z_max = bounds

    # Create temperature field mesh
    y_points, z_points = 50, 30
    y = np.linspace(y_min, y_max, y_points)
    z = np.linspace(z_min, z_max, z_points)
    y_grid, z_grid = np.meshgrid(y, z)
    x_grid = np.full_like(y_grid, x_center)

    # Temperature field (warmer near center)
    center_y = (y_min + y_max) / 2
    center_z = (z_min + z_max) / 2
    temperature = 20 + 30 * np.exp(-((y_grid - center_y) ** 2 + (z_grid - center_z) ** 2) / 0.001)

    # Create mesh
    points = np.c_[x_grid.ravel(), y_grid.ravel(), z_grid.ravel()]
    slice_mesh = pv.StructuredGrid()
    slice_mesh.points = points
    slice_mesh.dimensions = [1, y_points, z_points]
    slice_mesh["T_celsius"] = temperature.ravel()

    # Add temperature contour
    plotter.add_mesh(
        slice_mesh,
        scalars="T_celsius",
        cmap="hot",
        show_edges=False,
        opacity=0.7,
        scalar_bar_args={
            "title": "Temperature (°C)",
            "vertical": True,
            "position_x": 0.85,
            "position_y": 0.1,
            "n_labels": 8,
            "fmt": "%.1f",
        },
    )

    # Add baffle on cross-section
    baffle_y_min, baffle_y_max = y_min + 0.01, y_max - 0.01
    baffle_points = np.array(
        [
            [x_center, baffle_y_min, z_min],
            [x_center, baffle_y_max, z_min],
            [x_center, baffle_y_max, z_max],
            [x_center, baffle_y_min, z_max],
        ],
    )
    baffle_line = pv.PolyData(baffle_points)
    baffle_line.lines = np.array([4, 0, 1, 2, 3])

    plotter.add_mesh(baffle_line, color="red", line_width=10)
    plotter.add_points(baffle_points, color="yellow", point_size=15, render_points_as_spheres=True)


def create_demo_visualization(output_path: Path | None = None) -> Path:
    """Create a demo 2-panel visualization showing the concept.

    This creates a demonstration of the visualization layout without requiring
    actual OpenFOAM simulation data.

    Args:
        output_path: Path where to save the image. Defaults to cross_section_yz_demo.png

    Returns:
        Path to the saved image.

    """
    if output_path is None:
        output_path = Path.cwd() / "cross_section_yz_demo.png"

    logger.info("Creating demo visualization...")

    # Create 2-panel plotter
    plotter = pv.Plotter(shape=(1, 2), window_size=[2000, 1000], off_screen=True)

    # Define geometry bounds
    x_min, x_max = 0, 0.1
    y_min, y_max = 0, 0.05
    z_min, z_max = 0, 0.03
    x_center = (x_min + x_max) / 2
    bounds = (x_min, x_max, y_min, y_max, z_min, z_max)

    # LEFT PANEL: Isometric view
    plotter.subplot(0, 0)
    plotter.add_text(
        "Isometric View\n(showing cut plane location)",
        font_size=12,
        position="upper_edge",
    )
    _add_demo_geometry(plotter, bounds, x_center)
    plotter.view_isometric()
    plotter.add_axes()
    plotter.show_bounds(grid="back", location="outer", font_size=10)

    # RIGHT PANEL: Cross-section view
    plotter.subplot(0, 1)
    plotter.add_text(
        f"YZ-Plane Cross-Section at X = {x_center:.4f} m (Baffle Center)\n"
        "Temperature: °C, Velocity: Arrows",
        font_size=12,
        position="upper_edge",
    )
    _add_demo_cross_section(plotter, bounds, x_center)
    plotter.view_yz()
    plotter.camera.parallel_projection = True
    plotter.show_bounds(
        xtitle="Z (m)",
        ytitle="Y (m)",
        ztitle="X (m)",
        grid="back",
        location="outer",
        all_edges=True,
        font_size=12,
    )
    plotter.add_axes()

    # Save screenshot
    plotter.screenshot(str(output_path))
    logger.info("Demo visualization saved to: %s", output_path)

    return output_path


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
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Create demo visualization without running simulation",
    )

    args = parser.parse_args()

    # Handle demo mode
    if args.demo:
        logger.info("Running in demo mode...")
        create_demo_visualization()
        logger.info("Demo visualization completed!")
        return 0

    try:
        # Setup case directory
        logger.info("Setting up OpenFOAM case directory...")
        case_dir = setup_case(args.case_dir, openfoam_image=args.image)
        logger.info("Case directory: %s", case_dir)

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

    except (FileNotFoundError, RuntimeError, docker.errors.DockerException):
        logger.exception("Error occurred")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
