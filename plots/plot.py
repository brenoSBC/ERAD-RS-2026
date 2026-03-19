import matplotlib.pyplot as plt
import numpy as np

import load_data

FD = load_data.FD
SA = load_data.SA
SD = load_data.SD
TM = load_data.TM

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 14,
    "axes.labelsize": 18,
    "xtick.labelsize": 14,
    "ytick.labelsize": 14,
    "legend.fontsize": 14,
    "axes.linewidth": 1.2
})

patterns = FD["patterns"]
x = np.arange(len(patterns))  # posições no eixo x
width = 0.25  # largura das barras

frameworks = ["flink", "openmpi", "resipipe"]

for i, fw in enumerate(frameworks):
    means = []
    stds = []

    for j in range(len(patterns)):
        data = FD[fw][j]
        
        means.append(np.mean(data))
        stds.append(np.std(data))

    # posição deslocada pra cada framework
    plt.bar(x + i*width, means, width, yerr=stds, label=fw, capsize=5)

# ajustar eixo x
plt.xticks(x + width, patterns)

plt.title("FD")
plt.xlabel("Patterns")
plt.ylabel("Throughput")

plt.legend()
plt.grid(axis='y')

plt.show()

# datasets = [
#     {
#         ####################
#         #        FD        # 
#         ####################        
#         "name": "fd",

#         "patterns": ['fd_111', 'fd_121', 'fd_131', 'fd_141', 'fd_161', 'fd_181'],

#         "openmpi": [
#             [],
#             [],
#             [],
#             [],
#             [],
#             []
#         ],
#         "resipipe": [
#             [],
#             [],
#             [],
#             [],
#             [],
#             []
#         ],
#         "flink": [
#             [],
#             [],
#             [],
#             [],
#             [],
#             []
#         ]
#     },
#     {
#         ####################
#         #        SA        # 
#         ####################        
#         "name": "sa",

#         "patterns": ['sa111', 'sa121', 'sa131', 'sa141', 'sa161', 'sa181'],

#         "openmpi": [
#             [],
#             [],
#             [],
#             [],
#             [],
#             []
#         ],
#         "resipipe": [
#             [],
#             [],
#             [],
#             [],
#             [],
#             []
#         ],
#          "flink": [
#             [],
#             [],
#             [],
#             [],
#             [],
#             [],
#         ]
#     },
#     {
#         ####################
#         #        SD        # 
#         ####################        
#         "name": "sd",

#         "patterns": ['sd1111', 'sd1221', 'sd1331', 'sd1441', 'sd1641', 'sd1861'],

#         "openmpi": [
#             [],
#             [],
#             [],
#             [],
#             [],
#             []
#         ],
#         "resipipe": [
#             [],
#             [],
#             [],
#             [],
#             [],
#             []
#         ],
#          "flink": [
#             [],
#             [],
#             [],
#             [],
#             [],
#             [],
#         ]
#     },
#     {
#         ####################
#         #        TM        # 
#         ####################         
#         "name": "tm",
        
#         "patterns": ['tm1111', 'tm1221', 'tm1331', 'tm1441', 'sd1641', 'tm1861'],

#         "openmpi": [
#             [],
#             [],
#             [],
#             [],
#             [],
#             []
#         ],
#         "resipipe": [
#             [],
#             [],
#             [],
#             [],
#             [],
#             []
#         ],
#          "flink": [
#             [],
#             [],
#             [],
#             [],
#             [],
#             [],
#         ]
#     },
# ]
