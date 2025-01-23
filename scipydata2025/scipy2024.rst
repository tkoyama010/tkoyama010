SciPy 2024 カンファレンスレポート
=================================

小山哲央です。 去年の\ `SciPy
2023 <https://gihyo.jp/article/2023/08/scipy2023>`__\ に引き続き、今年もアメリカで開催されたSciPy
2024に参加してきました。 現地の様子をこのレポートで伝えたいと思います。

SciPyについて
-------------

``{figure} images/SciPy-2024-Logo.png :alt: SciPy 2024のロゴ :width: 400px SciPy 2024のロゴ``

`SciPy
2024 <https://www.scipy2024.scipy.org/>`__\ は科学技術計算やデータの可視化を専門とした国際カンファレンスです。
カンファレンスの目的はPythonのユーザーや開発者が結集し、知見を共有することです。
SciPyと聞くと\ `PythonライブラリのSciPy <https://github.com/scipy/scipy>`__\ を連想される方が多いと思います。
しかし、実際は様々なPythonライブラリのコミュニティが多数参加するカンファレンスです。
例えば、 `scikit-learn <https://scikit-learn.org/stable/>`__ や
`Matplotlib <https://matplotlib.org/>`__ プロジェクトが参加しています。
そのため、科学に関する\ `PyCon <https://us.pycon.org/2024/>`__\ であると表現したほうが適当です。

イベント概要は以下の通りです。

\```{list-table}

-

   -  URL
   -  https://www.scipy2024.scipy.org/

-

   -  日程

   -

      -  チュートリアル: 2024年7月 8日（月）、 9日（火）
      -  カンファレンス: 2024年7月10日（火）〜12日（金）
      -  スプリント: 2024年7月13日（土）、14日（日）

-

   -  場所
   -  アメリカ合衆国、ワシントン州タコマ

-

   -  会場
   -  `Tacoma Convention Center <https://tacomaconventioncenter.org/>`__

-

   -  参加者数

   -

      -  カンファレンス現地参加 638人
      -  カンファレンスオンライン参加 114人
      -  スプリント現地参加 238人
      -  ファイナンシャルエイド 16名
      -  ティーントラック参加者 7名

-

   -  主催
   -  `NumFOCUS <https://numfocus.org/>`__ \``\`

参加目的
--------

筆者は普段オープンソース活動の一環として\ `PyVista <https://github.com/pyvista/pyvista>`__\ というプロジェクトに参加しています。
このプロジェクトはPythonのデータ可視化ライブラリの中で近年最も注目されているものの1つです。
去年に引き続き今年もPyVistaグループの一員としてこのカンファレンスに参加しました。

さらに今年も、チュートリアルの共同議長をすることになりました。
チュートリアルの共同議長の活動として、チュートリアルのプロポーザルの募集とレビューの依頼および選別とスケジューリングを行いました。
チュートリアルの共同議長はSciPy 2023から引き続きの活動です。
そのため、今年は去年の経験を活かしてよりスムーズに活動を行うことができました。

チュートリアル講師
------------------

1日目と2日目にチュートリアルが行われました。
1日目、講師の体調不良により急遽チュートリアルが1つ中止になりました。
そのため、チュートリアルの共同議長がキャンセルされた会場に急遽入り、参加者とのコミュニケーションを取ることになりました。
その際、Matplotlibの開発者であるHannah Aizenman氏
(`@story645 <https://github.com/story645>`__) と話す機会がありました。
大学院生の頃から可視化に興味を持ち、Matplotlibの開発に携わっているとのことでした。

2日目は去年に引き続き、PyVistaのチュートリアルを行いました。
PyVistaの詳細については\ `SciPy
2022の記事 <https://gihyo.jp/article/2022/09/scipy2022>`__\ に書いていますのでそちらをご覧ください。
講師は以下のとおりです。

-  Bane Sullivan 氏
   (`@banesullivan <https://github.com/banesullivan>`__)
