import matplotlib.pyplot as plt
import numpy as np

# Generate random data
np.random.seed(0)
all_data = [np.random.normal(0, std_dev, 100) for std_dev in range(1, 4)]

fig, axs = plt.subplots(1, 3, figsize=(9, 3))

colors = ['red', 'black', 'blue']

# Generate plot for each data set
for data, color, ax in zip(all_data, colors, axs):
    ax.hist(data, bins=20, alpha=0.5, color=color, label=color)
    ax.legend()
#ad
plt.show()