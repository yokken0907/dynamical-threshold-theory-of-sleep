import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

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
omega = np.random.normal(1.0, 0.02, N)
K_max = 2.0
sigma = 0.3          # 外乱強度 (波及を促すため高め)

# 睡眠圧 (s) & 睡眠ゲート (q) パラメータ
a = 0.1 ; chi = 0.1 ; b = 0.08         # 疲労蓄積率 (aを修正)
tau_q = 20.0 ; beta_s = 5.0 ; s_c = 0.5
beta_R = 5.0 ; R_c = 0.8               # 局所同期崩壊による誘発項
beta_c = 0.2 ; T_c = 800.0

# 結合更新 (K), 保護場 (P), 自由エネルギー (F_s) パラメータ
tau_p = 50.0 ; Theta_p = 0.8
eta_W = 0.002 ; delta_W = 0.005        # 覚醒時の増強率 (過同期防止)
eta_K = 0.05 ; mu = 1.0 ; kappa = 0.1  # 睡眠時の固定点 K* = 0.1*P (修正済)
nu = 1.0                               # 自由エネルギー s^2 の係数

# ==========================================
# 2. ネットワークと入力の生成
# ==========================================
def generate_hierarchical_modular_network():
    G = nx.disjoint_union_all([nx.watts_strogatz_graph(n_m, 8, 0.1) for _ in range(M)])
    nodes = list(G.nodes())
    for _ in range(int(N * 0.02)):
        u = np.random.choice(nodes)
        v = np.random.choice(nodes)
        if u // n_m != v // n_m:
            G.add_edge(u, v)
    return nx.to_numpy_array(G)

A = generate_hierarchical_modular_network()

def get_filtered_poisson_input():
    u = np.zeros((steps, N))
    u_bg = 0.02
    v_local = np.arange(0, n_m * 4) # 第0～3モジュール (50%駆動)
    tau_u = 10.0
    
    for i in v_local:
        events = np.random.poisson(0.02, steps)
        for t_idx in np.where(events > 0)[0]:
            decay = np.exp(-np.arange(steps - t_idx) * dt / tau_u)
            u[t_idx:, i] += 0.5 * decay
    return u + u_bg

U_matrix = get_filtered_poisson_input()

# ==========================================
# 3. シミュレーション実行
# ==========================================
theta = np.random.uniform(0, 2*np.pi, N)
s = np.zeros(N)
q = np.zeros(N)
K = A * 0.5
P = np.zeros_like(K)

history = {"R_G": [], "Q": [], "K_mean": [], "s_mean": [], "s_local": [], "F_s": []}

# 選択的ダウンスケーリング解析用の状態保存変数
sleep_triggered = False
K_pre_sleep = None
P_pre_sleep = None

for t_idx in range(steps):
    if t_idx % 2000 == 0:
        print(f"Progress: {t_idx}/{steps} steps ({(t_idx/steps)*100:.1f}%)")
    t = t_idx * dt
    
    exp_theta = np.exp(1j * theta)
    R_i = np.zeros(N)
    for i in range(N):
        neighbors = np.where(A[i] > 0)[0]
        if len(neighbors) > 0:
            R_i[i] = np.abs(np.mean(exp_theta[neighbors] * np.exp(-1j * theta[i])))
    
    R_G = np.abs(np.mean(exp_theta))
    Q_mean = np.mean(q)
    C_t = np.cos(2 * np.pi * t / T_c)
    
    # 睡眠相への突入(Q > 0.5)を検知し、その瞬間のKとPを記録
    if not sleep_triggered and Q_mean > 0.5:
        sleep_triggered = True
        K_pre_sleep = K.copy()
        P_pre_sleep = P.copy()
        print(f"Sleep phase triggered at t={t:.1f}")

    # 変数更新
    coupling_term = np.zeros(N)
    for i in range(N):
        coupling_term[i] = np.sum(K[i] * np.sin(theta - theta[i]))
    noise = sigma * (1 - q) * np.random.normal(0, 1, N) * np.sqrt(dt)
    theta += (omega + coupling_term) * dt + noise
    
    s += (a * (1 - R_i) + chi * U_matrix[t_idx] - b * q * s) * dt
    s = np.maximum(s, 0)
    
    q_target = 1.0 / (1.0 + np.exp(-(beta_s * (s - s_c) - beta_c * C_t - beta_R * (R_i - R_c))))
    q += (q_target - q) / tau_q * dt
    
    cos_diff = np.cos(np.subtract.outer(theta, theta))
    P_target = 1.0 / (1.0 + np.exp(-10.0 * (cos_diff - Theta_p)))
    P += A * (P_target - P) / tau_p * dt
    
    q_bar = np.add.outer(q, q) / 2.0
    dK_wake = (1 - q_bar) * (eta_W * P * (K_max - K) - delta_W * K)
    dK_sleep = q_bar * eta_K * (kappa * P - mu * K)
    K += (dK_wake + dK_sleep) * dt * A
    
    # 自由エネルギー F_s の計算 (対称行列のため半分にする)
    F_s_coupling = np.sum(A * (0.5 * mu * K**2 - kappa * P * K)) / 2.0
    F_s_load = 0.5 * nu * np.sum(s**2)
    F_s = F_s_coupling + F_s_load
    
    history["R_G"].append(R_G)
    history["Q"].append(Q_mean)
    history["K_mean"].append(np.mean(K[A > 0]))
    history["s_mean"].append(np.mean(s))
    history["s_local"].append(np.mean(s[:n_m]))
    history["F_s"].append(F_s)

