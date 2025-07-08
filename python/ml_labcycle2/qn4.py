# from sklearn.datasets import load_iris
# from sklearn.cluster import KMeans
# from scipy.cluster.hierarchy import linkage, dendrogram
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
#
# # Load the Iris dataset
# iris = load_iris()
# X = iris.data
# iris_df = pd.DataFrame(X, columns=iris.feature_names)
#
# # K-Means Clustering
# kmeans = KMeans(n_clusters=3, random_state=42)
# kmeans_labels = kmeans.fit_predict(X)
#
# plt.figure(figsize=(6, 5))
# sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=kmeans_labels, palette='Set1')
# plt.title("K-Means Clustering on Iris Dataset")
# plt.xlabel("Sepal Length")
# plt.ylabel("Sepal Width")
# plt.show()
#
# # Hierarchical Clustering
# link = linkage(X, method='ward')
# plt.figure(figsize=(10, 6))
# dendrogram(link, labels=iris.target)
# plt.title("Hierarchical Clustering Dendrogram (Iris Dataset)")
# plt.xlabel("Sample Index")
# plt.ylabel("Distance")
# plt.show()




from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import linkage, dendrogram
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load the Iris dataset
iris = load_iris()
X = iris.data
iris_df = pd.DataFrame(X, columns=iris.feature_names)

# K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans_labels = kmeans.fit_predict(X)
centroids = kmeans.cluster_centers_

plt.figure(figsize=(6, 5))
sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=kmeans_labels, palette='Set1')
for i, c in enumerate(centroids):
    circle = plt.Circle((c[0], c[1]), 0.5, color='black', fill=False, linestyle='--')
    plt.gca().add_patch(circle)
plt.scatter(centroids[:, 0], centroids[:, 1], c='black', s=100, marker='X', label='Centroids')
plt.title("K-Means Clustering on Iris Dataset")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.legend()
plt.show()

# Hierarchical Clustering
link = linkage(X, method='ward')
plt.figure(figsize=(10, 6))
dendrogram(link, labels=iris.target)
plt.title("Hierarchical Clustering Dendrogram (Iris Dataset)")
plt.xlabel("Sample Index")
plt.ylabel("Distance")
plt.show()