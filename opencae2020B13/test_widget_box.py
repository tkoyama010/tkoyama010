import pyvista as pv
from pyvista import examples

mesh = examples.download_nefertiti()

p = pv.Plotter(notebook=False)
p.add_mesh_clip_box(mesh, color="white")
p.show()
