[drag=100 100, drop=center]

# PyVista Contribution 2020

## @tkoyama010

Note:

PyVista Contribution 2020というタイトルでトークをさせていただきます.
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
今回，シンポジウムでは2つのセッションでトークをします.
2回目はVTKのPythonの可視化ライブラリPyVistaについてお話します.

---

# なぜPyVistaか？

---

[drag=100 20, drop=0 0]

## VTKへのPythonicなインタフェース

[drag=45 80, drop=5 20, fit=0.5]
@code[python](opencae2020B13/test_bunny_org.py)

[drag=50 70, drop=50 20]
![height=1000](opencae2020B13/bunny.png)

[drag=15 10, drop=35 85]
↓つづく

Note:

このライブラリの最大の目標はVTKにPythonicなインタフェースを提供することです.
VTKは世界中の商用アプリケーション,研究開発,先進的な可視化アプリケーションの基盤として使われている信頼性のある可視化ライブラリです.
しかし,例えばこのstanford bunnyを使用してOBJファイルのロードとプロットを行う場合,vtk モジュールだけを使用すると大量のコードが必要になります。

---

[drag=100 20, drop=0 0]

## VTKへのPythonicなインタフェース

[drag=45 70, drop=5 20, fit=0.5]
@code[python](opencae2020B13/test_bunny.py)

[drag=50 70, drop=50 20]
![height=1000](opencae2020B13/bunny.png)

Note:

Pyvistaを使用して,同じobjファイルをロードしたりプロットすることができます:
メッシュオブジェクトはよりPython的で,コードはずっと単純です.
ガベージコレクションは自動的に処理され,ユーザがVTKプロットウィンドウを閉じた後にレンダラはクリーンアップされます.
PyVistaを使わずにvtkモジュールを直接使用するとユーザーはこれらの処理を全て自分で記述する必要があります.

---

[drag=100 20, drop=0 0]

## 対話型のプロットツール

[drag=45 70, drop=5 20, fit=0.5]
@code[python](opencae2020B13/test_widget_box.py)

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
@code[python](opencae2020B13/test_clip_box.py)
@[8-10]()

[drag=50 70, drop=50 20]
![height=1000](opencae2020B13/clip_box.png)

Note:

VTKには様々なフィルタが実装されています.
通常それらのフィルタを使用するには大量のコードが必要ですがPyVistaでは簡単にアクセスすることができます.
こちらはclip_boxというフィルタを使用した例です.
このフィルタは境界によって定義された境界ボックスによってデータセットをクリップします.
修正前の立方体meshとクリップ後のメッシュclipped_meshを比較すると正しくフィルタが処理されていることを確認できます.

---

[drag=100 10, drop=0 0]

## `matplotlib` のようなプロット

[drag=45 90, drop=5 10, fit=0.5]
@code[python](opencae2020B13/test_multi_renderers.py)

[drag=50 70, drop=50 20]
![height=1000](opencae2020B13/multi_renderers.png)

Note:

こちらはmatplotlibのようなsubplot機能を使用してVTKの各描画を行ったものです.
このような仕様のおかげでmatplotlibを使ったことのあるユーザーであれば直感的に使用することが可能です.
matplotlibでは3次元の描画は困難があるためCAEの描画を行う際にはPyVistaを使用することをおすすめします.

---

# 今年追加した機能

Note:

最後に今年追加した機能を2つご紹介します.

---

[drag=100 20, drop=0 0]

## @emoji[scissors] Shrinkフィルタ

[drag=45 70, drop=5 20, fit=0.5]
@code[python](opencae2020B13/test_shrink.py)

[drag=50 70, drop=50 20]
![height=1000](opencae2020B13/shrink.png)

Note:

1つ目はShrinkフィルタです.
このフィルタはメッシュを縮めることにより各メッシュ要素を独立して表示する機能です.
CAEの現場ではメッシュ作成の際に要素のつながりが不自然ではないかの確認に使用されます.
このメソッドに関する議論は梗概のプルリクエストで行われていますのでご興味のある方はそちらのご確認をお願いいたします.

---

[drag=100 20, drop=0 0]

## @emoji[scissors] Shrinkフィルタ

[drag=45 10, drop=5 20, fit=0.5, set=align-left]
メソッド

[drag=45 30, drop=5 30, fit=0.5]

