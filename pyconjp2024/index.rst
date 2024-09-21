.. |br| raw:: html

   <br>

=====================================================================
Pythonで |br| **3次元CG** を作りたい |br| 人のための **PyVista** 入門
=====================================================================

:Speaker: 小山哲央
:Date: 2024-09-28

.. 本日はこのトークをお聴きいただき、ありがとうございます。
.. 本日は、Pythonで3次元CGを作りたい人のためのPyVista入門と題して、Pythonで3次元CGを作成する方法についてお話しします。

自己紹介
========

.. まずは自己紹介をさせていただきます。
.. 私は小山哲央と申します。
.. 主にGitHubでPythonの3D可視化ライブラリPyVistaのメンテナンスとドキュメント翻訳をしています。
.. アカウント名はtkoyama010です。

.. container:: flex-container

   .. container:: half

      * :fab:`github` `@tkoyama010 <https://github.com/tkoyama010>`_
      * 3D 可視化ライブラリ `@pyvista <https://github.com/pyvista/pyvista>`_ メンテナ兼ドキュメント翻訳者

   .. container:: half

      .. image:: https://avatars.githubusercontent.com/u/7513610
         :alt: tkoyama010
         :width: 400px

もくじ
======

.. 本日の内容は以下の通りです。
.. まずはPythonでCGを作るのに必要なことの概要をお話し、その後、実際に3次元CGを作成する方法を紹介します。
.. モデリング、テクスチャ、マテリアル、ライティングというCGを作るための基本的な要素について説明します。
.. 次に空間のデータ分析を行うデモを行います。
.. 最後に応用例としてインタラクティブな可視化の方法について説明をします。

.. container:: flex-container

   .. container:: half

      - 概要

        - PythonでCG作成

      - 基礎編

        - モデリング
        - テクスチャ
        - ライティング
        - マテリアル

   .. container:: half

      - 応用編

        - 空間のデータ分析
        - 空間のデータ可視化

PythonでCG作成
==============

.. CGを作るのが初めての方もいるかもしれません。
.. そこで、まずはPythonでCGを作るのに必要なことについて説明します。

.. container:: flex-container

   .. container:: half

      - 概要

        - 👉 PythonでCG作成

      - 基礎編

        - モデリング
        - テクスチャ
        - ライティング
        - マテリアル

   .. container:: half

      - 応用編

        - 空間のデータ分析
        - 空間のデータ可視化

モデリング
----------

.. まずはモデリングについて説明します。
.. モデリングは、仮想3次元空間上に個々のポリゴンをつくる作業です。
.. これは、CGを作る際に最も基本的な作業です。
.. この作業を行うことで、仮想3次元空間上に自分の作成したい物体を配置することができます。

.. container:: flex-container

   .. container:: half

      - 仮想3次元空間上に個々のポリゴンをつくる。
      - CGを作る際に最も基本的な作業。
      - 仮想3次元空間上に自分の作成したい物体を配置することができる。

   .. container:: half

      .. pyvista-plot::
         :include-source: False

         import pyvista as pv
         pl = pv.Plotter()
         mesh = pv.Cylinder()
         pl.add_mesh(mesh)
         pl.show()

テクスチャ
---------------------

.. 次にテクスチャについて説明します。
.. テクスチャは、オブジェクトの質感を表現するための画像です。
.. 先程のモデリングで作成したオブジェクトに、テクスチャを貼り付けることで、CGをよりリアルに表現することができます。

.. container:: flex-container

   .. container:: half

      - 質感を表現するための画像をモデルに貼り付ける。
      - モデリングで作成したオブジェクトに、テクスチャを貼り付けることで、CGをよりリアルに表現することができる。

   .. container:: half

      .. pyvista-plot::
         :include-source: False

         import pyvista as pv
         from pyvista import examples as ex

         mesh = pv.Cylinder()

         filename = ex.mapfile

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
         mesh = pv.Cylinder()
         plotter = pv.Plotter(lighting='none')
         plotter.add_mesh(mesh, smooth_shading=True)
         light = pv.Light(position=(0, 1, 0), light_type='scene light')
         plotter.add_light(light)
         plotter.show()

