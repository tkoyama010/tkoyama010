#!/usr/bin/env python3
"""Run OpenFOAM circuitBoardCooling tutorial using Docker and visualize with PyVista."""

import os
import shutil
import tempfile
from pathlib import Path

import docker
import pyvista as pv


def run_openfoam_case(case_dir: Path, openfoam_image: str = "openfoam/openfoam11-paraview510"):
    """Run OpenFOAM case using Docker.
    
    Args:
        case_dir: Path to the OpenFOAM case directory
        openfoam_image: Docker image to use for running OpenFOAM
    """
    client = docker.from_env()
    
    print(f"Running OpenFOAM case in {case_dir}")
    print(f"Using Docker image: {openfoam_image}")
    
    # Pull the image if not available
    try:
        client.images.get(openfoam_image)
    except docker.errors.ImageNotFound:
        print(f"Pulling Docker image {openfoam_image}...")
        client.images.pull(openfoam_image)
    
    # Run Allmesh script (for circuit board cooling)
    print("\nRunning Allmesh...")
    container = client.containers.run(
        openfoam_image,
        command="bash -c './Allmesh-extrudeFromInternalFaces'",
        volumes={str(case_dir.absolute()): {"bind": "/case", "mode": "rw"}},
        working_dir="/case",
        remove=True,
        stdout=True,
        stderr=True,
    )
    print(container.decode())
    
    # Run chtMultiRegionFoam
    print("\nRunning chtMultiRegionFoam...")
    container = client.containers.run(
        openfoam_image,
        command="chtMultiRegionFoam",
        volumes={str(case_dir.absolute()): {"bind": "/case", "mode": "rw"}},
        working_dir="/case",
        remove=True,
        stdout=True,
        stderr=True,
    )
    print(container.decode())
    
    print("\nOpenFOAM simulation completed!")


def convert_to_vtk(case_dir: Path):
    """Convert OpenFOAM results to VTK format.
    
    Args:
        case_dir: Path to the OpenFOAM case directory
    """
    client = docker.from_env()
    openfoam_image = "openfoam/openfoam11-paraview510"
    
    print("\nConverting to VTK format...")
    container = client.containers.run(
        openfoam_image,
        command="bash -c 'foamToVTK -allRegions'",
        volumes={str(case_dir.absolute()): {"bind": "/case", "mode": "rw"}},
        working_dir="/case",
        remove=True,
        stdout=True,
        stderr=True,
    )
    print(container.decode())


def visualize_results(case_dir: Path):
    """Visualize OpenFOAM results using PyVista.
    
    Args:
        case_dir: Path to the OpenFOAM case directory
    """
    vtk_dir = case_dir / "VTK"
    
    if not vtk_dir.exists():
        print("VTK directory not found, converting results...")
        convert_to_vtk(case_dir)
    
    # Find the latest time directory in VTK
    vtk_folders = sorted([d for d in vtk_dir.iterdir() if d.is_dir()])
    if not vtk_folders:
        print("No VTK results found!")
        return
    
    latest_vtk = vtk_folders[-1]
    print(f"\nVisualizing results from time: {latest_vtk.name}")
    
    # Find all region directories (multiRegion case)
    region_dirs = [d for d in latest_vtk.iterdir() if d.is_dir()]
    
    if region_dirs:
        # MultiRegion case - visualize all regions
        print(f"Found {len(region_dirs)} regions:")
        for region_dir in region_dirs:
            print(f"  - {region_dir.name}")
        
        visualize_multiregion(latest_vtk, region_dirs)
    else:
        # Single region case
        visualize_single_region(latest_vtk)


def visualize_multiregion(vtk_dir: Path, region_dirs: list):
    """Visualize multiRegion case with all regions.
    
    Args:
        vtk_dir: Path to VTK time directory
        region_dirs: List of region directories
    """
    import numpy as np
    
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
            print(f"Loaded region: {region_name}")
            print(f"  Available fields: {mesh.array_names}")
    
    if not all_meshes:
        print("No mesh data found!")
        return
    
    # Left subplot: Temperature visualization
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
                    'title': 'Temperature (K)',
                    'vertical': True,
                    'position_x': 0.85,
                    'position_y': 0.1,
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
    plotter.camera_position = 'iso'
    
    # Right subplot: Velocity/Streamlines (if available)
    plotter.subplot(0, 1)
    plotter.add_text("Velocity Field", font_size=12)
    
    for region_name, mesh in all_meshes:
        if "U" in mesh.array_names:
            # Calculate velocity magnitude
            if mesh["U"].ndim == 2 and mesh["U"].shape[1] == 3:
                velocity_mag = np.linalg.norm(mesh["U"], axis=1)
                mesh["velocity_magnitude"] = velocity_mag
                
                plotter.add_mesh(
                    mesh,
                    scalars="velocity_magnitude",
                    cmap="coolwarm",
                    opacity=0.7,
                    show_edges=False,
                    scalar_bar_args={
                        'title': 'Velocity (m/s)',
                        'vertical': True,
                        'position_x': 0.85,
                        'position_y': 0.1,
                    },
                )
                
                # Add streamlines if possible
                try:
                    if mesh.n_points > 100:
                        # Create seed points for streamlines
                        bounds = mesh.bounds
                        seed = pv.Line(
                            [bounds[0], (bounds[2] + bounds[3])/2, (bounds[4] + bounds[5])/2],
                            [bounds[1], (bounds[2] + bounds[3])/2, (bounds[4] + bounds[5])/2],
                            resolution=20
                        )
                        streamlines = mesh.streamlines_from_source(
                            seed,
                            vectors="U",
                            max_time=100.0,
                        )
                        plotter.add_mesh(streamlines, color="black", line_width=2)
                except Exception as e:
                    print(f"Could not generate streamlines: {e}")
        else:
            # Show solid regions
            plotter.add_mesh(
                mesh,
                color="gray",
                opacity=0.3,
                show_edges=True,
            )
    
    plotter.add_axes()
    plotter.camera_position = 'iso'
    
    # Link cameras
    plotter.link_views()
    
    print("\nVisualization Controls:")
    print("  - Left: Temperature distribution")
    print("  - Right: Velocity field with streamlines")
    print("  - Mouse: Rotate, zoom, pan")
    print("  - 'q': Quit")
    print("  - 's': Screenshot")
    
    plotter.show()


