% This script is an implementation of the K-Means clustering algorithm
df = readmatrix('test_data.csv');
df = df(:, 1:2);

% Define the desired number of clusters
K = input('How many clusters are required? ');

% Randomly select the initial centroids
% I = randperm(size(df, 1), K); % random permutation

% Randomly assing the data to the clusters
clust = randi(K, size(df,1),1);

while true
	% compute the centroid of each cluster
	centroid = zeros(K, size(df, 2));
	for c = 1:K
		centroid(c, :) = mean(df(clust == c, :), 1);
	end
	
	% compute the euclidean distance to each centroid
	dist = zeros(size(clust, 1), K);
	for c = 1:K
		dist(:, c) = sqrt(sum((df - centroid(c, :)).^2, 2));
	end
	
	% reassign points to the closest cluster
	for i = 1:length(dist)
		if dist(i,
	end
end