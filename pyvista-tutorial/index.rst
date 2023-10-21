:orphan:
:og:image: ./_images/ogp/index.png
:og:image:alt: Title section for demo presentation
:og:description: Demo presentation of sphnx-revealjs

.. |br| raw:: html

   <br>

=========================================================
**PyVista** による |br| 3次元ビジュアライ |br| ゼーション
=========================================================

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

`PyVistaチュートリアル <https://pyvista.github.io/pyvista-tutorial-ja/index.html>`_
-----------------------------------------------------------------------------------

.. tab-set::

   .. tab-item:: JupyterLab

      .. raw:: html

         <video width="100%" height="auto" controls autoplay muted>
           <source src="_static/pyvista_jupyterlab_demo.mp4" type="video/mp4">
           Your browser does not support the video tag.
         </video>

   .. tab-item:: IPython

      .. raw:: html

         <video width="100%" height="auto" controls autoplay muted>
           <source src="_static/pyvista_ipython_demo.mp4" type="video/mp4">
           Your browser does not support the video tag.
         </video>

`インストール <https://pyvista.github.io/pyvista-tutorial-ja/getting-started.html>`_
------------------------------------------------------------------------------------

チュートリアルにはGoogle Colaboratoryのリンクが準備されています。

.. raw:: html

    <center>
      <a target="_blank" href="https://colab.research.google.com/github/pyvista/pyvista-tutorial/blob/gh-pages/notebooks/tutorial/00_intro/a_basic.ipynb">
        <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/ width="300px">
      </a>
    </center>

フォーラムにご質問ください。

.. raw:: html

    <center>
      <a target="_blank" href="https://github.com/pyvista/pyvista/discussions">
        <img src="https://img.shields.io/badge/GitHub-Discussions-green?logo=github" alt="Open In Colab"/ width="300px">
      </a>
    </center>

PyVistaチュートリアル
=====================

チュートリアルの概要
--------------------

+--------------------------------------+-----------------+-----------------------------------------------------+
| **レッスン**                         | **時間**        | **説明**                                            |
+--------------------------------------+-----------------+-----------------------------------------------------+
| はじめに                             | 11:00-11:20     | PyVistaを使って3Dビジュアライゼーションを行います． |
+--------------------------------------+-----------------+-----------------------------------------------------+
| JupyterでPyVistaを使う               | 11:20-11:40     | JupyterでPyVistaを使います．                        |
+--------------------------------------+-----------------+-----------------------------------------------------+

チュートリアルの概要
--------------------

+--------------------------------------+-----------------+-----------------------------------------------------+
| **レッスン**                         | **時間**        | **説明**                                            |
+--------------------------------------+-----------------+-----------------------------------------------------+
| 基本的な使い方                       | 11:40-12:00     | 3Dデータを読み込んでプロットします．                |
+--------------------------------------+-----------------+-----------------------------------------------------+
| メッシュとは?                        | 12:00-12:30     | PyVistaのデータ型の基本を学びます．                 |
+--------------------------------------+-----------------+-----------------------------------------------------+

チュートリアルの概要
--------------------

+--------------------------------------+-----------------+-----------------------------------------------------+
| **レッスン**                         | **時間**        | **説明**                                            |
+--------------------------------------+-----------------+-----------------------------------------------------+
| 休憩 |:coffee:|                      | 12:30-12:45     | 休憩．指を伸ばしてコーヒーを飲む．                  |
+--------------------------------------+-----------------+-----------------------------------------------------+
| プロットオプションとアニメーション   | 12:45-13:20     | 魅力的な3Dビジュアリゼーションを作成します．        |
+--------------------------------------+-----------------+-----------------------------------------------------+

チュートリアルの概要
--------------------

+--------------------------------------+-----------------+-----------------------------------------------------+
| **レッスン**                         | **時間**        | **説明**                                            |
+--------------------------------------+-----------------+-----------------------------------------------------+
| フィルタ                             | 13:20-13:45     | メッシュの解析と変更を行うためのフィルタAPIのデモ． |
+--------------------------------------+-----------------+-----------------------------------------------------+
| PyVistaの活用                        | 13:45-14:00     | あらゆる可視化に使用できることを紹介します．        |
+--------------------------------------+-----------------+-----------------------------------------------------+

`はじめに <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_intro/index.html>`_
========================================================================================

`簡単な例 <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_intro/index.html#brief-examples>`_
-------------------------------------------------------------------------------------------------------

`サーフェスメッシュの読み込みとプロット <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_intro/index.html#read-and-plot-a-surface-mesh>`_
---------------------------------------------------------------------------------------------------------------------------------------------------

.. revealjs-code-block:: python
   :data-line-numbers: 1|3|4

   from pyvista import examples

   mesh = examples.download_bunny()
   mesh.plot(cpos='xy')

.. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_1_0.png

`色を使った簡単な点群の構築 <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_intro/index.html#construct-a-simple-point-cloud-with-color>`_
----------------------------------------------------------------------------------------------------------------------------------------------------

