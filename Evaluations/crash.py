import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.ticker import FuncFormatter

# Data from the table
attempts = [1, 2, 3, 4, 5]
tool = [8034, 8034, 8034, 8034, 8034]
dfs = [18922, 17634, 16954, 15964, 19025]
rand = [17879, 16125, 15964, 18569, 17234]

# Custom scientific formatter for Y-axis
def scientific_format(y, pos):
    if y == 0:
        return r'$e^0$'
    exponent = int(np.log10(y))
    coefficient = y / 10**exponent
    return fr'${coefficient:.1f}e^{{{exponent}}}$'

# Create the plot
fig, ax = plt.subplots(figsize=(5, 2.5))

# Plotting tool 
ax.scatter(attempts, tool, marker=r'$\checkmark$', color='blue', s=150, label='ER-$\pi$')

# Plotting DFS
for i, value in enumerate(dfs):
    if value == 15964:
        ax.scatter(attempts[i], value, marker=r'$\checkmark$', color='darkmagenta', s=150)  # Tick mark
    else:
        ax.scatter(attempts[i], value, marker='x', color='darkmagenta', s=100)  # Cross mark

# Plotting Rand
ax.scatter(attempts, rand, marker='x', color='darkorange', s=100, label='Rand')

# Apply scientific formatter to Y-axis
ax.yaxis.set_major_formatter(FuncFormatter(scientific_format))

# Set Y-axis limits from 6.0e^3 to 2.0e^4
ax.set_ylim(6000, 20000)

# Existing equal-spaced ticks
yticks = np.arange(7500, 21000, 2500)

# Set the ticks
ax.set_yticks(yticks)

# Adding labels and title
ax.set_xlabel('Attempt #')
ax.set_ylabel('Interleavings #($log_{10}$)')
ax.set_xticks(attempts)  # Set x-ticks to show each attempt

# Adding a grid for better readability
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Custom legend handles with small rectangles
legend_handles = [
    Line2D([0], [0], color='blue', lw=10, label='ER-$\pi$'),
    Line2D([0], [0], color='darkmagenta', lw=10, label='DFS'),
    Line2D([0], [0], color='darkorange', lw=10, label='Rand')
]

# Add legend with custom handles
ax.legend(handles=legend_handles, fontsize=10, loc='upper center', 
          bbox_to_anchor=(0.5, 1.2), fancybox=True, ncol=3, 
          framealpha=0.0, edgecolor='none')

plt.tight_layout()
plt.savefig('crash.pdf', format='pdf', bbox_inches='tight')

# Show the plot
plt.show()
