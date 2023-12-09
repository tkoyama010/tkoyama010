:orphan:
:og:image: ./_images/ogp/index.png
:og:image:alt: Title section for demo presentation
:og:description: Demo presentation of sphnx-revealjs

.. |br| raw:: html

   <br>

====================================
**PyVista** プロジェクト |br| の紹介
====================================

:Speaker: Tetsuo Koyama
:Date: 2023-10-26

自己紹介
========

* :fab:`github` `@tkoyama010 <https://github.com/tkoyama010>`_
* `オープンCAE勉強会＠関東（構造など） <https://openfem-kanto.connpass.com/>`_
* `SciPy 2022カンファレンスレポート <https://gihyo.jp/article/2022/09/scipy2022>`_
* `SciPy 2023カンファレンスレポート <https://gihyo.jp/article/2023/08/scipy2023>`_

PyVista紹介 [#]_
================

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial.html#pyvista-tutorial


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

紹介の概要 [#]_
---------------

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

+--------------------------------------+-----------------------------------------------------+
| **レッスン**                         | **説明**                                            |
+--------------------------------------+-----------------------------------------------------+
| はじめに                             | PyVistaを使って3Dビジュアライゼーションを行います． |
+--------------------------------------+-----------------------------------------------------+
| JupyterでPyVistaを使う               | JupyterでPyVistaを使います．                        |
+--------------------------------------+-----------------------------------------------------+

.. revealjs-break::

+--------------------------------------+-----------------------------------------------------+
| **レッスン**                         | **説明**                                            |
+--------------------------------------+-----------------------------------------------------+
| 基本的な使い方                       | 3Dデータを読み込んでプロットします．                |
+--------------------------------------+-----------------------------------------------------+
| メッシュとは?                        | PyVistaのデータ型の基本を学びます．                 |
+--------------------------------------+-----------------------------------------------------+

.. revealjs-break::

+--------------------------------------+-----------------------------------------------------+
| **レッスン**                         | **説明**                                            |
+--------------------------------------+-----------------------------------------------------+
| プロットオプションとアニメーション   | 魅力的な3Dビジュアリゼーションを作成します．        |
+--------------------------------------+-----------------------------------------------------+
| フィルタ                             | メッシュの解析と変更を行うためのフィルタAPIのデモ． |
+--------------------------------------+-----------------------------------------------------+

.. revealjs-break::

+--------------------------------------+-----------------------------------------------------+
| **レッスン**                         | **説明**                                            |
+--------------------------------------+-----------------------------------------------------+
| PyVistaの活用                        | あらゆる可視化に使用できることを紹介します．        |
+--------------------------------------+-----------------------------------------------------+

はじめに [#]_
=============

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_intro/index.html

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
               ...
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

JupyterでPyVistaを使う [#]_
===========================

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_jupyter/index.html

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

既存データの活用 [#]_
---------------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/01_basic/index.html#using-existing-data

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         from pyvista.examples import (
             download_saddle_surface
         )

         dataset = download_saddle_surface()
         dataset.plot(color='tan')

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_2_01.png

.. revealjs-break::

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         dataset = examples.download_frog()
         dataset.plot(color='tan')

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_4_0.png

ファイルから読み込む [#]_
-------------------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/01_basic/index.html#read-from-a-file

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         import pyvista as pv
         dataset = pv.read('ironProt.vtk')
         dataset
         dataset.plot(volume=True)

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_6_0.png

メッシュとは? [#]_
==================

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/02_mesh/index.html

ポイントとは？ [#]_
-------------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/02_mesh/index.html#what-is-a-point

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         import numpy as np
         points = np.random.rand(100, 3)
         mesh = pv.PolyData(points)
         mesh.plot(
             point_size=10,
             style='points',
             color='tan'
         )

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_1_01.png
         :alt: what-is-a-point

セルとは？ [#]_
---------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/02_mesh/index.html#what-is-a-cell

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         mesh = examples.load_hexbeam()

         pl = pv.Plotter()
         pl.add_mesh(
             mesh,
             show_edges=True,
             color='white'
         )
         pl.add_points(
             mesh.points,
             color='red',
             point_size=20
         )

         single_cell = mesh.extract_cells(
             mesh.n_cells - 1
         )
         pl.add_mesh(
             single_cell,
             color='pink',
             edge_color='blue',
             line_width=5,
             show_edges=True
         )

         pl.show()

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

         mesh.point_data[
             'my point values'
         ] = np.arange(mesh.n_points)
         mesh.plot(
             scalars='my point values',
             cpos=cpos,
             show_edges=True
         )

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_5_0.png

セルデータ [#]_
---------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/02_mesh/index.html#cell-data

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         mesh.cell_data[
             'my cell values'
         ] = np.arange(mesh.n_cells)
         mesh.plot(
             scalars='my cell values',
             cpos=cpos,
             show_edges=True,
         )

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_6_01.png

.. revealjs-break::

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         uni = examples.load_uniform()
         pl = pv.Plotter(
             shape=(1, 2),
             border=False
         )
         pl.add_mesh(
             uni,
             scalars='Spatial Point Data',
             show_edges=True
         )
         pl.subplot(0, 1)
         pl.add_mesh(
             uni,
             scalars='Spatial Cell Data',
             show_edges=True
         )
         pl.show()

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

         cube = pv.Cube()
         cube.cell_data[
            'myscalars'
         ] = range(6)

         other_cube = cube.copy()
         other_cube.point_data[
            'myscalars'
         ] = range(8)

         pl = pv.Plotter(
            shape=(1, 2), border_width=1
         )
         pl.add_mesh(cube, cmap='coolwarm')
         pl.subplot(0, 1)
         pl.add_mesh(
            other_cube, cmap='coolwarm'
         )
         pl.show()

   .. container:: half

       .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_7_0.png

プロットオプションとアニメーション [#]_
=======================================

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/03_figures/index.html

Plotterオブジェクトにメッシュを追加する
---------------------------------------

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         mesh = pv.Wavelet()
         p = pv.Plotter()
         p.add_mesh(mesh)
         p.show()

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_1_02.png

.. revealjs-break::

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         mesh = pv.Wavelet()
         p = pv.Plotter()
         p.add_mesh(mesh, cmap='coolwarm')
         p.show()

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_2_03.png

.. revealjs-break::

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         from pyvista.examples import (
             download_st_helens
         )
         idata = download_st_helens()
         mesh = idata.warp_by_scalar()

         p = pv.Plotter()
         p.add_mesh(
             mesh,
             cmap='terrain',
             opacity="linear",
         )
         p.show()

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index-1_00_002.png

.. revealjs-break::

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         kinds = [
             'tetrahedron',
             'cube',
             'octahedron',
             'dodecahedron',
             'icosahedron',
         ]

         centers = [
             (0, 1, 0),
             (0, 0, 0),
             (0, 2, 0),
             (-1, 0, 0),
             (-1, 2, 0),
         ]

         solids = [
             pv.PlatonicSolid(
                 kind,
                 radius=0.4,
                 center=center,
             )
             for kind, center in zip(
                 kinds, centers
             )
         ]

         p = pv.Plotter(
             window_size=[1000, 1000]
         )

         for solid in solids:
             p.add_mesh(
                 solid,
                 color='silver',
                 specular=1.0,
                 specular_power=10,
             )

         p.view_vector((5.0, 2, 3))
         p.add_floor(
             '-z',
             lighting=True,
             color='tan',
             pad=1.0
         )
         p.enable_shadows()
         p.show()

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index-2_00_00.png

サブプロット [#]_
-----------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/03_figures/index.html#subplotting

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         import pyvista as pv

         p = pv.Plotter(shape=(1, 2))

         p.subplot(0, 0)
         p.add_mesh(pv.Sphere())

         p.subplot(0, 1)
         p.add_mesh(pv.Cube())

         p.show()

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index-3_00_00.png

.. revealjs-break::

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         mesh = pv.Wavelet()
         cntr = mesh.contour()
         slices = mesh.slice_orthogonal()

         p = pv.Plotter(shape=(1, 2))

         p.subplot(0, 0)
         p.add_mesh(cntr)

         p.subplot(0, 1)
         p.add_mesh(slices)

         p.link_views()
         p.view_isometric()
         p.show()

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index-4_00_00.png

.. revealjs-break::

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         import pyvista as pv

         mesh = pv.Wavelet()
         cntr = mesh.contour()
         slices = mesh.slice_orthogonal()
         thresh = mesh.threshold(200)

         p = pv.Plotter(shape="1|3")

         p.subplot(1)
         p.add_mesh(cntr)

         p.subplot(2)
         p.add_mesh(slices)

         p.subplot(3)
         p.add_mesh(thresh)

         p.subplot(0)
         p.add_mesh(mesh)

         p.link_views()
         p.view_isometric()
         p.show()

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

         import pyvista as pv
         from pyvista import examples

         mesh = examples.load_random_hills()

         p = pv.Plotter()
         p.add_mesh(mesh)
         p.show_axes()
         p.show()

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index-6_00_00.png

.. revealjs-break::

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         import pyvista as pv
         from pyvista import examples

         mesh = examples.load_random_hills()

         p = pv.Plotter()
         p.add_mesh(mesh)
         p.show_axes()
         p.show_bounds()
         p.show()

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index-7_00_00.png

フィルタ [#]_
=============

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/04_filters/index.html

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

         import pyvista as pv
         from pyvista import examples

         dataset = examples.load_uniform()
         dataset.set_active_scalars(
             "Spatial Point Data"
         )

         threshed = dataset.threshold(
             [100, 500]
         )

         outline = dataset.outline()
         pl = pv.Plotter()
         pl.add_mesh(outline, color="k")
         pl.add_mesh(threshed)
         pl.camera_position = [-2, 5, 3]
         pl.show()

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_2_04.png

.. revealjs-break::

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         import pyvista as pv
         from pyvista import examples

         dataset = examples.load_uniform()
         outline = dataset.outline()
         threshed = dataset.threshold(
             [100, 500]
         )
         contours = dataset.contour()
         slices = dataset.slice_orthogonal()
         glyphs = dataset.glyph(
             factor=1e-3,
             geom=pv.Sphere(),
             orient=False,
         )

         p = pv.Plotter(shape=(2, 2))
         # Show the threshold
         p.add_mesh(outline, color="k")
         p.add_mesh(
             threshed,
             show_scalar_bar=False,
         )
         p.camera_position = [-2, 5, 3]
         # Show the contour
         p.subplot(0, 1)
         p.add_mesh(outline, color="k")
         p.add_mesh(
             contours,
             show_scalar_bar=False
         )
         p.camera_position = [-2, 5, 3]
         # Show the slices
         p.subplot(1, 0)
         p.add_mesh(outline, color="k")
         p.add_mesh(
             slices,
             show_scalar_bar=False
         )
         p.camera_position = [-2, 5, 3]
         # Show the glyphs
         p.subplot(1, 1)
         p.add_mesh(outline, color="k")
         p.add_mesh(
             glyphs,
             show_scalar_bar=False
         )
         p.camera_position = [-2, 5, 3]
         p.link_views()
         p.show()

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index-1_00_003.png

フィルタパイプライン [#]_
-------------------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/04_filters/index.html#filter-pipeline

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python

         result = (
             dataset
             .threshold()
             .elevation()
             .clip(normal="z")
             .slice_orthogonal()
         )
         p = pv.Plotter()
         p.add_mesh(outline, color="k")
         p.add_mesh(
             result,
             scalars="Elevation",
         )
         p.view_isometric()
         p.show()

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_4_02.png

PyVistaの活用 [#]_
==================

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/05_action/index.html

GeoVistaの使用 [#]_
-------------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/05_action/a_lesson_geovista.html#using-geovista