PyVistaとは？
=============

.. 以上の要素を組み合わせて、3次元CGを作成します。
.. これらのCG作成作業をそれぞれPythonで実現をする方法を考えた際に一番今現状で使いやすいライブラリが我々が開発しているPyVistaです。
.. PyVistaは、MatplotlibやPandasのAPIを意識して作成しているため、これらのライブラリを使える人は簡単に使えます。
.. 皆さんの中でもMatplotlibを使用して描画をされている方はいらっしゃると思います。
.. Matplotlibは2次元のグラフを描画するにはとても強力なライブラリですが、3次元プロットの機能はそれほど強力ではありません。
.. そのため、3次元の空間情報や物体がどのように変形するかなどの表現をするには機能が不足しています。
.. また、Matplotlibで実現できないCGの表現もPyVistaで実現できます。

#. Pythonフレンドリな3D可視化ライブラリです。
#. MatplotlibやPandasのAPIに似ています。
#. Matplotlibで実現できないCGの表現もPyVistaで実現できます。
#. Jupyter NotebookやSphinxでのインタラクティブな可視化もサポートしています。

.. インストールは、pipコマンドでインストールすることが可能です。
.. condaコマンドのパッケージも用意はされていますが、pipでインストールするのが一般的です。
.. 標準ではJupyterの拡張機能がインストールされませんが、Allというオプションをつけることで拡張をインストールすることができます。

.. code-block:: bash

   $ pip install "pyvista[all]"

モデリング
==========

.. それでは、始めましょう。
.. まずは、モデリングの方法について説明します。

.. container:: flex-container

   .. container:: half

      - 概要

        - PythonでCG作成

      - 基礎編

        - 👉 モデリング
        - テクスチャ
        - ライティング
        - マテリアル

   .. container:: half

      - 応用編

        - 空間のデータ分析
        - 空間のデータ可視化

.. revealjs-break::

.. Pythonを起動して、PyVistaをインポートします。
.. Pythonのライブラリには、エイリアスをつけることができます。
.. Numpyをnpというエイリアスでインポートするのと同じように、PyVistaをpvというエイリアスでインポートします。
.. これはNumpyのnpと同じように、PyVistaで慣用的に使われるエイリアスです。
.. 次に、Cylinder()という関数を使って円柱のモデルを作成します。
.. PyVistaでは、様々なモデルを作成する関数が用意されています。
.. この関数を使って、簡単にモデルを作成することができます。
.. 作成したモデルをplot()関数で表示すると、右のように円柱のモデルが表示されます。
.. こちらは、今回のスライドの目玉機能なのですが、こちらのInteractive Sceneというタブをクリックすると、3Dモデルを自由に回転させることができます。
.. これが、どのような仕組みで動いているかは、後半の応用編で説明をします。

.. container:: flex-container

   .. container:: half

      .. code-block:: python

         # PyVistaをインポートする。

         import pyvista as pv

      .. code-block:: python

         # 円柱のモデルを作成する。

         mesh = pv.Cylinder()

      .. code-block:: python

         # 円柱のモデルを描画する。

         mesh.plot()

   .. container:: half

      .. pyvista-plot::
         :include-source: False

         import pyvista as pv
         mesh = pv.Cylinder()
         mesh.plot()

.. revealjs-break::

.. image:: https://docs.pyvista.org/_images/sphx_glr_create-geometric-objects_001.png
  :width: 750
  :alt: Geometric Objects
  :target: https://docs.pyvista.org/examples/00-load/create-geometric-objects#sphx-glr-examples-00-load-create-geometric-objects-py

.. revealjs-break::

