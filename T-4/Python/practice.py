import matplotlib.pyplot as plt
tree_heights = [61, 63, 64, 66, 68, 69, 71, 71.5, 72, 72.5, 73, 73.5, 74,
74.5, 76, 76.2, 76.5, 77, 77.5, 78, 78.5, 79, 79.2, 80, 81, 82,83, 84, 85, 87]
plt.hist(tree_heights, bins=20, color='green')
plt.title('Height of Trees', fontsize=20)
plt.xlabel('Height (inches)')
plt.ylabel('Frequency')
plt.show()