def visualize_single_region(vtk_dir: Path):
    """Visualize single region case.
    
    Args:
        vtk_dir: Path to VTK time directory
    """
    # Find VTK files
    vtk_files = list(vtk_dir.glob("*.vtk"))
    if not vtk_files:
        print("No VTK files found!")
        return
    
    # Load the internal mesh
    internal_vtk = vtk_dir / "internal.vtk"
    if internal_vtk.exists():
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
        
        print("Displaying visualization (close window to continue)...")
        plotter.show()
    else:
        print(f"Internal mesh not found at {internal_vtk}")


def setup_case(tutorial_path: str = None, openfoam_image: str = "openfoam/openfoam11-paraview510") -> Path:
    """Set up the OpenFOAM case directory.
    
    Args:
        tutorial_path: Path to the tutorial case (if None, uses temp directory)
        openfoam_image: Docker image to use for extracting tutorial
    
    Returns:
        Path to the case directory
    """
    if tutorial_path:
        case_dir = Path(tutorial_path)
        if not case_dir.exists():
            raise FileNotFoundError(f"Tutorial path not found: {tutorial_path}")
        return case_dir
    
    # Copy from $FOAM_TUTORIALS if available
    foam_tutorials = os.environ.get("FOAM_TUTORIALS")
    if foam_tutorials:
        tutorial_src = Path(foam_tutorials) / "heatTransfer" / "buoyantSimpleFoam" / "circuitBoardCooling"
        if tutorial_src.exists():
            temp_dir = Path(tempfile.mkdtemp(prefix="circuitboard_"))
            case_dir = temp_dir / "circuitBoardCooling"
            print(f"Copying tutorial from {tutorial_src} to {case_dir}")
            shutil.copytree(tutorial_src, case_dir)
            return case_dir
    
    # Extract from Docker container
    print("Extracting tutorial from Docker container...")
    try:
        client = docker.from_env()
    except Exception as e:
        raise RuntimeError(
            "Docker is not available. Please install and start Docker:\n"
            "  macOS: https://docs.docker.com/desktop/install/mac-install/\n"
            "  Linux: https://docs.docker.com/engine/install/\n"
            "  Windows: https://docs.docker.com/desktop/install/windows-install/\n"
            f"Error: {e}"
        )
    
    # Pull the image if not available
    try:
        client.images.get(openfoam_image)
    except docker.errors.ImageNotFound:
        print(f"Pulling Docker image {openfoam_image}...")
        client.images.pull(openfoam_image)
    
    temp_dir = Path(tempfile.mkdtemp(prefix="circuitboard_"))
    case_dir = temp_dir / "circuitBoardCooling"
    
    # Create a container and copy the tutorial files
    container = client.containers.create(openfoam_image, command="bash")
    try:
        # Get the tutorial path from the container
        tutorial_archive, _ = container.get_archive(
            "/opt/openfoam11/tutorials/multiRegion/CHT/circuitBoardCooling"
        )
        
        # Extract the archive
        import tarfile
        import io
        
        tar_stream = io.BytesIO()
        for chunk in tutorial_archive:
            tar_stream.write(chunk)
        tar_stream.seek(0)
        
        with tarfile.open(fileobj=tar_stream) as tar:
            tar.extractall(temp_dir)
        
        print(f"Tutorial extracted to {case_dir}")
        
    finally:
        container.remove()
    
    return case_dir


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Run OpenFOAM circuitBoardCooling tutorial with Docker and visualize"
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
        default="openfoam/openfoam11-paraview510",
        help="Docker image to use (default: openfoam/openfoam11-paraview510)",
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
        
        print("\nDone!")
        
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