-  Bill Little 氏 (`@bjlittle <https://github.com/bjlittle>`__)
-  Jaswant Panchumarti 氏 (`@jspanchu <https://github.com/jspanchu>`__)
-  Tetsuo Koyama (`@tkoyama010 <https://github.com/tkoyama010>`__)

Alex
Kaszynski氏(`@akaszynski <https://github.com/akaszynski>`__)は今年は家庭の事情で参加できなかったため、筆者達4人でチュートリアルを行いました。

Bane
Sullivan氏はPyVistaのプロジェクトの名付け親であり、PyVistaの開発をリードしています。
以前は、PyVistaのプロフェッショナルサポートを提供している\ `Kitware <https://www.kitware.com/>`__\ の従業員でした。

さらに、今年は\ `GeoVista <https://github.com/bjlittle/geovista>`__\ の作者であるBill
Little氏が参加してくれました。
GeoVistaは地図データをPyVistaで扱うためのライブラリです。 Bill
Little氏はイギリス気象庁(Met
Office)に勤めており、気象データの整理のためGeoVistaを開発しているとのことです。
Bill
Little氏は他にも地球科学データのライブラリ\ `iris <https://github.com/SciTools/iris>`__\ を10年以上開発してきたことでも有名です。

Jaswant
Panchumarti氏はVTKの開発チームの一員であり、最近はVTKのWebAssembly(Wasm)バージョンの開発に取り組んでいます。
VTKはC++で書かれた科学技術計算の分野で最も使われている可視化ライブラリの1つです。
PyVistaはそのラッパーとしてPythonからVTKを使いやすくしたものです。
VTKがWasmに対応することでPyVistaもブラウザ上で直接動いて高度な可視化を行うことが可能になります。

``{figure} images/pyvista-tutorial.jpg :alt: PyVistaのチュートリアルをする筆者 :width: 800px PyVistaのチュートリアルをする筆者``

筆者はチュートリアルにおいて、PyVistaの基礎的な使用方法の紹介を担当しました。
PyVistaをJupyterLabで使用する際の基本的な使い方を紹介しました。
さらに、参加者がPyVistaの機能を使ってサンプルデータを可視化できるようにサポートしました。

チュートリアルを通して、参加者とのコミュニケーションを取ることができました。
3次元の可視化を必要としている研究者やエンジニアが多く参加しており、PyVistaの需要が高いことがわかりました。

チュートリアル運営
------------------

PyVistaのチュートリアルは午前中に行われましたが、午後には他のチュートリアルも行われていました。
筆者は共同議長として\ `pyOpenSci <https://www.pyopensci.org/>`__\ のチュートリアルのサポートも行いました。
pyOpenSciはオープンソースソフトウェアの開発者が、研究者と協力して科学的なソフトウェアを開発するためのコミュニティです。
pyOpenSciのチュートリアルは研究者がPythonのパッケージングやドキュメンテーションの方法を学ぶことができる内容で、有益な情報を得ることができるチュートリアルでした。
しかし、チュートリアルの内容は上級者向けであるため、初心者の方には難しい内容だったと感じました。
運営側としてもこのチュートリアルは上級者向けであることを事前に伝えるべきだったとの反省がありました。

今年1年間チュートリアルの共同議長を務めてきた経験を活かし、来年も引き続きチュートリアルの運営を行いたいと考えています。

``{figure} images/tutorial-chairs.jpg :alt: SciPy 2024 チュートリアルの共同議長 :width: 800px SciPy 2024 チュートリアルの共同議長 左が筆者``

また、今回新しい取り組みとしてティーントラックが設けられました。
ティーントラックは10代の参加者を対象としたトラックで、Pythonの基礎的な使い方を学ぶことができる内容でした。
ティーントラックの参加者は7名であり、スポンサー企業のご子息の方が多かったです。
スポンサー企業にはPythonの教育に関心を持つ企業が多いため、親御様に好評だったようです。

