import matplotlib.pyplot as plt
import numpy as np

tamanhos = ["1.000", "10.000", "100.000"]
x = np.arange(len(tamanhos))
width = 0.25

# Tempos médios (N/C = None)
insert_tempo = [0.02206, 2.394407, None]
bubble_tempo  = [0.029623, 3.197125, None]
merge_tempo   = [0.0013, 0.017176, 0.235488]

# Trocas (N/C = None)
insert_trocas = [239421, 25050317, None]
bubble_trocas  = [239421, 25050317, None]
merge_trocas   = [9976, 133616, 1668928]

def substituir_none(valores):
    return [v if v is not None else 0 for v in valores]

def adicionar_nc(ax, valores, posicoes):
    for i, v in enumerate(valores):
        if v is None:
            ax.text(posicoes[i], 0.01, "N/C", ha="center", va="bottom", fontsize=8, color="black")

# ── Gráfico 1: Tempo Médio ────────────────────────────────────────────────
fig, ax1 = plt.subplots(figsize=(10, 6))

b1 = ax1.bar(x - width, substituir_none(insert_tempo), width, label="Insertion Sort – O(n²)",  color="red",    alpha=0.8)
b2 = ax1.bar(x,         substituir_none(bubble_tempo),  width, label="Bubble Sort – O(n²)",    color="orange", alpha=0.8)
b3 = ax1.bar(x + width, substituir_none(merge_tempo),   width, label="Merge Sort – O(n log n)",color="blue",   alpha=0.8)

adicionar_nc(ax1, insert_tempo, x - width)
adicionar_nc(ax1, bubble_tempo, x)

ax1.set_title("Comparativo de Tempo Médio de Execução")
ax1.set_xlabel("Tamanho do Vetor (n)")
ax1.set_ylabel("Tempo Médio (s)")
ax1.set_xticks(x)
ax1.set_xticklabels(tamanhos)
ax1.legend()
ax1.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("grafico_tempo.png", dpi=150)
plt.show()

# ── Gráfico 2: Trocas/Movimentações ──────────────────────────────────────
fig, ax2 = plt.subplots(figsize=(10, 6))

ax2.bar(x - width, substituir_none(insert_trocas), width, label="Insertion Sort – O(n²)",  color="red",    alpha=0.8)
ax2.bar(x,         substituir_none(bubble_trocas),  width, label="Bubble Sort – O(n²)",    color="orange", alpha=0.8)
ax2.bar(x + width, substituir_none(merge_trocas),   width, label="Merge Sort – O(n log n)",color="blue",   alpha=0.8)

adicionar_nc(ax2, insert_trocas, x - width)
adicionar_nc(ax2, bubble_trocas, x)

ax2.set_title("Comparativo de Trocas / Movimentações")
ax2.set_xlabel("Tamanho do Vetor (n)")
ax2.set_ylabel("Quantidade de Trocas / Movimentações")
ax2.set_xticks(x)
ax2.set_xticklabels(tamanhos)
ax2.legend()
ax2.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("grafico_trocas.png", dpi=150)
plt.show()