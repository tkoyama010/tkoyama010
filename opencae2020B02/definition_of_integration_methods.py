ims = []
# im_names is the array of IM name.
for im_name in im_names:
    ims.append(
        gf.Integ(
            "IM_PRODUCT("
            + im_name
            + ", "
            + method
            + ")"
        )
    )

mims = []
for mesh, im in zip(meshs, ims):
    mim = gf.MeshIm(mesh, im)
    mims.append(mim)
