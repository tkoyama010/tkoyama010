import pyvista as pv

mesh = pv.Sphere()

# pl = pv.Plotter()
pl = pv.Plotter(off_screen=True)
pl.camera_position = "xy"
pl.camera.zoom(0.4)
pl.add_mesh(mesh)
# pl.show()
pl.screenshot("sphere.png")
