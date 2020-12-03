fems = []
# fem_names is the array of FEM name.
for fem_name in fem_names:
    fems.append(
        gf.Fem(
            "FEM_PRODUCT("
            + fem_name
            + ","
            + fem_name
            + ")"
        )
    )

mfus = []
for mesh, fem in zip(meshs, fems):
    mfu = gf.MeshFem(mesh, 2)
    mfu.set_fem(fem)
    mfus.append(mfu)
