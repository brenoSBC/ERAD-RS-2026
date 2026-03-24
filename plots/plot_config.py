import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

FIRST_COLOR = {
    "openmpi": "#52B352",
    "resipipe": "#159CEB",
    "flink": "#F57C25",
}

SECOND_COLOR = {
    "openmpi": "#ABEBAB",
    "resipipe": "#bae1ff",
    "flink": "#ffdfba",
}

ERROR_COLOR = {
    "openmpi": "#00A600",
    "resipipe": "#0766F5",
    "flink": "#F0501A" ,
}

HATCH = {
    "openmpi": "//////\\\\\\\\\\\\",
    "resipipe": "//////\\\\\\\\\\\\",
    "flink": "//////\\\\\\\\\\\\",
}

DISPLAY_NAME = {
    "openmpi": "OpenMPI",
    "resipipe": "ResiPipe",
    "flink": "Flink",
}

LEGEND_CONFIG = {
    "loc": "upper center",
    "bbox_to_anchor": (0.5, 1.2),
    "ncol": 3,
    "frameon": False,
}

def apply():
    plt.rcParams.update({
        "font.family": "DejaVu Serif",
        "font.serif": ["Times New Roman"],
        "font.size": 17,
        "axes.titlesize": 17,
        "axes.labelsize": 17,
        "legend.fontsize": 17,
        "xtick.labelsize": 17,
        "ytick.labelsize": 17,
        "hatch.linewidth": 0.5, 
    })


def format_k(x, pos):
    if x >= 1000:
        v = x / 1000
        return f"{int(v)}K" if v.is_integer() else f"{v:.1f}K"
    return f"{int(x)}"

