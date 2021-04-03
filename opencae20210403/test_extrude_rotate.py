import pyvista as pv

pv.set_plot_theme("document")
# create a line and rotate it about the Z-axis
resolution = 10
line = pv.Line(
    pointa=(0, 0, 0),
    pointb=(1, 0, 0),
    resolution=2,
)
poly = line.extrude_rotate(resolution=resolution)

plotter = pv.Plotter(shape=(2, 1))
plotter.subplot(0, 0)
plotter.add_text("Line", font_size=24)
plotter.add_mesh(
    line, color="tan", show_edges=True
)
plotter.add_mesh(
    pv.PolyData(line.points),
    color="red",
    point_size=10,
    render_points_as_spheres=True,
)
plotter.subplot(1, 0)
plotter.add_text(
    "Extrude Rotated Line", font_size=24
)
plotter.add_mesh(
    poly, color="tan", show_edges=True
)
plotter.add_mesh(
    pv.PolyData(poly.points),
    color="red",
    point_size=10,
    render_points_as_spheres=True,
)

plotter.show(
    cpos="xy", screenshot="extrude_rotate.png"
)