.. また複数のモデルを作成することも可能です。
.. Matplotlibにおいては、複数のグラフを描画する場合、Figureオブジェクトを使って複数のグラフを描画することができます。
.. PyVistaでも同様に、Plotterオブジェクトを使って複数のモデルを描画することができます。
.. こちらのコードでは、Plotterオブジェクトを使って、円柱を2つ描画しています。
.. まず、Plotterオブジェクトを作成し、add_mesh()関数を使って円柱を追加します。
.. その際に、1目の円柱をtranslate()メソッドを使って上方向に1.0移動させています。
.. このメソッドはメッシュ自身を変更するため、inplace=Trueというオプションを指定しています。
.. このAPIはPandasに影響を受けているため、Pandasを使ったことがある方は使いやすいと思います。
.. また、もう1つの円柱を追加し、追加されたモデルをshow()メソッドで表示します。

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

テクスチャ
==========

.. 次にオブジェクトの質感を表現する「テクスチャ」の方法を紹介します。

.. container:: flex-container

   .. container:: half

      - 概要

        - PythonでCG作成

      - 基礎編

        - モデリング
        - 👉 テクスチャ
        - ライティング
        - マテリアル

   .. container:: half

      - 応用編

        - 空間のデータ分析
        - 空間のデータ可視化

.. revealjs-break::

.. テクスチャは、先ほどご説明申し上げた通り、物体をよりリアリティのあるように見せるために表面に画像を追加をするという操作CG上の操作です。
.. ここでは、テクスチャという方法を使用して、オブジェクトに画像を貼り付けます。
.. これをPyVistaで実現をする場合、 まずはテクスチャーに使用する画像をロードします。
.. その次に画像をテクスチャとして読み込みます。
.. これを先ほどのPlotterオブジェクトのtextureという引数に定義をしてあげると、こちらの右のようにテクスチャーが円筒貼り付けられます。

.. container:: flex-container

   .. container:: half

      .. code-block:: python

         # テクスチャに使用する画像を読み込み

         from pyvista import examples as ex

         filename = ex.mapfile

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
         from pyvista import examples as ex

         mesh = pv.Cylinder()

         filename = ex.mapfile

         texture = pv.read_texture(filename=filename)

         mesh.plot(texture=texture)

ライティング
============

.. 次にライティングについてご説明をします。

.. container:: flex-container

   .. container:: half

      - 概要

        - PythonでCG作成

      - 基礎編

        - モデリング
        - テクスチャ
        - 👉 ライティング
        - マテリアル

   .. container:: half

      - 応用編

        - 空間のデータ分析
        - 空間のデータ可視化

.. revealjs-break::

.. 先程ご説明した通り、ライティングは今まで作成をしたオブジェクトに光を当てることで、光と影を表現する操作です。
.. PyVistaにはLightオブジェクトが用意されています。
.. これを設定しPlotterオブジェクトに追加することで仮想空間上の3Dオブジェクトに光を当てることが可能になっています。
.. ちなみに、Plotterオブジェクトにはデフォルトでライティングが有効になっています。
.. そのため、ライティングを新しく定義する場合はlighting='none'というオプションを指定することでデフォルトのライティングを無効にします。
.. 次に仮想3D空間に配置する光の光源位置と光源の種類を定義します。
.. この例では、光源の位置を(0, 1, 0)に設定し、光源の種類を'scene light'に設定しています。
.. この光をPlotterオブジェクトに設定すると、右のように右斜め手前から光が当てられた状態になります。

.. container:: flex-container

   .. container:: half

      .. code-block:: python

         # Plotterクラスでlightingを無効にします。
         plotter = pv.Plotter(lighting='none')

      .. code-block:: python

         # 仮想3D空間に光を配置します。
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
         mesh = pv.Cylinder()
         plotter = pv.Plotter(lighting='none')
         plotter.add_mesh(mesh, smooth_shading=True)
         light = pv.Light(position=(0, 1, 0), light_type='scene light')
         plotter.add_light(light)
         plotter.show()

マテリアル
==========

.. このように、テクスチャを使って画像を貼り付けることで質感を表現することができますが、あまりリアリティがありません。
.. そこで、背景を設定して、背景の映り込みをテクスチャとして設定することで、よりリアリティのあるCGを作成してみます。

.. container:: flex-container

   .. container:: half

      - 概要

        - PythonでCG作成

      - 基礎編

        - モデリング
        - テクスチャ
        - ライティング
        - 👉 マテリアル

   .. container:: half

      - 応用編

        - 空間のデータ分析
        - 空間のデータ可視化

