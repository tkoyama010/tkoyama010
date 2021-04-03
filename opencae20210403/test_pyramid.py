import pyvista as pv

pv.set_plot_theme("document")
pointa = [1.0, 1.0, 0.0]
pointb = [-1.0, 1.0, 0.0]
pointc = [-1.0, -1.0, 0.0]
pointd = [1.0, -1.0, 0.0]
pointe = [0.0, 0.0, 1.0]
pyramid = pv.Pyramid(
    [pointa, pointb, pointc, pointd, pointe]
)
arc = pv.CircularArcFromNormal(
    center=[0.0, 0.0, 0.0]
)
p = pv.Plotter(shape=(2, 1))
p.subplot(0, 0)
p.add_text("Pyramid")
p.add_mesh(pyramid, color="tan", show_edges=True)
p.subplot(1, 0)
p.add_text("CircularArc")
p.add_mesh(
    arc,
    color="tan",
    show_edges=True,
    line_width=3,
)
p.show(screenshot="pyramid.png")
