import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.ticker import FuncFormatter

# Data
labels = ['Roshi-1', 'Roshi-2', 'Roshi-3', 'ODB-1', 'ODB-2', 'ODB-3', 'ODB-4', 'ODB-5', 'RDB-1', 'RDB-2', 'Yorkie-1', 'Yorkie-2']

tool = [2439.9656,
3753.58,
38769.52,
4325.179,
1890.93,
20320.56,
37298.448,
60352.34,
3560.48,
24504.012,
16125.921,
26692.68]
dfs = [9335.4391,
11041.396,
59300,
13285.427,
8668.24,
38539.93,
65761.18,
74352.34,
12964.98,
49805.116,
24350.107,
58765.08]
rand = [14325.7732,
18894.158,
73045.91,
24105.426,
19972.85,
53382.58,
78041.724,
80100,
28037.64,
68518.74,
42592.866,
70850.88]

# Set up positions for bars on X-axis
bar_width = 0.25
index = np.arange(len(labels)) * 1

# Set different colors for pattern lines
colors = sns.color_palette("husl", n_colors=3)

# Create a bar chart with different colored pattern lines
fig, ax = plt.subplots()

bars1 = ax.bar(index - bar_width, tool, width=bar_width, edgecolor='blue', label='ER-$\pi$', color='w', hatch='\\\\\\', linewidth=1)
bars2 = ax.bar(index, dfs, width=bar_width, edgecolor='darkmagenta', label='DFS', color='w', hatch='--', linewidth=1)
bars3 = ax.bar(index + bar_width, rand, width=bar_width, edgecolor='darkorange', label='Rand', color='w', hatch='xx', linewidth=1)

# Customize the chart appearance
# ax.set_xlabel('Path', fontsize=18)
ax.set_ylabel('Seconds ($log_{10}$)\n to reproduce bug', fontsize=10)
ax.set_xticks(index)
ax.set_xticklabels(labels, fontsize=10)

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
ax.set_ylim(100, 80000)

# Existing equal-spaced ticks
yticks = np.arange(10000, 90000, 10000)

# Add e^0, e^1, e^2 ticks (1, 10, 100)
yticks = np.concatenate(([1], yticks))

# Set the ticks
ax.set_yticks(yticks)

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

# Manually add arrows for specific bars (DFS and Rand of Roshi3, ODB4, ODB5, and Rand of Yorkie2)
arrows_to_draw = {
    'Roshi-3': ['dfs', 'rand'],
    'ODB-4': ['dfs', 'rand'],
    'ODB-5': ['dfs', 'rand'],
    'Yorkie-2': ['rand']
}

# Indexes for the specific bars (DFS and Rand of Roshi3, ODB4, ODB5, and Rand of Yorkie2)
manual_indices = {
    'Roshi-3': 2,  # Roshi-3 is at index 2
    'ODB-4': 6,    # ODB-4 is at index 6
    'ODB-5': 7,    # ODB-5 is at index 7
    'Yorkie-2': 11 # Yorkie-2 is at index 11
}

# Draw the arrows for the manually selected bars
for label, bar_types in arrows_to_draw.items():
    index = manual_indices[label]
    
    for bar_type in bar_types:
        if bar_type == 'dfs':
            rect = bars2[index]  # DFS bars
        elif bar_type == 'rand':
            rect = bars3[index]  # Rand bars
        
        # Get the height of the bar
        bar_height = rect.get_height()

        # Add a line for the tail just below the top of the bar
        ax.plot([rect.get_x() + rect.get_width() / 2, rect.get_x() + rect.get_width() / 2], 
                [bar_height - 5000, bar_height], color='black', lw=1.5)  # Tail line
        
        # Add the arrowhead at the top of the bar
        ax.annotate('',
                    xy=(rect.get_x() + rect.get_width() / 2, bar_height),  # Arrowhead at bar height
                    xytext=(rect.get_x() + rect.get_width() / 2, bar_height - 500),  # Tail slightly below
                    arrowprops=dict(facecolor='black', arrowstyle='-|>', lw=1.5),
                    ha='center', va='center')

# Save the chart as a PDF
plt.savefig('times.pdf', bbox_inches='tight')

# Show the plot
plt.show()