# ==========================================
# 4. 結果の可視化と保存
# ==========================================
time_axis = np.linspace(0, T, steps)

# --- Figure 1: 時系列ダイナミクス (F_s 追加版) ---
fig1, axes1 = plt.subplots(4, 1, figsize=(10, 16), sharex=True)

axes1[0].plot(time_axis, history["R_G"], label="Global Coherence (R_G)")
axes1[0].plot(time_axis, history["Q"], label="Sleep Propensity (Q)", color="red", linestyle="--")
axes1[0].set_ylabel("Order / State")
axes1[0].legend()
axes1[0].set_title("Global Dynamics: Synchronization vs Sleep")

axes1[1].plot(time_axis, history["s_mean"], label="Global Load (s_avg)")
axes1[1].plot(time_axis, history["s_local"], label="Local Load (s_local: Mod 0)", linewidth=2)
axes1[1].axhline(y=s_c, color='k', linestyle=':', label="Threshold (s_c)")
axes1[1].set_ylabel("Homeostatic Load")
axes1[1].legend()

axes1[2].plot(time_axis, history["K_mean"], label="Mean Coupling Strength (K)")
axes1[2].set_ylabel("Coupling K")
axes1[2].legend()

axes1[3].plot(time_axis, history["F_s"], label="Reduced Free Energy ($\mathcal{F}_s$)", color="purple")
axes1[3].set_ylabel("Free Energy")
axes1[3].set_xlabel("Time")
axes1[3].legend()

plt.tight_layout()
fig1.savefig("fig_timeseries_final.png", dpi=300)

# --- Figure 2: 選択的ダウンスケーリングの証明 (散布図) ---
if sleep_triggered:
    delta_K = K - K_pre_sleep
    
    # 結合が存在するエッジ (A > 0) のみ抽出 (上三角行列成分のみ)
    idx_upper = np.triu_indices(N, k=1)
    valid_edges = A[idx_upper] > 0
    
    P_vals = P_pre_sleep[idx_upper][valid_edges]
    dK_vals = delta_K[idx_upper][valid_edges]
    
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    ax2.scatter(P_vals, dK_vals, alpha=0.3, edgecolors='none', s=10)
    ax2.axhline(y=0, color='k', linestyle='--')
    ax2.set_xlabel("Pre-sleep Protection Field ($P_{ij}$)")
    ax2.set_ylabel("Change in Coupling ($\Delta K_{ij}$)")
    ax2.set_title("Selective Down-selection during Sleep Phase")
    fig2.savefig("fig_scatter_selective.png", dpi=300)
    print("Scatter plot generated.")
else:
    print("Sleep phase was not triggered. Scatter plot skipped.")

print("Simulation complete. Results saved as fig_timeseries_final.png and fig_scatter_selective.png")