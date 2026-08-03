import matplotlib.pyplot as plt
import numpy as np

# 1. 爆弾データの定義 (名前, 装薬量TNT当量[kg], 色)
gbu_data = {
    "GBU-12 (500 lb class)": {
        "tnt_kg": 87,      # Tritonal/PBXN-109等実質TNT換算値
        "color": "#3085C3",
        "desc": "近接支援・軽装甲目標用"
    },
    "GBU-31 JDAM (2000 lb class)": {
        "tnt_kg": 429,     # MK-84弾頭相当
        "color": "#E55604",
        "desc": "建造物・頑丈な目標用"
    },
    "GBU-28 Bunker Buster (5000 lb class)": {
        "tnt_kg": 950,     # BLU-113相当
        "color": "#2B2A4C",
        "desc": "地下バンカー・超重装甲目標用"
    }
}

def calculate_radii(tnt_kg):
    """
    簡易物理モデル(Hopkinson-Cranz スケーリング則に基づく):
    - Overpressure (過圧/爆風波致死半径): R ∝ W^(1/3)
    - Fragment (破片効果半径): R ∝ W^(1/2) 近似
    """
    # 致命的な爆風・高圧ゾーン (約100 kPa過圧)
    r_overpressure = 12.0 * (tnt_kg ** (1/3))
    
    # 有効破片加害半径 (軽車両・歩兵への致死・危害)
    r_fragment = 18.0 * (tnt_kg ** (0.42))
    
    return r_overpressure, r_fragment

# 2. 描画セットアップ
fig, axes = plt.subplots(1, 3, figsize=(16, 6), subplot_kw={'aspect': 'equal'})
fig.suptitle("GBU (Guided Bomb Unit) Blast & Lethality Comparison Simulator", fontsize=16, fontweight='bold')

angles = np.linspace(0, 2 * np.pi, 200)

for ax, (name, info) in zip(axes, gbu_data.items()):
    r_blast, r_frag = calculate_radii(info["tnt_kg"])
    color = info["color"]
    
    # 円の座標計算
    x_blast, y_blast = r_blast * np.cos(angles), r_blast * np.sin(angles)
    x_frag, y_frag = r_frag * np.cos(angles), r_frag * np.sin(angles)
    
    # 破片・加害エリア（外側の円）
    ax.fill(x_frag, y_frag, color=color, alpha=0.2, label=f"Frag Radius ({r_frag:.1f}m)")
    ax.plot(x_frag, y_frag, color=color, linestyle="--", linewidth=1.5)
    
    # 爆風・超高圧エリア（内側の円）
    ax.fill(x_blast, y_blast, color=color, alpha=0.6, label=f"Overpressure Radius ({r_blast:.1f}m)")
    ax.plot(x_blast, y_blast, color=color, linewidth=2)
    
    # 爆心地マーク
    ax.plot(0, 0, 'r*', markersize=12, label="Impact Point")
    
    # グラフの見た目調整
    max_range = 350  # 軸のスケールを統一
    ax.set_xlim(-max_range, max_range)
    ax.set_ylim(-max_range, max_range)
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.set_title(f"{name}\n({info['desc']})", fontsize=11)
    ax.set_xlabel("Distance (meters)")
    ax.set_ylabel("Distance (meters)")
    ax.legend(loc="upper right", fontsize=8)

plt.tight_layout()
plt.show()
