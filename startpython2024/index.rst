.. |br| raw:: html

   <br>

=====================================================================
Pythonで |br| **3次元CG** を作りたい |br| 人のための **PyVista** 入門
=====================================================================

:Speaker: 小山哲央
:Date: 2024-06-20

.. 本日はこのトークをお聴きいただき、ありがとうございます。
.. 本日は、Pythonで3次元CGを作りたい人のためのPyVista入門と題して、Pythonで3次元CGを作成する方法についてお話しします。

自己紹介
========

.. まずは自己紹介をさせていただきます。
.. 私は小山哲央と申します。
.. 主にGitHubでPythonの3D可視化ライブラリPyVistaのメンテナンスとドキュメント翻訳をしています。
.. アカウント名はtkoyama010です。
.. また、今年のScipy Conferenceではチュートリアルの共同議長を務めさせていただいています。

.. container:: flex-container

   .. container:: half

      * :fab:`github` `@tkoyama010 <https://github.com/tkoyama010>`_
      * 3D 可視化ライブラリ `@pyvista <https://github.com/pyvista/pyvista>`_ メンテナ兼ドキュメント翻訳者
      * `@scipy-conference <https://www.scipy2024.scipy.org/>`_ チュートリアル共同議長

   .. container:: half

      .. image:: https://avatars.githubusercontent.com/u/7513610
         :alt: tkoyama010
         :width: 400px

もくじ
======

.. 本日の内容は以下の通りです。
.. まずはPythonでCGを作るのに必要なことの概要をお話し、その後、実際に3次元CGを作成する方法を紹介します。
.. モデリング、テクスチャ、マテリアル、ライティングというCGを作るための基本的な要素について説明します。
.. 次にMinecraftのような洞窟の作成するデモを行います。
.. 最後に応用例としてインタラクティブな可視化の方法について説明をします。

+--------------------------------------+-----------------+
| **タイトル**                         | **時間**        |
+--------------------------------------+-----------------+
| PythonでCGを作るのに必要なこと       | 4分             |
+--------------------------------------+-----------------+
| モデリングをしてみよう               | 4分             |
+--------------------------------------+-----------------+
| テクスチャマッピングをしてみよう     | 3分             |
+--------------------------------------+-----------------+
| マテリアルを追加してみよう           | 2分             |
+--------------------------------------+-----------------+

.. revealjs-break::

+--------------------------------------+-----------------+
| **タイトル**                         | **時間**        |
+--------------------------------------+-----------------+
| ライティングをしてみよう             | 4分             |
+--------------------------------------+-----------------+
| Minecraftのような洞窟を作ってみよう  | 4分             |
+--------------------------------------+-----------------+
| インタラクティブに可視化をしてみよう | 4分             |
+--------------------------------------+-----------------+

CGを作るのに必要なこと
======================

.. CGを作るのが初めての方もいるかもしれません。
.. そこで、まずはCGを作るのに必要なことについて説明します。

モデリング
----------

.. まずはモデリングについて説明します。
.. モデリングは、仮想3次元空間上に個々の物体の形状をつくる作業です。
.. これは、CGを作る際に最も基本的な作業です。
.. この作業を行うことで、仮想3次元空間上に自分の作成したい物体を配置することができます。

.. container:: flex-container

   .. container:: half

      - 仮想3次元空間上に個々の物体の形状をつくる。
      - CGを作る際に最も基本的な作業。
      - 仮想3次元空間上に自分の作成したい物体を配置することができる。

   .. container:: half

      .. pyvista-plot:: 01_hello_world.py
         :include-source: False

テクスチャマッピング
---------------------

.. 次にテクスチャマッピングについて説明します。
.. テクスチャマッピングは、オブジェクトの質感を表現するための画像です。
.. 先程のモデリングで作成したオブジェクトに、テクスチャを貼り付けることで、CGをよりリアルに表現することができます。

