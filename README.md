# GBU Blast & Lethality Simulator

PythonとMatplotlibを使用した、代表的な誘導爆弾（GBU: Guided Bomb Unit）の爆発・加害範囲を可視化する簡易2Dシミュレーターです。

物理モデルに基づくスケーリング則を用いて、TNT換算の爆薬量から**超高圧波エリア（致死圏内）**および**破片飛散・加害エリア**のサイズを算出し、モデルごとの威力差を視覚的に比較できます。
<img width="1918" height="1097" alt="スクリーンショット 2026-08-04 071350" src="https://github.com/user-attachments/assets/9347f026-a736-4c0a-94f0-6fdec2e5dc00" />

---

## 爆弾モデル（プリセット）

| 爆弾モデル | 級 / 重量クラス | 想定TNT当量 (kg) | 主な用途・目標 |
| :--- | :--- | :--- | :--- |
| **GBU-12 Paveway II** | 500 lb class | 87 kg | 軽装甲車、近接航空支援（CAS） |
| **GBU-31 JDAM** | 2000 lb class | 429 kg | 建築物、要塞化目標 |
| **GBU-28 Bunker Buster** | 5000 lb class | 950 kg | 地下バンカー、超重装甲目標 |

---

## 特徴

* **Hopkinson-Cranz スケーリング則の適用**  
  爆風の過圧波半径（Overpressure Radius）を爆薬量の1/3乗の原則（$R \propto W^{1/3}$）に基づいて算出。
* **2段階の加害判定表示**
  * **Overpressure Radius（濃いエリア）**: 構造物破壊・人体への即死級の衝撃波影響圏。
  * **Fragment Radius（薄いエリア）**: 高速破片（フラグメンテーション）による危害・殺傷エリア。
* **統一スケール表示**  
  すべてのモデルを同じ距離スケール（メートル基準）で並列描画するため、規模感の差が直感的に把握可能。

---

## インストール & 実行方法

### 必要な依存ライブラリ
* Python 3.x
* `matplotlib`
* `numpy`

```bash
pip install matplotlib numpy
実行
Bash
python gbu_simulator.py
免責事項 (Disclaimer)
本プログラムは教育・研究・趣味目的の学術的プロトタイプです。

出力される数値は簡易的な物理計算式（スケーリング則および幾何近似）に基づく概算値であり、軍事・防衛上の厳密な爆発エネルギー・障害物による減衰・地質効果・高度等を完璧に計算するものではありません。
