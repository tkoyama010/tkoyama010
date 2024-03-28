import pyvista as pv
from pyvista.examples import download_cubemap_park

mesh = pv.Sphere()

# pl = pv.Plotter()
pl = pv.Plotter(off_screen=True)
dataset = download_cubemap_park()
pl.add_actor(dataset.to_skybox())
pl.camera_position = "xy"
pl.camera.zoom(0.4)
pl.add_mesh(mesh)
# pl.show()
pl.screenshot("skybox.png")