``{figure} images/teens.jpg :alt: ティーントラックの参加者 :width: 800px ティーントラックの参加者``

論文のレビュー
--------------

SciPyの大きな特徴として、トークやポスターの付属として論文も出すことができるということがあります。
参加者には研究者が多いためカンファレンスに参加することが研究者としての実績になるように考慮されていることがわかります。
今年の論文は\ `scipy-conference/scipy_proceedingsの2024ブランチ <https://github.com/scipy-conference/scipy_proceedings/tree/2024>`__\ に公開されています。
今回、写真の論文のエディターチームと食事をする機会がありました。
今年の論文の管理に関わっている方々が集まっており、これまでの運営の経緯や今後の展望について話を聞くことができました。

``{figure} images/proceedings.jpg :alt: 論文エディタチーム :width: 800px 論文エディタチーム右から2人目がRowan Cockett氏``

SciPyでは論文の管理にGitHubを使用しています。
論文を提出する際にはリポジトリにMarkdown形式で論文を提出し、CI/CDパイプラインを使ってPDFをプレビューする仕組みでした。
レビュワーはPull
Requestのコメント欄に論文の内容についてコメントを残すことでレビューを行います。
このシステムの利点は論文の管理がGitHubで行えるため、論文の変更履歴をGitHubの機能を使って管理できることです。
さらに、GitHubのPull
Requestの機能を使用しているため、査読者以外の人が論文の内容について自由にコメントを残すことができます。

筆者はこの論文のレビュワーのボランティアを行いました。
レビュワーは論文の内容を確認し、論文がカンファレンスの基準を満たしているかを判断します。
筆者が今年レビューした論文は以下の通りです。

1. `Paper: Mamba Models a replacement for Transformers?
   #917 <https://github.com/scipy-conference/scipy_proceedings/pull/917>`__
2. `Paper: THEIA: An Offline Tool for Tradespace Visualization
   #920 <https://github.com/scipy-conference/scipy_proceedings/pull/920>`__

論文の内容については公開されているため、興味のある方はリンクを参照してください。

さらに、今年からは\ `Curvenote <https://curvenote.com/>`__\ というサービスを利用して論文の管理を行っています。
Curvenoteは\ `MyST <https://myst-parser.readthedocs.io/en/latest/index.html>`__\ というMarkdownの拡張機能を使って論文を書くことができるサービスです。
CurvenoteにはMySTの開発者であるRowan
Cockett氏(`@rowanc1 <https://github.com/rowanc1>`__)が関わっています。
Rowan Cockett氏は今年のSciPyの論文の管理にも関わっています。 Rowan
Cockett氏の仕事により、論文のプレビューをCurvenoteでできるようになりました。

科学技術計算の分野のオープンソースソフトウェアの論文執筆には\ `JOSS(Journal
of Open Source
Software) <https://joss.theoj.org/>`__\ というジャーナルがあります。
JOSSにおいてもSciPyConferenceの論文査読システムを参考にしているとのことでした。
論文の査読システムがオープンであり、執筆者も査読者もオープンに議論を行う。
そんな論文執筆の未来を感じました。

ブース
------

カンファレンス会場には各組織がブースを出しており話を聞くことができます。
その中で印象に残ったブースをご紹介します。

Dask
~~~~

``{figure} images/dask.jpg :alt: Daskのブース :width: 800px Daskのブース手前がSarah Johnson氏``

