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
* ベストプラクティスを **効率的に** キャッチアップしたい

**Scientific Python** ライブラリ開発ガイド
==========================================

.. container:: flex-container

   .. container:: half

      .. only:: html
      
         .. image:: https://scientific-python.org/images/logo.svg

   .. container:: half

      * チュートリアル: ライブラリ開発の基本から始める
      * トピックガイド: ライブラリ開発の推奨ツールとベストプラクティスを学ぶ
      * 科学者や研究ソフトウェアエンジニアのためにScientific Pythonコミュニティによって維持されています。


リポジトリレビュー
==================

- 開発リポジトリのスタイルは :bdg-link-primary-line:`repo-review <https://scientific-python.github.io/repo-review/index.html>`  で確認できます。
- 今回はレビューのチェックリストをもとに開発ガイドを説明します。

リポジトリレビュー: General
===========================

* :bdg-link-primary-line:`PY001 <https://learn.scientific-python.org/development/guides/packaging-simple#PY001>` : Has a pyproject.toml
* :bdg-link-primary-line:`PY002 <https://learn.scientific-python.org/development/guides/packaging-simple#PY002>` : Has a README.(md|rst) file
* :bdg-link-primary-line:`PY003 <https://learn.scientific-python.org/development/guides/packaging-simple#PY003>` : Has a LICENSE* file
* :bdg-link-primary-line:`PY004 <https://learn.scientific-python.org/development/guides/packaging-simple#PY004>` : Has docs folder
* :bdg-link-primary-line:`PY005 <https://learn.scientific-python.org/development/guides/packaging-simple#PY005>` : Has tests folder
* :bdg-link-primary-line:`PY006 <https://learn.scientific-python.org/development/guides/style#PY006>` : Has pre-commit config
* :bdg-link-primary-line:`PY007 <https://learn.scientific-python.org/development/guides/tasks#PY007>` : Supports an easy task runner (nox or tox)

リポジトリレビュー: PyProject
=============================

* :bdg-link-primary-line:`PP002 <https://learn.scientific-python.org/development/guides/packaging-simple#PP002>` : Has a proper build-system table
* :bdg-link-primary-line:`PP003 <https://learn.scientific-python.org/development/guides/packaging-classic#PP003>` : Does not list wheel as a build-dep
* :bdg-link-primary-line:`PP301 <https://learn.scientific-python.org/development/guides/pytest#PP301>` : Has pytest in pyproject
* :bdg-link-primary-line:`PP302 <https://learn.scientific-python.org/development/guides/pytest#PP302>` : Sets a minimum pytest to at least 6
* :bdg-link-primary-line:`PP303 <https://learn.scientific-python.org/development/guides/pytest#PP303>` : Sets the test paths
* :bdg-link-primary-line:`PP304 <https://learn.scientific-python.org/development/guides/pytest#PP304>` : Sets the log level in pytest
* :bdg-link-primary-line:`PP305 <https://learn.scientific-python.org/development/guides/pytest#PP305>` : Specifies xfail_strict

.. revealjs-break::

* :bdg-link-primary-line:`PP306 <https://learn.scientific-python.org/development/guides/pytest#PP306>` : Specifies strict config
* :bdg-link-primary-line:`PP307 <https://learn.scientific-python.org/development/guides/pytest#PP307>` : Specifies strict markers
* :bdg-link-primary-line:`PP308 <https://learn.scientific-python.org/development/guides/pytest#PP308>` : Specifies useful pytest summary
* :bdg-link-primary-line:`PP309 <https://learn.scientific-python.org/development/guides/pytest#PP309>` : Filter warnings specified

リポジトリレビュー: Documentation
=================================

* :bdg-link-primary-line:`RTD100 <https://learn.scientific-python.org/development/guides/docs#RTD100>` : Uses ReadTheDocs (pyproject config)
* :bdg-link-primary-line:`RTD101 <https://learn.scientific-python.org/development/guides/docs#RTD101>` : You have to set the RTD version number to 2
* :bdg-link-primary-line:`RTD102 <https://learn.scientific-python.org/development/guides/docs#RTD102>` : You have to set the RTD build image
* :bdg-link-primary-line:`RTD103 <https://learn.scientific-python.org/development/guides/docs#RTD103>` : You have to set the RTD python version

リポジトリレビュー: GitHub Actions
==================================