.. container:: flex-container

   .. container:: half

      - 質感を表現するための画像をモデルに貼り付ける。
      - モデリングで作成したオブジェクトに、テクスチャを貼り付けることで、CGをよりリアルに表現することができる。

   .. container:: half

      .. pyvista-plot::
         :include-source: False

         import pyvista as pv
         from pyvista import examples

         mesh = pv.Cylinder()

         filename = examples.mapfile

         texture = pv.read_texture(filename=filename)

         mesh.plot(texture=texture)

ライティング
------------
.. ライティングは、3D空間に光を配置してオブジェクトを照らすことです。
.. 光源を配置することで、モデリングしたオブジェクトに影をつけることができます。
.. これにより、CGをよりリアルに表現することができます。

.. container:: flex-container

   .. container:: half

      - 仮想3D空間に光を配置してオブジェクトを照らす。
      - 光源を配置することで、モデリングしたオブジェクトに影をつけることができる。

   .. container:: half

      .. pyvista-plot::
         :include-source: False

         import pyvista as pv
         from pyvista import examples
         mesh = pv.Cylinder()
         plotter = pv.Plotter(lighting='none')
         plotter.add_mesh(mesh, smooth_shading=True)
         light = pv.Light(position=(0, 1, 0), light_type='scene light')
         plotter.add_light(light)
         plotter.show()

PyVistaとは？
=============

.. 以上の要素を組み合わせて、3次元CGを作成します。
.. これらをPythonで実現するために、3D可視化ライブラリPyVistaを使います。
.. PyVistaは、3D可視化のためのライブラリで、Pythonで3次元CGを作成する際に便利です。
.. PyVistaは、MatplotlibやPandasのAPIに似ているため、これらのライブラリを使える人は簡単に使えます。
.. また、Matplotlibで実現できないCGの表現もPyVistaで実現できます。

#. Pythonフレンドリな3D可視化ライブラリです。
#. MatplotlibやPandasのAPIに似ています。
#. Matplotlibで実現できないCGの表現もPyVistaで実現できます。

インストール
============

.. code-block:: bash

   $ pip install pyvista[all]

モデリングをしてみよう
======================

.. それでは、始めましょう。
.. まずは、モデリングの方法について説明します。
.. まずは、Pipを使って、PyVistaをインストールします。

.. container:: flex-container

   .. container:: half

      .. literalinclude:: 01_hello_world.py
         :language: python
         :lines: 1-3

      .. literalinclude:: 01_hello_world.py
         :language: python
         :lines: 5-7

      .. literalinclude:: 01_hello_world.py
         :language: python
         :lines: 9-11

   .. container:: half

      .. pyvista-plot:: 01_hello_world.py
         :include-source: False

モデリングをしてみよう
======================

.. それでは、始めましょう。
.. まずは、モデリングの方法について説明します。
.. まずは、Pipを使って、PyVistaをインストールします。

.. container:: flex-container

   .. container:: half

      .. code-block:: python

         # Plotterオブジェクト

         pl = pv.Plotter()

         # 円柱を上方向に1.0移動します

         mesh = pv.Cylinder()
         mesh.translate(xyz=(0, 0, 1), inplace=True)
         pl.add_mesh(mesh)

      .. code-block:: python

         # もう1つ円柱を追加します

         mesh = pv.Cylinder()
         pl.add_mesh(mesh)

         # 追加されたモデルを描画します

         pl.show()

   .. container:: half

      .. pyvista-plot::
         :include-source: False

         import pyvista as pv

         pl = pv.Plotter()

         mesh = pv.Cylinder()
         mesh.translate(xyz=(0, 0, 1), inplace=True)
         pl.add_mesh(mesh)

         mesh = pv.Cylinder()
         pl.add_mesh(mesh)

         pl.show()

テクスチャを追加してみよう
==========================

.. 次にオブジェクトの質感を表現する「テクスチャ」の方法を紹介します。
.. ここでは、テクスチャマッピングを使って、オブジェクトに画像を貼り付けます。

