import pyvista as pv

pv.set_plot_theme("document")
mesh = pv.Cube().triangulate().subdivide(3)

clipped_mesh = mesh.clip_box([0, 1, 0, 1, 0, 1])

p = pv.Plotter(shape=(1, 2))
p.subplot(0, 0)
p.add_text("Before Clip")
p.add_mesh(mesh, color="tan", show_edges=True)
p.subplot(0, 1)
p.add_text("After Clip")
p.add_mesh(
    clipped_mesh, color="tan", show_edges=True,
)
p.show(screenshot="clip_box.png")