`Dask <https://www.dask.org/>`__\ は大規模なデータセットを処理するためのPythonライブラリです。
DaskはNumPy、Pandas、Scikit-learnなどのライブラリと互換性があり、大規模なデータセットを処理する際に有用です。
Daskは分散処理を行うため、複数のコンピュータを使ってデータを処理することができます。
今回、DaskのブースではDaskの使い方を紹介するデモを行っていました。
写真手前にいるのはDaskをサポートしている\ `Coiled <https://coiled.io/>`__\ で働いているSarah
Johnson氏(`@scharlottej13 <https://github.com/scharlottej13>`__)です。
以前、来日した際に日本コミュニテイで食事をしたことがあります。 `PyCon US
2024の開幕、Day
1ライトニングトークに挑戦 <https://gihyo.jp/article/2024/07/pycon-us-2024>`__\ の記事でも登場しますので、興味のある方はご覧ください。
また、Daskの開発者であるMatthew
Rocklin氏(`@mrocklin <https://github.com/mrocklin>`__)もブースにいました。
氏はDaskの作者であり、現在も開発をリードしており、Coiledを起業しています。
Matthew
Rocklin氏とは以前、NumFOCUSの委員会で一緒に働いたことがあります。
とても親しみやすい方で、DaskやCoiledについての質問にも丁寧に答えてくれました。
Matthew Rocklin氏は\ `Dask in
Production <https://cfp.scipy.org/2024/talk/NGRVJJ/>`__\ というトークも行っていました。
内容に興味のある方はリンクを参照してください。

Streamlit
~~~~~~~~~

``{figure} images/streamlit.jpg :alt: Streamlitのブース :width: 800px Streamlitのブース``

`Streamlit <https://streamlit.io/>`__\ はデータサイエンスのためのアプリケーションを簡単に作成するためのPythonライブラリです。
従来、データサイエンスの結果を共有するためにはJupyter
Notebookを使っていましたが、Streamlitを使うことで簡単にWebアプリケーションを作成することができます。
StreamlitのブースではStreamlitの使い方を紹介するデモを行っていました。
日本のコミュニティでもStreamlitは人気があり、PyCon JP
TVでもStreamlitのハンズオンが行われています。 興味のある方は\ `PyCon JP
TV #42:
Streamlitを使ってQRコード生成アプリの作り方ライブデモ <https://www.youtube.com/live/dPe2JU2I1vk?si=1QQzNY1jYMVAuIBA>`__\ をご覧ください。
Streamlitのブースに設けられていたディスプレイには、日本の開発者として有名なYuichiro
Tachibana氏(`@whitphx <https://github.com/whitphx>`__)も表示されていました。
Yuichiro
Tachibana氏はStreamlitの開発にも貢献しており、サーバーレスのStreamlitアプリケーションを作成することができる\ `stlite <https://github.com/whitphx/stlite>`__\ というライブラリを開発しています。

キーノート
----------

``{figure} images/keynote.jpg :alt: キーノート :width: 800px キーノートを行うJulia Silge氏``

キーノートは日本での「基調講演」に当たるものです。
今年もカンファレンス3日間の間に1日1講演、計3回行われました。

その中で最も印象に残った1日目のJulia
Silge氏(`@juliasilge <https://github.com/juliasilge>`__)の\ `The right
tool for the job <https://juliasilge.github.io/scipy2024>`__
について紹介します。
氏はデータサイエンスの分野で活躍するデータサイエンティストであり、RやPythonを使ってデータ分析を行っています。
RやPythonはそれぞれ得意な分野があります。
氏はデータ分析の際には「適切なツールを選ぶことが重要である」と述べています。
氏はその両方を使ってきた経験から、片方の言語だけにこだわらず適切なツールを選ぶことが重要であると述べています。
また、片方の言語にあるツールがもう片方の言語にない場合もあり、それが新しいツールを作るきっかけになることもあると述べています。

トークセッション
----------------

トークセッションは事前にプロポーザルを提出し、その中で選ばれた講演が行われるセッションです。
カンファレンス中に聞いたトークセッションで特に印象に残ったトークをご紹介します。

My NumPy year: From no CPython C API experience to shipping a new DType in NumPy 2.0
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1件目はNathan
Goldbaum氏(`@ngoldbaum <https://github.com/ngoldbaum>`__)による\ `My
NumPy year: From no CPython C API experience to shipping a new DType in
NumPy 2.0 <https://cfp.scipy.org/2024/talk/8QAWZD/>`__\ です。
Goldbaum氏はQuansightで働いており、NumPy
2.0の開発で中心的な役割を果たしています。 トークでは新しいNumPy
DTypeの開発の裏話を紹介していました。
トークをきいていると、文字列データの扱いの話などはかなり複雑な話であることがわかりました。

