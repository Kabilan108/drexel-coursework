"""
K-Means Algorithm Impementation

The K-Means algorithm is an interative algorithm that partitions a dataset into K
distinct, non-overlapping clusters where each data point belongs to only one group.
It tries to make the intra-cluster datapoints as similar as possible while maximizing
the distance between the clusters.
Data points are assigned to a cluster such that the sum of the squared distance
between the data points and the cluster's centroid (arithmetic mean of all data points
in the cluster) is at the minimum.
The less variation within the clusters, the more homogeneous the data points are within
the same cluster.

Algorithm:
  - Specify the number of clusters, K
  - Initialize centroids
    - shuffle the dataset
    - randomly selecting K data points for the centroid w/o replacement
  - Keep iterating until there is no change to the centroids
    - Assign each data point to the closest cluster (centroid).
    - Compute the centroids for the clusters by taking the average pf all data points
      that belong to each cluster.
  - Compute the sum of the squared distance between data points and all centroids.
"""

# Import modules
import numpy as np
from numpy import random
from numpy.linalg import norm

# Define class
class KMeans:
  """Implementing the K-Means Algorithm"""

  def __init__(self, K, maxiter=1000, random_state=123):
    # Initialize class
    self.K = K
    self.maxiter = maxiter
    self.random_state = random_state

  def initialize_centroids(self, X):
    # Initialize the first K (random) centroids
    np.random.RandomState(self.random_state)
    random_idx = np.random.permutation(X.shape[0])
    centroids = X[random_idx[:self.K]]
    return centroids

  def compute_centroids(self, X, labels):
    # Method for computing centroids
    centroids = np.zeros( (self.K, X.shape[1]) )
    for k in range(self.K):
      # compute the centroids for each cluster
      centroids[k, :] = np.mean(X[labels == k, :], axis=0)
    return centroids

  def compute_distance(self, X, centroids):
    # Method for computing eucidean distance (norm) from each centroid
    distance = np.zeros( (X.shape[0], self.K) )
    for k in range(self.K):
      row_norm = norm(X - centroids[k, :], axis=1)
      distance[:, k] = np.square(row_norm)
    return distance

  def find_closest_cluster(self, distance):
    # Identify the closest cluster to the data
    return np.argmin(distance, axis=1)

  def fit(self, X):
    # Method for fitting given data to K-Means algorithm
    self.centroids = self.initialize_centroids(X)
    for i in range(self.maxiter):
      old_centroids = self.centroids
      # Compute distances
      distance = self.compute_distance(X, old_centroids)
      # Label data to closest cluster
      self.labels = self.find_closest_cluster(distance)
      # Compute cluster centroids
      self.centroids = self.compute_centroids(X, self.labels)
      # If cluster centers do not change, exit loop
      if np.all(old_centroids == self.centroids):
        break

  def predict(self, X):
    # Method for predicting which cluster some data would be assigned to
    distance = self.compute_distance(X, self.centroids)
    return self.find_closest_cluster(distance)