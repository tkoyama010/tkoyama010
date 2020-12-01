import numpy as np
import getfem as gf


m = gf.Mesh("import", "gid", "tripod.GiD.msh")
mfu = gf.MeshFem(m, 3)  # displacement
mfp = gf.MeshFem(m, 1)  # pressure
mfd = gf.MeshFem(m, 1)  # data
mim = gf.MeshIm(m, gf.Integ("IM_TETRAHEDRON(5)"))
degree = 2
mfu.set_fem(gf.Fem("FEM_PK(3,%d)" % (degree,)))
mfd.set_fem(gf.Fem("FEM_PK(3,0)"))
mfp.set_fem(gf.Fem("FEM_PK_DISCONTINUOUS(3,0)"))

P = m.pts()
ctop = abs(P[1, :] - 13) < 1e-6
cbot = abs(P[1, :] + 10) < 1e-6
pidtop = np.compress(ctop, list(range(0, m.nbpts())))
pidbot = np.compress(cbot, list(range(0, m.nbpts())))
ftop = m.faces_from_pid(pidtop)
fbot = m.faces_from_pid(pidbot)

NEUMANN_BOUNDARY = 1
DIRICHLET_BOUNDARY = 2
m.set_region(NEUMANN_BOUNDARY, ftop)
m.set_region(DIRICHLET_BOUNDARY, fbot)

E = 1e3
Nu = 0.3
Lambda = E * Nu / ((1 + Nu) * (1 - 2 * Nu))
Mu = E / (2 * (1 + Nu))

md = gf.Model("real")
md.add_fem_variable("u", mfu)
md.add_initialized_data("cmu", Mu)
md.add_initialized_data("clambda", Lambda)
md.add_isotropic_linearized_elasticity_brick(mim, "u", "clambda", "cmu")
md.add_initialized_data("VolumicData", [0, -1, 0])
md.add_source_term_brick(mim, "u", "VolumicData")
md.add_Dirichlet_condition_with_multipliers(mim, "u", mfu, 2)

md.solve("noisy", "max iter", 1)
