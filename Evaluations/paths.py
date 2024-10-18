import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.ticker import FuncFormatter

# Data
path_labels = ['Roshi-1', 'Roshi-2', 'Roshi-3', 'ODB-1', 'ODB-2', 'ODB-3', 'ODB-4', 'ODB-5', 'RDB-1', 'RDB-2', 'Yorkie-1', 'Yorkie-2']
rand = [4.813698754, 6.210069321, 19.7065321, 7.963258741, 4.301298635, 11.39846216, 13.5879631, 21.36987545, 6.659874563, 10.65897456, 12.96325874, 19.56874124]
dfs = [5.559763033, 6.059763033, 19.70834391, 8.680336964, 4.605520523, 12.11649961, 15.80634102, 23.79270567, 6.959763033, 10.94040835, 14.55106852, 21.05076659]
tool = [3.68632154, 4.69874123, 17.69852347, 6.702563214, 3.069874125, 9.632587413, 11.69852148, 18.36985215, 5.489632154, 8.658974125, 11.98746321, 17.69854124]

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
ax.set_ylabel('# Interleavings to reproduce bug', fontsize=10)
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
plt.savefig('paths.pdf', bbox_inches='tight')

# Show the plot
plt.show()