写真は最後にGoldbaum氏が開発のときに何を考えていたかを説明しているところです。
開発がつらすぎるという気持ちを猫の写真とともに表示しており、会場から笑いが起こりました。

普段、NumPyを使用しているユーザーとしては、Scientific
Pythonの基盤となるNumPyの開発の裏話を聞くことができてとても興味深かったです。

``{figure} images/numpy.jpg :alt: Nathan Goldbaum氏 開発がつらすぎるという気持ちを猫の写真とともに表示 :width: 800px Nathan Goldbaum氏 開発がつらすぎるという気持ちを猫の写真とともに表示``

SciPy Tools Plenary
~~~~~~~~~~~~~~~~~~~

2件目はSciPyのツールに関するトークセッションです。
このセッションでは、SciPyのツールに関するプロジェクトの開発者が登壇し、プロジェクトの紹介を行いました。
このセッションは毎年開催されており、SciPyのツールの最新情報が提供されるためとても人気があります。
今年は以下のプロジェクトが紹介されました。
ただし、列挙しているのは一部です。

-  `Dask <https://dask.org/>`__
-  `Xarray <http://xarray.pydata.org/en/stable/>`__
-  `Jupyter <https://jupyter.org/>`__
-  `Matplotlib <https://matplotlib.org/>`__

今回は特にJupyterの紹介が印象的でした。
Jupyterはデータサイエンスの分野で最も使われているツールの1つです。
今回の大きなトピックはJupyterのサードパーティーエクステンションである
`JupyterBook <https://jupyterbook.org/>`__ の紹介でした。
JupyterBookはJupyter Notebookを使って本を作成するためのツールです。
Jupyterで分析したデータをそのまま本にすることができるため、データサイエンスの分野で非常に便利です。
日本でも大学の授業でJupyterBookを使っているところが増えてきています。
今回、JupyterプロジェクトからJupyterBookが正式にJupyterの一部として扱われることが発表されました。
今後もこのツールに注目が集まることが予想されます。
興味のある方は\ `Jupyter Project
Updates <https://docs.google.com/presentation/d/1Tkm606t0xq_a_9rj-wjsqisnIzOP7OpggXWME7RXU7E/edit?usp=sharing>`__\ をご覧ください。

anywidget: custom Jupyter Widgets made easy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``{figure} images/anywidget.gif :alt: anywidgetのデモ :width: 800px anywidgetのデモ``

3件目はTrevor
Manz氏(`@manzt <https://github.com/manzt>`__)による\ `anywidget: custom
Jupyter Widgets made
easy <https://cfp.scipy.org/2024/talk/UMNVPH/>`__\ です。
`Anywidget <https://anywidget.dev/>`__
はJupyterのカスタムウィジェットを簡単に作成するためのライブラリです。
JupyterのカスタムウィジェットはJavaScriptとCSSを使って作成する必要があります。
AnywidgetはPython内にJavaScriptとCSSを指定することができるため、Jupyterのカスタムウィジェットを簡単に作成することができます。
図のGIFはAnywidgetのデモです。
今までは、Jupyterのカスタムウィジェットを作成するためにはcokkiecutterを使ってテンプレートからウィジェットを作成する必要がありました。
Anywidgetを使うことでPythonのコードにJavaScriptを埋め込むことができるため、以下のように簡単にカスタムウィジェットを作成することができます。

.. code:: python

   import pathlib
   import anywidget
   import traitlets

   class CounterWidget(anywidget.AnyWidget):
       _esm = pathlib.Path("index.js")
       _css = pathlib.Path("styles.css")
       value = traitlets.Int(0).tag(sync=True)

筆者もJupyterのカスタムウィジェットを作成したことがありますが、テンプレートから作成するのは手間がかかります。
周りの人の評判もとても良く、今後の開発に期待が持てるプロジェクトだと感じました。

