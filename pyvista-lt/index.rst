.. |br| raw:: html

   <br>

=====================================================================
**Python** で |br| **CG** を作りたい人のための |br|  **PyVista** 入門
=====================================================================

:Speaker: Tetsuo Koyama
:Date: 2024-03-28

自己紹介
========

- GitHubでtkoyama010というアカウント名で活動しています
- 科学技術計算の可視化に興味があります
- **PyVista** というPythonプロジェクトのメンテナをしています

PyVistaとは
===========

.. raw:: html

   <video width="75%" height="auto" controls autoplay muted>
     <source src="_static/pyvista_ipython_demo.mp4" type="video/mp4">
     Your browser does not support the video tag.
   </video>

今回は **PyVista** で **CG** に入門するというコンセプトでお話をします
=====================================================================

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

      .. image:: sphere.png

スカイボックスを追加する
========================

.. container:: flex-container

   .. container:: half

      .. code-block:: python

         from pyvista.examples import (
             download_cubemap_park
         )
         pl = pv.Plotter()
         dataset = download_cubemap_park()
         pl.add_actor(dataset.to_skybox())
         pl.add_mesh(mesh)
         pl.show()

   .. container:: half

      .. image:: skybox.png

物理ベースレンダリング(PBR)を実行する
=====================================

.. container:: flex-container

   .. container:: half

      .. code-block:: python

         pl = pv.Plotter(lighting=None)
         dataset = download_cubemap_park()
         pl.add_actor(dataset.to_skybox())
         pl.set_environment_texture(
             dataset, True
         )
         pl.add_mesh(
            mesh,
            pbr=True,
            roughness=0.1,
            metallic=0.5
         )
         pl.show()

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-docs-dev-ja/_images/pyvista-examples-downloads-download_cubemap_park-1_00_00.png

**pip install pyvista**
=======================
