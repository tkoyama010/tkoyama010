.. |br| raw:: html

   <br>

=====================================================================
**Python** で |br| **CG** を作りたい人のための |br|  **PyVista** 入門
=====================================================================

:Speaker: Tetsuo Koyama
:Date: 2024-03-28

自己紹介
========

PyVistaとは
===========

.. container:: flex-container

   .. container:: half

      .. raw:: html

         <video width="100%" height="auto" controls autoplay muted>
           <source src="_static/pyvista_jupyterlab_demo.mp4" type="video/mp4">
           Your browser does not support the video tag.
         </video>

   .. container:: half

      .. raw:: html

         <video width="100%" height="auto" controls autoplay muted>
           <source src="_static/pyvista_ipython_demo.mp4" type="video/mp4">
           Your browser does not support the video tag.
         </video>

球を作る
========

.. container:: flex-container

   .. container:: half

      .. code-block:: python

         import pyvista as pv

         mesh = pv.Sphere()
         pl = pv.Plotter()
         pl.add_mesh(mesh)
         pl.show()

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-docs-dev-ja/_images/plotting_0_0.png

物理ベースレンダリング(PBR)を実行する
=====================================

.. container:: flex-container

   .. container:: half

      .. code-block:: python

         import pyvista as pv

         mesh = pv.Sphere()
         pl.add_mesh(
            mesh,
            pbr=True,
            roughness=0.1,
            metallic=0.5
         )
         pl.show()

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-docs-dev-ja/_images/plotting_0_0.png

スカイボックスを追加する
========================

.. container:: flex-container

   .. container:: half

      .. code-block:: python

         dataset = download_cubemap_park()
         pl.add_actor(dataset.to_skybox())
         pl.set_environment_texture(
             dataset, True
         )

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-docs-dev-ja/_images/pyvista-examples-downloads-download_cubemap_park-1_00_00.png

**pip install pyvista**
=======================
