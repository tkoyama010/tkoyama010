import pyvista as pv
from pyvista import examples

pv.set_plot_theme("document")
mesh = examples.download_bunny_coarse()

# 視点方向の定義
cpos = [
    (0.2, 0.3, 0.9),
    (0, 0, 0),
    (0, 1, 0),
]

mesh.plot(
    cpos=cpos,
    show_edges=True,
    color=True,
    screenshot="bunny.png",
)