```python
def shrink(dataset, shrink_factor=1.0, progress_bar=False):
    if not (0.0 <= shrink_factor <= 1.0):
        raise ValueError("'shrink_factor' ...")
    alg = vtk.vtkShrinkFilter()
    alg.SetInputData(dataset)
    alg.SetShrinkFactor(shrink_factor)
    _update_alg(alg, progress_bar, 'Shrinking Mesh')
    output = pyvista.wrap(alg.GetOutput())
    if isinstance(dataset, vtk.vtkPolyData):
        return output.extract_surface()
```

[drag=45 10, drop=5 20, fit=0.5, set=align-left]
テストコード

[drag=45 30, drop=5 60, fit=0.5]

```python
def test_shrink():
    mesh = pyvista.Sphere()
    shrunk = mesh.shrink(shrink_factor=0.8)
    assert shrunk.n_cells == mesh.n_cells
    assert shrunk.area < mesh.area
```

[drag=50 70, drop=50 20]
![height=1000](opencae2020B13/shrink.png)

Note:

こちらが,追加したメソッドとテストコードですメソッドはDataSetFilterクラスに追加されています.
このクラスに追加したメソッドが呼び出されると対象のDataSetオブジェクトが引数datasetに渡されそれに対してフィルタ処理を行います.
また,PyVistaはテストにpytestを使用しています.
pytestはPythonのテストライブラリで接頭辞にtestがツイている関数をテストとして実行します.
今回のテストではシュリンク前とシュリンク後セルの数が等しく,シュリンク前のメッシュの面積がシュリンク後よりも大きいことを確認しました.
この機能は2020年11月08日のVersion 0.27.0 でリリースされました.

---

[drag=100 20, drop=0 0]

## @emoji[camera] Cameraオブジェクト

[drag=45 70, drop=5 20, fit=0.5]
@code[python](opencae2020B13/test_camera_zoom.py)

[drag=50 70, drop=50 20]
![height=1000](opencae2020B13/test_camera.png)

Note:

2つ目は現在開発中の機能です.
そのため梗概には載っておりません.
PyVistaに新たにcameraオブジェクトを追加することにしました.
これはvtkCameraオブジェクトのラッパークラスであり描画の視点位置と視線方向を制御するクラスです.
こちらは飛行機のメッシュをプロットした例です.

---

[drag=100 20, drop=0 0]

## @emoji[camera] Cameraオブジェクト

[drag=45 70, drop=5 20, fit=0.5]
@code[python](opencae2020B13/test_camera_zoom.py)
@[10]()

[drag=50 70, drop=50 20]
![height=1000](opencae2020B13/test_camera_zoom.png)

Note:

例えば、こちらのようにzoomを行うとカメラがズームされます.

---

[drag=100 20, drop=0 0]

## @emoji[camera] Cameraオブジェクト

[drag=45 70, drop=5 20, fit=0.5]
@code[python](opencae2020B13/test_camera_up.py)
@[10]()

[drag=50 70, drop=50 20]
![height=1000](opencae2020B13/test_camera_up.png)

Note:

例えば、こちらのようにupを行うとカメラの描画方向のベクトルが更新されます.
現在、こちらの機能は12月31日リリース予定のVersion0.28.0の主要機能として開発中です.
Version0.28.0のマイルストーンからこちらのプルリクエストの議論を確認することができます.

---

[drag=100 20, drop=0 0]

## まとめ

[drag=100 80, drop=0 20]

### なぜPyVistaか?

- VTKへのPythonicなインタフェース
- 対話型のプロットツール
- VTKフィルタへのアクセス
- `matplotlib` のようなプロット

### 追加機能

- @emoji[scissors] Shrink フィルタ
- @emoji[camera] Camera オブジェクト

Note:

まとめです.
PyVistaの利点として

- VTKへのPythonicなインタフェース
- 対話型のプロットツール
- VTKフィルタへのアクセス
- `matplotlib` のようなプロット
  を説明しました.

また今年追加したまたは追加ている機能としてShrinkフィルタとCameraオブジェクトを追加しました.
今年からPyVistaへのコントリビューションを開始したためまだあまり貢献できていませんが、今後コミット量を増やしていきたいとかんがえています.

---

[drag=80 90, drop=10 5]
![height=2000](opencae2020B13/contributions01.png)
