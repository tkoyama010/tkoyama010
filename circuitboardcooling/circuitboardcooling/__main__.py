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
DEFAULT_OPENFOAM_IMAGE = "openfoam/openfoam7-paraview56"
TUTORIAL_PATH = (
    "/opt/openfoam7/tutorials/heatTransfer/buoyantSimpleFoam/circuitBoardCooling"
)
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

    # Run blockMesh for mesh generation
    logger.info("Running blockMesh for mesh generation...")
    try:
        output = client.containers.run(
            openfoam_image,
            command=("/bin/bash -c 'source /opt/openfoam7/etc/bashrc && blockMesh'"),
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
                logger.info("blockMesh output:\n%s", filtered_output)
        logger.info("blockMesh completed")
    except docker.errors.ContainerError as e:
        logger.exception("blockMesh failed: %s", e.stderr.decode("utf-8"))
        raise

    # Run buoyantSimpleFoam solver
    logger.info("Running buoyantSimpleFoam solver...")
    try:
        output = client.containers.run(
            openfoam_image,
            command="/bin/bash -c 'source /opt/openfoam7/etc/bashrc && buoyantSimpleFoam'",
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
        # buoyantSimpleFoam is a single region case
        output = client.containers.run(
            openfoam_image,
            command="/bin/bash -c 'source /opt/openfoam7/etc/bashrc && foamToVTK'",
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

    Creates three visualizations similar to XSim tutorial:
    1. Mesh visualization
    2. Velocity (U) field
    3. Temperature (T) field

    Args:
        case_dir: Path to the OpenFOAM case directory.

    """
    vtk_dir = case_dir / "VTK"

    if not vtk_dir.exists():
        convert_to_vtk(case_dir)

    # Find VTK files - OpenFOAM 7 structure is different
    # Look for case_*.vtk files directly in VTK directory
    case_vtk_files = sorted(vtk_dir.glob("case_*.vtk"))

    if not case_vtk_files:
        logger.warning("No case VTK files found")
        return

    # Use the latest time (highest number)
    latest_vtk = case_vtk_files[-1]
    logger.info("Visualizing results from: %s", latest_vtk.name)

    mesh = pv.read(str(latest_vtk))
    logger.info("Loaded mesh with %d points and %d cells", mesh.n_points, mesh.n_cells)

    # Create output directory for images
    output_dir = Path.cwd()

    # 1. Visualize mesh
    visualize_mesh(mesh, output_dir / "mesh.png")

    # 2. Visualize velocity field
    visualize_velocity(mesh, output_dir / "velocity.png")

    # 3. Visualize temperature field
    visualize_temperature(mesh, output_dir / "temperature.png")

    logger.info("Visualization completed. Images saved to: %s", output_dir)


def visualize_mesh(mesh: pv.DataSet, output_path: Path) -> None:
    """Visualize mesh structure.

    Args:
        mesh: PyVista mesh dataset.
        output_path: Path to save the image.

    """
    plotter = pv.Plotter(off_screen=True, window_size=[1200, 900])

    # Enable parallel projection
    plotter.enable_parallel_projection()

    # Add mesh with edges
    plotter.add_mesh(
        mesh,
        color="white",
        show_edges=True,
        edge_color="black",
        line_width=1,
        opacity=1.0,
    )

    # Set default view
    plotter.view_isometric()

    # Add axes
    plotter.add_axes()
    plotter.show_bounds(
        grid="back",
        location="outer",
        font_size=10,
    )

    # Save
    plotter.screenshot(str(output_path))
    logger.info("Mesh visualization saved to: %s", output_path)


def visualize_velocity(mesh: pv.DataSet, output_path: Path) -> None:
    """Visualize velocity field.

    Args:
        mesh: PyVista mesh dataset.
        output_path: Path to save the image.

    """
    if "U" not in mesh.array_names:
        logger.warning("Velocity field 'U' not found in mesh")
        return

    plotter = pv.Plotter(off_screen=True, window_size=[1200, 900])

    # Enable parallel projection
    plotter.enable_parallel_projection()

    # Calculate velocity magnitude
    velocity_data = mesh["U"]
    if velocity_data.ndim == NUMPY_DIM_2D and velocity_data.shape[1] == NUMPY_DIM_3D:
        velocity_mag = np.linalg.norm(velocity_data, axis=1)
        mesh["velocity_magnitude"] = velocity_mag

        # Add mesh with velocity magnitude coloring
        plotter.add_mesh(
            mesh,
            scalars="velocity_magnitude",
            cmap="jet",
            show_edges=False,
            scalar_bar_args={
                "title": "Velocity [m/s]",
                "vertical": True,
                "position_x": 0.85,
                "position_y": 0.1,
            },
        )

        # Add velocity vectors (glyphs)
        # Subsample for clearer visualization
        if mesh.n_points > 200:
            every_n = max(1, mesh.n_points // 100)
            indices = np.arange(0, mesh.n_points, every_n)
            subsample = mesh.extract_points(indices)
        else:
            subsample = mesh

        # Scale factor for arrows
        max_vel = velocity_mag.max()
        if max_vel > 0:
            scale_factor = mesh.length * 0.05 / max_vel

            arrows = subsample.glyph(
                orient="U",
                scale="velocity_magnitude",
                factor=scale_factor,
                geom=pv.Arrow(),
            )

            plotter.add_mesh(
                arrows,
                color="black",
                opacity=0.6,
            )

    # Set XY plane view (top view)
    plotter.view_xy()

    # Add axes
    plotter.add_axes()
    plotter.show_bounds(
        grid="back",
        location="outer",
        font_size=10,
    )

    # Save
    plotter.screenshot(str(output_path))
    logger.info("Velocity visualization saved to: %s", output_path)


def visualize_temperature(mesh: pv.DataSet, output_path: Path) -> None:
    """Visualize temperature field.

    Args:
        mesh: PyVista mesh dataset.
        output_path: Path to save the image.

    """
    if "T" not in mesh.array_names:
        logger.warning("Temperature field 'T' not found in mesh")
        return

    plotter = pv.Plotter(off_screen=True, window_size=[1200, 900])

    # Convert temperature to Celsius
    t_kelvin = mesh["T"]
    t_celsius = t_kelvin - 273.15
    mesh["T_celsius"] = t_celsius

    # Add mesh with temperature coloring
    plotter.add_mesh(
        mesh,
        scalars="T_celsius",
        cmap="jet",
        show_edges=False,
        scalar_bar_args={
            "title": "Temperature [°C]",
            "vertical": True,
            "position_x": 0.85,
            "position_y": 0.1,
        },
    )

    # Set view
    plotter.camera_position = "iso"
    plotter.camera.azimuth = 45
    plotter.camera.elevation = 30

    # Add axes
    plotter.add_axes()
    plotter.show_bounds(
        grid="back",
        location="outer",
        font_size=10,
    )

    # Save
    plotter.screenshot(str(output_path))
    logger.info("Temperature visualization saved to: %s", output_path)


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
        # Prepare initial conditions for existing case
        _prepare_initial_conditions(case_dir)
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
            # Prepare initial conditions
            _prepare_initial_conditions(case_dir)
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
        # Get the tutorial path from the container (using OpenFOAM 7 path)
        tutorial_archive, _ = container.get_archive(
            TUTORIAL_PATH,
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

    # Prepare initial conditions: copy 0.orig to 0
    _prepare_initial_conditions(case_dir)

    return case_dir


def _prepare_initial_conditions(case_dir: Path) -> None:
    """Prepare initial conditions by copying 0.orig to 0 if needed.

    Args:
        case_dir: Path to the OpenFOAM case directory.

    """
    zero_orig = case_dir / "0.orig"
    zero_dir = case_dir / "0"

    # If 0 directory doesn't exist and 0.orig exists, copy it
    if not zero_dir.exists() and zero_orig.exists():
        logger.info("Copying initial conditions from 0.orig to 0...")
        shutil.copytree(zero_orig, zero_dir)
        logger.info("Initial conditions prepared")
    elif zero_dir.exists():
        logger.debug("0 directory already exists")
    else:
        logger.warning("Neither 0 nor 0.orig directory found")


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
        "--update-mesh-only",
        type=str,
        help="Update mesh.png only using existing VTK file (provide path to VTK file)",
    )
    parser.add_argument(
        "--update-velocity-only",
        type=str,
        help="Update velocity.png only using existing VTK file (provide path to VTK file)",
    )
    parser.add_argument(
        "--convert-vtk-only",
        type=str,
        help="Convert OpenFOAM results to VTK format only (provide path to case directory)",
    )

    args = parser.parse_args()

    try:
        # Update mesh image only
        if args.update_mesh_only:
            logger.info("Updating mesh.png from: %s", args.update_mesh_only)
            vtk_file = Path(args.update_mesh_only)
            if not vtk_file.exists():
                msg = f"VTK file not found: {vtk_file}"
                raise FileNotFoundError(msg)

            mesh = pv.read(str(vtk_file))
            output_path = Path(__file__).parent.parent / "mesh.png"
            visualize_mesh(mesh, output_path)
            logger.info("Mesh image updated successfully!")
            return 0

        # Update velocity image only
        if args.update_velocity_only:
            logger.info("Updating velocity.png from: %s", args.update_velocity_only)
            vtk_file = Path(args.update_velocity_only)
            if not vtk_file.exists():
                msg = f"VTK file not found: {vtk_file}"
                raise FileNotFoundError(msg)

            mesh = pv.read(str(vtk_file))
            output_path = Path(__file__).parent.parent / "velocity.png"
            visualize_velocity(mesh, output_path)
            logger.info("Velocity image updated successfully!")
            return 0

        # Convert to VTK only
        if args.convert_vtk_only:
            logger.info("Converting to VTK from: %s", args.convert_vtk_only)
            case_dir = Path(args.convert_vtk_only)
            if not case_dir.exists():
                msg = f"Case directory not found: {case_dir}"
                raise FileNotFoundError(msg)
            
            convert_to_vtk(case_dir)
            logger.info("VTK conversion completed successfully!")
            return 0

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