.. revealjs-code-block:: python
   :data-line-numbers: 1|2|3|4|5

   import pyvista as pv
   import numpy as np
   points = np.random.random((1000, 3))
   pc = pv.PolyData(points)
   pc.plot(scalars=points[:, 2], point_size=5.0, cmap='jet')

.. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_2_0.png

`他のライブラリとの比較 <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_intro/index.html#how-other-libraries-compare>`_
----------------------------------------------------------------------------------------------------------------------------------

.. tab-set::

   .. tab-item:: vtk

      .. image:: https://miro.medium.com/max/1400/1*B3aEPDxSvgR6Giyh4I4a2w.jpeg
         :alt: VTK
         :width: 70%


   .. tab-item:: ParaView

      .. image:: https://www.kitware.com/main/wp-content/uploads/2018/11/ParaView-5.6.png
         :alt: ParaView
         :width: 70%

   .. tab-item:: vedo

      .. image:: https://user-images.githubusercontent.com/32848391/80292484-50757180-8757-11ea-841f-2c0c5fe2c3b4.jpg
         :alt: vedo
         :width: 70%

   .. tab-item:: Mayavi

      .. image:: https://viscid-hub.github.io/Viscid-docs/docs/dev/_images/mvi-000.png
         :alt: mayavi
         :width: 70%

`JupyterでPyVistaを使う <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_jupyter/index.html>`_
========================================================================================================

.. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/jupyter.png
   :alt: jupyter
   :width: 70%

`PyVista用Trame Jupyterバックエンド <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_jupyter/index.html#trame-jupyter-backend-for-pyvista>`_
------------------------------------------------------------------------------------------------------------------------------------------------------

`Trame Jupyter モード <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_jupyter/index.html#trame-jupyter-modes>`_
--------------------------------------------------------------------------------------------------------------------------

`Jupyter-Server-Proxy <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_jupyter/index.html#jupyter-server-proxy>`_
---------------------------------------------------------------------------------------------------------------------------


`基本的な使い方 <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/01_basic/index.html>`_
==============================================================================================

`既存データの活用 <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/01_basic/index.html#using-existing-data>`_
--------------------------------------------------------------------------------------------------------------------

.. revealjs-code-block:: python
   :data-line-numbers: 1-3|1|2|3|5-12|5|6|7|8|9|10|11|12|1-12

   >>> from pyvista import examples
   >>> dataset = examples.download_saddle_surface()
   >>> dataset

   PolyData (..............)
     N Cells:    5131
     N Points:   2669
     N Strips:   0
     X Bounds:   -2.001e+01, 2.000e+01
     Y Bounds:   -6.480e-01, 4.024e+01
     Z Bounds:   -6.093e-01, 1.513e+01
     N Arrays:   0

`既存データの活用 <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/01_basic/index.html#using-existing-data>`_
--------------------------------------------------------------------------------------------------------------------

.. revealjs-code-block:: python
   :data-line-numbers: 1

   >>> dataset.plot(color='tan')

.. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_2_01.png
   :alt: using-existing-data
   :width: 70%

`ファイルから読み込む <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/01_basic/index.html#read-from-a-file>`_
---------------------------------------------------------------------------------------------------------------------

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
     Spacing:      1.000e+00, 1.000e+00, 1.000e+00
     N Arrays:     1

`ファイルから読み込む <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/01_basic/index.html#read-from-a-file>`_
---------------------------------------------------------------------------------------------------------------------

.. revealjs-code-block:: python
   :data-line-numbers: 1

   >>> dataset.plot(volume=True)

.. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_6_0.png
   :alt: read-from-a-file
   :width: 70%

`メッシュとは? <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/02_mesh/index.html>`_
============================================================================================

`ポイントとは？ <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/02_mesh/index.html#what-is-a-point>`_
-------------------------------------------------------------------------------------------------------------

.. revealjs-code-block:: python
   :data-line-numbers: 1-3|1|2|3|1-3

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
   >>>                       (-0.28, 0.94, -0.21)]
   >>> pl.show()

`セルとは？ <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/02_mesh/index.html#what-is-a-cell>`_
--------------------------------------------------------------------------------------------------------

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

`プロットオプションと <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/03_figures/index.html>`_  |br| `アニメーション <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/03_figures/index.html>`_
=============================================================================================================================================================================================================

`基礎編 <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/03_figures/index.html#the-basics>`_
---------------------------------------------------------------------------------------------------

`シーンの制御 <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/03_figures/index.html#controlling-the-scene>`_
--------------------------------------------------------------------------------------------------------------------

`フィルタ <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/04_filters/index.html>`_
==========================================================================================

`フィルタパイプライン <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/04_filters/index.html#filter-pipeline>`_
----------------------------------------------------------------------------------------------------------------------

`PyVistaの活用 <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/05_action/index.html>`_
==============================================================================================
