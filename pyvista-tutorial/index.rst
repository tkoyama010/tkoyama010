:orphan:
:og:image: ./_images/ogp/index.png
:og:image:alt: Title section for demo presentation
:og:description: Demo presentation of sphnx-revealjs

=====================================
PyVistaによる3Dビジュアライゼーション
=====================================

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

本日はGoogle Colaboratoryを使用します。

.. raw:: html

    <center>
      <a target="_blank" href="https://colab.research.google.com/github/pyvista/pyvista-tutorial/blob/gh-pages/notebooks/tutorial/00_intro/a_basic.ipynb">
        <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/ width="300px">
      </a>
    </center>

他の環境についてはフォーラムにご質問ください。

.. raw:: html

    <center>
      <a target="_blank" href="https://github.com/pyvista/pyvista/discussions">
        <img src="https://img.shields.io/badge/GitHub-Discussions-green?logo=github" alt="Open In Colab"/ width="300px">
      </a>
    </center>

概要
====

チュートリアルの概要
--------------------

+--------------------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------+
| **レッスン**                         | **時間**        | **説明**                                                                                                              |
+--------------------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------+
| はじめに                             | 11:00-11:20     | はじめに - PyVistaを使ってPythonで3Dビジュアライゼーションを行います．                                                |
+--------------------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------+
| JupyterでPyVistaを使う               | 11:20-11:40     | JupyterでPyVistaを使います．                                                                                          |
+--------------------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------+

チュートリアルの概要
--------------------

+--------------------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------+
| **レッスン**                         | **時間**        | **説明**                                                                                                              |
+--------------------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------+
| 基本的な使い方                       | 11:40-12:00     | pyvista.examples モジュールと外部ファイルを使って，3Dデータを読み込んでプロットします．                               |
+--------------------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------+
| メッシュとは?                        | 12:00-12:30     | PyVistaのデータ型の基本を学び，一般的な3Dファイル形式を開いてデータを3Dで可視化する方法を紹介します．                 |
+--------------------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------+

チュートリアルの概要
--------------------

+--------------------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------+
| **レッスン**                         | **時間**        | **説明**                                                                                                              |
+--------------------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------+
| 休憩 |:coffee:|                      | 12:30-12:45     | 休憩．指を伸ばしてコーヒーを飲む．                                                                                    |
+--------------------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------+
| プロットオプションとアニメーション   | 12:45-13:20     | PyVistaプロッティングAPIの多くの機能を実演し，魅力的な3Dビジュアリゼーションとタッチオンアニメーションを作成します．  |
+--------------------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------+

チュートリアルの概要
--------------------

+--------------------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------+
| **レッスン**                         | **時間**        | **説明**                                                                                                              |
+--------------------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------+
| フィルタ                             | 13:20-13:45     | メッシュの解析と変更を行うためのPyVistaフィルタAPIのデモを行います．                                                  |
+--------------------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------+
| PyVistaの活用                        | 13:45-14:00     | PyVistaがすでにいくつかのプロジェクトで使用されており，あらゆる可視化に使用できることを紹介します．                   |
+--------------------------------------+-----------------+-----------------------------------------------------------------------------------------------------------------------+

`はじめに <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_intro/index.html>`_
========================================================================================

Code highlighting
-----------------

.. code-block:: python

   revealjs_script_plugins = [
       {
           "name": "RevealHighlight",
           "src": "revealjs4/plugin/highlight/highlight.js",
       },
   ]

These codes are highlighting by ``RevealHighlight`` plugin.

.. revealjs-break::

.. code-block:: rst

   .. code-block:: python

      print("hello world")

You can use ``code-block`` and ``literalinclude`` for code highlighting.

.. revealjs-break::

.. revealjs-code-block:: rst
   :data-line-numbers: 1|2

   .. revealjs-code-block:: rst
      :data-line-numbers: 1|2

      print("hello world")

Using ``revealjs-code-block``, line-level highlighting works.

.. revealjs-break::

.. revealjs-literalinclude:: ./conf.py
   :language: python
   :lines: 45-58
   :data-line-numbers: 2-5|6-9|10-13

You can include other file with step-by-step highlighting by ``revealjs-literalinclude``.

.. revealjs-break::

.. code-block:: rst

   .. revealjs-code-block:: python
      :data-ln-start-from: 47

.. revealjs-code-block:: python
   :data-ln-start-from: 47

   revealjs_script_plugins = [
       {
           "name": "RevealHighlight",
           "src": "revealjs4/plugin/highlight/highlight.js",
       },
   ]

You can use ``data-ln-start-from`` for display line numbers from specify value.

.. revealjs-break::

.. revealjs-literalinclude:: ./conf.py
   :data-ln-start-from: 47
   :lines: 47-60

``revealjs-literalinclude`` can use it too.

`JupyterでPyVistaを使う <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_jupyter/index.html>`_
========================================================================================================

`基本的な使い方 <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/01_basic/index.html>`_
==============================================================================================

`メッシュとは? <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/02_mesh/index.html>`_
============================================================================================

`プロットオプションとアニメーション <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/03_figures/index.html>`_
====================================================================================================================

`フィルタ <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/04_filters/index.html>`_
==========================================================================================

`PyVistaの活用 <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/05_action/index.html>`_
==============================================================================================

おまけ
======

`他のライブラリとの比較 <https://pyvista.github.io/pyvista-tutorial-ja/tutorial/00_intro/index.html#how-other-libraries-compare>`_
----------------------------------------------------------------------------------------------------------------------------------

.. tab-set::

   .. tab-item:: vtk

      .. image:: https://miro.medium.com/max/1400/1*B3aEPDxSvgR6Giyh4I4a2w.jpeg
         :alt: VTK
         :width: 75%


   .. tab-item:: ParaView

      .. image:: https://www.kitware.com/main/wp-content/uploads/2018/11/ParaView-5.6.png
         :alt: ParaView
         :width: 75%

   .. tab-item:: vedo

      .. image:: https://user-images.githubusercontent.com/32848391/80292484-50757180-8757-11ea-841f-2c0c5fe2c3b4.jpg
         :alt: vedo
         :width: 75%

   .. tab-item:: Mayavi

      .. image:: https://viscid-hub.github.io/Viscid-docs/docs/dev/_images/mvi-000.png
         :alt: Mayavi
         :width: 75%
