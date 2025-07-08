import numpy as np
import pandas as pd
from scipy.spatial.distance import euclidean, cityblock, cosine

labels1 = ['A', 'B', 'C', 'D']
points1 = np.array([[1, 2], [2, 3], [4, 8], [7, 8]])

def create_distance_matrix(points, dist_func):
    n = len(points)
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            matrix[i][j] = dist_func(points[i], points[j])
    return pd.DataFrame(matrix, index=labels1, columns=labels1)

euclidean_df = create_distance_matrix(points1, euclidean)
manhattan_df = create_distance_matrix(points1, cityblock)
cos_sim_ab = 1 - cosine(points1[0], points1[1])
print("Euclidean Distance Matrix:\n", euclidean_df.round(2))
print("\nManhattan Distance Matrix:\n", manhattan_df.astype(int))
print("\nCosine Similarity between A and B:", round(cos_sim_ab, 3))