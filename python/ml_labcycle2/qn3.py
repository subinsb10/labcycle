import numpy as np
from sklearn.cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt

labels3 = ['A', 'B', 'C', 'D', 'E', 'F']
points3 = np.array([[1, 2], [2, 1], [1, 0], [10, 10], [11, 11], [10, 11]])
kmeans = KMeans(n_clusters=2, random_state=0).fit(points3)
kmeans_labels = kmeans.labels_
kmeans_centroids = kmeans.cluster_centers_
print("\nK-Means Cluster Labels:", dict(zip(labels3, kmeans_labels)))
print("K-Means Centroids:\n", kmeans_centroids)

plt.figure(figsize=(6, 5))
sns.scatterplot(x=points3[:, 0], y=points3[:, 1], hue=kmeans_labels, palette='Set1')
plt.scatter(kmeans_centroids[:, 0], kmeans_centroids[:, 1], s=200, c='black', marker='X', label='Centroids')
plt.legend()
plt.title("K-Means Clustering (k=2)")
plt.show()