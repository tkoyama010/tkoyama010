.. |br| raw:: html

   <br>

=====================================================================
Pythonで |br| **3次元CG** を作りたい |br| 人のための **PyVista** 入門
=====================================================================

:Speaker: 小山哲央
:Date: 2024-06-20

自己紹介
========

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

+--------------------------------------+-----------------+
| **タイトル**                         | **時間**        |
+--------------------------------------+-----------------+
| モデリングをしてみよう               |                 |
+--------------------------------------+-----------------+
| テクスチャを追加してみよう           |                 |
+--------------------------------------+-----------------+
| マテリアルを追加してみよう           |                 |
+--------------------------------------+-----------------+

.. revealjs-break::

+--------------------------------------+-----------------+
| **タイトル**                         | **時間**        |
+--------------------------------------+-----------------+
| ライティングをしてみよう             |                 |
+--------------------------------------+-----------------+
| Minecraftのような洞窟を作ってみよう  |                 |
+--------------------------------------+-----------------+
| インタラクティブに可視化をしてみよう |                 |
+--------------------------------------+-----------------+

モデリングをしてみよう
======================

.. revealjs-break::

.. container:: flex-container

   .. container:: half

       * XXXXX XXXXX XXXXX XXXXX XXXXX

       .. code-block:: bash

          $ pip install pyvista

       .. code-block:: python

          import pyvista as pv

          mesh = pv.Sphere()

          mesh.plot()

   .. container:: half

       .. pyvista-plot::
           :include-source: False

           import pyvista as pv

           mesh = pv.Sphere()

           mesh.plot()


テクスチャを追加してみよう
==========================

オブジェクトの質感を表現する「テクスチャ」の方法を紹介します。

マテリアルを追加してみよう
==========================

オブジェクトの質感を表現する「マテリアル」の方法を紹介します。

ライティングをしてみよう
========================

3D空間に光を配置してオブジェクトを照らす「ライティング」の方法を紹介します。

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
