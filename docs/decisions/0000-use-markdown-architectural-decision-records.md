---
status: accepted
date: 2026-07-17
decision-makers: [tkoyama010]
consulted: []
informed: []
---

# Markdown Architecture設計記録(MADR)を導入する

## 背景と問題

tkoyama010リポジトリでは、アーキテクチャに関わる重要な決定がIssueやPRの説明の中にしか残されていない。そのため、後から「なぜその決定をしたのか」を探すのが難しく、決定の根拠が失われやすい。このプロジェクトで行われたアーキテクチャの決定（アーキテクチャ、コード、その他の分野を含む）を、一貫性がありバージョン管理可能な方法で記録したい。どのようなフォーマットと構造にするべきか？

## 決定の基準

- **根拠の明文化**: 暗黙の仮定を明示し、将来のコントリビューターが「何が」決まったかだけでなく「なぜ」決まったかを理解できるようにする。["A rational design process: How and why to fake it"](https://doi.org/10.1109/TSE.1986.6312940)も参照。
- **バージョン管理との親和性**: 記録はプレーンテキストで、Gitでコードと一緒に差分・レビューできること。
- **低オーバーヘッド**: フォーマットは軽量で、記録を書くことが負担にならないこと。
- **わかりやすさ**: 著者・レビュアーの双方が読みやすく、スキャンしやすい構造であること。
- **ツールの可用性**: 積極的にメンテナンスされており、サポートツールがあるフォーマットを優先する。
- **汎用性**: アーキテクチャ、設計、ツールなど、あらゆる種類の決定を記録できること。

## 検討した選択肢

- [MADR](https://adr.github.io/madr/) 4.0.0 — Markdown Architecture設計記録
- [Michael Nygardのテンプレート](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions) — "ADR"という言葉の最初の形
- [持続可能なアーキテクチャ決定](https://www.infoq.com/articles/sustainable-architectural-design-decisions) — Y-Statements
- その他のテンプレートは [https://github.com/joelparkerhenderson/architecture_decision_record](https://github.com/joelparkerhenderson/architecture_decision_record) を参照
- 形式なし — ファイルフォーマットと構造に規約を設けない

## 決定内容

選択肢: **「MADR 4.0.0」**を採用。決定の基準に最も適合するため。軽量なMarkdownテンプレートでオプションセクションを持ち、あらゆる決定（純粋なアーキテクチャに限らない）を記録でき、積極的にメンテナンスされておりツールサポートもある。

### 影響

- 良い点: アーキテクチャの根拠が `docs/decisions/` にコードと一緒に存在し、同じレビュー/PRフローを通る。
- 良い点: `NNNN-title-with-dashes.md` というファイル名の規約により、記録が発見可能でソート可能。
- 良い点: MADRテンプレートのオプションセクションにより、短い決定は短く、複雑な決定は拡張できる。
- 良い点: YAML front matter（`status`、`date`、`decision-makers`、`consulted`、`informed`）が決定のライフサイクルを追跡する軽量メタデータを提供。
- 悪い点: コントリビューターがテンプレートを学び、重要な決定には記録を作成することを覚える必要がある。
- 中立: MADRの規約をそのまま採用し、テンプレートをフォークしないため、多少の柔軟性を犠牲にしてメンテナンスされたアップストリームに従う。

### 確認方法

この決定の遵守は以下で確認する:

1. `docs/decisions/` ディレクトリが存在し、[MADR 4.0.0リリース](https://github.com/adr/madr/tree/4.0.0/template)からコピーしたMADRテンプレート（`adr-template.md`）が含まれている。
1. 最初の具体的な記録 `docs/decisions/0000-use-markdown-architectural-decision-records.md` がこのIssueの内容を反映しており、PRでマージされる。
1. 以降のアーキテクチャに関わる重要な提案には、IssueからリンクされたMADR記録が添えられる。

## 検討した選択肢の pros と cons

### MADR 4.0.0 — Markdown Architecture設計記録

[https://adr.github.io/madr/](https://adr.github.io/madr/) を参照

- 良い点: プレーンMarkdownであり、バージョン管理の親和性と低オーバーヘッドの基準を満たす。
- 良い点: 構造（背景と問題 → 決定の基準 → 検討した選択肢 → 決定内容 → pros/cons → 補足情報）がわかりやすく、1段落から複数ページまでスケールする。
- 良い点: プロジェクトは活発で、4.0.0は2024-09-17にリリースされ、例、変更履歴、ツール（markdownlint設定、initスクリプト）がある。
- 良い点: あらゆる決定を記録でき、汎用性の基準を満たす。
- 中立: 必須ではないが採用するYAML front matterが付属。
- 悪い点: コントリビューターが学ぶ必要がある小さなドキュメント規約を導入する。

### Michael Nygardのテンプレート

[http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions](http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions) を参照

- 良い点: 元のADRテンプレートであり、広く引用されている。
- 良い点: 最小限: タイトル、背景、決定、ステータス、影響。
- 中立: 簡潔さは魅力的だが、選択肢の比較や基準の記録ができない。
- 悪い点: 「検討した選択肢」「pros/cons」セクションがなく、代替案とトレードオフが記録されない。
- 悪い点: メンテナンスされたツールや公式なMarkdownソースがなく、多くの変種が存在。

### 持続可能なアーキテクチャ決定 — Y-Statements

[https://www.infoq.com/articles/sustainable-architectural-design-decisions](https://www.infoq.com/articles/sustainable-architectural-design-decisions) を参照

- 良い点: Y-Statement（`Z` の文脈で、`Q` に直面し、`B` を達成するために `S` を決定し、`D` を受け入れる）は簡潔で明示的なトレードオフを強制。
- 中立: フォーマットは単一文パターンであり、完全なドキュメントテンプレートではない。
- 悪い点: 詳細なpros/consを持つ複数選択肢の比較にスケールしない。
- 悪い点: MADRより採用が少なく、ツールサポートも少ない。

### その他のテンプレート

[https://github.com/joelparkerhenderson/architecture_decision_record](https://github.com/joelparkerhenderson/architecture_decision_record) を参照

- 良い点: 多くの変種（Planguage、MADR、Nygard、Y-Statementなど）があり、ニッチな用途に合うものを選べる。
- 中立: 知名度の低いテンプレートを選ぶと、自己メンテナンスが必要。
- 悪い点: 選択肢の多様性自体がコスト: どのテンプレートを選ぶかコントリビューターが学ぶ必要があり、コミュニティドキュメントも少ない。

### 形式なし — ファイルフォーマットと構造に規約を設けない

- 良い点: 初期コストがゼロで、学ぶテンプレートもない。
- 悪い点: 記録のスタイルがばらつき、根拠が省略され、見つけにくくなる — 明示的な根拠とわかりやすさの基準を満たさない。
- 悪い点: `docs/decisions/` の規約とファイル名パターンがないと、決定がIssueやPRに散在し、脱したい状況のまま。

## 補足情報

- MADRホームページ: [https://adr.github.io/madr/](https://adr.github.io/madr/)
- MADR 4.0.0リリース: [https://github.com/adr/madr/releases/tag/4.0.0](https://github.com/adr/madr/releases/tag/4.0.0)
- MADRテンプレート（開発版）: [https://github.com/adr/madr/blob/develop/template/adr-template.md](https://github.com/adr/madr/blob/develop/template/adr-template.md)
- 初期化スニペット: `npm install madr && mkdir -p docs/decisions && cp node_modules/madr/template/* docs/decisions/`
- この記録は、MADR自身のADR-0000に合わせて `docs/decisions/0000-use-markdown-architectural-decision-records.md` に配置される。
