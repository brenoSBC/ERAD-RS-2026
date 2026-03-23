import matplotlib.pyplot as plt
import numpy as np

import load_data
import plot_config 


def plot_app(application, pattern, name):
    x = np.arange(len(pattern))
    fig, ax = plt.subplots(figsize=plot_config.FIG_SIZE)

    for i, fw in enumerate(frameworks):

        means = []
        stds = []

        for j in range(len(pattern)):
            data = application[fw][j]
            means.append(np.mean(data))
            stds.append(np.std(data))
        
        ax.bar(
            x + i*(width + gap),                                                                                                                        # move cada framework para o lado
            means,
            width,
            yerr=stds,                                                                                                                                   # barra de erro (std)
            capsize=plot_config.std_capsize,                                                                                                                           # linha horizontal em cima e embaixo da linha de erro
            label=plot_config.DISPLAY_NAME[fw],                                                                                                         # nome na legenda
            facecolor=plot_config.SECOND_COLOR[fw],                                                                                          # cor interna da barra
            edgecolor=plot_config.FIRST_COLOR[fw],                                                                                               # cor do hatch
            error_kw=dict(ecolor=plot_config.ERROR_COLOR[fw], linewidth=plot_config.std_linewidth, capthick=plot_config.std_capthick),                # cor da linha de erro e espessura
            hatch=plot_config.HATCH[fw],                                                                                                                  # tipo de hatch
            linewidth=0.9,                                                                                                                                  # espessura da borda da barra
        )

    # legenda no topo
    ax.legend(plot_config.LEGEND_CONFIG)

    ax.set_xticks(x + width)        
    ax.set_xticklabels(pattern)

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
    plt.savefig(f"{name}.png", dpi=300)                      # salva imagem, dpi=300 qualidade alta
    plt.close()     




FD = load_data.FD
SA = load_data.SA
SD = load_data.SD
TM = load_data.TM

patterns_fd = FD["patterns"]
patterns_sa = SA["patterns"]
patterns_sd = SD["patterns"]
patterns_tm = TM["patterns"]


plot_config.apply()

width = plot_config.width                                #largura de cada barra
gap = plot_config.gap0

frameworks = ["openmpi", "resipipe", "flink"]

plot_app(FD, patterns_fd, "FD")
plot_app(SA, patterns_sa, "SA")
plot_app(SD, patterns_sd, "SD")
plot_app(TM, patterns_tm, "TM")