BoFセッション
-------------

BoFはBirds of a
Featherの略で、司会が短いプレゼンテーションを行い、大部分の時間は出席者全員で議論を行うセッションです。
Birds of a
Featherは一般的には「同類」という意味ですが、IT分野では「あるテーマについて集まった、非公式自発的な集団」という意味もあります。

Community Feedback on the NumPy 2.0 Release
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

今年はNumPy
2.0の移行についてのフィードバックを議論するBoFセッションが行われました。
今回のメジャーバージョンアップではNumPyプロジェクトから事前にnightly
wheelが提供されていたので各プロジェクトもリリース後すぐにNumpy
2.0への対応バージョンをリリースできました。

会場からは以下のような意見が出されました。

1. nightly
   wheelsが提供されているが、これを使っているユーザーはどの程度いるか？
2. NumPyの関数が、0次元配列が適切であるようなケースでもほとんどの場合にスカラ値を返すことについて、どう考えているか？

20年以上にわたりPythonの科学技術計算の基盤となってきたNumPyがメジャーバージョンアップすることは大きな話題となっています。

Proceedings
~~~~~~~~~~~

SciPyの論文のプロシージングについてのBoFセッションも行われました。
プロシージングは元々はカンファレンスに提出された論文などをまとめて公開するための冊子のことです。
SciPyでは前述の通り、論文をGitHubで管理しており、プロシージングもGitHubで作成しています。
今年はCurvenoteを使って論文の管理を行っているため、Curvenoteの使い勝手や今後の展望について議論が行われました。
論文の編集チームがこのBoFを開催しています。
論文のレビューワーは常に不足しているため、新しいレビューワーを募集していました。

今回、論文を提出した際にSciPyカンファレンスの先進的な論文管理システムに感銘を受け、レビューワーとして参加したいという方が2から3名いました。
筆者も去年から論文のレビューを行っていますが、動機はその人たちと同じでした。

レビューワー募集とは別に、レビューの方法についての議論も行われました。
その中で、自分のドメインとは異なる論文をレビューする場合、どのようにレビューを行うかについて筆者が質問しました。
自分のドメインと異なる論文をレビューする場合、論文の内容についての知識が不足しているため、レビューが難しいと感じることがあります。
そのような場合、論文の内容についてのチェックをするのではなく、それが論じているプロジェクトが外部のユーザーからどのように見えるかをチェックすることが重要だとの意見が出されました。
その際には、自分の手元の環境で論文の内容を再現することが重要であるとのコメントをもらいました。
SciPyの論文の基本は、オープンソースプロジェクトの成果を共有することです。
そのためには、ドメインは関係なく、論文の内容を再現できるようにすることが重要だと感じました。

``{figure} images/bof.jpg :alt: ProceedingsのBoFセッション(左に座っているのが筆者) :width: 800px ProceedingsのBoFセッション(左に座っているのが筆者)``

ポスターセッション
------------------

ポスターセッションは各プロジェクトをポスターで紹介するセッションです。
セッション中は写真のように会場の一部にポスターが貼られています。

今年もPyVistaプロジェクトとしてポスターセッションに参加しました。
ポスターを制作する前に運営から\ `#betterposter <https://twitter.com/hashtag/betterposter>`__\ というハッシュタグが紹介されます。
これはMike Morrison氏
(`@drmikemorrison <https://www.youtube.com/@drmikemorrison>`__)
により提唱されたムーブメントです。
`#betterposter <https://x.com/search?q=%23betterposter>`__\ のムーブメントについては、\ `SciPy
2023の記事 <https://www.scipy2023.scipy.org/>`__\ で紹介しています。
このムーブメントの元となった動画は `How to create a better research
poster in less time <https://youtu.be/1RwJbhkCA58>`__
というタイトルでMorrison氏のYouTubeチャンネルに公開されています。
今回Morrison氏はSciPyの論文管理について\ `Next-level conference
abstracts are coming to
science <https://youtu.be/CtqjD1X_5QQ?si=IQoYOlqntgJ7hi5E>`__\ という動画を公開してくれました。
興味のある方はぜひ動画を見てみてください。
SciPyカンファレンスに参加する人は皆、カンファレンスでの情報交換をいかに効果的に行うかを真剣に考えています。
筆者にはそれがとても心地よく感じられました。
画像はSciPyのポスターの様子です。
#betterposterのテンプレートを元にして作成されています。
それにより、プロジェクトの情報を効果的に伝えることができるようになっています。
今回のPyVistaのポスターも#betterposterのテンプレートを元にして作成しました。