.. container:: flex-container

   .. container:: half

      .. code-block:: python

         # テクスチャに使用する画像を読み込み

         from pyvista import examples

         filename = examples.mapfile

      .. code-block:: python

         # 画像をテクスチャとして読み込み

         texture = pv.read_texture(filename=filename)

      .. code-block:: python

         # テクスチャをオブジェクトに貼り付け

         mesh.plot(texture=texture)

   .. container:: half

      .. pyvista-plot::
         :include-source: False

         import pyvista as pv
         from pyvista import examples

         mesh = pv.Cylinder()

         filename = examples.mapfile

         texture = pv.read_texture(filename=filename)

         mesh.plot(texture=texture)


マテリアルを追加してみよう
==========================

.. さらに、オブジェクトの質感を表現する「マテリアル」の方法を紹介します。

.. container:: flex-container

   .. container:: half

      .. code-block:: python

         # スカイボックスを追加する
         from pyvista import examples as ex
         cubemap = ex.download_sky_box_cube_map()
         pl.add_actor(cubemap.to_skybox())

      .. code-block:: python

         # 物理ベースレンダリングを使用してモデリング
         pl.set_environment_texture(cubemap)
         pl.add_mesh(
             mesh,
             color='linen',
             pbr=True,
             metallic=0.8,
             roughness=0.1,
             diffuse=1
         )

   .. container:: half

       .. pyvista-plot::
         :include-source: False

         import pyvista as pv
         from pyvista import examples

         # Load the statue mesh
         mesh = pv.Cylinder()

         # Download skybox
         cubemap = examples.download_sky_box_cube_map()

         pl = pv.Plotter()
         pl.add_actor(cubemap.to_skybox())
         pl.set_environment_texture(cubemap)
         pl.add_mesh(mesh, color='linen', pbr=True, metallic=0.8, roughness=0.1, diffuse=1)

         pl.show()

ライティングをしてみよう
========================

.. container:: flex-container

   .. container:: half

      .. code-block:: python

         # Plotterクラスでlightingを無効にします。
         plotter = pv.Plotter(lighting='none')

      .. code-block:: python

         # 3D空間に光を配置します。
         light = pv.Light(
             position=(0, 1, 0),
             light_type='scene light'
         )

      .. code-block:: python

         # Plotterクラスに光を追加します。
         pl.add_light(light)
         plotter.show()

   .. container:: half

      .. pyvista-plot::
         :include-source: False

         import pyvista as pv
         from pyvista import examples
         mesh = pv.Cylinder()
         plotter = pv.Plotter(lighting='none')
         plotter.add_mesh(mesh, smooth_shading=True)
         light = pv.Light(position=(0, 1, 0), light_type='scene light')
         plotter.add_light(light)
         plotter.show()

Minecraftのような洞窟を作ってみよう
===================================

.. container:: flex-container

   .. container:: half

       .. code-block:: python

          # Perlin noiseを使ってグリッドを作成

          function = pv.perlin_noise(
              amplitude=1,
              freq=(1, 1, 1),
              phase=(0, 0, 0)
          )

       .. code-block:: python

          # データを格納したグリッドを生成

          grid = pv.sample_function(
              function=function,
              bounds=[0, 3.0, -0, 1.0, 0, 1.0],
              dim=(120, 40, 40),
          )

   .. container:: half

       .. pyvista-plot::
          :include-source: False

          import pyvista as pv

          noise = pv.perlin_noise(amplitude=1, freq=(1, 1, 1), phase=(0, 0, 0))
          grid = pv.sample_function(noise, [0, 3.0, -0, 1.0, 0, 1.0], dim=(120, 40, 40))

          mn, mx = [grid['scalars'].min(), grid['scalars'].max()]
          clim = (mn, mx * 1.8)
          grid.plot(
              cmap='gist_earth_r',
              background='white',
              show_scalar_bar=False,
              lighting=True,
              clim=clim,
              show_edges=False,
          )

.. revealjs-break::

