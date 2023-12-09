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

コミュニティ紹介
================

* `オープンCAE勉強会＠関東（構造など） <https://openfem-kanto.connpass.com/>`_

はじめに
========

* PyVistaプロジェクトのコミュティ活動を中心に紹介します．
* みなさまの今後のOSS活動の参考になれば幸いです．

参考記事
--------

* `SciPy 2022カンファレンスレポート <https://gihyo.jp/article/2022/09/scipy2022>`_
* `SciPy 2023カンファレンスレポート <https://gihyo.jp/article/2023/08/scipy2023>`_

PyVistaプロジェクト
===================

.. image:: https://gihyo.jp/assets/images/article/2022/09/scipy2022/001.png

VTKとPyVistaのPythonAPIの比較 [#]_
----------------------------------

.. [#] https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_intro/index.html#read-and-plot-a-surface-mesh

.. container:: flex-container

   .. container:: half

      .. tab-set::

         .. tab-item:: VTK

            .. code:: python

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

            .. code:: python

               from pyvista import examples

               mesh = examples.download_bunny()
               mesh.plot(cpos='xy')

   .. container:: half

      .. image:: https://pyvista.github.io/pyvista-tutorial-ja/_images/index_1_0.png
