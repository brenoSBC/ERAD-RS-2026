import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 14,
    "axes.labelsize": 18,
    "xtick.labelsize": 14,
    "ytick.labelsize": 14,
    "legend.fontsize": 14,
    "axes.linewidth": 1.2
})

datasets = [
    {
        ####################
        #        FD        # 
        ####################        
        "name": "fd",

        "patterns": ['fd_111', 'fd_121', 'fd_131', 'fd_141', 'fd_161', 'fd_181'],

        "openmpi": [
            [],
            [],
            [],
            [],
            [],
            []
        ],
        "resipipe": [
            [],
            [],
            [],
            [],
            [],
            []
        ],
        "flink": [
            [],
            [],
            [],
            [],
            [],
            []
        ]
    },
    {
        ####################
        #        SA        # 
        ####################        
        "name": "sa",

        "patterns": ['sa111', 'sa121', 'sa131', 'sa141', 'sa161', 'sa181'],

        "openmpi": [
            [],
            [],
            [],
            [],
            [],
            []
        ],
        "resipipe": [
            [],
            [],
            [],
            [],
            [],
            []
        ],
         "flink": [
            [],
            [],
            [],
            [],
            [],
            [],
        ]
    },
    {
        ####################
        #        SD        # 
        ####################        
        "name": "sd",

        "patterns": ['sd1111', 'sd1221', 'sd1331', 'sd1441', 'sd1641', 'sd1861'],

        "openmpi": [
            [],
            [],
            [],
            [],
            [],
            []
        ],
        "resipipe": [
            [],
            [],
            [],
            [],
            [],
            []
        ],
         "flink": [
            [],
            [],
            [],
            [],
            [],
            [],
        ]
    },
    {
        ####################
        #        TM        # 
        ####################         
        "name": "tm",
        
        "patterns": ['tm1111', 'tm1221', 'tm1331', 'tm1441', 'sd1641', 'tm1861'],

        "openmpi": [
            [],
            [],
            [],
            [],
            [],
            []
        ],
        "resipipe": [
            [],
            [],
            [],
            [],
            [],
            []
        ],
         "flink": [
            [],
            [],
            [],
            [],
            [],
            [],
        ]
    },
]

# média e desvio padrão
def mean_std(data):
    arr = np.array(data)
    mean = np.mean(arr, axis=1) # média por linha
    std = np.std(arr, axis=1, ddof=1)
    return mean, std


for dataset in datasets:
        for system in ["openmpi", "resipipe", "flink"]: 
            dataset[f"{system}_mean"], dataset[f"{system}_std"] = mean_std(dataset[system])