.. container:: flex-container

   .. container:: half

       .. code-block:: python

          # 値が0.02より大きい部分を抽出

          out = grid.threshold(value=0.02)

   .. container:: half

       .. pyvista-plot::
          :include-source: False

          import pyvista as pv

          noise = pv.perlin_noise(amplitude=1, freq=(1, 1, 1), phase=(0, 0, 0))
          grid = pv.sample_function(noise, [0, 3.0, -0, 1.0, 0, 1.0], dim=(120, 40, 40))

          out = grid.threshold(0.02)
          mn, mx = [out['scalars'].min(), out['scalars'].max()]
          clim = (mn, mx * 1.8)
          out.plot(
              cmap='gist_earth_r',
              background='white',
              show_scalar_bar=False,
              lighting=True,
              clim=clim,
              show_edges=False,
          )

インタラクティブに可視化をしてみよう
====================================

.. さて、最後にインタラクティブな可視化の方法について説明します。
.. 皆様は、Pythonでコードを書いて、その結果を見るときに、どのような方法を使っていますか？

Sphinxによる可視化
------------------

.. まずは、Sphinxを使って、Pythonで3次元CGを作成する方法を説明します。
.. PyVistaをインストールすると、SphinxのドキュメントにPyVistaの3D可視化拡張機能が追加されます。

.. container:: flex-container

   .. container:: half

      .. code-block:: rst

         .. pyvista-plot::
            :include-source: False

            # pyvista-plotディレクティブを使って、
            # Sphinxドキュメントに右のような
            # 3D可視化を追加することができます。

            import pyvista as pv
            mesh = pv.Cylinder()
            mesh.plot()

            # このスライドもSphinxで作成しています。
            # SphinxでReveal.jsのスライドを作成する
            # sphinx-revealjsを使っています。

   .. container:: half

      .. pyvista-plot::
         :include-source: False

         import pyvista as pv
         mesh = pv.Cylinder()
         mesh.plot()

Jupyterによる可視化
-------------------

.. また、Jupyter Notebookを使って、Pythonで3次元CGを作成する方法もあります。
.. PyVistaは標準でJupyter Notebookでの可視化をサポートしています。
.. Jupyter Notebookを使っている方も多いと思いますが、PyVistaを使えば、Jupyter Notebook上でインタラクティブな可視化が可能です。

.. raw:: html

   <video width="80%" height="auto" controls autoplay muted>
     <source src="_static/pyvista_jupyterlab_demo.mp4" type="video/mp4">
     Your browser does not support the video tag.
   </video>

Streamlitによる可視化
---------------------

.. さらに、StreamlitやPanelを使えば、Webアプリケーションとしても可視化が可能です。
.. これにより、Pythonで3次元CGを作成する際に、より効率的に作業ができるようになります。
.. そのため、皆様がこれらのツールを使って、Pythonで3次元CGを作成する際に様々な方法を試してみてください。
.. 現在、公式ではこの機能はサポートされていませんが、サードパーティ製のツールを使うことで、Webアプリケーションとしての可視化も可能です。

.. raw:: html

   <p align="center">
   <a href="https://stpyvista.streamlit.app"><img alt="Streamlit Cloud" src="https://raw.githubusercontent.com/edsaac/stpyvista/main/assets/stpyvista_intro_crop.gif" width="600"></a>
   </p>

ご清聴ありがとうございました
============================

Please star!

.. raw:: html

    <!-- Place this tag where you want the button to render. -->
    <a class="github-button" href="https://github.com/pyvista/pyvista" data-icon="octicon-star" data-size="large" data-show-count="true" aria-label="Star pyvista/pyvista on GitHub">Star</a>
    <!-- Place this tag in your head or just before your close body tag. -->
    <script async defer src="https://buttons.github.io/buttons.js"></script>

.. ご清聴ありがとうございました。
.. 本日は、Pythonで3次元CGを作る方法についてお話ししました。
.. また、空間上のデータを使用して、Minecraftのような洞窟を作成する方法や、インタラクティブな可視化の方法についても説明しました。
.. この発表が皆様のお役に立てれば幸いです。
.. ご清聴ありがとうございました。
