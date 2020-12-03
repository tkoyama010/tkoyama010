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

[drag=45 10, drop=5 20]
### Structure of library

[drag=45 60, drop=5 30]
![height=500](https://getfem.readthedocs.io/en/latest/_images/getfem_structure1.png)

[drag=50 10, drop=50 20]
### Screenshot of example

[drag=50 60, drop=50 30]
![height=500](https://getfem.readthedocs.io/ja/latest/_images/tripod.png)

---
## Cantilever problem

---
[drag=100 20, drop=0 0, set=align-center]
### Parameter of cantilever problem

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
### Mesh generation

[drag=45 70, drop=5 20, set=align-left, fit=0.7]
@code[python](opencae2020B02/mesh_generation.py)

[drag=50 70, drop=50 20]
![height=700](https://getfem-examples.readthedocs.io/en/latest/_images/cantilever_13_0.png)

---
[drag=100 20, drop=0 0, set=align-center]
### Definition of finite elements methods

[drag=45 70, drop=5 20, set=align-left, fit=0.7]
@code[python](opencae2020B02/definition_of_finite_elements_methods.py)

---
[drag=100 20, drop=0 0, set=align-center]
### Definition of integration method

[drag=45 70, drop=5 20, set=align-left, fit=0.7]
@code[python](opencae2020B02/definition_of_integration_methods.py)

---
[drag=100 20, drop=0 0, set=align-center]
### Model definition

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
### Linearized elasticity bricks pstrain

[drag=45 70, drop=5 20, set=align-left, fit=0.7]
```python
for md, mim in zip(mds, mims):
    md.add_isotropic_linearized_elasticity_brick_pstrain(mim, "u", "E", "Nu")
```
---
[drag=100 20, drop=0 0, set=align-center]
### Boundary condition at the left and right side of the beam

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
### Model solve

[drag=45 70, drop=5 20, set=align-left, fit=0.7]
```python
for md in mds:
    md.solve()

for md, mfu, case in zip(mds, mfus, cases):
    u = md.variable("u")
```
