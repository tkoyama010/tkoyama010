import pyvista as pv

pv.set_plot_theme("document")
mesh = pv.Sphere()
shrunk_mesh = mesh.shrink(shrink_factor=0.8)
p = pv.Plotter(shape=(1, 2))
p.subplot(0, 0)
p.add_text("Before Shrink")
p.add_mesh(mesh, color="tan", show_edges=True)
p.subplot(0, 1)
p.add_text("After Shrink")
p.add_mesh(
    shrunk_mesh,
    color="tan",
    show_edges=True,
)
p.show(screenshot="shrink.png")
