
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
import matplotlib.pyplot as plt

labels2 = ['P1', 'P2', 'P3', 'P4', 'P5']
points2 = np.array([[1, 1], [2, 1], [4, 3], [5, 4], [1, 0]])

link_single = linkage(points2, method='single')
link_complete = linkage(points2, method='complete')
link_average = linkage(points2, method='average')

clusters_single = fcluster(link_single, 2, criterion='maxclust')
print("\nSingle Linkage Clusters (k=2):", dict(zip(labels2, clusters_single)))

plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
dendrogram(link_single, labels=labels2)
plt.title("Single Linkage")
plt.subplot(1, 3, 2)
dendrogram(link_complete, labels=labels2)
plt.title("Complete Linkage")
plt.subplot(1, 3, 3)
dendrogram(link_average, labels=labels2)
plt.title("Average Linkage")
plt.tight_layout()
plt.show()