スカイボックス
--------------

.. まずは、映り込みに使用する背景を表示してみましょう。
.. ゲームなどのCGを作成する際には、背景にスカイボックスを設定することが一般的です。
.. 左下の画像がスカイボックスの例です。
.. 上下左右前後の6つの面の画像を背景に設定することで全方向に背景を表示することができます。
.. PyVistaでは、download_sky_box_cube_map()関数を使って、標準のスカイボックスをダウンロードすることができます。
.. 右がスカイボックスを表示した例です。
.. 中央にサンプルの球が表示されています。
.. これを使って、背景の映り込みをテクスチャとして設定することで、よりリアリティのあるCGを作成してみます。

.. container:: flex-container

   .. container:: half

      .. code-block:: python

         from pyvista import examples as ex

         # スカイボックスをダウンロードする

         cube_map = ex.download_sky_box_cube_map()

         cube_map.plot()

      .. image::  https://upload.wikimedia.org/wikipedia/commons/b/b4/Skybox_example.png
         :alt: skybox
         :width: 400px

   .. container:: half

       .. pyvista-plot::
         :include-source: False
         :force_static:

         from pyvista import examples as ex
         cube_map = ex.download_sky_box_cube_map()
         cube_map.plot()

質感と背景の映り込み
--------------------

.. それでは、質感と背景の映り込みを追加してみましょう。
.. まずは、スカイボックスを背景に設定します。
.. その次に、背景の映込をテクスチャとして設定します。
.. 映り込みを表現する際にはオブジェクトの表面に反射する光の強さを設定する必要があります。
.. これは物理ベースレンダリングと呼ばれる手法を使って表現することができます。
.. この機能を使用するにはpbr(Physically Based Renderingの略)のフラグをTrueに設定します。

.. container:: flex-container

   .. container:: half

      .. code-block:: python

         # スカイボックスを背景に設定する
         pl.add_actor(cube_map.to_skybox())
         # 背景の映込をテクスチャとして設定する
         pl.set_environment_texture(cube_map)

         # 物理ベースレンダリングを使用して
         # 表面に反射する光の強さを設定する
         pl.add_mesh(
            mesh,
            pbr=True,
            metallic=0.8,
            roughness=0.1,
            diffuse=1
         )

   .. container:: half

       .. pyvista-plot::
         :include-source: False
         :force_static:

         import pyvista as pv
         from pyvista import examples as ex
         mesh = pv.Cylinder()
         cube_map = ex.download_sky_box_cube_map()
         pl = pv.Plotter()
         pl.add_actor(cube_map.to_skybox())
         pl.set_environment_texture(cube_map)
         pl.add_mesh(mesh, pbr=True, metallic=0.8, roughness=0.1, diffuse=1)
         pl.show(cpos="xy")

空間のデータ分析
================

.. 単にコンピュータグラフィクを表示するだけでなく、表示するオブジェクトにデータを持たせて処理をすることも可能です。

.. container:: flex-container

   .. container:: half

      - 概要

        - PythonでCG作成

      - 基礎編

        - モデリング
        - テクスチャ
        - ライティング
        - マテリアル

   .. container:: half

      - 応用編

        - 👉 空間のデータ分析
        - 空間のデータ可視化

.. revealjs-break::

.. PythonでCGを表示することができましたが、せっかくPythonを使用しているので3D空間のデータ分析を行いたい。
.. PyVistaではCGを表示するだけでなく、ポリゴンにデータを持たせてPandasのように処理をするメソッドが整備されています。

- Pythonを使用しているので3D空間のデータ分析も行いたい。
- PyVistaではポリゴンにデータを持たせてPandasのように処理をするメソッドが整備されている。

地理データの領域抽出
--------------------

.. container:: flex-container

   .. container:: half

       .. image:: https://geovista.readthedocs.io/ja/latest/_images/03ec9a185acb4a41055cab869e98ba0b2cbde1a6d237c291113bba4575595c48.png
         :width: 1000px

   .. container:: half

       .. image:: https://geovista.readthedocs.io/ja/latest/_images/988b4c4404c11e0f3097bda9f322f23f8c6ebcb797542eb665a72452a6810f11.png
         :width: 1000px

