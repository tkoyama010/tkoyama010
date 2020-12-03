[drag=100 100, drop=center]

# GetFEM Contribution 2020
## Tetsuo Koyama

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
tkoyama010というアカウントでOSSを活動しています.
TwitterアカウントとGitHubアカウントは同じです.
フォローよろしくお願いたします.
私は有限要素法のソフトウェア実装とコンピューターグラフィックスによる視覚化に興味があります.
GitHubでのOSS活動の他に技術同人誌としてGetFEMというライブラリの本を執筆しています.
Twitterの固定ツイートからリンクが辿れるようになっていますのでご興味のある方はそちらをご覧ください.
今回，シンポジウムでは2つのセッションでトークをします.
1日目の今日は有限要素法ライブラリGetFEMについてお話します.

---
[drag=100 20, drop=0 0]
## GetFEMとは?

[drag=45 10, drop=5 20]
### ライブラリの構造

[drag=45 60, drop=5 30]
![height=500](https://getfem.readthedocs.io/en/latest/_images/getfem_structure1.png)

[drag=50 60, drop=50 30]
![height=500](https://getfem.readthedocs.io/en/latest/_images/tripod.png)

Note:

GetFEMは共同開発をベースとしたオープンソースのライブラリです．
有限要素法を用いて線形および非線形偏微分方程式の連成モデルを解くための最も柔軟な枠組みを提供することを目的としています．
このライブラリの大きな特徴として,有限要素法ライブラリのオブジェクトと積分法のオブジェクトが分離されていることが上げられます．
今回は簡単な例を通して，このライブラリにより従来の有限要素法プログラムと比較して柔軟なパラスタの実装が可能であることを説明します．

---
[drag=100 50, drop=0 0]
# 片持はりの問題
[drag=100 50, drop=0 50]
![height=50](./opencae2020B02/badge.svg)
![height=50](https://cdn.pixabay.com/photo/2016/04/22/14/31/mouse-1345876_960_720.png)

Note:

対象とする問題は片持はりの問題で，GetFEMのPythonインターフェースで実装を行います．
GetFEMは他にScilab・Matlab・Octave・C++のインターフェースもあり，そちらで同様に実装することも可能です．
使用したDockerfileのURLは梗概にあります．
ローカルにインストールせずにこの例を実行したい場合は，梗概にあるこちらのピンクのボタンをクリックすることでJupyterをクラウドで実行できます．

---
[drag=100 20, drop=0 0, set=align-center]
### 片持はりの問題のパラメータ

[drag=45 70, drop=5 20, set=align-left]
- 幾何条件
$L=10mm$
- 境界条件
$P=-1.0 N/mm^2$
- 材料条件
$E=10000 N/mm^2$, $\nu = 0.0$

[drag=50 70, drop=50 20]
![height=500](http://kentiku-kouzou.jp/kouzourikigaku/katamotitawami/1.png)

Note:

片持はりの形状寸法は，長さL=10mm，高さh=1mm，奥行き1mmです．
ポアソン効果を無視するため，ポアソン比は0.0としています．

---
[drag=100 20, drop=0 0, set=align-center]
### 片持はり問題のパラメータ

[drag=100 80, drop=0 20, set=align-center]
| 要素            | 1x4 メッシュ | 4x2 メッシュ | 4x4 メッシュ | 16x8 メッシュ |
| --------------- | ------------ | ------------ | ------------ | ------------- |
| 2次要素         | case11       | case12       | case13       | case14        |
| 1次完全積分要素 | case21       | case22       | case23       | case24        |
| 1次低減積分要素 | case31       | case32       | case33       | case34        |
| 1次非適合要素   | case41       | case42       | case43       | case44        |

Note:

メッシュと有限要素法と積分法が異なる16ケースを計算しました．
使用する要素は2次要素・1次完全積分要素・1次低減積分要素・1次非適合要素の4種類です．
メッシュは縦方向と横方向がそれぞれ1x4，4x2，4x4，16x8のメッシュを使用しました．
それぞれのケースの操作は同じですので，各オブジェクトの配列を作成してforループで操作をします．

---
[drag=100 20, drop=0 0, set=align-center]
### メッシュ生成

[drag=45 70, drop=5 20, set=align-left, fit=0.6]
@code[python](opencae2020B02/mesh_generation.py)

[drag=50 70, drop=50 20]
![height=700](https://getfem-examples.readthedocs.io/en/latest/_images/cantilever_13_0.png)

Note:

まず，Meshオブジェクトを作成します．
xsとysは，長さと高さ方向の配列のメッシュ分割数とします．
"cartesian"コマンドをコンストラクタで指定することで構造化メッシュをすばやく構築することができます．

---
[drag=100 20, drop=0 0, set=align-center]
### 有限要素法の定義

[drag=45 70, drop=5 20, set=align-left, fit=0.6]
@code[python](opencae2020B02/definition_of_finite_elements_methods.py)

[drag=50 80, drop=50 20, set=align-center, fit=0.6]
| 要素                  | 有限要素法(1次元)             |
| --------------------- | ----------------------------- |
| **2次**完全積分要素       | FEM_PK(1,2)                   |
| **1次**完全積分要素       | FEM_PK(1,1)                   |
| **1次**低減積分要素       | FEM_PK(1,1)                   |
| **1次非適合**完全積分要素 | FEM_PK_WITH_CUBIC_BUBBLE(1,1) |

Note:

片持はりの変位を近似するMeshFEMオブジェクトを用いて各メッシュの有限要素法を定義します．
FEM_PK(1,2)は2次多項式を持つ1次元の単体に対する古典的Lagrange法です．
同様に，FEM_PK(1,1)は1次多項式を持つ1次元の単体に対する古典的Lagrange法です．
さらに，FEM_PK_WITH_CUBIC_BUBBLE(1,1)は気泡関数を追加した1次多項式を持つ1次元の単体に対する古典的Lagrange法です．
GetFEMは1次元の有限要素法を使いFEM_PRODUCTを宣言することで2次の有限要素法を宣言することが可能です．

---
[drag=100 20, drop=0 0, set=align-center]
### 積分法の定義

[drag=45 70, drop=5 20, set=align-left, fit=0.6]
@code[python](opencae2020B02/definition_of_integration_methods.py)

[drag=50 80, drop=50 20, set=align-center, fit=0.6]
| 要素                  | 積分法(1次元) |
| --------------------- | ------------- |
| 2次**完全積分**要素       | IM_GAUSS1D(4) |
| 1次**完全積分**要素       | IM_GAUSS1D(2) |
| 1次**低減積分**要素       | IM_GAUSS1D(0) |
| 1次非適合**完全積分**要素 | IM_GAUSS1D(4) |

Note:

IM_GAUSS1Dは引数の値の2分の1+1点のGauss積分を表します．
それぞれの積分に必要な積分点数を指定することで積分法を宣言します．
GetFEM
このように，GetFEMでは有限要素法を個別に定義可能であり，通常別要素で定義されている有限要素法を共通にすることで簡潔な実装を実現しています．

---
[drag=100 20, drop=0 0, set=align-center]
### Modelオブジェクトの定義

[drag=95 70, drop=5 20, set=align-left, fit=0.6]
```python
# モデルオブジェクトの作成
mds = []
for mfu in mfus:
    md = gf.Model("real")
    md.add_fem_variable("u", mfu)
    mds.append(md)

# 定数の定義
E = 10000 # N/mm2
Nu = 0.0

for md in mds:
    md.add_initialized_data("E", E)
    md.add_initialized_data("Nu", Nu)

# 平面ひずみ要素の追加
for md, mim in zip(mds, mims):
    md.add_isotropic_linearized_elasticity_brick_pstrain(mim, "u", "E", "Nu")
```

Note:

次に,各ケースに対しModelオブジェクトを定義します．
その際,add_fem_variableメソッドを用いて変位の変数として"u"を定義します．
さらに,add_initialized_dataメソッドを用いてモデルオブジェクトの定数として特性値を定義しました．
そして,add_isotropic_linearized_elasticity_brick_pstrainメソッドでモデルに平面ひずみ要素の項を追加します．

---
[drag=100 20, drop=0 0, set=align-center]
### はりの左側と右側の境界条件

[drag=95 70, drop=5 20, set=align-left, fit=0.6]
```python
# Dirichlet条件の設定
for (md, mim, mfu, fem) in zip(mds, mims, mfus, fems):
    if fem.is_lagrange():
        md.add_Dirichlet_condition_with_simplification("u", LEFT_BOUND)
    else:
        md.add_Dirichlet_condition_with_multipliers(mim, "u", mfu, LEFT_BOUND)

# Neumann条件の設定
b = 1.0 # (幅) mm
h = 1.0 # (高さ) mm
F = 1.0 # N/mm2
for (md, mfu, mim) in zip(mds, mfus, mims):
    md.add_initialized_data("F", [0, F / (b * h)])
    md.add_source_term_brick(mim, "u", "F", RIGHT_BOUND)
```

Note:

最後に,左側の領域にDirichlet条件を右側の領域にNeumann条件を設定します．

---
[drag=100 20, drop=0 0, set=align-center]
### Modelオブジェクトの求解

[drag=45 70, drop=5 20, set=align-left, fit=0.6]
```python
for md in mds:
    md.solve()
    u = md.variable("u")
```

[drag=50 10, drop=50 30, set=align-center, fit=0.5]
FEMの解/理論解

[drag=50 30, drop=50 40, set=align-center, fit=0.5]
| 要素            | 1x4 メッシュ | 4x2 メッシュ | 4x4 メッシュ | 16x8 メッシュ |
| --------------- | ------------ | ------------ | ------------ | ------------- |
| 2次要素         | 0.999        | 1.000        | 1.000        | 1.006         |
| 1次完全積分要素 | 0.244        | 0.244        | 0.244        | 0.841         |
| 1次低減積分要素 | 7.517e+11    | 1.317        | 1.056        | 1.021         |
| 1次非適合要素   | 0.999        | 1.000        | 1.000        | 1.006         |

Note:

一度モデルが正しく定義されればsolveメソッドで簡単に解くことができます．
計算された変位"u"はvariableメソッドで取得することが可能です．
よく知られているように,2次要素と1次の非適合要素は1次要素よりも精度が高くなっています．
1次の低減積分要素は,高さのメッシュ分割が1の場合にロッキングが発生しています．
一方,高さ方向を4分割以上にした場合は良好な解となっています．
1次の完全積分要素では,メッシュ分割を密にしても,曲げ変形に対して堅めの解となることが分かります．
