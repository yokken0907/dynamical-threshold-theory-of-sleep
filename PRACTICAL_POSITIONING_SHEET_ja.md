# 実務位置づけシート

## 技術名

Dynamical Threshold Theory of Sleep  
DTTS  
睡眠の動的閾値理論

## 簡易分類フォルダ名

睡眠相転移・回復ダイナミクスのネットワーク理論

## 対象分野

- 睡眠理論
- 数理神経科学
- adaptive network dynamics
- oscillator network modeling
- homeostatic recovery model
- complex systems biology
- AI支援理論形成

## 現場課題

睡眠は、homeostatic recovery、local sleep、synaptic renormalization、circadian regulationなど複数の説明系がある一方、それらを単一のnetwork-dynamical frameworkとして扱う理論は十分に整理されていない。

## DTTSの役割

DTTSは、wakefulnessをnoisy adaptive synchronization regimeとして、sleepをlocal load accumulationとcoherence degradationが集団閾値を超えた後のsleep-dominant renormalization phaseとして扱う。

## 期待効果

- local loadとglobal transitionを同じ数理枠で扱える。
- sleep propensityの局所・集団的上昇を表現できる。
- naive adaptive couplingのunbounded pathologyをbounded free-energy flowで避ける。
- protected interactionが選択的に保存されるという、uniform weakeningではないdown-selectionを表現できる。

## 検証済み範囲

論文では、hierarchical modular small-world network上のproof-of-concept simulationにより、以下が示されている。

- spatially heterogeneous homeostatic burden
- rapid growth of mean sleep propensity
- bounded downscaling of mean coupling strength
- reduced free-energy relaxation after transient overshoot
- stronger pre-sleep protectionを持つedgeの選択的保存

## 未検証範囲

- ヒト睡眠データ
- 動物実験データ
- EEG / LFP / imaging data
- 睡眠障害診断
- 臨床応用
- 薬理・治療介入
- 実脳ネットワークへの直接対応

## 実装への次ステップ

1. paper companion archiveとして公開する。
2. donation sentenceを正式投稿版から削除する。
3. simulation codeとfigure outputを整理する。
4. PUBLIC-GATEでmedical/clinical overclaimを防ぐ。
5. 将来的には公開睡眠データセットへの弱い定性的比較、またはlocal sleep literatureとの対応表を作る。

## 想定読者

- 数理神経科学研究者
- 睡眠理論研究者
- complex systems研究者
- adaptive network dynamics研究者
- AI支援理論形成に関心のある読者
- A10 Evidence-Lock Protocol評価者

## 誇張しない一文の結論

DTTSは、睡眠様遷移を適応的ネットワークの回復相ダイナミクスとして記述する数理プロトタイプであり、臨床睡眠モデル、医療ツール、ヒトデータ検証、または完全な生物学的睡眠理論を主張するものではない。
