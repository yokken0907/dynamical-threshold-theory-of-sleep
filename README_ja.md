# 睡眠の動的閾値理論

このリポジトリは、以下のAI支援独立研究論文に対応するGitHub配置用フォルダである。

**Dynamical Threshold Theory of Sleep: A Network Prototype for Recovery Phase Transitions**

著者: 吉村圭司（Independent Researcher）  
状態: GitHub-ready paper companion archive v0.1.1-public-gate

## 簡易分類フォルダ名

**睡眠相転移・回復ダイナミクスのネットワーク理論**

## 位置づけ

Dynamical Threshold Theory of Sleep（DTTS）は、睡眠様の遷移を、適応的多細胞ネットワークにおける回復相ダイナミクスとして記述する数理・計算プロトタイプである。

構成要素は以下である。

- adaptive phase oscillator
- local homeostatic load
- local sleep propensity
- noisy wake-like perturbation
- selective protection of coupling structure
- bounded sleep-dominant free-energy relaxation

## 主張しないこと

本リポジトリは、以下を主張しない。

- 臨床睡眠診断
- 医療助言
- ヒト被験者検証
- 睡眠機能の神経科学的証明
- 治療介入
- 実脳データへの直接フィッティング
- 完全な生物学的睡眠理論

## 現在の状態

これはpaper companion archiveおよびproof-of-concept simulation recordであり、医療・臨床・実験神経科学の検証パッケージではない。

## PUBLIC-GATE-0 status

判定: `PASS-WITH-MINOR-PUBLICATION-FIXES-A10-DTTS-PUBLIC-GATE-0`  
公開版: `v0.1.1-public-gate`  
分類: 睡眠相転移・回復ダイナミクスのネットワーク理論

このリポジトリは、A10 Evidence-Lock Protocol型の公開前監査により、主張境界・非主張事項・manifest整合性・GitHub/Zenodo/Jxiv方針を固定した public-gate 版である。

## Zenodo-safe citation metadata

Zenodoアーカイブ時のメタデータ検証衝突を避けるため、この pre-DOI public-gate 版では、root直下の有効な `CITATION.cff` を意図的に置いていない。

下書き引用メタデータは以下に保存している。

`docs/citation_metadata/CITATION_DRAFT_pre_doi.cff`

Zenodo DOI付与後、README、論文メタデータ、引用ファイルにDOIを反映した follow-up DOI-metadata release を切ることを想定する。

## 医療・健康主張の境界

DTTSは、睡眠様遷移を扱う数理・計算プロトタイプであり、臨床睡眠モデル、医療助言、診断・治療ツール、ヒト被験者検証、または完全な生物学的睡眠理論ではない。

## 技術的ビジュアル案内

初めて本リポジトリを見る技術的関心のある読者向けに、ブラウザだけで開ける技術的ビジュアル案内ページを同梱しています。

`docs/technical_visual_orientation/index.html`

このページは、Dynamical Threshold Theory of Sleep の構造をプロジェクト固有の観点から整理する補助資料です。本リポジトリにおける mission variable は sleep-quality scoring、medical diagnosis、treatment guidance、または clinical prediction ではなく、reduced dynamical-threshold model において homeostatic load、arousal/activation pressure、adaptive threshold、synchronization、noise、recovery-state variables を通じて wake-like persistence、threshold crossing、sleep-like recovery consolidation、fragmentation risk を識別する sleep-like recovery-transition diagnosis です。

また、このページでは reduced dynamical-threshold model としての位置づけ、load / arousal / threshold / synchronization channels、recovery-basin interpretation、evidence hierarchy、リポジトリ閲覧順、および medical claim boundary を短く整理しています。主要な図解セクションには replay control を付けており、静的テンプレートではなく診断ロジックを段階的に確認できます。

このページは説明補助であり、medical / clinical computation を実行するものではありません。診断、治療、患者別予測、wearable-device certification、medical-device readiness、または臨床的妥当性を示すものでもなく、論文本体、source materials、figures、または専門家による独立評価を置き換えるものでもありません。
