import pyvista as pv
from pyvista import examples

pv.set_plot_theme("document")
mesh = examples.load_airplane()
plotter = pv.Plotter(off_screen=True)
plotter.add_mesh(
    mesh, color="tan", show_edges=True
)
plotter.show(
    screenshot="test_camera.png"
)
