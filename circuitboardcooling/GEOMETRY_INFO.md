# Circuit Board Cooling - Geometry Information

## Overall Domain Dimensions

Based on the demo visualization code, the circuit board cooling model has the following dimensions:

### Main Domain (Fluid Region)
- **X direction (Length)**: 0.0 to 0.1 m (100 mm)
- **Y direction (Width)**: 0.0 to 0.05 m (50 mm)  
- **Z direction (Height)**: 0.0 to 0.03 m (30 mm)
- **Total Volume**: 100 mm × 50 mm × 30 mm = 150,000 mm³ (0.00015 m³)

### Coordinate System
- **X**: Main flow direction (inlet at X=0, outlet at X=0.1m)
- **Y**: Width direction (horizontal, perpendicular to flow)
- **Z**: Height direction (vertical, gravity direction)

## Internal Objects

### Baffle (Heat Transfer Plate)
- **Location**: Center of domain at X = 0.05 m (50 mm from inlet)
- **Thickness**: 0.002 m (2 mm)
- **Y extent**: 0.01 m to 0.04 m (10 mm margins on each side)
  - Width: 0.03 m (30 mm)
  - Margins from sides: 10 mm left, 10 mm right
- **Z extent**: 0.0 m to 0.03 m (full height, 30 mm)
- **Material**: Solid plate (acts as heat source/sink)

### Baffle Geometry Details
```
X position: 0.048 m to 0.052 m (center at 0.05 m)
Y position: 0.01 m to 0.04 m
Z position: 0.0 m to 0.03 m (bottom to top)

Baffle dimensions:
- Thickness (X): 2 mm
- Width (Y): 30 mm  
- Height (Z): 30 mm
```

## Flow Configuration

### Inlet
- **Location**: X = 0 m plane
- **Area**: 50 mm × 30 mm = 1500 mm²

### Outlet  
- **Location**: X = 0.1 m plane
- **Area**: 50 mm × 30 mm = 1500 mm²

### Flow Path
- Air enters at X = 0 (bottom)
- Flows upward through domain
- Encounters baffle at X = 0.05 m
- Splits around baffle (left and right)
- Recombines after baffle
- Exits at X = 0.1 m (top)

## Cross-Section View

The visualization shows a cross-section at X = 0.05 m (baffle center):

```
Z (mm)
 30 ┌─────────────────────────────────┐
    │                                 │
    │                                 │
 15 │          ┌─────────┐            │  <- Baffle
    │          │ Baffle  │            │     (red rectangle)
    │          └─────────┘            │
  0 └─────────────────────────────────┘
    0        10   20   30   40      50  Y (mm)
             ↑         ↑         ↑
         margin    baffle    margin
         (10mm)    (30mm)    (10mm)
```

## Scale Reference
- Total domain: About the size of a small electronic device
- Comparable to: Mobile phone dimensions
- Baffle: Similar to a small heat sink fin

## Visualization Cut Plane
- **Location**: YZ plane at X = 0.05 m
- **Purpose**: Shows temperature distribution and flow patterns around baffle
- **Shows**: How air flows around the obstacle and temperature gradients


## 3D Perspective View

```
        Z (Height, 30mm)
        ↑
        │
        │     ┌───────────────────────────────┐
        │    /│                              /│
        │   / │                             / │
        │  /  │        BAFFLE (2mm thick) /  │
        │ /   │        at X=50mm         /   │
        │/    │                         /    │
        └─────┼────────────────────────┼─────┼──→ X (Flow, 100mm)
             /│                       /     /
            / │                      /     /
           /  │                     /     /
          /   └────────────────────┘     /
         /                              /
        └──────────────────────────────┘
       Y (Width, 50mm)
```

## Dimensions Summary Table

| Component | X (mm) | Y (mm) | Z (mm) | Volume (mm³) |
|-----------|--------|--------|--------|--------------|
| **Fluid Domain** | 0 → 100 | 0 → 50 | 0 → 30 | 150,000 |
| **Baffle** | 48 → 52 (2mm thick) | 10 → 40 | 0 → 30 | 1,800 |
| **Left Gap** | - | 0 → 10 | - | - |
| **Right Gap** | - | 40 → 50 | - | - |

## Flow Characteristics

### Reynolds Number Estimation
- Hydraulic diameter: ~0.039 m
- Typical air velocity: ~0.5 m/s
- Air kinematic viscosity: ~1.5×10⁻⁵ m²/s
- **Re ≈ 1,300** (laminar to transitional flow)

### Flow Regions
1. **Inlet Region** (X: 0 → 40 mm)
   - Developing flow
   - Uniform temperature
   
2. **Baffle Region** (X: 40 → 60 mm)
   - Flow separation
   - Recirculation zones
   - Maximum heat transfer
   - Baffle center at X = 50 mm
   
3. **Outlet Region** (X: 60 → 100 mm)
   - Flow reattachment
   - Thermal wake
   - Exit development

## Heat Transfer Zones

### Hot Zone
- Baffle surface (red in visualization)
- Temperature: ~50°C (estimated)
- Acts as heat source

### Cool Zone  
- Inlet air (blue in visualization)
- Temperature: ~20°C (ambient)

### Mixed Zone
- Downstream of baffle
- Temperature gradient: 20°C → 35°C

## Mesh Resolution (Typical)

For CFD simulation:
- **Domain cells**: ~100,000 - 500,000 cells
- **Near baffle**: Refined mesh (0.5 - 1 mm cell size)
- **Bulk flow**: Coarser mesh (2 - 3 mm cell size)
- **Boundary layer**: 5-10 layers near baffle

## Physical Properties (Air at 20°C)

- **Density**: 1.204 kg/m³
- **Dynamic viscosity**: 1.825×10⁻⁵ Pa·s
- **Thermal conductivity**: 0.0257 W/(m·K)
- **Specific heat**: 1005 J/(kg·K)
- **Prandtl number**: 0.713

## Baffle Material (Typical Assumption)

- **Material**: Aluminum or Steel
- **Thermal conductivity**: 200-400 W/(m·K)
- **Density**: 2700-7800 kg/m³
- **Specific heat**: 900-500 J/(kg·K)

## Simulation Parameters

- **Solver**: buoyantPimpleFoam (conjugate heat transfer)
- **Turbulence model**: k-ε or laminar
- **Time stepping**: Transient or steady-state
- **Convergence**: Temperature and velocity residuals < 10⁻⁵

---

**Note**: These dimensions are based on the demo visualization code. Actual OpenFOAM tutorial 
geometry may vary slightly. For exact dimensions, refer to the OpenFOAM case files 
(blockMeshDict, STL files, or snappyHexMeshDict).

Last updated: 2025-12-28
