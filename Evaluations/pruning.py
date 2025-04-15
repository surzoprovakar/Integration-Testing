import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
import matplotlib.pyplot as plt

# Data
bugs = ['Roshi-1', 'Roshi-2', 'Roshi-3', 'ODB-1', 'ODB-2', 'ODB-3', 'ODB-4', 'ODB-5', 'RDB-1', 'RDB-2', 'Yorkie-1', 'Yorkie-2']
grouping = [40,30,35,55,37,23,35,35,25,32,20,46]
replica = [14,20,17,10,22,18,23,10,15,28,38,18]
ind = [26,35,19,20,16,29,22,38,35,20,20,21]
failed = [20,15,29,15,25,30,20,17,25,20,22,15]

# Colors and hatch patterns
edgecolors = ['steelblue', 'indigo', 'darkolivegreen', 'indianred']
hatch_patterns = ['....', '////', '**', '\|\|']

fig, ax = plt.subplots(figsize=(6, 4)) 

# Bar widths and positions
bar_width = 0.3
y_pos = range(len(bugs))

# Adjusting y positions to decrease gap
y_pos = [i * 0.45 for i in y_pos]

# Plot each segment of the bars
grouping_bar = ax.barh(y_pos, grouping, edgecolor=edgecolors[0], fill=False, hatch=hatch_patterns[0], height=bar_width, label='Grouping')
replica_bar = ax.barh(y_pos, replica, left=grouping, edgecolor=edgecolors[1], fill=False, hatch=hatch_patterns[1], height=bar_width, label='Replica')
ind_bar = ax.barh(y_pos, ind, left=[grouping[i] + replica[i] for i in range(len(grouping))], edgecolor=edgecolors[2], fill=False, hatch=hatch_patterns[2], height=bar_width, label='Ind')
failed_bar = ax.barh(y_pos, failed, left=[grouping[i] + replica[i] + ind[i] for i in range(len(grouping))], edgecolor=edgecolors[3], fill=False, hatch=hatch_patterns[3], height=bar_width, label='Failed')

# Y-axis labels
ax.set_yticks(y_pos)
ax.set_yticklabels(bugs[::-1], fontsize=10)  # Reverse the order of categories and set fontsize

# X-axis as percentage
ax.set_xlim(0, 100)
ax.set_xticks([0, 25, 50, 75, 100])
ax.set_xticklabels(['0%', '25%', '50%', '75%', '100%'], fontsize=10)  # Set fontsize


# fig.set_size_inches(6, 5)

# Add legends
legend1 = ax.legend([grouping_bar, replica_bar], 
                    ['Event-Grouping', 'Replica-Specific'], 
                    loc='upper center', bbox_to_anchor=(0.5, 1.11), ncol=2, 
                    fancybox=True, handlelength=4, edgecolor='dimgray')

legend2 = ax.legend([ind_bar, failed_bar], 
                    ['Event-Independence', 'Failed-Ops'], 
                    loc='lower center', bbox_to_anchor=(0.5, -0.17), ncol=2,
                    fancybox=True, handlelength=4, edgecolor='dimgray')

# Add the legends manually to the axes
ax.add_artist(legend1)
ax.add_artist(legend2)

# Show grid
# ax.grid(True, axis='x', linestyle='--')

# Save the plot as a PDF file
plt.tight_layout()
plt.savefig('pruning-ratio.pdf', format='pdf', bbox_inches='tight')

# Display the plot
plt.show()