.. revealjs-break::

.. container:: flex-container

   .. container:: half

      - `threshold() <https://docs.pyvista.org/api/core/_autosummary/pyvista.datasetfilters.threshold>`__ メソッドは、メッシュ上のスカラー配列からnan値を持つセルを削除します。
        (`Region Manifold Extraction <https://geovista.readthedocs.io/ja/latest/tutorials/region-manifold-extraction.html>`__)

      .. code-block:: python

         # 海域の領域を抽出する
         sea_region = region.threshold()

   .. container:: half

       .. image:: https://geovista.readthedocs.io/ja/latest/_images/0e28e39d9b5fc24fc452e8dba12ec43fd2c59ba90a04eadd20529549800d40f0.png
         :width: 1000px

空間のデータ可視化
==================

.. さて、最後に分析結果可視化の方法について説明します。
.. 皆様は、Pythonでコードを書いて、その結果を見るときに、どのような方法を使っていますか？
.. Pythonのエコシステムは非常に豊富で、様々な結果の処理ツールがあります。
.. ここでは、Sphinx、Jupyter Notebook、Streamlitといったツールを使って、Pythonで3次元CGを作成する方法を紹介します。

.. container:: flex-container

   .. container:: half

      - 概要

        - PythonでCG作成

      - 基礎編

        - モデリング
        - テクスチャ
        - ライティング
        - マテリアル

   .. container:: half

      - 応用編

        - 空間のデータ分析
        - 👉 空間のデータ可視化

Sphinxによる可視化
------------------

.. まずは、Sphinxを使って、Pythonで3次元CGを作成する方法を説明します。
.. SphinxはPythonのドキュメントを作成するためのツールです。
.. Sphinxを使用するとPythonのコードをドキュメントに埋め込むことができます。
.. PyVistaをインストールすると、Sphinxのドキュメントにコードを埋め込むのと同じ方法でPyVistaの3D可視化のコードを埋め込むことができます。

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
            # 詳しくはsphinx-revealjsで検索！

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

.. 近年、StreamlitのようなWebUIフレームワークが注目されています。
.. PyVistaを、StreamlitやPanelを使えば、Webアプリケーションとしても可視化が可能です。
.. これにより、Pythonで3次元CGを作成する際に、より効率的に作業ができるようになります。
.. 現在、公式ではこの機能はサポートされていませんが、サードパーティ製のツールを使うことで、Webアプリケーションとしての可視化も可能です。
.. こちらは、Streamlitを使って作成したWebアプリケーションの例です。
.. stpyvistaというサードパーティ製のツールを使って、PyVistaの3D可視化をStreamlitで表示しています。

.. raw:: html

   <p align="center">
   <a href="https://stpyvista.streamlit.app"><img alt="Streamlit Cloud" src="https://raw.githubusercontent.com/edsaac/stpyvista/main/assets/stpyvista_intro_crop.gif" width="600"></a>
   </p>

ご清聴ありがとうございました
============================

.. raw:: html

    <!-- Place this tag where you want the button to render. -->
    <a class="github-button" href="https://github.com/pyvista/pyvista" data-icon="octicon-star" data-size="large" data-show-count="true" aria-label="Star pyvista/pyvista on GitHub">Star</a>
    <!-- Place this tag in your head or just before your close body tag. -->
    <script async defer src="https://buttons.github.io/buttons.js"></script>

.. |contrib.rocks| image:: https://contrib.rocks/image?repo=pyvista/pyvista
   :target: https://github.com/pyvista/pyvista/graphs/contributors
   :alt: contrib.rocks

|contrib.rocks|

.. ご清聴ありがとうございました。
.. 本日は、Pythonで3次元CGを作る方法についてお話ししました。
.. また、空間上のデータを使用して分析する方法や、可視化の方法についても説明しました。
.. この発表が皆様のお役に立てれば幸いです。
.. ご清聴ありがとうございました。
