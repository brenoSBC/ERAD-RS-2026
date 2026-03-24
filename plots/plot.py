import matplotlib.pyplot as plt
import numpy as np

import load_data
import plot_config 


def plot_app(application, pattern, name):

    width = 0.24
    gap = 0.015
    
    # posições base no eixo x (uma por configuração de paralelismo)
    x = np.arange(len(pattern))
    
    # fig = a imagem completa
    # ax  = o sistema de eixos, onde os dados são plotados (barras, linhas...)
    fig, ax = plt.subplots(figsize=(8, 4.5))           

    for i, fw in enumerate(frameworks):

        means = []
        stds = []

        for j in range(len(pattern)):
            data = application[fw][j]
            means.append(np.mean(data))
            stds.append(np.std(data))
        
        ax.bar(
            x + i*(width + gap),                                                                                                # desloca cada framework para o lado
            means,                                                                                                              # altura das barras (média)
            width=0.24,                                                                                                         # largura de cada barra
            yerr=stds,                                                                                                          # tamanho da barra de erro (desvio padrão)
            capsize=8,                                                                                                          # tamanho das linhas nas extremidades da barra de erro
            label=plot_config.DISPLAY_NAME[fw],                                                                                 # nome na legenda
            facecolor=plot_config.SECOND_COLOR[fw],                                                                             # cor de preenchimento da barra
            edgecolor=plot_config.FIRST_COLOR[fw],                                                                              # cor da borda da barra e do hatch
            error_kw=dict(
                        ecolor=plot_config.ERROR_COLOR[fw],   # cor da barra de erro
                        linewidth=0.6,                        # espessura da linha da barra de erro
                        capthick=0.6                          # espessura das extremidades da barra de erro
            ),   

            hatch=plot_config.HATCH[fw],                                                                                        # tipo do hatch
            linewidth=0.9,                                                                                                      # espessura da borda da barra
        )

    ax.legend(**plot_config.LEGEND_CONFIG)                    # desenha a legenda
 
    ax.set_xticks(x + width)                                  # define onde ficam os ticks no eixo X (posição dos labels)
    ax.set_xticklabels(pattern)                               # define os nomes dos ticks (ex: "111", "121", ...)

    ax.set_xlabel("Configuração de paralelismo")              # nome do eixo X
    ax.set_ylabel("Vazão [itens/s]")                          # nome do eixo Y


    # formata eixo Y para milhares (ex: 70000 → 70K)
    ax.yaxis.set_major_formatter(
        plt.FuncFormatter(plot_config.format_k)
    )

    
    ax.grid(axis='y', linestyle="--", alpha=0.5)         # grid, linhas pontilhadas para ajudar a ler os valores
    ax.set_axisbelow(True)                               # garante que o grid fique atrás das barras

    plt.tight_layout(rect=[0, 0, 1, 0.9])                # ajusta espaçamento automático (evita cortar legenda/títulos)
    plt.savefig(f'graphs/{name}.pdf', dpi=300)           # salva figura
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

frameworks = ["openmpi", "resipipe", "flink"]

plot_app(FD, patterns_fd, "FD")
plot_app(SA, patterns_sa, "SA")
plot_app(SD, patterns_sd, "SD")
plot_app(TM, patterns_tm, "TM")
