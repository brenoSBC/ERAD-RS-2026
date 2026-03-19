import matplotlib.pyplot as plt
import numpy as np
import load_data
import plot_config 

plot_config.apply()

FD = load_data.FD
patterns = FD["patterns"]
frameworks = ["flink", "openmpi", "resipipe"]
colors = ["#1f77b4", "#d62728", "#2ca02c"]
x = np.arange(len(patterns))
width = 0.25

plt.figure(figsize=(8,5))

for i, fw in enumerate(frameworks):
    means = []
    stds = []
    for j in range(len(patterns)):
        data = FD[fw][j]
        means.append(np.mean(data))
        stds.append(np.std(data))
    
    plt.bar(x + i*width, means, width, yerr=stds, capsize=5,
            label=fw, color=colors[i])

plt.xticks(x + width, patterns)
plt.xlabel("Patterns")
plt.ylabel("Throughput")
plt.title("FD - Comparison")
plt.grid(axis='y')
plt.legend()
plt.tight_layout()
plt.savefig("FD_comparison.png", dpi=300)
plt.close()