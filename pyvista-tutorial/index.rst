:orphan:
:og:image: ./_images/ogp/index.png
:og:image:alt: Title section for demo presentation
:og:description: Demo presentation of sphnx-revealjs

.. |br| raw:: html

   <br>

======================================================
**PyVista** による |br| 3D |br| ビジュアライゼーション
======================================================

:Instructor: Tetsuo Koyama
:Date: 2023-10-26

自己紹介
========

|:clock11:| 11:00-11:05

インストラクター紹介
--------------------

* :fab:`twitter` @tkoyama010
* :fab:`github` @tkoyama010
* `ARK Information Systems, INC. <https://www.ark-info-sys.co.jp/>`_ 所属

TA紹介
------

* :fab:`twitter` @matsu_yarukinai
* :fab:`github` @matsubaraDaisuke

PyVistaチュートリアル [#]_
==========================

|:clock11:| 11:05-11:10

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial.html#pyvista-tutorial

.. button-link:: https://github.com/pyvista/pyvista-tutorial/raw/gh-pages/notebooks.zip
   :color: primary
   :shadow:

   Download the Tutorial's Jupyter Notebooks

ご質問 [#]_
-----------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial.html#questions

PyVistaについて何か質問があれば， |br| フォーラムに気軽に投稿してください．

.. raw:: html

    <center>
      <a target="_blank" href="https://github.com/pyvista/pyvista/discussions">
        <img src="https://img.shields.io/badge/GitHub-Discussions-green?logo=github" alt="Open In Colab"/ width="300px">
      </a>
    </center>

チュートリアルの概要 [#]_
-------------------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial.html#tutorial-overview

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

.. revealjs-break::

+--------------------------------------+-----------------+-----------------------------------------------------+
| **レッスン**                         | **時間**        | **説明**                                            |
+--------------------------------------+-----------------+-----------------------------------------------------+
| はじめに                             | 11:10-11:30     | PyVistaを使って3Dビジュアライゼーションを行います． |
+--------------------------------------+-----------------+-----------------------------------------------------+
| JupyterでPyVistaを使う               | 11:30-11:40     | JupyterでPyVistaを使います．                        |
+--------------------------------------+-----------------+-----------------------------------------------------+

.. revealjs-break::

+--------------------------------------+-----------------+-----------------------------------------------------+
| **レッスン**                         | **時間**        | **説明**                                            |
+--------------------------------------+-----------------+-----------------------------------------------------+
| 基本的な使い方                       | 11:40-12:00     | 3Dデータを読み込んでプロットします．                |
+--------------------------------------+-----------------+-----------------------------------------------------+
| メッシュとは?                        | 12:00-12:40     | PyVistaのデータ型の基本を学びます．                 |
+--------------------------------------+-----------------+-----------------------------------------------------+

.. revealjs-break::

+--------------------------------------+-----------------+-----------------------------------------------------+
| **レッスン**                         | **時間**        | **説明**                                            |
+--------------------------------------+-----------------+-----------------------------------------------------+
| 休憩 |:coffee:|                      | 12:40-12:55     | 休憩．指を伸ばしてコーヒーを飲みます．              |
+--------------------------------------+-----------------+-----------------------------------------------------+
| プロットオプションとアニメーション   | 12:55-13:15     | 魅力的な3Dビジュアリゼーションを作成します．        |
+--------------------------------------+-----------------+-----------------------------------------------------+

.. revealjs-break::

+--------------------------------------+-----------------+-----------------------------------------------------+
| **レッスン**                         | **時間**        | **説明**                                            |
+--------------------------------------+-----------------+-----------------------------------------------------+
| フィルタ                             | 13:15-13:40     | メッシュの解析と変更を行うためのフィルタAPIのデモ． |
+--------------------------------------+-----------------+-----------------------------------------------------+
| PyVistaの活用                        | 13:40-14:00     | あらゆる可視化に使用できることを紹介します．        |
+--------------------------------------+-----------------+-----------------------------------------------------+

はじめに [#]_
=============

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_intro/index.html

|:clock11:| 11:10-11:15

沿革 [#]_
---------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_intro/index.html#brief-history

PyVistaは誰のためのものですか？ [#]_
------------------------------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_intro/index.html#who-is-pyvista-for

簡単な例 [#]_
-------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_intro/index.html#brief-examples

サーフェスメッシュの読み込みとプロット [#]_
-------------------------------------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_intro/index.html#read-and-plot-a-surface-mesh

.. container:: flex-container

   .. container:: half

      .. tab-set::

         .. tab-item:: VTK

            .. revealjs-code-block:: python

               import vtk

               reader = vtk.vtkSTLReader()
               reader.SetFileName("bunny.stl")
               mapper = vtk.vtkPolyDataMapper()
               output_port = reader.GetOutputPort()
               mapper.SetInputConnection(output_port)
               actor = vtk.vtkActor()
               actor.SetMapper(mapper)
               ren = vtk.vtkRenderer()
               renWin = vtk.vtkRenderWindow()
               renWin.AddRenderer(ren)
               iren = vtk.vtkRenderWindowInteractor()
               iren.SetRenderWindow(renWin)
               ren.AddActor(actor)
               iren.Initialize()
               renWin.Render()
               iren.Start()
               del iren, renWin

         .. tab-item:: PyVista

            .. revealjs-code-block:: python

               from pyvista import examples

               mesh = examples.download_bunny()
               mesh.plot(cpos='xy')

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_1_0.png


色を使った簡単な点群の構築 [#]_
-------------------------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_intro/index.html#construct-a-simple-point-cloud-with-color

.. container:: flex-container

   .. container:: half

       .. revealjs-code-block:: python

         import pyvista as pv
         import numpy as np


         points = np.random.random((1000, 3))
         pc = pv.PolyData(points)
         pc.plot(
             scalars=points[:, 2],
             point_size=5.0,
             cmap='jet'
         )

   .. container:: half

       .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_2_0.png

他のライブラリとの比較 [#]_
---------------------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_intro/index.html#how-other-libraries-compare

はじめに-演習 [#]_
------------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_intro/index.html#exercises

|:clock11:| 11:15-11:30

MyBinder
--------

.. raw:: html

    <center>
      <a target="_blank" href="https://mybinder.org/v2/gh/pyvista/pyvista-tutorial/gh-pages?urlpath=lab/tree/notebooks">
        <img src="https://static.mybinder.org/badge_logo.svg" alt="Launch on Binder"/ width="300px">
      </a>
    </center>

Google Colab
------------

.. raw:: html

    <center>
      <a target="_blank" href="https://colab.research.google.com/github/pyvista/pyvista-tutorial/blob/gh-pages/notebooks/tutorial/00_intro/a_basic.ipynb">
        <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/ width="300px">
      </a>
    </center>

JupyterでPyVistaを使う [#]_
===========================

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_jupyter/index.html

|:clock1130:| 11:30-11:40

.. revealjs-break::

.. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/jupyter.png
   :alt: jupyter
   :width: 40%

vtk.jsでデータを可視化する [#]_
-------------------------------

.. [#] https://kitware.github.io/vtk-js/

.. image:: https://www.kitware.com/main/wp-content/uploads/2021/12/image-1.png
   :alt: vtkjs
   :width: 20%

Trameでデータを可視化する [#]_
------------------------------

.. [#] https://kitware.github.io/trame/

.. raw:: html

    <iframe src="https://player.vimeo.com/video/764741737?muted=1" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>

JupyterでPyVistaを使う [#]_
---------------------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_jupyter/index.html

.. container:: flex-container

   .. container:: one-third

      .. image:: https://discourse.vtk.org/uploads/default/optimized/2X/e/e17639ec07a6819961efd3462ea1987087e2cf9e_2_441x500.jpeg

   .. container:: one-third

      .. image:: https://discourse.vtk.org/uploads/default/optimized/2X/2/2bf11e292cdd7fb03a1819016e0d34a9b82a6ddf_2_441x500.jpeg

   .. container:: one-third

      .. image:: https://discourse.vtk.org/uploads/default/optimized/2X/1/1dcf2d605e57e1d9c161e8a195c8da680184507c_2_441x500.jpeg

インストール  [#]_
------------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_jupyter/index.html#installation

.. revealjs-code-block:: bash

    pip install 'jupyterlab<4.0.0' 'ipywidgets<8.0.0' 'pyvista[all,trame]'

基本的な使い方 [#]_
===================

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/01_basic/index.html

|:clock1130:| 11:40-11:45

既存データの活用 [#]_
---------------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/01_basic/index.html#using-existing-data

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         >>> from pyvista.examples import (
         ...     download_saddle_surface
         ... )
         >>> dataset = download_saddle_surface()
         >>> dataset
         PolyData (..............)
           N Cells:    5131
           N Points:   2669
           N Strips:   0
           X Bounds:   -2.001e+01, 2.000e+01
           Y Bounds:   -6.480e-01, 4.024e+01
           Z Bounds:   -6.093e-01, 1.513e+01
           N Arrays:   0
         >>> dataset.plot(color='tan')

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_2_01.png

.. revealjs-break::

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         >>> dataset = examples.download_frog()
         >>> dataset
         ImageData (..............)
           N Cells:      31594185
           N Points:     31960000
           X Bounds:     0.000e+00, 4.990e+02
           Y Bounds:     0.000e+00, 4.690e+02
           Z Bounds:     0.000e+00, 2.025e+02
           Dimensions:   500, 470, 136
           Spacing:      1.000e+00, 1.000e+00, ...
           N Arrays:     1
         >>> dataset.plot(color='tan')

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_4_0.png

ファイルから読み込む [#]_
-------------------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/01_basic/index.html#read-from-a-file

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         >>> import pyvista as pv
         >>> dataset = pv.read('ironProt.vtk')
         >>> dataset
         ImageData (..............)
           N Cells:      300763
           N Points:     314432
           X Bounds:     0.000e+00, 6.700e+01
           Y Bounds:     0.000e+00, 6.700e+01
           Z Bounds:     0.000e+00, 6.700e+01
           Dimensions:   68, 68, 68
           Spacing:      1.000e+00, 1.000e+00,
           N Arrays:     1
         >>> dataset.plot(volume=True)

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_6_0.png

基本的な使い方-演習 [#]_ [#]_
-----------------------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/01_basic/index.html#exercises

.. [#] https://pyvista.github.io/pyvista-docs-dev-ja/

|:clock12:| 11:45-11:55

基本的な使い方-解答 [#]_ [#]_
-----------------------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/01_basic/index.html#solutions

.. [#] https://pyvista.github.io/pyvista-docs-dev-ja/

|:clock12:| 11:55-12:00

メッシュとは? [#]_
==================

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/02_mesh/index.html

|:clock12:| 12:00-12:15

ポイントとは？ [#]_
-------------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/02_mesh/index.html#what-is-a-point

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         >>> import numpy as np
         >>> points = np.random.rand(100, 3)
         >>> mesh = pv.PolyData(points)
         >>> mesh.plot(
         ...     point_size=10,
         ...     style='points',
         ...     color='tan'
         ,,, )

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_1_01.png
         :alt: what-is-a-point

セルとは？ [#]_
---------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/02_mesh/index.html#what-is-a-cell

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         >>> mesh = examples.load_hexbeam()

         >>> pl = pv.Plotter()
         >>> pl.add_mesh(
         ...     mesh,
         ...     show_edges=True,
         ...     color='white'
         ... )
         >>> pl.add_points(
         ...     mesh.points,
         ...     color='red',
         ...     point_size=20
         ... )

         >>> single_cell = mesh.extract_cells(
         ...     mesh.n_cells - 1
         ... )
         >>> pl.add_mesh(
         ...     single_cell,
         ...     color='pink',
         ...     edge_color='blue',
         ...     line_width=5,
         ...     show_edges=True
         ... )

         >>> pl.show()

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_4_01.png

アトリビュートとは? [#]_
------------------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/02_mesh/index.html#what-are-attributes

- ポイントデータ
- セルデータ
- フィールドデータ

ポイントデータ [#]_
-------------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/02_mesh/index.html#point-data

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         >>> mesh.point_data[
         ...     'my point values'
         ... ] = np.arange(mesh.n_points)
         >>> mesh.plot(
         ...     scalars='my point values',
         ...     cpos=cpos,
         ...     show_edges=True
         ... )

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_5_0.png

セルデータ [#]_
---------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/02_mesh/index.html#cell-data

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         >>> mesh.cell_data[
         ...     'my cell values'
         ... ] = np.arange(mesh.n_cells)
         >>> mesh.plot(
         ...     scalars='my cell values',
         ...     cpos=cpos,
         ...     show_edges=True,
         ... )

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_6_01.png

.. revealjs-break::

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         >>> uni = examples.load_uniform()
         >>> pl = pv.Plotter(
         ...     shape=(1, 2),
         ...     border=False
         ... )
         >>> pl.add_mesh(
         ...     uni,
         ...     scalars='Spatial Point Data',
         ...     show_edges=True
         ... )
         >>> pl.subplot(0, 1)
         >>> pl.add_mesh(
         ...     uni,
         ...     scalars='Spatial Cell Data',
         ...     show_edges=True
         ... )
         >>> pl.show()

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index-1_00_001.png

フィールドデータ [#]_
---------------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/02_mesh/index.html#field-data

スカラーをメッシュに割り当てる [#]_
-----------------------------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/02_mesh/index.html#field-data

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         >>> cube = pv.Cube()
         >>> cube.cell_data[
         ...    'myscalars'
         ... ] = range(6)

         >>> other_cube = cube.copy()
         >>> other_cube.point_data[
         ...    'myscalars'
         ... ] = range(8)

         >>> pl = pv.Plotter(
         ,,,    shape=(1, 2), border_width=1
         ... )
         >>> pl.add_mesh(cube, cmap='coolwarm')
         >>> pl.subplot(0, 1)
         >>> pl.add_mesh(
         ...    other_cube, cmap='coolwarm'
         ... )
         >>> pl.show()

   .. container:: half

       .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_7_0.png

メッシュとは? - 演習 [#]_ [#]_
------------------------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/02_mesh/index.html#exercises

.. [#] https://pyvista.github.io/pyvista-docs-dev-ja/

|:clock12:| 12:15-12:35

メッシュとは? - 解答 [#]_ [#]_
------------------------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/02_mesh/index.html#solutions

.. [#] https://pyvista.github.io/pyvista-docs-dev-ja/

|:clock12:| 12:35-12:40

休憩 |:coffee:|
===============

|:clock1230:| 12:40-12:55

プロットオプションとアニメーション [#]_
=======================================

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/03_figures/index.html

|:clock1:| 12:55-13:00

Plotterオブジェクトにメッシュを追加する
---------------------------------------

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         >>> mesh = pv.Wavelet()
         >>> p = pv.Plotter()
         >>> p.add_mesh(mesh)
         >>> p.show()

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_1_02.png

.. revealjs-break::

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         >>> mesh = pv.Wavelet()
         >>> p = pv.Plotter()
         >>> p.add_mesh(mesh, cmap='coolwarm')
         >>> p.show()

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_2_03.png

.. revealjs-break::

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         >>> from pyvista.examples import (
         ...     download_st_helens
         ... )
         >>> idata = download_st_helens()
         >>> mesh = idata.warp_by_scalar()

         >>> p = pv.Plotter()
         >>> p.add_mesh(
         ...     mesh,
         ...     cmap='terrain',
         ...     opacity="linear",
         ... )
         >>> p.show()

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index-1_00_002.png

.. revealjs-break::

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         >>> kinds = [
         ...     'tetrahedron',
         ...     'cube',
         ...     'octahedron',
         ...     'dodecahedron',
         ...     'icosahedron',
         ... ]
         >>>
         >>> centers = [
         ...     (0, 1, 0),
         ...     (0, 0, 0),
         ...     (0, 2, 0),
         ...     (-1, 0, 0),
         ...     (-1, 2, 0),
         ... ]
         >>>
         >>> solids = [
         ...     pv.PlatonicSolid(
         ...         kind,
         ...         radius=0.4,
         ...         center=center,
         ...     )
         ...     for kind, center in zip(
         ...         kinds, centers
         ...     )
         ... ]
         >>>
         >>> p = pv.Plotter(
         ...     window_size=[1000, 1000]
         ... )
         >>>
         >>> for solid in solids:
         >>>     p.add_mesh(
         ...         solid,
         ...         color='silver',
         ...         specular=1.0,
         ...         specular_power=10,
         ...     )
         >>>
         >>> p.view_vector((5.0, 2, 3))
         >>> p.add_floor(
         ...     '-z',
         ...     lighting=True,
         ...     color='tan',
         ...     pad=1.0
         ... )
         >>> p.enable_shadows()
         >>> p.show()

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index-2_00_00.png

サブプロット [#]_
-----------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/03_figures/index.html#subplotting

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         >>> import pyvista as pv
         >>>
         >>> p = pv.Plotter(shape=(1, 2))
         >>>
         >>> p.subplot(0, 0)
         >>> p.add_mesh(pv.Sphere())
         >>>
         >>> p.subplot(0, 1)
         >>> p.add_mesh(pv.Cube())
         >>>
         >>> p.show()

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index-3_00_00.png

.. revealjs-break::

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         >>> mesh = pv.Wavelet()
         >>> cntr = mesh.contour()
         >>> slices = mesh.slice_orthogonal()
         >>>
         >>> p = pv.Plotter(shape=(1, 2))
         >>>
         >>> p.subplot(0, 0)
         >>> p.add_mesh(cntr)
         >>>
         >>> p.subplot(0, 1)
         >>> p.add_mesh(slices)
         >>>
         >>> p.link_views()
         >>> p.view_isometric()
         >>> p.show()

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index-4_00_00.png

.. revealjs-break::

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         >>> import pyvista as pv
         >>>
         >>> mesh = pv.Wavelet()
         >>> cntr = mesh.contour()
         >>> slices = mesh.slice_orthogonal()
         >>> thresh = mesh.threshold(200)
         >>>
         >>> p = pv.Plotter(shape="1|3")
         >>>
         >>> p.subplot(1)
         >>> p.add_mesh(cntr)
         >>>
         >>> p.subplot(2)
         >>> p.add_mesh(slices)
         >>>
         >>> p.subplot(3)
         >>> p.add_mesh(thresh)
         >>>
         >>> p.subplot(0)
         >>> p.add_mesh(mesh)
         >>>
         >>> p.link_views()
         >>> p.view_isometric()
         >>> p.show()

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index-5_00_00.png

シーンの制御 [#]_
-----------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/03_figures/index.html#controlling-the-scene

軸と境界の表示 [#]_
-------------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/03_figures/index.html#axes-and-bounds

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         >>> import pyvista as pv
         >>> from pyvista import examples

         >>> mesh = examples.load_random_hills()

         >>> p = pv.Plotter()
         >>> p.add_mesh(mesh)
         >>> p.show_axes()
         >>> p.show()

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index-6_00_00.png

.. revealjs-break::

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         >>> import pyvista as pv
         >>> from pyvista import examples

         >>> mesh = examples.load_random_hills()

         >>> p = pv.Plotter()
         >>> p.add_mesh(mesh)
         >>> p.show_axes()
         >>> p.show_bounds()
         >>> p.show()

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index-7_00_00.png

プロットオプションとアニメーション - 演習 [#]_ [#]_
---------------------------------------------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/03_figures/index.html#exercises

.. [#] https://pyvista.github.io/pyvista-docs-dev-ja/

|:clock1:| 13:00-13:15

プロットオプションとアニメーション - 解答 [#]_ [#]_
---------------------------------------------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/03_figures/index.html#solutions

.. [#] https://pyvista.github.io/pyvista-docs-dev-ja/

|:clock1:| 13:15-13:20

フィルタ [#]_
=============

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/04_filters/index.html

|:clock1:| 13:20-13:25

threshold [#]_
--------------

.. [#] https://pyvista.github.io/pyvista-docs-dev-ja/api/core/_autosummary/pyvista.DataSetFilters.threshold.html#pyvista.DataSetFilters.threshold

contour [#]_
------------

.. [#] https://pyvista.github.io/pyvista-docs-dev-ja/api/core/_autosummary/pyvista.DataSetFilters.contour.html#pyvista-datasetfilters-contour

slice_orthogonal [#]_
---------------------

.. [#] https://pyvista.github.io/pyvista-docs-dev-ja/api/core/_autosummary/pyvista.DataSetFilters.slice_orthogonal.html#pyvista.DataSetFilters.slice_orthogonal

glyph [#]_
----------

.. [#] https://pyvista.github.io/pyvista-docs-dev-ja/api/core/_autosummary/pyvista.DataSetFilters.glyph.html#pyvista.DataSetFilters.glyph

elevation [#]_
--------------

.. [#] https://pyvista.github.io/pyvista-docs-dev-ja/api/core/_autosummary/pyvista.DataSetFilters.elevation.html#pyvista.DataSetFilters.elevation

clip [#]_
---------

.. [#] https://pyvista.github.io/pyvista-docs-dev-ja/api/core/_autosummary/pyvista.DataSetFilters.clip.html#pyvista.DataSetFilters.clip

フィルタ
--------

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         >>> import pyvista as pv
         >>> from pyvista import examples

         >>> dataset = examples.load_uniform()
         >>> dataset.set_active_scalars(
         ...     "Spatial Point Data"
         ... )

         >>> threshed = dataset.threshold(
         ...     [100, 500]
         ... )

         >>> outline = dataset.outline()
         >>> pl = pv.Plotter()
         >>> pl.add_mesh(outline, color="k")
         >>> pl.add_mesh(threshed)
         >>> pl.camera_position = [-2, 5, 3]
         >>> pl.show()

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_2_04.png

.. revealjs-break::

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         >>> import pyvista as pv
         >>> from pyvista import examples

         >>> dataset = examples.load_uniform()
         >>> outline = dataset.outline()
         >>> threshed = dataset.threshold(
         ...     [100, 500]
         ... )
         >>> contours = dataset.contour()
         >>> slices = dataset.slice_orthogonal()
         >>> glyphs = dataset.glyph(
         ...     factor=1e-3,
         ...     geom=pv.Sphere(),
         ..      orient=False,
         >>> )

         >>> p = pv.Plotter(shape=(2, 2))
         >>> # Show the threshold
         >>> p.add_mesh(outline, color="k")
         >>> p.add_mesh(
         ...     threshed,
         ...     show_scalar_bar=False,
         ... )
         >>> p.camera_position = [-2, 5, 3]
         >>> # Show the contour
         >>> p.subplot(0, 1)
         >>> p.add_mesh(outline, color="k")
         >>> p.add_mesh(
         ...     contours,
         ...     show_scalar_bar=False
         ... )
         >>> p.camera_position = [-2, 5, 3]
         >>> # Show the slices
         >>> p.subplot(1, 0)
         >>> p.add_mesh(outline, color="k")
         >>> p.add_mesh(
         ...     slices,
         ...     show_scalar_bar=False
         ... )
         >>> p.camera_position = [-2, 5, 3]
         >>> # Show the glyphs
         >>> p.subplot(1, 1)
         >>> p.add_mesh(outline, color="k")
         >>> p.add_mesh(
         ...     glyphs,
         ...     show_scalar_bar=False
         ... )
         >>> p.camera_position = [-2, 5, 3]
         >>> p.link_views()
         >>> p.show()

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index-1_00_003.png

フィルタパイプライン [#]_
-------------------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/04_filters/index.html#filter-pipeline

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         >>> result = (
         ...     dataset
         ...     # NaN 値をすべて消去します．
         ...     .threshold()
         ...     # 高さに対応するスカラー値を
         ...     # 生成します．
         ...     .elevation()
         ...     # データセットを半分にカット
         ...     # します．
         ...     .clip(normal="z")
         ...     # 各軸平面に沿ってスライスを
         ...     # 3つ作成します．
         ...     .slice_orthogonal()
         ... )
         >>> p = pv.Plotter()
         >>> p.add_mesh(outline, color="k")
         >>> p.add_mesh(
         ...     result,
         ...     scalars="Elevation",
         ... )
         >>> p.view_isometric()
         >>> p.show()

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_4_02.png

フィルタ - 演習 [#]_ [#]_
-------------------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/04_filters/index.html#exercises

.. [#] https://pyvista.github.io/pyvista-docs-dev-ja/

|:clock1:| 13:25-13:35

フィルタ - 解答 [#]_ [#]_
-------------------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/04_filters/index.html#solutions

.. [#] https://pyvista.github.io/pyvista-docs-dev-ja/

|:clock1:| 13:35-13:40

PyVistaの活用 [#]_
==================

|:clock130:| 13:40-14:00

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/05_action/index.html

GeoVistaの使用 [#]_
-------------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/05_action/a_lesson_geovista.html#using-geovista
