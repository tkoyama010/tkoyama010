import pyvista as pv
from pyvista import examples
import matplotlib.pyplot as plt

pv.set_plot_theme("document")
m = examples.load_uniform()
m["height"] = m.points[:, 2]

normal = [0, 1, 0]
polar = [m.bounds[0], m.bounds[2], m.bounds[5]]
center = [m.bounds[0], m.bounds[2], m.bounds[4]]
angle = 90.0

sampled = m.sample_over_circular_arc_normal(
    center,
    normal=normal,
    polar=polar,
    angle=angle,
)

values = sampled.get_array("height")
distance = sampled["Distance"]

plt.plot(distance, values)
plt.title("height Profile")
plt.xlabel("Distance")
plt.ylabel("height")
plt.savefig("plot_over_circular_arc2.png")
