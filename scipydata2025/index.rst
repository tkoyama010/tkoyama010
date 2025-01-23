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
