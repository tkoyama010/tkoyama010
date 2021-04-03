import pyvista as pv
from pyvista import examples
import matplotlib.pyplot as plt

m = examples.download_st_helens()

# Make two points to construct the line between
a = [m.center[0], m.bounds[2], m.bounds[5]]
b = [m.center[0], m.bounds[3], m.bounds[5]]

sampled = m.sample_over_line(a, b)
values = sampled.get_array("Elevation")
distance = sampled["Distance"]

plt.plot(distance, values)
plt.title("Elevation Profile")
plt.xlabel("Distance")
plt.ylabel("Height above sea level")
plt.savefig("plot_over_line2.png")
