.. |br| raw:: html

   <br>

=============================================================
**Scientific Python** |br| ライブラリ開発ガイド |br| を読もう
=============================================================

:Speaker: Tetsuo Koyama
:Date: 2024-01-20

お前誰よ
========

* :fab:`twitter` @tkoyama010 :fab:`github` @tkoyama010
* 研究ソフトウェアエンジニア
* Scientific Pythonライブラリ `PyVista` の開発者。
* `ARK Information Systems, INC. <https://www.ark-info-sys.co.jp/>`_ 所属

これは何よ
==========

* Pythonライブラリ開発 **ベストプラクティス** と **サイエンス** のキャッチアップ両立が大変
* **ベストプラクティス** をキャッチアップしたい

**Scientific Python** ライブラリ開発ガイド
==========================================

.. container:: flex-container

   .. container:: half

      .. only:: html
      
         .. image:: https://scientific-python.org/images/logo.svg

   .. container:: half

      * チュートリアル: ライブラリ開発の基本から始める
      * トピックガイド: ライブラリ開発の推奨ツールとベストプラクティスを学ぶ
      * このガイドは、科学者や研究ソフトウェアエンジニアのためにScientific Pythonコミュニティによって維持されています。


リポジトリレビュー
==================

- 開発リポジトリのスタイルは :bdg-link-primary-line:`repo-review <https://scientific-python.github.io/repo-review/index.html>`  で確認できます。
- 今回はレビューのルールをもとに開発ガイドを説明します。

リポジトリレビュー: General
===========================

* :bdg-link-primary-line:`PY001 <https://learn.scientific-python.org/development/guides/packaging-simple#PY001>` : Has a pyproject.toml
* :bdg-link-primary-line:`PY002 <https://learn.scientific-python.org/development/guides/packaging-simple#PY002>` : Has a README.(md|rst) file
* :bdg-link-primary-line:`PY003 <https://learn.scientific-python.org/development/guides/packaging-simple#PY003>` : Has a LICENSE* file
* :bdg-link-primary-line:`PY004 <https://learn.scientific-python.org/development/guides/packaging-simple#PY004>` : Has docs folder
* :bdg-link-primary-line:`PY005 <https://learn.scientific-python.org/development/guides/packaging-simple#PY005>` : Has tests folder
* :bdg-link-primary-line:`PY006 <https://learn.scientific-python.org/development/guides/style#PY006>` : Has pre-commit config
* :bdg-link-primary-line:`PY007 <https://learn.scientific-python.org/development/guides/tasks#PY007>` : Supports an easy task runner (nox or tox)
