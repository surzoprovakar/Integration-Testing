import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.ticker import FuncFormatter

# Data
path_labels = ['Roshi-1', 'Roshi-2', 'Roshi-3', 'ODB-1', 'ODB-2', 'ODB-3', 'ODB-4', 'ODB-5', 'RDB-1', 'RDB-2', 'Yorkie-1', 'Yorkie-2']
rand = [6.984563241, 9.632178564, 26.39854789, 13.57412536, 5.987798465, 17.00005632, 15.32597412, 29.36974632, 11.00698521, 12.36987412, 18.10005874, 23.48485456]
dfs = [8.963587413, 10.57896125, 28.25987413, 14.25789631, 7.605520523, 17.11649961, 16.80634102, 32.79270567, 11.55976303, 14.94040835, 19.55106852, 25.05076659]
tool = [5.47856321, 7.48984551, 23.5698741, 11.87412699, 4.503004587, 15.32896325, 13.25874126, 26.39874126, 9.687456321, 11.06987413, 16.32587412, 21.36987416]

# Set up positions for bars on X-axis
bar_width = 0.25
index = np.arange(len(path_labels)) * 1

# Set different colors for pattern lines
colors = sns.color_palette("husl", n_colors=3)

# Create a bar chart with different colored pattern lines
fig, ax = plt.subplots()

bars1 = ax.bar(index - bar_width, rand, width=bar_width, edgecolor='darkorange', label='Rand', color='w', hatch='xxxx', linewidth=1)
bars2 = ax.bar(index, dfs, width=bar_width, edgecolor='teal', label='DFS', color='w', hatch='----', linewidth=1)
bars3 = ax.bar(index + bar_width, tool, width=bar_width, edgecolor='blue', label='ER-$\pi$', color='w', hatch='\\\\\\', linewidth=1)

# Customize the chart appearance
# ax.set_xlabel('Path', fontsize=18)
ax.set_ylabel('Seconds to reproduce bug', fontsize=10)
ax.set_xticks(index)
ax.set_xticklabels(path_labels, fontsize=10)

# Set the size of the figure to 8.33 × 5.15 inches
fig.set_size_inches(12, 3)

# Function to format the Y-axis labels as 1e^something
def scientific_format(y, pos):
    if y == 0:
        return r'$e^0$'
    exponent = int(np.log10(y))
    coefficient = y / 10**exponent
    # print(coefficient)
    return fr'${coefficient:.1f}e^{{{exponent}}}$'

# Set the formatter for the Y-axis
ax.yaxis.set_major_formatter(FuncFormatter(scientific_format))

# Add a legend
# ax.legend(fontsize=16)
ax.legend(fontsize=10, loc='upper center', bbox_to_anchor=(0.5, 1.15), fancybox=True, ncol=3)

# Draw horizontal lines for each "Tool" bar
for i, x in enumerate(index + bar_width):
    ax.hlines(tool[i], x - 2.5* bar_width, x + 0.5*bar_width, color='blue', linestyle='-', linewidth=2)

# Save the chart as a PDF
plt.savefig('times.pdf', bbox_inches='tight')

# Show the plot
plt.show()