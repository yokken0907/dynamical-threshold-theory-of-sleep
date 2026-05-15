import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

# ==========================================
# 1. パラメータ設定 (Numerical Settings)
# ==========================================
N = 512              # 全ノード数
M = 8                # モジュール数 (64ノード/モジュール)
n_m = N // M
T = 1000.0           # シミュレーション時間
dt = 0.05            # タイムステップ
steps = int(T / dt)

# 蔵本モデル・同期パラメータ
omega = np.random.normal(1.0, 0.02, N)  # 固有振動数
K_max = 2.0                            # 結合強度の最大値
sigma = 0.3                            # 外乱強度

# 睡眠圧 (s) & 睡眠ゲート (q) パラメータ
a = 0.1 ; chi = 0.1 ; b = 0.08        # sの時間発展係数
tau_q = 20.0 ; beta_s = 5.0 ; s_c = 0.5 # qの感度と閾値
beta_R = 5.0 ; R_c = 0.8
beta_c = 0.2 ; T_c = 800.0             # 概日リズム成分

# 結合更新 (K) & 保護場 (P) パラメータ
tau_p = 50.0 ; Theta_p = 0.8           # Pの時定数と閾値
eta_W = 0.002 ; delta_W = 0.005         # 覚醒時の増強率
eta_K = 0.05 ; mu = 1.0 ; kappa = 0.1  # 睡眠時の正規化率

# ==========================================
# 2. 階層モジュール型ネットワークの生成
# ==========================================
def generate_hierarchical_modular_network():
    G = nx.disjoint_union_all([nx.watts_strogatz_graph(n_m, 8, 0.1) for _ in range(M)])
    # モジュール間接続 (疎結合)
    nodes = list(G.nodes())
    for _ in range(int(N * 0.02)):
        u = np.random.choice(nodes)
        v = np.random.choice(nodes)
        if u // n_m != v // n_m:
            G.add_edge(u, v)
    return nx.to_numpy_array(G)

A = generate_hierarchical_modular_network()

# ==========================================
# 3. 入力信号 u(t) の生成 (Filtered Poisson Input)
# ==========================================
def get_filtered_poisson_input():
    u = np.zeros((steps, N))
    u_bg = 0.02
    v_local = np.arange(0, n_m * 4)
    tau_u = 10.0
    
    for i in v_local:
        # 平均間隔50ステップでイベント発生
        events = np.random.poisson(0.02, steps)
        for t_idx in np.where(events > 0)[0]:
            decay = np.exp(-np.arange(steps - t_idx) * dt / tau_u)
            u[t_idx:, i] += 0.5 * decay
    return u + u_bg

U_matrix = get_filtered_poisson_input()

# ==========================================
# 4. シミュレーション実行 (Main Loop)
# ==========================================
theta = np.random.uniform(0, 2*np.pi, N)
s = np.zeros(N)
q = np.zeros(N)
K = A * 0.5  # 初期結合強度
P = np.zeros_like(K)

# 記録用データ
history = {"R_G": [], "Q": [], "K_mean": [], "s_mean": [], "s_local": []}

for t_idx in range(steps):
    if t_idx % 1000 == 0:
        print(f"Progress: {t_idx}/{steps} steps ({(t_idx/steps)*100:.1f}%)")
    t = t_idx * dt

    # 局所秩序パラメータ R_i の計算
    exp_theta = np.exp(1j * theta)
    R_i = np.zeros(N)
    for i in range(N):
        neighbors = np.where(A[i] > 0)[0]
        if len(neighbors) > 0:
            R_i[i] = np.abs(np.mean(exp_theta[neighbors] * np.exp(-1j * theta[i])))
    
    # 秩序パラメータ R_G (全体)
    R_G = np.abs(np.mean(exp_theta))
    
    # 概日リズム C(t)
    C_t = np.cos(2 * np.pi * t / T_c)
    
    # --- 変数更新 (Euler-Maruyama) ---
    # 1. 位相 theta
    coupling_term = np.zeros(N)
    for i in range(N):
        coupling_term[i] = np.sum(K[i] * np.sin(theta - theta[i]))
    noise = sigma * (1 - q) * np.random.normal(0, 1, N) * np.sqrt(dt)
    theta += (omega + coupling_term) * dt + noise
    
    # 2. 睡眠圧 s
    s += (a * (1 - R_i) + chi * U_matrix[t_idx] - b * q * s) * dt
    s = np.maximum(s, 0)
    
    # 3. 睡眠ゲート q (Sigmoid型)
    q_target = 1.0 / (1.0 + np.exp(-(beta_s * (s - s_c) - beta_c * C_t - beta_R * (R_i - R_c))))
    q += (q_target - q) / tau_q * dt
    
    # 4. 保護場 P (History-dependent)
    cos_diff = np.cos(np.subtract.outer(theta, theta))
    P_target = 1.0 / (1.0 + np.exp(-10.0 * (cos_diff - Theta_p)))
    P += A * (P_target - P) / tau_p * dt
    
    # 5. 結合更新 K (選択的ダウンスケーリング)
    q_bar = np.add.outer(q, q) / 2.0
    # 覚醒側 (q_bar ~ 0): Potentiation
    dK_wake = (1 - q_bar) * (eta_W * P * (K_max - K) - delta_W * K)
    # 睡眠側 (q_bar ~ 1): Renormalization (Gradient descent)
    dK_sleep = q_bar * eta_K * (kappa * P - mu * K)
    K += (dK_wake + dK_sleep) * dt * A
    
    # データの保存
    history["R_G"].append(R_G)
    history["Q"].append(np.mean(q))
    history["K_mean"].append(np.mean(K[A > 0]))
    history["s_mean"].append(np.mean(s))
    history["s_local"].append(np.mean(s[:n_m]))

# ==========================================
# 5. 結果の可視化
# ==========================================
time_axis = np.linspace(0, T, steps)
fig, axes = plt.subplots(3, 1, figsize=(10, 12), sharex=True)

axes[0].plot(time_axis, history["R_G"], label="Global Coherence (R_G)")
axes[0].plot(time_axis, history["Q"], label="Sleep Propensity (Q)", color="red", linestyle="--")
axes[0].set_ylabel("Order / State")
axes[0].legend()
axes[0].set_title("Global Dynamics: Synchronization vs Sleep")

axes[1].plot(time_axis, history["s_mean"], label="Global Load (s_avg)")
axes[1].plot(time_axis, history["s_local"], label="Local Load (s_local: Module 0)", linewidth=2)
axes[1].axhline(y=s_c, color='k', linestyle=':', label="Threshold (s_c)")
axes[1].set_ylabel("Homeostatic Load")
axes[1].legend()

axes[2].plot(time_axis, history["K_mean"], label="Mean Coupling Strength (K)")
axes[2].set_ylabel("Coupling K")
axes[2].set_xlabel("Time")
axes[2].legend()

plt.tight_layout()
#plt.show()
plt.savefig("simulation_result.png", dpi=300)
print("Simulation complete. Result saved as simulation_result.png")
