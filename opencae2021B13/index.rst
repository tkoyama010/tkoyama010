.. opencae2021B13 documentation master file, created by
   sphinx-quickstart on Thu Dec  2 11:20:56 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

========================
GetFEM Contribution 2021
========================

@tkoyama010


CoFEAプロジェクトについて
=========================

- オープンソースソフトウェアの信頼性を高めるために、たくさんのベンチマーク問題と実問題が解析されます。
- シミュレーション環境を正しく設定する方法に関する情報が1箇所に集められますので、誰でも設定できます。
- スクリプトとツールによって拡張されたシミュレーションワークフローが確立され、オープンソースツールの使用が容易になります。
- オープンソース・ソフトウェアに関するメッセージがインターネット上に広がり、コミュニティーの成長を助けるでしょう。

貢献の方法
==========

あなたが貢献できる方法はたくさんあります:

- シミュレーションソフトの使い方を知っていればモデルの作成を手伝うことができます
- もしあなたが文章を書くのが得意なら、文書を書くのを手伝うことができます
- 最後に、あなたが上の何も持っていないと思っているが、熱心に学びたいと思っているなら、私たちに知らせてください!

ライセンス
==========

- CoFEA計画を目的として作成された技術的コンテンツはすべて、クリエイティブ・コモンズBY-NC-SA4.0ライセンスです。
  簡単に言えば、2つの条件下でコンテンツを共有し適応させることができます。
- コンテンツが何らかの形で共有される場合には、CoFEA計画に適切なクレジットを与えなければなりません。

音叉ベンチマーク
================

.. image:: https://cofea-ja.readthedocs.io/ja/latest/_images/fork-geo-results.png

材料特性
========

- 下の表は、解析で使用されたすべての材料特性を示しています。
  これらの特性は鋼材の挙動を再現することを目的としています。

.. csv-table::
   :header: 特性, 値, 単位

      密度 :math:`\rho` , :math:`7829.0`, :math:`kg/m^3`
      ヤング率 :math:`E` , :math:`2.07 \cdot 10^{11}`, :math:`Pa`
      ポアソン比, :math:`0.33`,

境界条件
========

これは自由体モードシミュレーションであるため、音叉に境界条件が割り当てられていません。

結果
====

- 異なる要素タイプとメッシュサイズを持つ多数のシミュレーションをチューニングモデルに対して行いました。
  次のアニメーションは、Calculixコードの結果を示しています。

.. image:: https://cofea-ja.readthedocs.io/ja/latest/_images/movie.gif

結論
====

以上の解析からいくつかの結論が得られます。

- オープンソースソフトウェアを使用して、正しい解を得ることが可能です。
- 3つのソルバーはすべて非常に類似した応答を返しましたが、CalculixとElmerが最も簡単に設定できたように思います。
  それらは追加設定なしで剛体モードを選択しました。
  一方、Code_Asterは、非剛体モードのみを検索するように設定するか( ‘Bande’ という設定で可能)、モデルを拘束する必要があります。

コードの比較
============

.. image:: https://cofea-ja.readthedocs.io/ja/latest/_images/code-comparison.png

四面体メッシュ
==============

.. image:: https://cofea-ja.readthedocs.io/ja/latest/_images/tet-comparison.png


六面体メッシュ
==============

.. image:: https://cofea-ja.readthedocs.io/ja/latest/_images/hex-comparison.png


初期化
======

.. literalinclude:: tuning_fork.py
   :language: python
   :lines: 6-12

モデルのパラメータ
==================

.. literalinclude:: tuning_fork.py
   :language: python
   :lines: 20-29

メッシュ生成その1
=================

.. literalinclude:: tuning_fork.py
   :language: python
   :lines: 35-84

メッシュ生成その2
=================

.. literalinclude:: tuning_fork.py
   :language: python
   :lines: 92-96

有限要素法と積分法の定義
========================

.. literalinclude:: tuning_fork.py
   :language: python
   :lines: 105-119

質量行列と剛性行列のアセンブリング
==================================

.. literalinclude:: tuning_fork.py
   :language: python
   :lines: 125-140

固有値解析を解く
================

.. literalinclude:: tuning_fork.py
   :language: python
   :lines: 156-209

まとめ
======

- CoFEAプロジェクトについて説明した。
- CoFEAプロジェクトにGetFEMの結果を追加した。
