import pyvista as pv
from pyvista import examples

pv.set_plot_theme("document")
plotter = pv.Plotter(shape=(2, 2))

plotter.subplot(0, 0)
plotter.add_text("Render Window 0", font_size=15)
plotter.add_mesh(examples.load_globe())

plotter.subplot(0, 1)
plotter.add_text("Render Window 1", font_size=15)
plotter.add_mesh(
    pv.Cube(),
    show_edges=True,
    color="tan",
)

plotter.subplot(1, 0)
plotter.add_text("Render Window 2", font_size=15)
sphere = pv.Sphere()
plotter.add_mesh(sphere, scalars=sphere.points[:, 2])
plotter.add_scalar_bar("Z")
# plotter.add_axes()
plotter.add_axes(interactive=True)

plotter.subplot(1, 1)
plotter.add_text("Render Window 3", font_size=15)
plotter.add_mesh(
    pv.Cone(),
    color="g",
    show_edges=True,
)
plotter.show_bounds(all_edges=True)

# Display the window
plotter.show(screenshot="multi_renderers.png")
