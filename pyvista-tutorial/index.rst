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

はじめに
========

インストラクター紹介
--------------------

* :fab:`twitter` @tkoyama010
* :fab:`github` @tkoyama010
* `ARK Information Systems, INC. <https://www.ark-info-sys.co.jp/>`_ 所属

TA紹介
------

* :fab:`twitter` @matsu_yarukinai
* :fab:`github` @matsubaraDaisuke

作者紹介
--------

.. |contrib.rocks| image:: https://contrib.rocks/image?repo=pyvista/pyvista
   :target: https://github.com/pyvista/pyvista/graphs/contributors
   :alt: contrib.rocks
   :width: 60%

|contrib.rocks|

.. _contributors page: https://github.com/pyvista/pyvista/graphs/contributors/
.. _list of authors: https://docs.pyvista.org/getting-started/authors.html#authors
.. _contrib rocks: https://contrib.rocks

`PyVistaチュートリアル <https://pyvista.github.io/pyvista-tutorial-ja/tutorial.html#pyvista-tutorial>`_
=======================================================================================================

.. button-link:: https://github.com/pyvista/pyvista-tutorial/raw/gh-pages/notebooks.zip
   :color: primary
   :shadow:

   Download the Tutorial's Jupyter Notebooks

`ご質問 <https://pyvista.github.io/pyvista-tutorial-ja/tutorial.html#questions>`_
---------------------------------------------------------------------------------

PyVistaについて何か質問があれば， |br| フォーラムに気軽に投稿してください．

.. raw:: html

    <center>
      <a target="_blank" href="https://github.com/pyvista/pyvista/discussions">
        <img src="https://img.shields.io/badge/GitHub-Discussions-green?logo=github" alt="Open In Colab"/ width="300px">
      </a>
    </center>

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

`チュートリアルの概要 <https://pyvista.github.io/pyvista-tutorial-ja/tutorial.html#tutorial-overview>`_
-------------------------------------------------------------------------------------------------------

.. tab-set::

   .. tab-item:: JupyterLab

      .. raw:: html

         <video width="70%" height="auto" controls autoplay muted>
           <source src="_static/pyvista_jupyterlab_demo.mp4" type="video/mp4">
           Your browser does not support the video tag.
         </video>

   .. tab-item:: IPython

      .. raw:: html

         <video width="70%" height="auto" controls autoplay muted>
           <source src="_static/pyvista_ipython_demo.mp4" type="video/mp4">
           Your browser does not support the video tag.
         </video>

`チュートリアルの概要 <https://pyvista.github.io/pyvista-tutorial-ja/tutorial.html#tutorial-overview>`_
-------------------------------------------------------------------------------------------------------

+--------------------------------------+-----------------+-----------------------------------------------------+
| **レッスン**                         | **時間**        | **説明**                                            |
+--------------------------------------+-----------------+-----------------------------------------------------+
| はじめに                             | 11:00-11:20     | PyVistaを使って3Dビジュアライゼーションを行います． |
+--------------------------------------+-----------------+-----------------------------------------------------+
| JupyterでPyVistaを使う               | 11:20-11:40     | JupyterでPyVistaを使います．                        |
+--------------------------------------+-----------------+-----------------------------------------------------+

`チュートリアルの概要 <https://pyvista.github.io/pyvista-tutorial-ja/tutorial.html#tutorial-overview>`_
-------------------------------------------------------------------------------------------------------

+--------------------------------------+-----------------+-----------------------------------------------------+
| **レッスン**                         | **時間**        | **説明**                                            |
+--------------------------------------+-----------------+-----------------------------------------------------+
| 基本的な使い方                       | 11:40-12:00     | 3Dデータを読み込んでプロットします．                |
+--------------------------------------+-----------------+-----------------------------------------------------+
| メッシュとは?                        | 12:00-12:30     | PyVistaのデータ型の基本を学びます．                 |
+--------------------------------------+-----------------+-----------------------------------------------------+

