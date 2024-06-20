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

- PythonでCGを作るのに必要なこと
- モデリングをしてみよう
- テクスチャを追加してみよう
- マテリアルを追加してみよう
- ライティングをしてみよう
- 空間のデータ分析をしてみよう
- インタラクティブに可視化をしてみよう

PythonでCGを作るのに必要なこと
==============================

.. CGを作るのが初めての方もいるかもしれません。
.. そこで、まずはPythonでCGを作るのに必要なことについて説明します。

- 👉 PythonでCGを作るのに必要なこと
- モデリングをしてみよう
- テクスチャを追加してみよう
- マテリアルを追加してみよう
- ライティングをしてみよう
- 空間のデータ分析をしてみよう
- インタラクティブに可視化をしてみよう

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

インストール
============

.. インストールは、pipコマンドでインストールすることが可能です。
.. condaコマンドのパッケージも用意はされていますが、pipでインストールするのが一般的です。
.. 標準ではJupyterの拡張機能がインストールされませんが、Allというオプションをつけることで拡張をインストールすることができます。

.. code-block:: bash

   $ pip install "pyvista[all]"

モデリングをしてみよう
======================

.. それでは、始めましょう。
.. まずは、モデリングの方法について説明します。

- PythonでCGを作るのに必要なこと
- 👉 モデリングをしてみよう
- テクスチャを追加してみよう
- マテリアルを追加してみよう
- ライティングをしてみよう
- 空間のデータ分析をしてみよう
- インタラクティブに可視化をしてみよう

.. revealjs-break::

.. Pythonを起動して、PyVistaをインポートします。
.. Pythonのライブラリには、

.. container:: flex-container

   .. container:: half

      .. code-block:: python

         # PyVistaをインポートする。

         import pyvista as pv

      .. code-block:: python

         # 円柱のモデルを作成する。

         mesh = pv.Cylinder()

      .. code-block:: python

         # 球体のモデルを描画する。

         mesh.plot()

   .. container:: half

      .. pyvista-plot::
         :include-source: False

         import pyvista as pv
         mesh = pv.Cylinder()
         mesh.plot()

.. revealjs-break::

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

- PythonでCGを作るのに必要なこと
- モデリングをしてみよう
- 👉 テクスチャを追加してみよう
- マテリアルを追加してみよう
- ライティングをしてみよう
- 空間のデータ分析をしてみよう
- インタラクティブに可視化をしてみよう

.. revealjs-break::

.. テクスチャは、先ほどご説明申し上げた通り、物体をよりリアリティのあるように見せるために表面に画像を追加をするという操作CG上の操作です。
.. ここでは、テクスチャマッピングという方法を使用して、オブジェクトに画像を貼り付けます。
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

マテリアルを追加してみよう
==========================

.. このように、テクスチャを使って画像を貼り付けることで質感を表現することができますが、あまりリアリティがありません。
.. そこで、背景を設定して、背景の映り込みをテクスチャとして設定することで、よりリアリティのあるCGを作成してみます。

- PythonでCGを作るのに必要なこと
- モデリングをしてみよう
- テクスチャを追加してみよう
- 👉 マテリアルを追加してみよう
- ライティングをしてみよう
- 空間のデータ分析をしてみよう
- インタラクティブに可視化をしてみよう

スカイボックスを表示してみよう
------------------------------

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

質感と背景の映り込みを追加してみよう
------------------------------------

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

ライティングをしてみよう
========================

.. 次にライティングについてご説明をします。

- PythonでCGを作るのに必要なこと
- モデリングをしてみよう
- テクスチャを追加してみよう
- マテリアルを追加してみよう
- 👉 ライティングをしてみよう
- 空間のデータ分析をしてみよう
- インタラクティブに可視化をしてみよう

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

空間のデータ分析をしてみよう
============================

.. 単にコンピュータグラフィクを表示するだけでなく、表示するオブジェクトにデータを持たせて処理をすることも可能です。

- PythonでCGを作るのに必要なこと
- モデリングをしてみよう
- テクスチャを追加してみよう
- マテリアルを追加してみよう
- ライティングをしてみよう
- 👉 空間のデータ分析をしてみよう
- インタラクティブに可視化をしてみよう

.. revealjs-break::

.. PythonでCGを表示することができましたが、せっかくPythonを使用しているので3D空間のデータ分析を行いたい。
.. PyVistaではCGを表示するだけでなく、ポリゴンにデータを持たせてPandasのように処理をするメソッドが整備されています。

