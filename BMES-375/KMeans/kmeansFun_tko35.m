function [clustered_X] = kmeansFun_tko35(X, K, maxiter)
  % K-Means Algorithm Impementation
  % The K-Means algorithm is an interative algorithm that partitions a dataset into K
	% distinct, non-overlapping clusters where each data point belongs to only one group.
	% It tries to make the intra-cluster datapoints as similar as possible while maximizing
	% the distance between the clusters.
	% Data points are assigned to a cluster such that the sum of the squared distance
	% between the data points and the cluster's centroid (arithmetic mean of all data points
	% in the cluster) is at the minimum.
	% The less variation within the clusters, the more homogeneous the data points are within
	% the same cluster.
	%
	% Algorithm:
	%   - Specify the number of clusters, K
	%   - Initialize centroids
	%     - shuffle the dataset
	%     - randomly selecting K data points for the centroid w/o replacement
	%   - Keep iterating until there is no change to the centroids
	%     - Assign each data point to the closest cluster (centroid).
	%     - Compute the centroids for the clusters by taking the average pf all data points
	%       that belong to each cluster.
	%   - Compute the sum of the squared distance between data points and all centroids.

	% Define default values
	if ~exist('K', 'var'); K = 2; end
	if ~exist('maxiter', 'var'); maxiter = 1000; end
	
  % Initialzie centroids
	  function centroids = initialize_centroids(X)
			random_idx = randperm(size(X, 1));
			centroids = X(random_idx(1:K), :);
		end
	% Compute centroids
	function centroids = compute_centroids(X, labels)
		centroids = zeros(K, size(X, 2));
		for k = 1:K
			centroids(k, :) = mean(X(labels == k, :), 1);
		end
	end
  % Compute distances
	function distance = compute_distance(X, centroids)
		distance = zeros(size(X,1), K);
		for k = 1:K
			row_norm = vecnorm(X - centroids(k, :), 2, 2);
			distance(:, k) = row_norm .^ 2;
		end
	end
  % Find the closest cluster
	function labels = find_closest_cluster(distance)
		[~,labels] = min(distance, [], 2);
	end

  % Cluster the data
	centroids = initialize_centroids(X);
	for i = 1:maxiter
		old_centroids = centroids;
		distance = compute_distance(X, old_centroids);
		labels = find_closest_cluster(distance);
		centroids = compute_centroids(X, labels);
		% Exit loop if cluster centers dont change
		if all(old_centroids == centroids)
			break;
		end
	end
	% Combine data to return
	clustered_X = [X labels];
end