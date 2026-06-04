# 睡眠の動的閾値理論 v0.3.2

**睡眠様回復遷移、閾値ダイナミクス、ヒステリシス、選択的保護、救済レジームに関する claim-bounded toy-network 診断アーカイブ。**

著者: 吉村圭司（Independent Researcher）  
公開状態: `v0.3.2-public-landing-and-metadata-refresh`  
Repository: https://github.com/yokken0907/dynamical-threshold-theory-of-sleep  
Project website: https://yokken0907.github.io/dynamical-threshold-theory-of-sleep/

## Project website

ブラウザで閲覧できる公開ランディングページはこちらです。

https://yokken0907.github.io/dynamical-threshold-theory-of-sleep/

## 現在の公開版

本リポジトリは、v0.3.1統合DTTSパッケージの公開入口・メタデータ刷新版です。
可読性、GitHub Pages公開、メタデータ整理、検索導線、manifest整合性を整えるために再構成しています。

このv0.3.2は、既存v0.3.1統合版を超える新たな臨床・医療・生物学・治療上の主張を導入するものではありません。
リポジトリ構造、claim boundary、公開ページ、メタデータの刷新版です。

## DTTSとは何か

Dynamical Threshold Theory of Sleep（DTTS）は、簡略化された適応ネットワークにおける**睡眠様回復遷移ダイナミクス**を扱う数理・計算プロトタイプです。
toy-model設定内で、閾値的ゲート立ち上がり、ヒステリシス様持続、選択的保護、急性負荷からの回復、topology/noise頑健性、失敗境界、救済レジーム分類、凍結救済ポリシーholdout挙動を扱います。

統合論文本体はこちらです。

- `paper/integrated_v0_3_1/DTTS_integrated_model_audit_synthesis_v0_3_1.pdf`

v0.3.0統合補遺はこちらです。

- `paper/addendum_v0_3_0/DTTS_threshold_hysteresis_rescue_regime_addendum_v0_3_0_with_github_url.pdf`

## 主張境界

本リポジトリは、以下を主張しません。

- 臨床睡眠診断
- 医療助言
- 治療方針
- ヒト被験者検証
- 動物睡眠データ検証
- EEGまたはウェアラブル機器による予測
- 医療機器としての準備性
- 患者個別の睡眠状態予測
- 治療介入
- 睡眠機能の神経科学的証明
- 実脳データへの直接フィッティング
- 完全な生物学的睡眠理論

標準短文:

> DTTSは、睡眠様回復遷移ダイナミクスを扱う claim-bounded な数理toy-networkプロトタイプであり、臨床睡眠モデル、医療ツール、ヒト/動物データ検証、EEG/ウェアラブル予測、治療指針、または完全な生物学的睡眠理論ではありません。

## このリポジトリの目的

本リポジトリは、AI支援による独立研究アーカイブを、厳格な医療・生物学的主張境界のもとで公開・検討可能な形で保存するものです。
理論的議論、教育的整理、再現性確認、専門家レビューのための資料であり、医療・臨床用途を意図しません。

## 技術的ビジュアル案内

ブラウザだけで開ける案内ページを同梱しています。

- `docs/index.html`
- `docs/technical_visual_orientation/index.html`
- `docs/visual_orientation/index.html`

これらは説明補助資料であり、医療計算、診断、治療助言、臨床予測、ウェアラブル認証、医療機器評価を行うものではありません。

## ライセンス

本リポジトリは、`LICENSE` および `LICENSE_EVALUATION_ONLY.txt` に記載された source-defined Evaluation-Only license を用います。
Zenodoでは CC-BY-NC-4.0 ではなく、source-defined / other-open 相当の選択肢で扱ってください。

## AI利用開示

本プロジェクトはAI支援を用いて作成・改訂されています。`AI_ASSISTANCE_DISCLOSURE.md` を参照してください。

## 連絡先

吉村圭司  
Email: yokken0907@gmail.com
