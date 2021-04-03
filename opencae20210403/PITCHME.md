[drag=100 100, drop=center]

# PyVista Contribution 2021 Jan-Mar
## @tkoyama010

Note:

PyVista Contribution 2021 Jan-Marというタイトルでトークをさせていただきます.
よろしくお願いいたします.

---
[drag=20 20, drop=15 0]
![height=200](https://avatars3.githubusercontent.com/u/7513610?s=400&u=3a29937127b197c7181f08901441c800271b5ba0&v=4)

[drag=50 20, drop=35 0]
## Tetsuo Koyama

[drag=25 5, drop=15 20]
@fa[twitter] @fa[github] tkoyama010

[drag=15 5, drop=40 20]
![height=50](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=python&logoColor=white&color=2bbc8a)

[drag=15 5, drop=55 20]
![height=50](https://img.shields.io/badge/Code-C++-informational?style=flat&logo=c%2B%2B&logoColor=white&color=2bbc8a)

[drag=15 5, drop=70 20]
![height=50](https://img.shields.io/badge/Editors-Vim-informational?style=flat&logoColor=white&color=2bbc8a)

[drag=30 60, drop=5 30]
![height=1000](https://s2.booth.pm/11310e3f-8ea5-4a2e-921b-350dbd11b9c3/i/1304104/5bbe6711-286a-4071-98f8-7e31a3b77b48_base_resized.jpg)

[drag=30 60, drop=35 30]
![height=1000](https://s2.booth.pm/11310e3f-8ea5-4a2e-921b-350dbd11b9c3/i/1574241/bbb0e33d-9969-4282-9f2d-389a043ed863_base_resized.jpg)

[drag=30 60, drop=65 30]
![height=1000](https://s2.booth.pm/11310e3f-8ea5-4a2e-921b-350dbd11b9c3/i/1727985/518a6acb-ae4b-40a1-9a1c-2ae04e9497fc_base_resized.jpg)

Note:

まずは自己紹介をさせてください.
tkoyama010というアカウントでOSS活動しています.
TwitterアカウントとGitHubアカウントは同じです.
フォローよろしくお願いたします.
私は有限要素法のソフトウェア実装とコンピューターグラフィックスによる視覚化に興味があります.
GitHubでのOSS活動の他に技術同人誌としてGetFEMというライブラリの本を執筆しています.
Twitterの固定ツイートからリンクが辿れるようになっていますのでご興味のある方はそちらをご覧ください.
最近，PyVistaという可視化ライブラリのOSSの開発に開発者チームとして参加しています．
今回はそれについてお話します．

---
# なぜPyVistaか？

Note:
まずはPyVistaが何を目指しているのかご説明します．

---
[drag=100 20, drop=0 0]
## VTKへのPythonicなインタフェース

[drag=45 80, drop=5 20, fit=0.5]
@code[python](opencae20210403/test_bunny_org.py)

[drag=50 70, drop=50 20]
![height=1000](opencae20210403/bunny.png)

[drag=15 10, drop=35 85]
つづく

Note:

このライブラリの最大の目標はVTKにPythonicなインタフェースを提供することです.
VTKは世界中の商用アプリケーション,研究開発,先進的な可視化アプリケーションの基盤として使われている信頼性のある可視化ライブラリです.
しかし,例えばこのstanford bunnyを使用してOBJファイルのロードとプロットを行う場合,vtk モジュールだけを使用すると大量のコードが必要になります。

---
[drag=100 20, drop=0 0]
## VTKへのPythonicなインタフェース

[drag=45 70, drop=5 20, fit=0.5]
@code[python](opencae20210403/test_bunny.py)

[drag=50 70, drop=50 20]
![height=1000](opencae20210403/bunny.png)

Note:

Pyvistaを使用して,同じobjファイルをロードしたりプロットすることができます:
メッシュオブジェクトはよりPython的で,コードはずっと単純です.
ガベージコレクションは自動的に処理され,ユーザがVTKプロットウィンドウを閉じた後にレンダラはクリーンアップされます.
PyVistaを使わずにvtkモジュールを直接使用するとユーザーはこれらの処理を全て自分で記述する必要があります.

---
[drag=100 20, drop=0 0]
## 対話型のプロットツール

[drag=45 70, drop=5 20, fit=0.5]
@code[python](opencae20210403/test_widget_box.py)

[drag=50 70, drop=50 20]
![](https://pyvista-doc.readthedocs.io/ja/latest/_images/box-clip.gif)

Note:

また,PyVistaには,クリッピング,スライス,および閾値などのフィルタを制御するためにレンダリングシーンに追加できるいくつかのウィジェットがあります.
具体的には,ボックス,プレーン,およびラインまたはスライダバーの位置を制御するウィジェットがあり,これらはすべてカスタムコールバック関数を使用して高度にカスタマイズできます.
こちらに示した例はボックスウィジェットです.

---
[drag=100 20, drop=0 0]
## VTKフィルタへのアクセス

[drag=45 70, drop=5 20, fit=0.5]
@code[python](opencae20210403/test_clip_box.py)
@[8-10]()

[drag=50 70, drop=50 20]
![height=1000](opencae20210403/clip_box.png)

Note:

VTKには様々なフィルタが実装されています.
通常それらのフィルタを使用するには大量のコードが必要ですがPyVistaでは簡単にアクセスすることができます.
こちらはclip_boxというフィルタを使用した例です.
このフィルタは境界によって定義された境界ボックスによってデータセットをクリップします.
修正前の立方体meshとクリップ後のメッシュclipped_meshを比較すると正しくフィルタが処理されていることを確認できます.

---
[drag=100 10, drop=0 0]
## ```matplotlib``` のようなプロット

[drag=45 90, drop=5 10, fit=0.5]
@code[python](opencae20210403/test_multi_renderers.py)

[drag=50 70, drop=50 20]
![height=1000](opencae20210403/multi_renderers.png)

Note:

こちらはmatplotlibのようなsubplot機能を使用してVTKの各描画を行ったものです.
このような仕様のおかげでmatplotlibを使ったことのあるユーザーであれば直感的に使用することが可能です.
matplotlibでは3次元の描画は困難があるためCAEの描画を行う際にはPyVistaを使用することをおすすめします.

---
# 1月から3月までに追加した機能

Note:

最後に1月から3月までに追加した機能を3つご紹介します.
以下のスライドでは左がPythonの全ソース，右がそれによりプロットできる図となります.

---
[drag=100 20, drop=0 0]
## ジオメトリオブジェクト

[drag=45 70, drop=5 20, fit=0.5]
@code[python](opencae20210403/test_geometric_objects.py)

[drag=50 70, drop=50 20]
![height=1000](opencae20210403/geometric_objects.png)


Note:
PyVistaには，単純なジオメトリオブジェクトを生成する関数がいくつかあります．
既存のジオメトリオブジェクトにはここにプロットした円柱・矢印・球・平面・線分・ボックスなどがあります．

---
[drag=100 20, drop=0 0]
## 四角錐・円弧ジオメトリ作成機能

[drag=45 70, drop=5 20, fit=0.5]
@code[python](opencae20210403/test_pyramid.py)

[drag=50 70, drop=50 20]
![height=1000](opencae20210403/pyramid.png)

Note:

今回新しく四角錐・円弧ジオメトリ作成機能を追加しました.
Pyramid関数は5点で定義される角錐を作成します．
角錐の点．最初の4つの点が四角形の面上の反時計回りの4つの点になり，最後の点が頂点になるように，点が順序付けられます．
CircularArcFromNormal関数は中心とベクトルを指定することで円弧を作成します．

---
[drag=100 20, drop=0 0]
## 押出し回転機能

[drag=45 70, drop=5 20, fit=0.5]
@code[python](opencae20210403/test_extrude_rotate.py)

[drag=50 70, drop=50 20]
![height=1000](opencae20210403/extrude_rotate.png)

Note:
また，2つ目の機能追加としてジオメトリを使用した押出し回転機能も追加しました．
この機能では，フリーエッジとフリーラインから面を作成し，頂点からラインを作成して，ポリゴンデータを押出します．
たとえば，線分をスイープすると円柱シェルが作成され，円をスイープするとトーラスが作成されます．
このフィルタは，円柱，ボトル，ワイングラスなどの軸対称オブジェクトのモデリングに使用できます．
または，スプリングやコルク抜きなどの移動/回転対称オブジェクトなども作成できます．

---
[drag=100 20, drop=0 0]
## 線上のサンプリング値プロット機能

[drag=45 70, drop=5 20, fit=0.5]
@code[python](opencae20210403/test_plot_over_line1.py)

[drag=50 70, drop=50 20]
![height=1000](opencae20210403/plot_over_line1.png)

Note:
さらに，PyVistaでは既存の機能として線上のサンプリング値プロット機能があります．
この機能は，こちらに示すようなコンター図があった場合，ユーザーが指定した線に沿ってデータセットをサンプリングし，プロットします．
右の図はPyVistaに用意されているデータ例です．
A点とB点の間で指定した線に沿ってデータをサンプリングします．

---
[drag=100 20, drop=0 0]
## 線上のサンプリング値プロット機能

[drag=45 70, drop=5 20, fit=0.5]
@code[python](opencae20210403/test_plot_over_line2.py)

[drag=50 70, drop=50 20]
![height=1000](opencae20210403/plot_over_line2.png)

Note:
先程ご説明した線のジオメトリオブジェクトを使用したメソッドsample_over_lineを使用してデータをサンプリングしています．
取得したデータはnumpy配列で返されるためmatplotlibで右図のように可視化することができます．

---
[drag=100 20, drop=0 0]
## 円弧上のサンプリング値プロット機能

[drag=45 80, drop=5 20, fit=0.5]
@code[python](opencae20210403/test_plot_over_circular_arc1.py)

[drag=50 70, drop=50 20]
![height=1000](opencae20210403/plot_over_circular_arc1.png)

Note:
同様のことを先程説明した円弧のジオメトリックオブジェクトを使用して行います．
こちらが3つ目の機能です．
右の図はPyVistaに用意されている別のデータ例です．
A点とB点の間で指定した円弧に沿ってデータをサンプリングします．

---
[drag=100 20, drop=0 0]
## 円弧上のサンプリング値プロット機能

[drag=45 70, drop=5 20, fit=0.5]
@code[python](opencae20210403/test_plot_over_circular_arc2.py)

[drag=50 70, drop=50 20]
![height=1000](opencae20210403/plot_over_circular_arc2.png)

Note:
先程ご説明した円弧のジオメトリオブジェクトを使用したメソッドsample_over_circular_arc_normalを使用してデータをサンプリングしています．
取得したデータはnumpy配列で返されるためmatplotlibで右図のように可視化することができます．

---
[drag=100 20, drop=0 0]
## まとめ

[drag=100 80, drop=0 20]
### なぜPyVistaか?
- VTKへのPythonicなインタフェース
- 対話型のプロットツール
- VTKフィルタへのアクセス
- ```matplotlib``` のようなプロット

### 追加機能
- 四角錐・円弧ジオメトリ作成機能
- 押出し回転機能
- 円弧上のサンプリング値プロット機能

Note:
まとめです.
PyVistaの利点として
- VTKへのPythonicなインタフェース
- 対話型のプロットツール
- VTKフィルタへのアクセス
- ```matplotlib``` のようなプロット
を説明しました.

また今年追加した3つの機能について説明をしました.
PyVistaにご興味のある方はご使用・ご感想をお待ちしております．