`チュートリアルの概要 <https://pyvista.github.io/pyvista-tutorial-ja/tutorial.html#tutorial-overview>`_
-------------------------------------------------------------------------------------------------------

+--------------------------------------+-----------------+-----------------------------------------------------+
| **レッスン**                         | **時間**        | **説明**                                            |
+--------------------------------------+-----------------+-----------------------------------------------------+
| 休憩 |:coffee:|                      | 12:30-12:45     | 休憩．指を伸ばしてコーヒーを飲みます．              |
+--------------------------------------+-----------------+-----------------------------------------------------+
| プロットオプションとアニメーション   | 12:45-13:20     | 魅力的な3Dビジュアリゼーションを作成します．        |
+--------------------------------------+-----------------+-----------------------------------------------------+

`チュートリアルの概要 <https://pyvista.github.io/pyvista-tutorial-ja/tutorial.html#tutorial-overview>`_
-------------------------------------------------------------------------------------------------------

+--------------------------------------+-----------------+-----------------------------------------------------+
| **レッスン**                         | **時間**        | **説明**                                            |
+--------------------------------------+-----------------+-----------------------------------------------------+
| フィルタ                             | 13:20-13:45     | メッシュの解析と変更を行うためのフィルタAPIのデモ． |
+--------------------------------------+-----------------+-----------------------------------------------------+
| PyVistaの活用                        | 13:45-14:00     | あらゆる可視化に使用できることを紹介します．        |
+--------------------------------------+-----------------+-----------------------------------------------------+

`はじめに <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_intro/index.html>`_
========================================================================================

11:00-11:10

`簡単な例 <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_intro/index.html#brief-examples>`_
-------------------------------------------------------------------------------------------------------

`サーフェスメッシュの  <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_intro/index.html#read-and-plot-a-surface-mesh>`_ |br| `読み込みとプロット <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_intro/index.html#read-and-plot-a-surface-mesh>`_
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python
         :data-line-numbers: 1-4|1|3|4

         from pyvista import examples

         mesh = examples.download_bunny()
         mesh.plot(cpos='xy')

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_1_0.png


`色を使った簡単な点群の構築 <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_intro/index.html#construct-a-simple-point-cloud-with-color>`_
----------------------------------------------------------------------------------------------------------------------------------------------------

.. container:: flex-container

   .. container:: half

       .. revealjs-code-block:: python
         :data-line-numbers: 1-11|1|2|5|6|7-11|1-11

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

`他のライブラリとの比較 <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_intro/index.html#how-other-libraries-compare>`_
----------------------------------------------------------------------------------------------------------------------------------

.. tab-set::

   .. tab-item:: vtk

      .. image:: https://miro.medium.com/max/1400/1*B3aEPDxSvgR6Giyh4I4a2w.jpeg
         :alt: VTK
         :width: 50%


   .. tab-item:: ParaView

      .. image:: https://www.kitware.com/main/wp-content/uploads/2018/11/ParaView-5.6.png
         :alt: ParaView
         :width: 50%

   .. tab-item:: vedo

      .. image:: https://user-images.githubusercontent.com/32848391/80292484-50757180-8757-11ea-841f-2c0c5fe2c3b4.jpg
         :alt: vedo
         :width: 40%

   .. tab-item:: Mayavi

      .. image:: https://viscid-hub.github.io/Viscid-docs/docs/dev/_images/mvi-000.png
         :alt: mayavi
         :width: 50%

`はじめに-演習 <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_intro/index.html#exercises>`_
-------------------------------------------------------------------------------------------------------

11:10-11:20

`JupyterでPyVistaを使う <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_jupyter/index.html>`_
========================================================================================================

11:20-11:40

.. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/jupyter.png
   :alt: jupyter
   :width: 40%

`vtk.jsでデータを可視化する <https://kitware.github.io/vtk-js/>`_
-----------------------------------------------------------------