- Pythonを使用しているので3D空間のデータ分析も行いたい。
- PyVistaではポリゴンにデータを持たせてPandasのように処理をするメソッドが整備されている。

Minecraftのような洞窟を作ってみよう
-----------------------------------

.. ここでは、グリッド状に並んだポリゴンを作成し、MineCraftのような洞窟を作成してみます。
.. Mincraftでは、ランダムな地形を生成するためにデータが使用されています。
.. 今回はそれらのデータがこちらのコードのdataという変数に格納されているとします。
.. 準備したグリッドをplot()関数で表示すると、右のようにデータの値がコンターとなって表示されます。
.. グリッドの中で値が小さいポリゴンを削除してMineCraftのような洞窟を作成してみます。

.. container:: flex-container

   .. container:: half

       .. code-block:: python

          # 右図のグリッドを構成するポリゴンの数
          >>> grid.number_of_points
          180999

          # 各点の値のデータを定義したNumPy配列
          >>> data
          array([-0.29131388, ...])

          # サイズはポリゴンの数と同じであることを確認
          >>> len(data)
          180999

       .. code-block:: python

          # 辞書のように定義できます
          >>> grid['data'] = data
          >>> grid['data']
          pyvista_ndarray([-0.29131388, ...])

   .. container:: half

       .. pyvista-plot::
          :include-source: False

          import pyvista as pv

          noise = pv.perlin_noise(amplitude=1, freq=(1, 1, 1), phase=(0, 0, 0))
          grid = pv.sample_function(noise, [0, 3.0, -0, 1.0, 0, 1.0], dim=(120, 40, 40))
          grid = grid.point_data_to_cell_data()

          clim = (0.0, grid['scalars'].max())
          grid.plot(
              cmap='gist_earth_r',
              background='white',
              show_scalar_bar=True,
              lighting=True,
              clim=clim,
              show_edges=True,
              n_colors=20,
          )

.. revealjs-break::

.. 値が大きい部分を抽出するには、threshold()メソッドを使用して値が0.02より大きい部分を抽出することができます。
.. その結果値の小さい部分が削除され、右のように洞窟のようなポリゴンが表示されます。
.. このように、PyVistaを使って、グリッドごとのデータを作成し、洞窟のような形状を作成することができます。
.. この例を通して、PyVistaを使ってデータを持たせたオブジェクトを作成しその値をもとに処理をする方法を学ぶことができます。

.. container:: flex-container

   .. container:: half

       .. code-block:: python

          # データの最小値と最大値を取得
          >>> grid['data'].min()
          -0.85
          >>> grid['data'].max()
          0.903

       .. code-block:: python

          # データが0.0565より大きいグリッドを抽出
          out = grid.threshold(value=0.0565)

       .. code-block:: python

          # 抽出後の最小値と最大値を取得
          >>> out['data'].min()
          0.0565
          >>> out['data'].max()
          0.903

   .. container:: half

       .. pyvista-plot::
          :include-source: False

          import pyvista as pv

          noise = pv.perlin_noise(amplitude=1, freq=(1, 1, 1), phase=(0, 0, 0))
          grid = pv.sample_function(noise, [0, 3.0, -0, 1.0, 0, 1.0], dim=(120, 40, 40))
          grid = grid.point_data_to_cell_data()

          out = grid.threshold(0.0565)
          clim = (0.0, out['scalars'].max())
          out.plot(
              cmap='gist_earth_r',
              background='white',
              show_scalar_bar=True,
              lighting=True,
              clim=clim,
              show_edges=True,
              n_colors=20,
          )

インタラクティブに可視化をしてみよう
====================================

.. さて、最後にインタラクティブな可視化の方法について説明します。
.. 皆様は、Pythonでコードを書いて、その結果を見るときに、どのような方法を使っていますか？
.. Pythonのエコシステムは非常に豊富で、様々な結果の処理ツールがあります。
.. ここでは、Sphinx、Jupyter Notebook、Streamlitといったツールを使って、Pythonで3次元CGを作成する方法を紹介します。

- PythonでCGを作るのに必要なこと
- モデリングをしてみよう
- テクスチャを追加してみよう
- マテリアルを追加してみよう
- ライティングをしてみよう
- 空間のデータ分析をしてみよう
- 👉 インタラクティブに可視化をしてみよう

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
.. また、空間上のデータを使用して、Minecraftのような洞窟を作成する方法や、インタラクティブな可視化の方法についても説明しました。
.. この発表が皆様のお役に立てれば幸いです。
.. ご清聴ありがとうございました。
