import getfem as gf
import numpy as np


L = 10.0 # mm
b = 1.0 # mm
h = 1.0 # mm

meshs = []
for case, x, y in zip(cases, xs, ys):
    X = np.arange(x + 1) * L / x
    Y = np.arange(y + 1) * h / y
    mesh = gf.Mesh("cartesian", X, Y)