* :bdg-link-primary-line:`GH100 <https://learn.scientific-python.org/development/guides/gha-basic#GH100>` : Has GitHub Actions config
* :bdg-link-primary-line:`GH101 <https://learn.scientific-python.org/development/guides/gha-basic#GH101>` : Has nice names
* :bdg-link-primary-line:`GH102 <https://learn.scientific-python.org/development/guides/gha-basic#GH102>` : Auto-cancel on repeated PRs
* :bdg-link-primary-line:`GH103 <https://learn.scientific-python.org/development/guides/gha-basic#GH103>` : At least one workflow with manual dispatch trigger
* :bdg-link-primary-line:`GH104 <https://learn.scientific-python.org/development/guides/gha-wheel#GH104>` : Use unique names for upload-artifact
* :bdg-link-primary-line:`GH200 <https://learn.scientific-python.org/development/guides/gha-basic#GH200>` : Maintained by Dependabot
* :bdg-link-primary-line:`GH210 <https://learn.scientific-python.org/development/guides/gha-basic#GH210>` : Maintains the GitHub action versions with Dependabot

.. revealjs-break::

* :bdg-link-primary-line:`GH211 <https://learn.scientific-python.org/development/guides/gha-basic#GH211>` : Do not pin core actions as major versions
* :bdg-link-primary-line:`GH212 <https://learn.scientific-python.org/development/guides/gha-basic#GH212>` : Require GHA update grouping

リポジトリレビュー: MyPy
========================

* :bdg-link-primary-line:`MY100 <https://learn.scientific-python.org/development/guides/style#MY100>` : Uses MyPy (pyproject config)
* :bdg-link-primary-line:`MY101 <https://learn.scientific-python.org/development/guides/style#MY101>` : MyPy strict mode
* :bdg-link-secondary-line:`MY102` : MyPy show_error_codes deprecated
* :bdg-link-primary-line:`MY103 <https://learn.scientific-python.org/development/guides/style#MY103>` : MyPy warn unreachable
* :bdg-link-primary-line:`MY104 <https://learn.scientific-python.org/development/guides/style#MY104>` : MyPy enables ignore-without-code
* :bdg-link-primary-line:`MY105 <https://learn.scientific-python.org/development/guides/style#MY105>` : MyPy enables redundant-expr
* :bdg-link-primary-line:`MY106 <https://learn.scientific-python.org/development/guides/style#MY106>` : MyPy enables truthy-bool

リポジトリレビュー: Pre-commit
==============================

* :bdg-link-primary-line:`PC100 <https://learn.scientific-python.org/development/guides/style#PC100>` : Has pre-commit-hooks
* :bdg-link-primary-line:`PC110 <https://learn.scientific-python.org/development/guides/style#PC110>` : Uses black or ruff-format
* :bdg-link-primary-line:`PC111 <https://learn.scientific-python.org/development/guides/style#PC111>` : Uses blacken-docs
* :bdg-link-primary-line:`PC140 <https://learn.scientific-python.org/development/guides/style#PC140>` : Uses mypy
* :bdg-link-primary-line:`PC160 <https://learn.scientific-python.org/development/guides/style#PC160>` : Uses codespell
* :bdg-link-primary-line:`PC170 <https://learn.scientific-python.org/development/guides/style#PC170>` : Uses PyGrep hooks (only needed if RST present)
* :bdg-link-primary-line:`PC180 <https://learn.scientific-python.org/development/guides/style#PC180>` : Uses prettier

.. revealjs-break::

* :bdg-link-primary-line:`PC190 <https://learn.scientific-python.org/development/guides/style#PC190>` : Uses Ruff
* :bdg-link-primary-line:`PC191 <https://learn.scientific-python.org/development/guides/style#PC191>` : Ruff show fixes if fixes enabled
* :bdg-link-primary-line:`PC901 <https://learn.scientific-python.org/development/guides/style#PC901>` : Custom pre-commit CI message

リポジトリレビュー: Ruff
========================

* :bdg-link-primary-line:`RF001 <https://learn.scientific-python.org/development/guides/style#RF001>` : Has Ruff config
* :bdg-link-primary-line:`RF002 <https://learn.scientific-python.org/development/guides/style#RF002>` : Target version must be set
* :bdg-link-primary-line:`RF003 <https://learn.scientific-python.org/development/guides/style#RF003>` : src directory specified if used
* :bdg-link-primary-line:`RF101 <https://learn.scientific-python.org/development/guides/style#RF101>` : Bugbear must be selected
* :bdg-link-primary-line:`RF102 <https://learn.scientific-python.org/development/guides/style#RF102>` : isort must be selected
* :bdg-link-primary-line:`RF103 <https://learn.scientific-python.org/development/guides/style#RF103>` : pyupgrade must be selected
* :bdg-link-secondary-line:`RF201`: Avoid using deprecated config settings

.. revealjs-break::

* :bdg-link-secondary-line:`RF202`: Use (new) lint config section

まとめ
======

- 開発リポジトリのスタイルは :bdg-link-primary-line:`repo-review <https://scientific-python.github.io/repo-review/index.html>`  で確認できます。
- レビューチェックリストをもとに開発ガイドを読むことで、ベストプラクティスのキャッチアップが **効率的に** できます。
