import pyvista as pv
from pyvista import examples

pv.set_plot_theme("document")
m = examples.load_uniform()
# Make two points at the bounds of the mesh and one at
# the center to construct a circular arc.
normal = [0, 1, 0]
polar = [m.bounds[0], m.bounds[2], m.bounds[5]]
center = [m.bounds[0], m.bounds[2], m.bounds[4]]
angle = 90.0
# Preview how this circular arc intersects this mesh
arc = pv.CircularArcFromNormal(
    center, 100, normal, polar, angle
)
p = pv.Plotter()
p.add_mesh(m, style="wireframe", color="w")
p.add_mesh(arc, color="b")
a = arc.points[0]
b = arc.points[-1]
p.add_point_labels(
    [a, b],
    ["A", "B"],
    font_size=48,
    point_color="red",
    text_color="red",
)
p.show(screenshot="plot_over_circular_arc1.png")
