# circuitboardcooling

OpenFOAM circuitBoardCooling tutorial runner with Docker (via Colima) and PyVista visualization.

## Features

- Automatic extraction of OpenFOAM circuitBoardCooling tutorial from Docker image
- Run OpenFOAM multiRegion CHT simulations in Docker containers (no local OpenFOAM installation needed)
- Uses Colima as Docker runtime (free, open-source, no licensing issues)
- Visualize temperature/velocity fields with PyVista
- Package-based execution with Python Docker SDK

## Quick Start

### 1. Install Colima (one-time setup)

```bash
# Install Docker CLI and Colima
brew install docker colima

# Start Colima with appropriate resources
colima start --cpu 4 --memory 8
```

### 2. Set up environment

Add to your `~/.zshrc` (or `~/.bashrc`):

```bash
export DOCKER_HOST=unix://$HOME/.colima/default/docker.sock
```

Then reload:

```bash
source ~/.zshrc
```

### 3. Install the package

```bash
cd circuitboardcooling
uv pip install -e .
```

### 4. Run the simulation

```bash
# Run full simulation with visualization
uv run python -m circuitboardcooling

# Or using the installed command
circuitboardcooling
```

## Installation

### Colima Docker Runtime

**Important**: This package uses Colima instead of Docker Desktop to avoid licensing restrictions.

Colima is a free, open-source container runtime for macOS (and Linux):

- No licensing restrictions
- Compatible with Docker CLI and Python Docker SDK
- Lightweight and fast

```bash
# Install Docker CLI and Colima
brew install docker colima

# Start Colima
colima start --cpu 4 --memory 8

# Set Docker socket for Python SDK
export DOCKER_HOST=unix://$HOME/.colima/default/docker.sock

# Make it permanent (add to ~/.zshrc or ~/.bashrc)
echo 'export DOCKER_HOST=unix://$HOME/.colima/default/docker.sock' >> ~/.zshrc
```

### Python Package

```bash
cd circuitboardcooling
pip install -e .
```

Or with uv:

```bash
uv pip install -e .
```

## Requirements

### Runtime

- Colima (Docker runtime)
- Docker CLI

### Python Dependencies

- Python 3.8+
- docker (Python SDK for Docker API)
- pyvista (for 3D visualization)
- numpy

## Usage

**Important**: Make sure `DOCKER_HOST` environment variable is set before running.

### Basic Usage

Run with default settings (extracts tutorial from Docker):

```bash
export DOCKER_HOST=unix://$HOME/.colima/default/docker.sock
python -m circuitboardcooling

# or with uv
uv run python -m circuitboardcooling
```

### Command Options

Use existing case directory:

```bash
python -m circuitboardcooling --case-dir /path/to/case
```

Skip simulation and only visualize:

```bash
python -m circuitboardcooling --skip-run
```

Skip visualization (headless mode):

```bash
python -m circuitboardcooling --no-viz
```

Use specific Docker image:

```bash
python -m circuitboardcooling --image openfoam/openfoam11-paraview510
```

Get help:

```bash
circuitboardcooling --help
```

### Quick Commands Reference

```bash
# Colima management
colima start              # Start Colima
colima stop               # Stop Colima (to save resources)
colima status             # Check Colima status
colima delete             # Delete Colima VM (to start fresh)

# Run simulation
python -m circuitboardcooling                    # Full simulation + viz
python -m circuitboardcooling --skip-run         # Only visualization
python -m circuitboardcooling --no-viz           # Only simulation
```

## How It Works

1. **Setup**: Extracts the circuitBoardCooling tutorial from OpenFOAM Docker image
2. **Mesh Generation**: Runs Allmesh script (extrudeFromInternalFaces strategy)
3. **Simulation**: Executes chtMultiRegionFoam solver for conjugate heat transfer
4. **Conversion**: Converts OpenFOAM results to VTK format (all regions)
5. **Visualization**: Displays 3D temperature and velocity fields using PyVista

## Visualization Features

The PyVista visualization automatically detects multiRegion cases and provides:

### MultiRegion Layout (circuitBoardCooling)

- **Dual subplot view**:
  - Left: Temperature distribution across all regions
  - Right: Velocity field with streamlines (fluid regions)
- **All regions displayed**: Fluid and solid regions with different visualizations
- **Linked camera views**: Synchronized rotation and zoom
- **Interactive controls**:
  - Mouse drag: Rotate view
  - Mouse wheel: Zoom
  - Right-click drag: Pan
  - Press 's': Save screenshot
  - Press 'q': Quit

### Temperature Visualization

- Hot colormap (blue → red)
- All regions with temperature field shown
- Scalar bar with temperature range in Kelvin

### Velocity Visualization

- Coolwarm colormap
- Velocity magnitude field
- Streamlines showing flow patterns
- Solid regions shown as semi-transparent gray

### Single Region Support

Falls back to simple visualization for single-region cases.

## About the Tutorial

The circuitBoardCooling case is a multiRegion CHT (Conjugate Heat Transfer) tutorial that simulates:

- Heat transfer in electronic circuit boards
- Multiple solid and fluid regions
- Coupled heat conduction and convection

## Troubleshooting

### Docker connection error

```bash
# Make sure DOCKER_HOST is set
echo $DOCKER_HOST
# Should output: unix://$HOME/.colima/default/docker.sock

# Make sure Colima is running
colima status
```

### Platform warning (linux/amd64 on arm64)

This is expected on Apple Silicon Macs. Colima uses Rosetta 2 to run x86 images.

### Visualization doesn't show

Make sure you have a display available. For headless systems, use `--no-viz`.

## Package Structure

- Distribution name (for pip): `circuitboardcooling`
- Import name (in code): `circuitboardcooling`

```
circuitboardcooling/
├── README.md
├── pyproject.toml
└── circuitboardcooling/
    ├── __init__.py
    └── __main__.py
```

## Technical Details

### Implementation

- Uses Python Docker SDK (not CLI subprocess)
- Tutorial path: `/opt/openfoam11/tutorials/multiRegion/CHT/circuitBoardCooling`
- Workflow:
  1. Extract tutorial from Docker container
  2. Run `Allmesh-extrudeFromInternalFaces`
  3. Run `chtMultiRegionFoam` solver
  4. Convert to VTK with `-allRegions` flag
  5. Visualize with PyVista

### Why Colima?

1. **No Docker Desktop License Issues**: Free and open-source
2. **Clean Python Docker SDK API**: No subprocess management needed
3. **Lightweight**: Lower resource usage than Docker Desktop
4. **Compatible**: Works with standard Docker CLI and SDK

## License

OpenFOAM is licensed under GPL v3. Colima is licensed under MIT.
