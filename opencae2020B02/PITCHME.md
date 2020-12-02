[drag=100 100, drop=center]

# GetFEM Contribution 2020
## Tetsuo Koyama

---
[drag=20 20, drop=15 0]
![height=200](https://avatars3.githubusercontent.com/u/7513610?s=400&u=3a29937127b197c7181f08901441c800271b5ba0&v=4)

[drag=50 20, drop=35 0]
## Tetsuo Koyama

[drag=25 5, drop=15 20]
@fa[twitter] @fa[github] tkoyama010

[drag=15 5, drop=40 20]
![height=50](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=python&logoColor=white&color=2bbc8a)

[drag=15 5, drop=55 20]
![height=50](https://img.shields.io/badge/Code-C++-informational?style=flat&logo=c%2B%2B&logoColor=white&color=2bbc8a)

[drag=15 5, drop=70 20]
![height=50](https://img.shields.io/badge/Editors-Vim-informational?style=flat&logoColor=white&color=2bbc8a)

[drag=30 60, drop=5 30]
![height=1000](https://s2.booth.pm/11310e3f-8ea5-4a2e-921b-350dbd11b9c3/i/1304104/5bbe6711-286a-4071-98f8-7e31a3b77b48_base_resized.jpg)

[drag=30 60, drop=35 30]
![height=1000](https://s2.booth.pm/11310e3f-8ea5-4a2e-921b-350dbd11b9c3/i/1574241/bbb0e33d-9969-4282-9f2d-389a043ed863_base_resized.jpg)

[drag=30 60, drop=65 30]
![height=1000](https://s2.booth.pm/11310e3f-8ea5-4a2e-921b-350dbd11b9c3/i/1727985/518a6acb-ae4b-40a1-9a1c-2ae04e9497fc_base_resized.jpg)

---
[drag=100 20, drop=0 0]
## What is GetFEM?

[drag=45 70, drop=5 20, fit=0.3]
@code[python](opencae2020B02/demo_tripod.py)

[drag=20 10, drop=30 20]
![height=500](https://upload.wikimedia.org/wikipedia/commons/f/f8/Python_logo_and_wordmark.svg)

[drag=50 70, drop=50 20]
![height=500](https://getfem.readthedocs.io/ja/latest/_images/tripod.png)

---
# Cantilever problem

---
[drag=100 20, drop=0 0, set=align-center]
## Parameter

[drag=45 70, drop=5 20, set=align-left]
- Geometory Condition
$L=10mm$
- Boundary Condition
$P=1.0 N/mm^2$
- Material Condition
$E=10000 N/mm^2$, $\nu = 0.0$

[drag=50 70, drop=50 20]
![height=500](http://kentiku-kouzou.jp/kouzourikigaku/katamotitawami/1.png)

---
[drag=100 20, drop=0 0, set=align-center]
## Mesh generation

[drag=45 70, drop=5 20, set=align-left, fit=0.7]
```python
import getfem as gf
import numpy as np


L = 10.0
b = 1.0
h = 1.0

meshs = []
for case, x, y in zip(cases, xs, ys):
    X = np.arange(x + 1) * L / x
    Y = np.arange(y + 1) * h / y
    mesh = gf.Mesh("cartesian", X, Y)
```
[drag=50 70, drop=50 20]
![height=700](https://getfem-examples.readthedocs.io/en/latest/_images/cantilever_13_0.png)

---
[drag=100 20, drop=0 0, set=align-center]
## Definition of finite elements methods and integration method

[drag=45 70, drop=5 20, set=align-left, fit=0.7]
```python
fems = []
# fem_names is the array of finite element method name.
for fem_name in fem_names:
    fems.append(gf.Fem("FEM_PRODUCT(" + fem_name + "," + fem_name + ")"))

mfus = []
for mesh, fem in zip(meshs, fems):
    mfu = gf.MeshFem(mesh, 2)
    mfu.set_fem(fem)
    mfus.append(mfu)

ims = []
# im_names is the array of integral method name.
for im_name in im_names:
    ims.append(gf.Integ("IM_PRODUCT(" + im_name + ", " + method + ")"))

mims = []
for mesh, im in zip(meshs, ims):
    mim = gf.MeshIm(mesh, im)
    mims.append(mim)
```

---
[drag=100 20, drop=0 0, set=align-center]
## Model definition

[drag=45 70, drop=5 20, set=align-left, fit=0.7]
```python
mds = []
for mfu in mfus:
    md = gf.Model("real")
    md.add_fem_variable("u", mfu)
    mds.append(md)

E = 10000 # N/mm2
Nu = 0.0

for md in mds:
    md.add_initialized_data("E", E)
    md.add_initialized_data("Nu", Nu)
```

---
[drag=100 20, drop=0 0, set=align-center]
## Linearized elasticity bricks pstrain

[drag=45 70, drop=5 20, set=align-left, fit=0.7]
```python
for md, mim in zip(mds, mims):
    md.add_isotropic_linearized_elasticity_brick_pstrain(mim, "u", "E", "Nu")
```
---
[drag=100 20, drop=0 0, set=align-center]
## Boundary condition at the left and right side of the beam

[drag=45 70, drop=5 20, set=align-left, fit=0.7]
```python
for (md, mim, mfu, fem) in zip(mds, mims, mfus, fems):
    if fem.is_lagrange():
        md.add_Dirichlet_condition_with_simplification("u", LEFT_BOUND)
    else:
        md.add_Dirichlet_condition_with_multipliers(mim, "u", mfu, LEFT_BOUND)

F = 1.0 # N/mm2
for (md, mfu, mim) in zip(mds, mfus, mims):
    md.add_initialized_data("F", [0, F / (b * h)])
    md.add_source_term_brick(mim, "u", "F", RIGHT_BOUND)
```

---
[drag=100 20, drop=0 0, set=align-center]
## Model solve

[drag=45 70, drop=5 20, set=align-left, fit=0.7]
```python
for md in mds:
    md.solve()

for md, mfu, case in zip(mds, mfus, cases):
    u = md.variable("u")
```

---
[drag=50 20, drop=0 0, set=align-center]
### API of Exporting Mesh, MeshFem object to XML VTK format

[drag=45 40, drop=5 20, set=align-left, fit=0.7]
There are essentially four ways to view the result of GetFEM computations:
- Scilab, Octave or Matlab, with the interface. 
- The open-source Paraview or PyVista or any other Legacy VTK file viewer.
- The open-source OpenDX program.
- The open-source Gmsh program.
- **The open-source Paraview or PyVista or any other XML VTK file viewer.**

[drag=45 30, drop=5 60, set=align-left, fit=0.7]
```python
Mesh.export_to_vtu(self, string filename, ... [," ascii" ][," quality" ])
MeshFem.export_to_vtu(self, string filename, ... [," ascii" ][," quality" ])
Slice.export_to_vtu(self, string filename, ... [,’ ascii’ ][,’ quality’ ])
```
[drag=50 20, drop=50 0, set=align-center]
### What's New in GetFEM 5.4

[drag=45 40, drop=50 20, set=align-left, fit=0.7]
- The use of Python 3 instead of Python 2.7 by default
- Support for Lumped Mass Matrix
- Support for Houbolt method
