import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.ticker import FuncFormatter

# Data
path_labels = ['Roshi-1', 'Roshi-2', 'Roshi-3', 'ODB-1', 'ODB-2', 'ODB-3', 'ODB-4', 'ODB-5', 'RDB-1', 'RDB-2', 'Yorkie-1', 'Yorkie-2']

tool = [504, 778, 7864, 0, 0, 0, 0, 0, 0, 0, 1231, 5173]
dfs = [2869, 3124, 18934, 0, 0, 0, 0, 0, 0, 0, 1877, 9063]
rand = [3788, 3946, 26987, 0, 0, 0, 0, 0, 0, 0, 2126, 12568]

# Set up positions for bars on X-axis
bar_width = 0.25
index = np.arange(len(path_labels)) * 1

# Set different colors for pattern lines
colors = sns.color_palette("husl", n_colors=3)

# Create a bar chart with different colored pattern lines
fig, ax = plt.subplots()

bars1 = ax.bar(index - bar_width, tool, width=bar_width, edgecolor='blue', label='ER-$\pi$', color='w', hatch='\\\\\\', linewidth=1)
bars2 = ax.bar(index, dfs, width=bar_width, edgecolor='darkmagenta', label='DFS', color='w', hatch='--', linewidth=1)
bars3 = ax.bar(index + bar_width, rand, width=bar_width, edgecolor='darkorange', label='Rand', color='w', hatch='xx', linewidth=1)

# Customize the chart appearance
# ax.set_xlabel('Path', fontsize=18)
ax.set_ylabel('# Interleavings explored\n to reproduce bug', fontsize=10)
ax.set_xticks(index)
ax.set_xticklabels(path_labels, fontsize=10)

# Set x-axis limits to reduce extra space
ax.set_xlim(index[0] - bar_width * 3, index[-1] + bar_width * 3)

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


# Set Y-axis limits to 10 and 10000
ax.set_ylim(10, 10000)

# Set Y-ticks to display 1e^1 to 1e^4
# yticks = [10, 100, 1000, 10000]
# ax.set_yticks(yticks)

# Set the formatter for the Y-axis
ax.yaxis.set_major_formatter(FuncFormatter(scientific_format))

# Adjust the layout to prevent overlap
plt.tight_layout()

# Add a legend
# ax.legend(fontsize=16)
ax.legend(fontsize=10, loc='upper center', bbox_to_anchor=(0.5, 1.12), 
          fancybox=True, ncol=3, handlelength=4, framealpha=0.0, edgecolor='none')

# Draw horizontal lines for each "Tool" bar
for i, x in enumerate(index + bar_width):
    ax.hlines(tool[i], x - 2.5* bar_width, x + 0.5*bar_width, color='blue', linestyle='-', linewidth=2)

# Check if values exceed the y-axis limit and draw upward arrows
for bar_group, data, label in zip([bars1, bars2, bars3], [tool, dfs, rand], ['tool', 'dfs', 'rand']):
    for i, rect in enumerate(bar_group):
        height = data[i]
        if height > 10000:
            # Add a line for the tail
            ax.plot([rect.get_x() + rect.get_width() / 2, rect.get_x() + rect.get_width() / 2], 
                    [9400, 10000], color='black', lw=1.5)  # Tail line
            
            # Add the arrowhead
            ax.annotate('',
                        xy=(rect.get_x() + rect.get_width() / 2, 10000),  # Arrowhead at 10000
                        xytext=(rect.get_x() + rect.get_width() / 2, 9800),  # Tail slightly below
                        arrowprops=dict(facecolor='black', arrowstyle='-|>', lw=1.5),
                        ha='center', va='center')

# Save the chart as a PDF
plt.savefig('paths.pdf', bbox_inches='tight')

# Show the plot
plt.show()