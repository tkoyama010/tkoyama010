:orphan:
:og:image: ./_images/ogp/index.png
:og:image:alt: Title section for demo presentation
:og:description: Demo presentation of sphnx-revealjs

.. |br| raw:: html

   <br>

.. **PyVista** による |br| 3D |br| ビジュアライゼーション

======================================
3D Visualization |br| with **PyVista**
======================================

:Instructor: Bane Sullivan, Bill Little, Jaswant Panchumarti, Tetsuo Koyama
:Date: 2024-7-9

.. 自己紹介
.. ========

self-introduction
=================

|:clock8:| 8:00-8:05

.. インストラクター紹介
.. --------------------

introduction of instructors
---------------------------

* :fab:`github` @banesullivan
* :fab:`github` @bjlittle
* :fab:`github` @jspanchu
* :fab:`github` @tkoyama010

.. PyVistaチュートリアル [#]_
.. ==========================

PyVista Tutorial [#]_
=====================

|:clock8:| 8:05-8:10

.. [#] https://tutorial.pyvista.org/tutorial.html#pyvista-tutorial

.. button-link:: https://github.com/pyvista/pyvista-tutorial/raw/gh-pages/notebooks.zip
   :color: primary
   :shadow:

   Download the Tutorial's Jupyter Notebooks

.. ご質問 [#]_
.. -----------

Questions [#]_
--------------

.. [#] https://tutorial.pyvista.org/tutorial.html#community-support

.. PyVistaについて何か質問があれば， |br| フォーラムに気軽に投稿してください．

If you have any questions about PyVista, |br| feel free to post on the forum.

.. raw:: html

    <center>
      <a target="_blank" href="https://github.com/pyvista/pyvista/discussions">
        <img src="https://img.shields.io/badge/GitHub-Discussions-green?logo=github" alt="Open In Colab"/ width="300px">
      </a>
    </center>

.. チュートリアルの概要 [#]_
.. -------------------------

Tutorial Overview [#]_
----------------------

.. [#] https://tutorial.pyvista.org/tutorial.html#tutorial-overview

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

.. +--------------------------------------+-----------------+-----------------------------------------------------+
.. | **レッスン**                         | **時間**        | **説明**                                            |
.. +--------------------------------------+-----------------+-----------------------------------------------------+
.. | はじめに                             |  8:10- 8:30     | PyVistaを使って3Dビジュアライゼーションを行います． |
.. +--------------------------------------+-----------------+-----------------------------------------------------+
.. | JupyterでPyVistaを使う               |  8:30- 8:50     | JupyterでPyVistaを使います．                        |
.. +--------------------------------------+-----------------+-----------------------------------------------------+

+--------------------------------------+-----------------+-----------------------------------------------------+
| **Lesson**                           | **Time**        | **Description**                                     |
+--------------------------------------+-----------------+-----------------------------------------------------+
| Introduction                         |  8:10- 8:30     | Use PyVista to create 3D visualizations.            |
+--------------------------------------+-----------------+-----------------------------------------------------+
| PyVista&Jupyter                      |  8:30- 8:50     | Use PyVista in Jupyter.                             |
+--------------------------------------+-----------------+-----------------------------------------------------+

.. revealjs-break::

.. +--------------------------------------+-----------------+-----------------------------------------------------+
.. | **レッスン**                         | **時間**        | **説明**                                            |
.. +--------------------------------------+-----------------+-----------------------------------------------------+
.. | 基本的な使い方                       |  8:50- 9:10     | 3Dデータを読み込んでプロットします．                |
.. +--------------------------------------+-----------------+-----------------------------------------------------+
.. | メッシュとは?                        |  9:10- 9:40     | PyVistaのデータ型の基本を学びます．                 |
.. +--------------------------------------+-----------------+-----------------------------------------------------+

+--------------------------------------+-----------------+-----------------------------------------------------+
| **Lesson**                           | **Time**        | **Description**                                     |
+--------------------------------------+-----------------+-----------------------------------------------------+
| Basic Usage                          |  8:50- 9:10     | Load and plot 3D data.                              |
+--------------------------------------+-----------------+-----------------------------------------------------+
| What is a Mesh?                      |  9:10- 9:40     | Learn the basics of PyVista's data types.           |
+--------------------------------------+-----------------+-----------------------------------------------------+

.. revealjs-break::

.. +--------------------------------------+-----------------+-----------------------------------------------------+
.. | **レッスン**                         | **時間**        | **説明**                                            |
.. +--------------------------------------+-----------------+-----------------------------------------------------+
.. | 休憩 |:coffee:|                      |  9:40- 9:55     | 休憩．指を伸ばしてコーヒーを飲みます．              |
.. +--------------------------------------+-----------------+-----------------------------------------------------+
.. | プロットオプションとアニメーション   |  9:55-10:15     | 魅力的な3Dビジュアリゼーションを作成します．        |
.. +--------------------------------------+-----------------+-----------------------------------------------------+

+--------------------------------------+-----------------+-----------------------------------------------------+
| **Lesson**                           | **Time**        | **Description**                                     |
+--------------------------------------+-----------------+-----------------------------------------------------+
| Break |:coffee:|                     |  9:40- 9:55     | Take a break. Stretch your fingers and drink coffee.|
+--------------------------------------+-----------------+-----------------------------------------------------+
| Plotting Options and Animation       |  9:55-10:15     | Create compelling 3D visualizations.                |
+--------------------------------------+-----------------+-----------------------------------------------------+

.. revealjs-break::

.. +--------------------------------------+-----------------+-----------------------------------------------------+
.. | **レッスン**                         | **時間**        | **説明**                                            |
.. +--------------------------------------+-----------------+-----------------------------------------------------+
.. | フィルタ                             | 10:15-10:40     | メッシュの解析と変更を行うためのフィルタAPIのデモ． |
.. +--------------------------------------+-----------------+-----------------------------------------------------+
.. | PyVistaの活用                        | 10:40-11:00     | あらゆる可視化に使用できることを紹介します．        |
.. +--------------------------------------+-----------------+-----------------------------------------------------+

+--------------------------------------+-----------------+--------------------------------------------------------------+
| **Lesson**                           | **Time**        | **Description**                                              |
+--------------------------------------+-----------------+--------------------------------------------------------------+
| Filters                              | 10:15-10:40     | Demonstration of the filter API for analyzing and alteration |
+--------------------------------------+-----------------+--------------------------------------------------------------+
| PyVista in Action                    | 10:40-11:00     | Introduction to what you can do with PyVista.                |
+--------------------------------------+-----------------+--------------------------------------------------------------+

.. はじめに [#]_
.. =============

Introduction [#]_
=================

.. [#] https://tutorial.pyvista.org/tutorial/00_intro/index.html

|:clock8:|  8:10- 8:15

.. 沿革 [#]_
.. ---------

Brief History [#]_
------------------

.. [#] https://tutorial.pyvista.org/tutorial/00_intro/index.html#brief-history

.. PyVistaは誰のためのものですか？ [#]_
.. ------------------------------------

Who is PyVista for? [#]_
------------------------

.. [#] https://tutorial.pyvista.org/tutorial/00_intro/index.html#who-is-pyvista-for

.. 簡単な例 [#]_
.. -------------

Brief Examples [#]_
-------------------

.. [#] https://tutorial.pyvista.org/tutorial/00_intro/index.html#brief-examples

.. サーフェスメッシュの読み込みとプロット [#]_
.. -------------------------------------------

Read and Plot a Surface Mesh [#]_
---------------------------------

.. [#] https://tutorial.pyvista.org/tutorial/00_intro/index.html#read-and-plot-a-surface-mesh

.. container:: flex-container

   .. container:: half

      .. code-block:: python

         from pyvista import examples

         mesh = examples.download_bunny()
         mesh.plot(cpos='xy')

   .. container:: half

      .. pyvista-plot::
         :include-source: False

         from pyvista import examples

         mesh = examples.download_bunny()
         mesh.plot(cpos='xy')


.. 色を使った簡単な点群の構築 [#]_
.. -------------------------------

Construct a Simple Point Cloud with Color [#]_
----------------------------------------------

.. [#] https://tutorial.pyvista.org/tutorial/00_intro/index.html#construct-a-simple-point-cloud-with-color

.. container:: flex-container

   .. container:: half

       .. code-block:: python

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

      .. pyvista-plot::
         :include-source: False

         import pyvista as pv
         import numpy as np

         points = np.random.random((1000, 3))
         pc = pv.PolyData(points)
         pc.plot(
             scalars=points[:, 2],
             point_size=5.0,
             cmap='jet'
         )

.. 他のライブラリとの比較 [#]_
.. ---------------------------

How Other Libraries Compare [#]_
--------------------------------

.. [#] https://tutorial.pyvista.org/tutorial/00_intro/index.html#how-other-libraries-compare

.. はじめに-演習 [#]_
.. ------------------

Introduction Exercises [#]_
---------------------------

.. [#] https://tutorial.pyvista.org/tutorial/00_intro/index.html#exercises

|:clock8:|  8:15- 8:30

.. MyBinder
.. --------

MyBinder
--------

.. raw:: html

    <center>
      <a target="_blank" href="https://mybinder.org/v2/gh/pyvista/pyvista-tutorial/gh-pages?urlpath=lab/tree/notebooks">
        <img src="https://static.mybinder.org/badge_logo.svg" alt="Launch on Binder"/ width="300px">
      </a>
    </center>

.. Google Colab
.. ------------

Google Colab
------------

.. raw:: html

    <center>
      <a target="_blank" href="https://colab.research.google.com/github/pyvista/pyvista-tutorial/blob/gh-pages/notebooks/tutorial/00_intro/a_basic.ipynb">
        <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/ width="300px">
      </a>
    </center>

.. JupyterでPyVistaを使う [#]_
.. ===========================

PyVista&Jupyter [#]_
====================

.. [#] https://tutorial.pyvista.org/tutorial/00_jupyter/index.html

|:clock830:| 8:30- 8:50

.. revealjs-break::

.. image:: https://tutorial.pyvista.org/_images/jupyter.png
   :alt: jupyter
   :width: 40%

.. vtk.jsでデータを可視化する [#]_
.. -------------------------------

Visualize Data with vtk.js [#]_
-------------------------------

.. [#] https://kitware.github.io/vtk-js/

.. image:: https://www.kitware.com/main/wp-content/uploads/2021/12/image-1.png
   :alt: vtkjs
   :width: 20%

.. Trameでデータを可視化する [#]_
.. ------------------------------

Visualize Data with Trame [#]_
------------------------------

.. [#] https://kitware.github.io/trame/

.. raw:: html

    <iframe src="https://player.vimeo.com/video/686840298?muted=1" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>

.. JupyterでPyVistaを使う [#]_
.. ---------------------------

Using PyVista in Jupyter [#]_
-----------------------------

.. [#] https://tutorial.pyvista.org/tutorial/00_jupyter/index.html

.. container:: flex-container

   .. container:: one-third

      .. image:: https://discourse.vtk.org/uploads/default/optimized/2X/e/e17639ec07a6819961efd3462ea1987087e2cf9e_2_441x500.jpeg

   .. container:: one-third

      .. image:: https://discourse.vtk.org/uploads/default/optimized/2X/2/2bf11e292cdd7fb03a1819016e0d34a9b82a6ddf_2_441x500.jpeg

   .. container:: one-third

      .. image:: https://discourse.vtk.org/uploads/default/optimized/2X/1/1dcf2d605e57e1d9c161e8a195c8da680184507c_2_441x500.jpeg

.. インストール  [#]_
.. ------------------

Installation [#]_
-----------------

.. [#] https://tutorial.pyvista.org/tutorial/00_jupyter/index.html#installation

.. revealjs-code-block:: bash

    pip install 'jupyterlab' 'pyvista[all]'

.. 基本的な使い方 [#]_
.. ===================

Basic Usage [#]_
================

.. [#] https://tutorial.pyvista.org/tutorial/01_basic/index.html

|:clock830:|  8:50- 8:55

.. 既存データの活用 [#]_
.. ---------------------

Using Existing Data [#]_
------------------------

.. [#] https://tutorial.pyvista.org/tutorial/01_basic/index.html#using-existing-data

.. container:: flex-container

   .. container:: half

      .. code-block:: python

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

      .. pyvista-plot::
         :include-source: False

         from pyvista.examples import download_saddle_surface

         dataset = download_saddle_surface()
         dataset.plot(color='tan')

.. revealjs-break::

.. container:: flex-container

   .. container:: half

      .. code-block:: python

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
         >>> dataset.plot(volume=True)

   .. container:: half

      .. pyvista-plot::
         :include-source: False

         from pyvista import examples

         dataset = examples.download_frog()
         dataset.plot(volume=True)

.. ファイルから読み込む [#]_
.. -------------------------

Read from a File [#]_
---------------------

.. [#] https://tutorial.pyvista.org/tutorial/01_basic/index.html#read-from-a-file

.. container:: flex-container

   .. container:: half

      .. code-block:: python

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

      .. pyvista-plot::
         :include-source: False

         import pyvista as pv

         dataset = pv.read('ironProt.vtk')
         dataset.plot(volume=True)

.. 基本的な使い方-演習 [#]_ [#]_
.. -----------------------------

Basic Usage Exercises [#]_ [#]_
-------------------------------

.. [#] https://tutorial.pyvista.org/tutorial/01_basic/index.html#exercises

.. [#] https://docs.pyvista.org/version/dev/

|:clock9:|  8:55- 9:05

.. 基本的な使い方-解答 [#]_ [#]_
.. -----------------------------

Basic Usage Solutions [#]_ [#]_
-------------------------------

.. [#] https://tutorial.pyvista.org/tutorial/01_basic/index.html#solutions

.. [#] https://docs.pyvista.org/version/dev/

|:clock9:|  9:05- 9:10

.. メッシュとは? [#]_
.. ==================

What is a Mesh? [#]_
====================

.. [#] https://tutorial.pyvista.org/tutorial/02_mesh/index.html

|:clock9:|  9:10- 9:25

.. ポイントとは？ [#]_
.. -------------------

What is a Point? [#]_
---------------------

.. [#] https://tutorial.pyvista.org/tutorial/02_mesh/index.html#what-is-a-point

.. container:: flex-container

   .. container:: half

      .. code-block:: python

         >>> import numpy as np
         >>> points = np.random.rand(100, 3)
         >>> mesh = pv.PolyData(points)
         >>> mesh.plot(
         ...     point_size=10,
         ...     style='points',
         ...     color='tan'
         ... )

   .. container:: half

      .. pyvista-plot::
         :include-source: False

         import numpy as np
         import pyvista as pv

         points = np.random.rand(100, 3)
         mesh = pv.PolyData(points)
         mesh.plot(
             point_size=10,
             style='points',
             color='tan'
         )

.. セルとは？ [#]_
.. ---------------

What is a Cell? [#]_
--------------------

.. [#] https://tutorial.pyvista.org/tutorial/02_mesh/index.html#what-is-a-cell

.. container:: flex-container

   .. container:: half

      .. code-block:: python

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

      .. pyvista-plot::
         :include-source: False

         import pyvista as pv
         from pyvista import examples

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

.. アトリビュートとは? [#]_
.. ------------------------

What are Attributes? [#]_
-------------------------

.. [#] https://tutorial.pyvista.org/tutorial/02_mesh/index.html#what-are-attributes

.. - ポイントデータ
.. - セルデータ
.. - フィールドデータ

- Point Data
- Cell Data
- Field Data

.. ポイントデータ [#]_
.. -------------------

Point Data [#]_
---------------

.. [#] https://tutorial.pyvista.org/tutorial/02_mesh/index.html#point-data

.. container:: flex-container

   .. container:: half

      .. code-block:: python

         >>> mesh.point_data[
         ...     'my point values'
         ... ] = np.arange(mesh.n_points)
         >>> mesh.plot(
         ...     scalars='my point values',
         ...     cpos=cpos,
         ...     show_edges=True
         ... )

   .. container:: half

      .. pyvista-plot::
         :context:
         :include-source: False

         import numpy as np
         import pyvista as pv
         from pyvista import examples

         mesh = examples.load_hexbeam()
         cpos = [(6.20, 3.00, 7.50),
                 (0.16, 0.13, 2.65),
                 (-0.28, 0.94, -0.21)]

         mesh.point_data[
             'my point values'
         ] = np.arange(mesh.n_points)
         mesh.plot(
             scalars='my point values',
             cpos=cpos,
             show_edges=True
         )

.. セルデータ [#]_
.. ---------------

Cell Data [#]_
--------------

.. [#] https://tutorial.pyvista.org/tutorial/02_mesh/index.html#cell-data

.. container:: flex-container

   .. container:: half

      .. code-block:: python

         >>> mesh.cell_data[
         ...     'my cell values'
         ... ] = np.arange(mesh.n_cells)
         >>> mesh.plot(
         ...     scalars='my cell values',
         ...     cpos=cpos,
         ...     show_edges=True,
         ... )

   .. container:: half

      .. pyvista-plot::
         :context:
         :include-source: False

         import pyvista as pv
         import numpy as np
         from pyvista import examples

         mesh = examples.load_hexbeam()

         mesh.cell_data[
             'my cell values'
         ] = np.arange(mesh.n_cells)
         mesh.plot(
             scalars='my cell values',
             cpos=cpos,
             show_edges=True,
         )

.. revealjs-break::

.. container:: flex-container

   .. container:: half

      .. code-block:: python

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

      .. pyvista-plot::
         :context:
         :include-source: False

         import pyvista as pv
         from pyvista import examples

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

.. フィールドデータ [#]_
.. ---------------------

Field Data [#]_
---------------

.. [#] https://tutorial.pyvista.org/tutorial/02_mesh/index.html#field-data

.. スカラーをメッシュに割り当てる [#]_
.. -----------------------------------

Assign Scalars to Mesh [#]_
---------------------------

.. [#] https://tutorial.pyvista.org/tutorial/02_mesh/index.html#field-data

.. container:: flex-container

   .. container:: half

      .. code-block:: python

         >>> cube = pv.Cube()
         >>> cube.cell_data[
         ...    'myscalars'
         ... ] = range(6)

         >>> other_cube = cube.copy()
         >>> other_cube.point_data[
         ...    'myscalars'
         ... ] = range(8)

         >>> pl = pv.Plotter(
         ...    shape=(1, 2), border_width=1
         ... )
         >>> pl.add_mesh(cube, cmap='coolwarm')
         >>> pl.subplot(0, 1)
         >>> pl.add_mesh(
         ...    other_cube, cmap='coolwarm'
         ... )
         >>> pl.show()

   .. container:: half

        .. pyvista-plot::
           :context:
           :include-source: False

           import pyvista as pv

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

.. メッシュとは? - 演習 [#]_ [#]_
.. ------------------------------

What is a Mesh? - Exercises [#]_ [#]_
-------------------------------------

.. [#] https://tutorial.pyvista.org/tutorial/02_mesh/index.html#exercises

.. [#] https://docs.pyvista.org/version/dev/

|:clock9:|  9:25- 9:45

.. メッシュとは? - 解答 [#]_ [#]_
.. ------------------------------

What is a Mesh? - Solutions [#]_ [#]_
-------------------------------------

.. [#] https://tutorial.pyvista.org/tutorial/02_mesh/index.html#solutions

.. [#] https://docs.pyvista.org/version/dev/

|:clock9:| 9:45- 9:50

.. 休憩 |:coffee:|
.. ===============

Break |:coffee:|
================

|:clock930:|  9:40- 9:55

.. プロットオプションとアニメーション [#]_
.. =======================================

Plotting Options and Animation [#]_
===================================

.. [#] https://tutorial.pyvista.org/tutorial/03_figures/index.html

|:clock10:|  9:55-10:00

.. Plotterオブジェクトにメッシュを追加する
.. ---------------------------------------

Add Plotter Object to Mesh
--------------------------

.. container:: flex-container

   .. container:: half

      .. code-block:: python

         >>> mesh = pv.Wavelet()
         >>> p = pv.Plotter()
         >>> p.add_mesh(mesh)
         >>> p.show()

   .. container:: half

      .. pyvista-plot::
         :context:
         :include-source: False

         mesh = pv.Wavelet()
         p = pv.Plotter()
         p.add_mesh(mesh)
         p.show()

.. revealjs-break::

.. container:: flex-container

   .. container:: half

      .. code-block:: python

         >>> mesh = pv.Wavelet()
         >>> p = pv.Plotter()
         >>> p.add_mesh(mesh, cmap='coolwarm')
         >>> p.show()

   .. container:: half

      .. pyvista-plot::
         :context:
         :include-source: False

         mesh = pv.Wavelet()
         p = pv.Plotter()
         p.add_mesh(mesh, cmap='coolwarm')
         p.show()

.. revealjs-break::

.. container:: flex-container

   .. container:: half

      .. code-block:: python

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

      .. pyvista-plot::
         :context:
         :include-source: False

         from pyvista.examples import download_st_helens

         idata = download_st_helens()
         mesh = idata.warp_by_scalar()

         p = pv.Plotter()
         p.add_mesh(
             mesh,
             cmap='terrain',
             opacity="linear",
         )
         p.show()

.. revealjs-break::

.. container:: flex-container

   .. container:: half

      .. code-block:: python

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

      .. image:: https://tutorial.pyvista.org/_images/index-2_00_00.png

.. サブプロット [#]_
.. -----------------

Subplotting [#]_
----------------

.. [#] https://tutorial.pyvista.org/tutorial/03_figures/index.html#subplotting

.. container:: flex-container

   .. container:: half

      .. code-block:: python

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

      .. pyvista-plot::
         :context:
         :include-source: False

         import pyvista as pv

         p = pv.Plotter(shape=(1, 2))

         p.subplot(0, 0)
         p.add_mesh(pv.Sphere())

         p.subplot(0, 1)
         p.add_mesh(pv.Cube())

         p.show()

.. revealjs-break::

.. container:: flex-container

   .. container:: half

      .. code-block:: python

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

      .. image:: https://tutorial.pyvista.org/_images/index-4_00_00.png

.. revealjs-break::

.. container:: flex-container

   .. container:: half

      .. code-block:: python

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

      .. image:: https://tutorial.pyvista.org/_images/index-5_00_00.png

.. シーンの制御 [#]_
.. -----------------

Control the Scene [#]_
----------------------

.. [#] https://tutorial.pyvista.org/tutorial/03_figures/index.html#controlling-the-scene

.. 軸と境界の表示 [#]_
.. -------------------

Axes and Bounds [#]_
--------------------

.. [#] https://tutorial.pyvista.org/tutorial/03_figures/index.html#axes-and-bounds

.. container:: flex-container

   .. container:: half

      .. code-block:: python

         >>> import pyvista as pv
         >>> from pyvista import examples

         >>> mesh = examples.load_random_hills()

         >>> p = pv.Plotter()
         >>> p.add_mesh(mesh)
         >>> p.show_axes()
         >>> p.show()

   .. container:: half

      .. pyvista-plot::
         :context:
         :include-source: False

         import pyvista as pv
         from pyvista import examples

         mesh = examples.load_random_hills()

         p = pv.Plotter()
         p.add_mesh(mesh)
         p.show_axes()
         p.show()

.. revealjs-break::

.. container:: flex-container

   .. container:: half

      .. code-block:: python

         >>> import pyvista as pv
         >>> from pyvista import examples

         >>> mesh = examples.load_random_hills()

         >>> p = pv.Plotter()
         >>> p.add_mesh(mesh)
         >>> p.show_axes()
         >>> p.show_bounds()
         >>> p.show()

   .. container:: half

      .. pyvista-plot::
         :context:
         :include-source: False

         import pyvista as pv
         from pyvista import examples

         mesh = examples.load_random_hills()

         p = pv.Plotter()
         p.add_mesh(mesh)
         p.show_axes()
         p.show_bounds()
         p.show()

.. プロットオプションとアニメーション - 演習 [#]_ [#]_
.. ---------------------------------------------------

Plotting Options and Animation - Exercises [#]_ [#]_
----------------------------------------------------

.. [#] https://tutorial.pyvista.org/tutorial/03_figures/index.html#exercises

.. [#] https://docs.pyvista.org/version/dev/

|:clock10:| 10:00-10:15

.. プロットオプションとアニメーション - 解答 [#]_ [#]_
.. ---------------------------------------------------

Plotting Options and Animation - Solutions [#]_ [#]_
----------------------------------------------------

.. [#] https://tutorial.pyvista.org/tutorial/03_figures/index.html#solutions

.. [#] https://docs.pyvista.org/version/dev/

|:clock10:| 10:15-10:20

.. フィルタ [#]_
.. =============

Filters [#]_
============

.. [#] https://tutorial.pyvista.org/tutorial/04_filters/index.html

|:clock10:| 10:20-10:25

threshold [#]_
--------------

.. container:: flex-container

   .. container:: half

      .. code-block:: python

         import pyvista as pv
         noise = pv.perlin_noise(
             0.1, (1, 1, 1), (0, 0, 0)
         )
         grid = pv.sample_function(
             noise,
             [0, 1.0, -0, 1.0, 0, 1.0],
             dim=(20, 20, 20)
         )
         grid.plot(
             cmap='gist_earth_r',
             show_scalar_bar=True,
             show_edges=False,
         )

   .. container:: half

      .. pyvista-plot::
         :context:
         :include-source: False

         import pyvista as pv
         noise = pv.perlin_noise(0.1, (1, 1, 1), (0, 0, 0))
         grid = pv.sample_function(
             noise, [0, 1.0, -0, 1.0, 0, 1.0], dim=(20, 20, 20)
         )
         grid.plot(
             cmap='gist_earth_r',
             show_scalar_bar=True,
             show_edges=False,
         )

.. [#] https://docs.pyvista.org/version/dev/api/core/_autosummary/pyvista.DataSetFilters.threshold.html#pyvista.DataSetFilters.threshold

contour [#]_
------------

.. container:: flex-container

   .. container:: half

      .. code-block:: python

         from pyvista import examples
         hills = examples.load_random_hills()
         contours = hills.contour()
         contours.plot(line_width=5)

   .. container:: half

      .. pyvista-plot::
         :context:
         :include-source: False

         from pyvista import examples
         hills = examples.load_random_hills()
         contours = hills.contour()
         contours.plot(line_width=5)

.. [#] https://docs.pyvista.org/version/dev/api/core/_autosummary/pyvista.DataSetFilters.contour.html#pyvista-datasetfilters-contour

slice_orthogonal [#]_
---------------------

.. container:: flex-container

   .. container:: half

      .. code-block:: python

         from pyvista import examples
         hills = examples.load_random_hills()
         slices = hills.slice_orthogonal(contour=False)
         slices.plot(line_width=5)

   .. container:: half

      .. pyvista-plot::
         :context:
         :include-source: False

         from pyvista import examples
         hills = examples.load_random_hills()
         slices = hills.slice_orthogonal(contour=False)
         slices.plot(line_width=5)

.. [#] https://docs.pyvista.org/version/dev/api/core/_autosummary/pyvista.DataSetFilters.slice_orthogonal.html#pyvista.DataSetFilters.slice_orthogonal

glyph [#]_
----------

.. container:: flex-container

   .. container:: half

      .. code-block:: python

         import pyvista as pv
         from pyvista import examples
         mesh = examples.load_random_hills()
         arrows = mesh.glyph(
             scale="Normals",
             orient="Normals",
             tolerance=0.05
         )
         pl = pv.Plotter()
         actor = pl.add_mesh(arrows, color="black")
         actor = pl.add_mesh(
             mesh,
             scalars="Elevation",
             cmap="terrain",
             show_scalar_bar=False,
         )
         pl.show()

   .. container:: half

      .. pyvista-plot::
         :context:
         :include-source: False

         import pyvista as pv
         from pyvista import examples
         mesh = examples.load_random_hills()
         arrows = mesh.glyph(
             scale="Normals", orient="Normals", tolerance=0.05
         )
         pl = pv.Plotter()
         actor = pl.add_mesh(arrows, color="black")
         actor = pl.add_mesh(
             mesh,
             scalars="Elevation",
             cmap="terrain",
             show_scalar_bar=False,
         )
         pl.show()

.. [#] https://docs.pyvista.org/version/dev/api/core/_autosummary/pyvista.DataSetFilters.glyph.html#pyvista.DataSetFilters.glyph

elevation [#]_
--------------

.. container:: flex-container

   .. container:: half

      .. code-block:: python

         import pyvista as pv
         sphere = pv.Sphere()
         sphere_elv = sphere.elevation()
         sphere_elv.plot(smooth_shading=True)

   .. container:: half

      .. pyvista-plot::
         :context:
         :include-source: False

         import pyvista as pv
         sphere = pv.Sphere()
         sphere_elv = sphere.elevation()
         sphere_elv.plot(smooth_shading=True)

.. [#] https://docs.pyvista.org/version/dev/api/core/_autosummary/pyvista.DataSetFilters.elevation.html#pyvista.DataSetFilters.elevation

clip [#]_
---------

.. container:: flex-container

   .. container:: half

      .. code-block:: python

         import pyvista as pv
         cube = pv.Cube().triangulate().subdivide(3)
         clipped_cube = cube.clip()
         clipped_cube.plot()

   .. container:: half

      .. pyvista-plot::
         :context:
         :include-source: False

         import pyvista as pv
         cube = pv.Cube().triangulate().subdivide(3)
         clipped_cube = cube.clip()
         clipped_cube.plot()

.. revealjs-break::

.. container:: flex-container

   .. container:: half

      .. code-block:: python

         import pyvista as pv
         cube = pv.Cube().triangulate().subdivide(3)
         clipped_cube = cube.clip('z')
         clipped_cube.plot()

   .. container:: half

      .. pyvista-plot::
         :context:
         :include-source: False

         import pyvista as pv
         cube = pv.Cube().triangulate().subdivide(3)
         clipped_cube = cube.clip('z')
         clipped_cube.plot()

.. [#] https://docs.pyvista.org/version/dev/api/core/_autosummary/pyvista.DataSetFilters.clip.html#pyvista.DataSetFilters.clip

.. フィルタ
.. --------

Filters
-------

.. container:: flex-container

   .. container:: half

      .. code-block:: python

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

      .. pyvista-plot::
         :context:
         :include-source: False

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

.. revealjs-break::

.. container:: flex-container

   .. container:: half

      .. code-block:: python

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

      .. pyvista-plot::
         :context:
         :include-source: False

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

.. フィルタパイプライン [#]_
.. -------------------------

Filter Pipeline [#]_
--------------------

.. [#] https://tutorial.pyvista.org/tutorial/04_filters/index.html#filter-pipeline

.. container:: flex-container

   .. container:: half

      .. code-block:: python

         >>> result = (
         ...     dataset
         ...     .threshold()
         ...     .elevation()
         ...     .clip(normal="z")
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

      .. pyvista-plot::
         :context:
         :include-source: False

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

.. フィルタ - 演習 [#]_ [#]_
.. -------------------------

Filters - Exercises [#]_ [#]_
-----------------------------

.. [#] https://tutorial.pyvista.org/tutorial/04_filters/index.html#exercises

.. [#] https://docs.pyvista.org/version/dev/

|:clock10:| 10:25-10:35

.. フィルタ - 解答 [#]_ [#]_
.. -------------------------

Filters - Solutions [#]_ [#]_
-----------------------------

.. [#] https://tutorial.pyvista.org/tutorial/04_filters/index.html#solutions

.. [#] https://docs.pyvista.org/version/dev/

|:clock10:| 10:35-10:40

.. PyVistaの活用 [#]_
.. ==================

PyVisa in Action [#]_
=====================

|:clock1030:| 10:40-11:00

.. [#] https://tutorial.pyvista.org/tutorial/05_action/index.html

.. GeoVistaの使用 [#]_
.. -------------------

GeoVista [#]_
-------------

.. [#] https://tutorial.pyvista.org/tutorial/05_action/a_lesson_geovista.html#using-geovista