PyVistaのポスターセッションに来た人は、GeoVistaに興味を持っている人が多かったです。
Bill
Little氏はその場にはいなかったため、筆者がGeoVistaについての質問に答えることになりました。
ユーザーと対面で相談にのるよい機会ですので今後もポスターセッションへの参加は続けていきたいと考えています。

``{figure} images/scipy-poster.jpg :alt: SciPyプロジェクトのポスター :width: 800px SciPyプロジェクトのポスター``

``{figure} images/poster.png :alt: PyVistaプロジェクトのポスター :width: 800px PyVistaプロジェクトのポスター``

スプリント
----------

``{figure} images/sprint.jpg :alt: スプリントの様子 Bill Little氏 (左) と筆者 (右) :width: 800px スプリントの様子 Bill Little氏 (左) と筆者 (右)``

最後の2日間はスプリントが行われました。
スプリントは自分の興味のあるオープンソースプロジェクトに対して、コードのテスト、バグの修正、新機能の追加、ドキュメントの改善など、様々な貢献を行うセッションです。
また、オープンソースの作者やメンテナがサポートすることで、オープンソース初心者に貢献の場を提供することも大きな目的です。

今年も去年に引き続きPyVistaのスプリントを開催しました。
スプリントにはGeoVistaの開発者であるBill Little氏が参加してくれました。
また、先程のMySTの開発者であるRowan Cockett氏も参加してくれました。
Rowan
Cockett氏はMySTのスプリントも開催しており、そのスプリントでPyVistaをMySTに対応させる作業を行ってくれました。
これが、MySTでリリースされれば、PyVistaの3次元可視化がMySTで行えるようになります。
科学や論文執筆の世界がPythonコミュニティによって変わっていくのではとの期待が持てる作業でした。

``{figure} images/myst-sprint.gif :alt: MyST上で動作するPyVistaの3次元可視化 :width: 800px MyST上で動作するPyVistaの3次元可視化``

スプリントに参加して毎年感じますがプロジェクト同士で議論をするにはスプリントが最適です。
SciPy 2022ではpoliastro と議論が出来ましたし、SciPy 2023はGeoVista
と議論ができました。 さらに、今年はMySTと議論ができました。
他のプロジェクトと議論をすることで、自分たちのプロジェクトが今後どこに向かうべきかを見定めることができます。

最後に
------

今年もチュートリアル・カンファレンス・スプリント全日参加することができて満足しました。
特にスプリントでは他のプロジェクトと議論をすることができ、自分たちのプロジェクトの今後の方針を見定めることができました。
今回の参加も\ `NumFOCUS <https://numfocus.org/>`__\ のフィナンシャルエイドにより実現しました。
カンファレンスに参加するチャンスを与えてくださったことに対してここに記して感謝をいたします。
アメリカ渡航などの詳しい話は\ `こちらのPodcast <https://podcast.terapyon.net/episodes/0106.html>`__\ で話しています。
ぜひお聴きください。

``{figure} images/friends.jpg :alt: scikit-imageのLars Grüter氏(右)とzarrのSanket Verma氏(左)と空港で記念撮影 :width: 800px scikit-imageのLars Grüter氏(右)とzarrのSanket Verma氏(左)と空港で記念撮影``
