import pyvista as pv
from pyvista import examples

pv.set_plot_theme("document")
m = examples.download_st_helens()
# Make two points to construct the line between
a = [m.center[0], m.bounds[2], m.bounds[5]]
b = [m.center[0], m.bounds[3], m.bounds[5]]
# Preview how this line intersects this mesh
line = pv.Line(a, b)
p = pv.Plotter()
p.add_mesh(m)
p.add_mesh(line, color="white", line_width=10)
p.add_point_labels(
    [a, b],
    ["A", "B"],
    font_size=48,
    point_color="red",
    text_color="red",
)
p.show(screenshot="plot_over_line1.png")
