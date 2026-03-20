import matplotlib.pyplot as plt
import numpy as np

import load_data
import plot_config 

# fonte, tamanho de texto, etc (visual padrão)
plot_config.apply()

TM = load_data.TM
patterns = TM["patterns"]

frameworks = ["openmpi", "resipipe", "flink"]


x = np.arange(len(patterns))
width = 0.24                                        #largura de cada barra

fig, ax = plt.subplots(figsize=(8,4.5))             # cria o fundo(fig) e onde o gráfico vai ser desenhado(ax)

gap = 0.01
for i, fw in enumerate(frameworks):

    means = []
    stds = []

    for j in range(len(patterns)):
        data = TM[fw][j]
        means.append(np.mean(data))
        stds.append(np.std(data))
    
    ax.bar(
        x + i*(width + gap),                                                                            # move cada framework para o lado
        means,
        width,
        yerr=stds,                                                                                      # barra de erro (std)
        capsize=8,                                                                                      # linha horizontal em cima e embaixo da linha de erro
        label=plot_config.DISPLAY_NAMES[fw],                                                            # nome na legenda
        facecolor=plot_config.BACK_COLORS[fw],                                                          # cor interna da barra
        edgecolor=plot_config.COLORS[fw],                                                               # cor do hatch
        error_kw=dict(ecolor=plot_config.ERROS_COLORS[fw], linewidth=0.6, capthick=0.6),                # cor da linha de erro e espessura
        hatch=plot_config.HATCHES[fw],                                                                  # tipo de hatch
        linewidth=0.9,                                                                                  # espessura da borda da barra
    )

# legenda no topo
ax.legend(
    loc="upper center",             # coloca a legenda acima do gráfico
    bbox_to_anchor=(0.5, 1.2),   
    ncol=3,                      
    frameon=False                
)

ax.set_xticks(x + width)        
ax.set_xticklabels(patterns)

ax.set_xlabel("Configuração de paralelismo")
ax.set_ylabel("Vazão [itens/s]")

# formatter
# transforma milhares em 'K' - 70000 = 70K
ax.yaxis.set_major_formatter(
    plt.FuncFormatter(plot_config.format_k)
)

# grid
ax.grid(axis='y', linestyle="--", alpha=0.5)        # linhas pontilhadas para ajudar a ler os valores
ax.set_axisbelow(True)                              # grid fica atrás das barras

plt.tight_layout(rect=[0, 0, 1, 0.9])               # espaço pra legenda evita que coisas se sobreponham
plt.savefig("TM.png", dpi=300)                      # salva imagem, dpi=300 qualidade alta
plt.close()     