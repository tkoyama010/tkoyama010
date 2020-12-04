import vtk

# create reader
reader = vtk.vtkOBJReader()
reader.SetFileName("bunny.obj")

mapper = vtk.vtkPolyDataMapper()
if vtk.VTK_MAJOR_VERSION <= 5:
    mapper.SetInput(reader.GetOutput())
else:
    mapper.SetInputConnection(
        reader.GetOutputPort()
    )

# create actor
actor = vtk.vtkActor()
actor.SetMapper(mapper)

# Create a rendering window and renderer
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)

# Create a renderwindowinteractor
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

# Assign actor to the renderer
ren.AddActor(actor)

# Enable user interface interactor
iren.Initialize()
renWin.Render()
iren.Start()

# clean up objects
del iren
del renWin