.. image:: https://www.kitware.com/main/wp-content/uploads/2021/12/image-1.png
   :alt: vtkjs
   :width: 20%

`Trameでデータを可視化する <https://kitware.github.io/trame/>`_
---------------------------------------------------------------

.. raw:: html

    <iframe src="https://player.vimeo.com/video/764741737?muted=1" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>

`JupyterでPyVistaを使う <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_jupyter/index.html>`_
--------------------------------------------------------------------------------------------------------

.. container:: flex-container

   .. container:: one-third

      .. image:: https://discourse.vtk.org/uploads/default/optimized/2X/e/e17639ec07a6819961efd3462ea1987087e2cf9e_2_441x500.jpeg

   .. container:: one-third

      .. image:: https://discourse.vtk.org/uploads/default/optimized/2X/2/2bf11e292cdd7fb03a1819016e0d34a9b82a6ddf_2_441x500.jpeg

   .. container:: one-third

      .. image:: https://discourse.vtk.org/uploads/default/optimized/2X/1/1dcf2d605e57e1d9c161e8a195c8da680184507c_2_441x500.jpeg

`インストール <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_jupyter/index.html#installation>`_
-----------------------------------------------------------------------------------------------------------

.. revealjs-code-block:: bash

    pip install 'jupyterlab<4.0.0' 'ipywidgets<8.0.0' 'pyvista[all,trame]'

`基本的な使い方 <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/01_basic/index.html>`_
==============================================================================================

11:40-11:50

`既存データの活用 <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/01_basic/index.html#using-existing-data>`_
--------------------------------------------------------------------------------------------------------------------

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python
         :data-line-numbers: 1-14|1-3|4|5|6-14|6|7|8|9|10|11|12|13|14|1-14

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

`ファイルから読み込む <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/01_basic/index.html#read-from-a-file>`_
---------------------------------------------------------------------------------------------------------------------

.. container:: flex-container

   .. container:: half

      .. revealjs-code-block:: python
         :data-line-numbers: 1-3|1|2|3|5-13|5|6|7|8|9|10|11|12|13|1-13

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

`演習 <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/01_basic/index.html#exercises>`_
----------------------------------------------------------------------------------------------

11:50-12:00

`メッシュとは? <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/02_mesh/index.html>`_
============================================================================================

12:00-12:20

`ポイントとは？ <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/02_mesh/index.html#what-is-a-point>`_
-------------------------------------------------------------------------------------------------------------

.. revealjs-code-block:: python
   :data-line-numbers: 1-4|1|2|3|4|1-4

   >>> import numpy as np
   >>> points = np.random.rand(100, 3)
   >>> mesh = pv.PolyData(points)
   >>> mesh.plot(point_size=10, style='points', color='tan')

.. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_1_01.png
   :alt: what-is-a-point
   :width: 70%

`セルとは？ <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/02_mesh/index.html#what-is-a-cell>`_
--------------------------------------------------------------------------------------------------------

