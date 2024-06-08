.. |br| raw:: html

   <br>

=====================================================================
Pythonで |br| **3次元CG** を作りたい |br| 人のための **PyVista** 入門
=====================================================================

:Speaker: 小山哲央
:Date: 2024-06-20

自己紹介
========

.. まずは自己紹介をさせていただきます。
.. 私は小山哲央と申します。
.. 現在、3D可視化ライブラリPyVistaのメンテナ兼ドキュメント翻訳者をしています。
.. また、今年のScipy Conferenceではチュートリアルの共同議長を務めさせていただきました。
.. 今日は、私がメンテナンスしているPyVistaを使って、Pythonで3次元CGを作る方法についてお話しします。

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
.. モデリング、テクスチャ、マテリアル、ライティング、Minecraftのような洞窟の作成、インタラクティブな可視化の方法について説明をします。

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

.. まずはPythonでCGを作るのに必要なことについてお話しします。
.. 3次元CGを作るために必要な基本的な要素について説明します。

モデリング
----------

.. モデリングは、仮想3次元空間上に個々の物体の形状をつくる作業です。

- 仮想3次元空間上に個々の物体の形状をつくる。

テクスチャマッピング
---------------------

.. テクスチャマッピングは、オブジェクトの質感を表現するための画像です。

- オブジェクトの質感を表現するための画像をモデルに貼り付ける。

ライティング
------------
.. ライティングは、3D空間に光を配置してオブジェクトを照らすことです。
.. これらの要素を組み合わせて、3次元CGを作成します。

- 3D空間に光を配置してオブジェクトを照らす。

PyVistaとは？
=============

.. これらを実現するために、Pythonの3D可視化ライブラリPyVistaを使います。
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

.. revealjs-break::

.. container:: flex-container

   .. container:: half

      .. code-block:: bash

         $ python

      .. literalinclude:: 01.py
         :language: python
         :lines: 1-3

      .. literalinclude:: 01.py
         :language: python
         :lines: 5-7

      .. literalinclude:: 01.py
         :language: python
         :lines: 9-11

   .. container:: half

      .. pyvista-plot:: 01.py
         :include-source: False


テクスチャを追加してみよう
==========================

.. 次にオブジェクトの質感を表現する「テクスチャ」の方法を紹介します。

.. revealjs-break::

.. ここでは、テクスチャマッピングを使って、オブジェクトに画像を貼り付けます。

.. container:: flex-container

   .. container:: half

       .. code-block:: python


マテリアルを追加してみよう
==========================

.. さらに、オブジェクトの質感を表現する「マテリアル」の方法を紹介します。

.. container:: flex-container

   .. container:: half

       .. code-block:: python

          import pyvista.examples as ex
          dataset = ex.download_cubemap_park()
          pl.add_actor(dataset.to_skybox())
          pl.set_environment_texture(
              dataset, True
          )
          pl.add_mesh(
             mesh,
             pbr=True,
             roughness=0.1,
             metallic=0.5,
          )
          pl.show()

   .. container:: half

       .. pyvista-plot::
           :include-source: False

           import pyvista as pv
           import pyvista.examples as ex

           pl = pv.Plotter(lighting=None)
           mesh = pv.Sphere()
           dataset = ex.download_cubemap_park()
           pl.add_actor(dataset.to_skybox())
           pl.set_environment_texture(
               dataset, True
           )
           pl.add_mesh(
              mesh,
              pbr=True,
              roughness=0.1,
              metallic=0.5,
           )
           pl.show()

ライティングをしてみよう
========================

.. container:: flex-container

   .. container:: half

      .. code-block:: python

         # 3D空間に光を配置します。
         import pyvista as pv
         import pyvista.examples as ex

         pl = pv.Plotter(lighting=None)
         light = pv.Light(position=(0, 0, 20), focal_point=(0, 0, 0), color='white')
         light.positional = True
         light.cone_angle = 40
         light.exponent = 10
         light.intensity = 3
         light.show_actor()
         floor = pv.Plane(center=(0, 0, 0), i_size=30, j_size=25)
         pl.add_mesh(floor)
         pl.add_light(light)
         pl.enable_shadows()
         mesh = pv.Sphere(center=(0, 0, 5), radius=5.0)
         pl.add_mesh(
            mesh,
            pbr=True,
            roughness=0.1,
            metallic=0.5,
         )
         pl.show()


   .. container:: half

      .. pyvista-plot::
         :include-source: False

         import pyvista as pv
         import pyvista.examples as ex

         pl = pv.Plotter(lighting=None)
         light = pv.Light(position=(0, 0, 20), focal_point=(0, 0, 0), color='white')
         light.positional = True
         light.cone_angle = 40
         light.exponent = 10
         light.intensity = 3
         light.show_actor()
         floor = pv.Plane(center=(0, 0, 0), i_size=30, j_size=25)
         pl.add_mesh(floor)
         pl.add_light(light)
         pl.enable_shadows()
         mesh = pv.Sphere(center=(0, 0, 5), radius=5.0)
         pl.add_mesh(
            mesh,
            pbr=True,
            roughness=0.1,
            metallic=0.5,
         )
         pl.show()


Minecraftのような洞窟を作ってみよう
===================================

.. revealjs-break::

.. container:: flex-container

   .. container:: half

       * パーリンノイズを使って地形を生成
       * ボクセル化して立方体を生成

   .. container:: half

       .. pyvista-plot::
          :include-source: False

          import pyvista as pv
          freq = (1, 1, 1)
          noise = pv.perlin_noise(1, freq, (0, 0, 0))
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
            mesh = pv.Sphere()
            mesh.plot()

            # このスライドもSphinxで作成しています。
            # SphinxでReveal.jsのスライドを作成する
            # sphinx-revealjsを使っています。

   .. container:: half

      .. pyvista-plot::
         :include-source: False

         import pyvista as pv
         mesh = pv.Sphere()
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