.. revealjs-code-block:: python
   :data-line-numbers: 1-14

   >>> mesh = examples.load_hexbeam()

   >>> pl = pv.Plotter()
   >>> pl.add_mesh(mesh, show_edges=True, color='white')
   >>> pl.add_points(mesh.points, color='red', point_size=20)

   >>> single_cell = mesh.extract_cells(mesh.n_cells - 1)
   >>> pl.add_mesh(single_cell, color='pink', edge_color='blue',
   ...             line_width=5, show_edges=True)

   >>> pl.camera_position = [(6.20, 3.00, 7.50),
   >>>                       (0.16, 0.13, 2.65),
   >>> pl.show()

.. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_4_01.png
   :alt: what-is-a-cell
   :width: 70%

`アトリビュートとは? <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/02_mesh/index.html#what-are-attributes>`_
----------------------------------------------------------------------------------------------------------------------

- ポイントデータ
- セルデータ
- フィールドデータ

`ポイントデータ <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/02_mesh/index.html#point-data>`_
--------------------------------------------------------------------------------------------------------

.. revealjs-code-block:: python
   :data-line-numbers: 1-2

   >>> mesh.point_data['my point values'] = np.arange(mesh.n_points)
   >>> mesh.plot(scalars='my point values', cpos=cpos, show_edges=True)

.. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_5_0.png
   :alt: point-data
   :width: 70%

`セルデータ <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/02_mesh/index.html#cell-data>`_
---------------------------------------------------------------------------------------------------

.. revealjs-code-block:: python
   :data-line-numbers: 1-2

   >>> mesh.cell_data['my cell values'] = np.arange(mesh.n_cells)
   >>> mesh.plot(scalars='my cell values', cpos=cpos, show_edges=True)

.. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_6_01.png
   :alt: cell-data
   :width: 70%

`セルデータ <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/02_mesh/index.html#cell-data>`_
---------------------------------------------------------------------------------------------------

.. revealjs-code-block:: python
   :data-line-numbers: 1-6

   >>> uni = examples.load_uniform()
   >>> pl = pv.Plotter(shape=(1, 2), border=False)
   >>> pl.add_mesh(uni, scalars='Spatial Point Data', show_edges=True)
   >>> pl.subplot(0, 1)
   >>> pl.add_mesh(uni, scalars='Spatial Cell Data', show_edges=True)
   >>> pl.show()

.. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index-1_00_001.png
   :alt: cell-data
   :width: 70%

`フィールドデータ <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/02_mesh/index.html#field-data>`_
----------------------------------------------------------------------------------------------------------

`スカラーをメッシュに割り当てる <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/02_mesh/index.html#assigning-scalars-to-a-mesh>`_
-----------------------------------------------------------------------------------------------------------------------------------------

.. revealjs-code-block:: python
   :data-line-numbers: 1-11

   >>> cube = pv.Cube()
   >>> cube.cell_data['myscalars'] = range(6)

   >>> other_cube = cube.copy()
   >>> other_cube.point_data['myscalars'] = range(8)

   >>> pl = pv.Plotter(shape=(1, 2), border_width=1)
   >>> pl.add_mesh(cube, cmap='coolwarm')
   >>> pl.subplot(0, 1)
   >>> pl.add_mesh(other_cube, cmap='coolwarm')
   >>> pl.show()

`スカラーをメッシュに割り当てる <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/02_mesh/index.html#assigning-scalars-to-a-mesh>`_
-----------------------------------------------------------------------------------------------------------------------------------------

.. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_7_0.png
   :alt: assigning-scalars-to-a-mesh
   :width: 70%

`メッシュとは? - 演習 <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/02_mesh/index.html#exercises>`_
-------------------------------------------------------------------------------------------------------------

12:20-12:30

休憩 |:coffee:|
===============

12:30-12:45

`プロットオプションと <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/03_figures/index.html>`_  |br| `アニメーション <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/03_figures/index.html>`_
=============================================================================================================================================================================================================

`add_mesh`
----------

.. revealjs-code-block:: python
   :data-line-numbers: 1-4|1|2|3|4|1-4

   >>> mesh = pv.Wavelet()
   >>> p = pv.Plotter()
   >>> p.add_mesh(mesh)
   >>> p.show()

.. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_1_02.png
   :alt: the-basics
   :width: 70%

`add_mesh`
----------

.. revealjs-code-block:: python
   :data-line-numbers: 1-4|1|2|3|4|1-4

   >>> mesh = pv.Wavelet()
   >>> p = pv.Plotter()
   >>> p.add_mesh(mesh, cmap='coolwarm')
   >>> p.show()

.. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_2_03.png
   :alt: the-basics
   :width: 70%

`add_mesh`
----------

.. revealjs-code-block:: python
   :data-line-numbers: 1-5|1|2|3|4|5|1-5

   >>> mesh = examples.download_st_helens().warp_by_scalar()

   >>> p = pv.Plotter()
   >>> p.add_mesh(mesh, cmap='terrain', opacity="linear")
   >>> p.show()

.. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index-1_00_002.png
   :alt: the-basics
   :width: 70%

`add_mesh`
----------

.. revealjs-code-block:: python
   :data-line-numbers: 1-15

   >>> kinds = [
   ...     'tetrahedron',
   ...     'cube',
   ...     'octahedron',
   ...     'dodecahedron',
   ...     'icosahedron',
   ... ]
   >>> centers = [
   ...     (0, 1, 0),
   ...     (0, 0, 0),
   ...     (0, 2, 0),
   ...     (-1, 0, 0),
   ...     (-1, 2, 0),
   ... ]

`add_mesh`
----------

.. revealjs-code-block:: python
   :data-line-numbers: 1-11

   >>> solids = [
   ...     pv.PlatonicSolid(kind, radius=0.4, center=center)
   ...     for kind, center in zip(kinds, centers)
   ... ]

`add_mesh`
----------

.. revealjs-code-block:: python
   :data-line-numbers: 1-11

   >>> p = pv.Plotter(window_size=[1000, 1000])
   >>> for ind, solid in enumerate(solids):
   >>>     p.add_mesh(
   ...         solid, color='silver', specular=1.0, specular_power=10
   ...     )

   >>> p.view_vector((5.0, 2, 3))
   >>> p.add_floor('-z', lighting=True, color='tan', pad=1.0)
   >>> p.enable_shadows()

`add_mesh`
----------

.. revealjs-code-block:: python
   :data-line-numbers: 1

   >>> p.show()

.. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index-2_00_00.png
   :alt: the-basics
   :width: 70%

`シーンの制御 <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/03_figures/index.html#controlling-the-scene>`_
--------------------------------------------------------------------------------------------------------------------

`軸と境界 <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/03_figures/index.html#axes-and-bounds>`_
----------------------------------------------------------------------------------------------------------

.. revealjs-code-block:: python
   :data-line-numbers: 1-8|1-2|4|6-7|8|1-8

   >>> import pyvista as pv
   >>> from pyvista import examples

   >>> mesh = examples.load_random_hills()

   >>> p = pv.Plotter()
   >>> p.add_mesh(mesh)
   >>> p.show_axes()

`軸と境界 <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/03_figures/index.html#axes-and-bounds>`_
----------------------------------------------------------------------------------------------------------

.. revealjs-code-block:: python
   :data-line-numbers: 1

   >>> p.show()

.. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index-6_00_00.png
   :alt: the-basics
   :width: 70%

`軸と境界 <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/03_figures/index.html#axes-and-bounds>`_
----------------------------------------------------------------------------------------------------------

.. revealjs-code-block:: python
   :data-line-numbers: 1-9|1-2|4|6-7|8-9|1-9

   >>> import pyvista as pv
   >>> from pyvista import examples

   >>> mesh = examples.load_random_hills()

   >>> p = pv.Plotter()
   >>> p.add_mesh(mesh)
   >>> p.show_axes()
   >>> p.show_bounds()

`軸と境界 <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/03_figures/index.html#axes-and-bounds>`_
----------------------------------------------------------------------------------------------------------

.. revealjs-code-block:: python
   :data-line-numbers: 1

   >>> p.show()

.. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index-7_00_00.png
   :alt: the-basics
   :width: 70%

`フィルタ <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/04_filters/index.html>`_
==========================================================================================

.. revealjs-code-block:: python
   :data-line-numbers: 1-10

   >>> import pyvista as pv
   >>> from pyvista import examples

   >>> dataset = examples.load_uniform()
   >>> dataset.set_active_scalars("Spatial Point Data")

   >>> # Apply a threshold over a data range
   >>> threshed = dataset.threshold([100, 500])

   >>> outline = dataset.outline()

`フィルタ <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/04_filters/index.html>`_
------------------------------------------------------------------------------------------

.. revealjs-code-block:: python
   :data-line-numbers: 1-10

   >>> pl = pv.Plotter()
   >>> pl.add_mesh(outline, color="k")
   >>> pl.add_mesh(threshed)
   >>> pl.camera_position = [-2, 5, 3]
   >>> pl.show()

.. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_2_04.png
   :alt: filters
   :width: 70%

`フィルタ <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/04_filters/index.html>`_
------------------------------------------------------------------------------------------

.. revealjs-code-block:: python
   :data-line-numbers: 1-99

   >>> import pyvista as pv
   >>> from pyvista import examples

   >>> dataset = examples.load_uniform()
   >>> outline = dataset.outline()
   >>> threshed = dataset.threshold([100, 500])
   >>> contours = dataset.contour()
   >>> slices = dataset.slice_orthogonal()
   >>> glyphs = dataset.glyph(
   ...     factor=1e-3, geom=pv.Sphere(), orient=False
   >>> )

`フィルタ <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/04_filters/index.html>`_
------------------------------------------------------------------------------------------

.. revealjs-code-block:: python
   :data-line-numbers: 1-99

   >>> p = pv.Plotter(shape=(2, 2))
   >>> # Show the threshold
   >>> p.add_mesh(outline, color="k")
   >>> p.add_mesh(threshed, show_scalar_bar=False)
   >>> p.camera_position = [-2, 5, 3]
   >>> # Show the contour
   >>> p.subplot(0, 1)
   >>> p.add_mesh(outline, color="k")
   >>> p.add_mesh(contours, show_scalar_bar=False)
   >>> p.camera_position = [-2, 5, 3]

`フィルタ <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/04_filters/index.html>`_
------------------------------------------------------------------------------------------

.. revealjs-code-block:: python
   :data-line-numbers: 1-99

   >>> # Show the slices
   >>> p.subplot(1, 0)
   >>> p.add_mesh(outline, color="k")
   >>> p.add_mesh(slices, show_scalar_bar=False)
   >>> p.camera_position = [-2, 5, 3]
   >>> # Show the glyphs
   >>> p.subplot(1, 1)
   >>> p.add_mesh(outline, color="k")
   >>> p.add_mesh(glyphs, show_scalar_bar=False)
   >>> p.camera_position = [-2, 5, 3]

`フィルタ <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/04_filters/index.html>`_
------------------------------------------------------------------------------------------

.. revealjs-code-block:: python
   :data-line-numbers: 1-99

   >>> p.link_views()
   >>> p.show()

.. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index-1_00_003.png
   :alt: filters
   :width: 70%

`フィルタパイプライン <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/04_filters/index.html#filter-pipeline>`_
----------------------------------------------------------------------------------------------------------------------

#. まず， `threshold` フィルタを空にして， `NaN` 値をすべて消去します．
#. `elevation` フィルタを使用して，高さに対応するスカラー値を生成します．
#. `clip` フィルタを使用して，データセットを半分にカットします．
#. `slice_orthogonal` フィルタを使用して，各軸平面に沿ってスライスを3つ作成します．

`フィルタパイプライン <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/04_filters/index.html#filter-pipeline>`_
----------------------------------------------------------------------------------------------------------------------

.. revealjs-code-block:: python
   :data-line-numbers: 1-2

   >>> result = dataset.threshold().elevation()
   ...          .clip(normal="z").slice_orthogonal()
   >>> p = pv.Plotter()
   >>> p.add_mesh(outline, color="k")
   >>> p.add_mesh(result, scalars="Elevation")
   >>> p.view_isometric()
   >>> p.show()

.. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_4_02.png
   :alt: filter-pipeline
   :width: 70%

`PyVistaの活用 <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/05_action/index.html>`_
==============================================================================================
