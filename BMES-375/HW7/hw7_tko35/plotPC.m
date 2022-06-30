function plotPC(pc, var, varargin)
  % This function generates a 2 or 3 dimensional PCA plot
	% INPUT: pc - matrix of principal components
	%        var - variances for each principal components
	%        groups - groups to color figure with
	% Merge Plot Options
	opt = mergeoptions(struct('parent', [], 'groups', [], 'dim', 2,...
		                        'main', 'PCA for Significantly Diffferentially Expressed Genes',...
														'figsize', [600 400]), varargin{:});
  % Convert variances to percentages if necessary
	if sum(var) ~= 100; var = var / sum(var) * 100; end
	
  % Plot PCs
	if isempty(opt.parent)
		figure('Name', 'Principal Component Analysis',...
			     'Position', [0 0 opt.figsize]);
	end
		
	if opt.dim == 2
		if isempty(opt.groups)
			scatter(pc(:,1), pc(:,2), 50, 'filled', 'MarkerFaceAlpha', 0.15);
		else
			gscatter(pc(:,1), pc(:,2), opt.groups);
		end
		title(opt.main, 'FontSize', 14)
		xlabel(sprintf('PC1 (%.2f%% of variance)', var(1)), 'FontSize', 13);
		ylabel(sprintf('PC2 (%.2f%% of variance)', var(2)), 'FontSize', 13);
	elseif opt.dim == 3
		if isempty(opt.groups)
			scatter3(pc(:, 1), pc(:, 2), pc(:, 3), 40, 'filled',...
	       'MarkerFaceAlpha', 0.7);
		else
			scatter3(pc(:, 1), pc(:, 2), pc(:, 3), 40, opt.groups, 'filled',...
	       'MarkerFaceAlpha', 0.7);
		end
		xlabel(sprintf('PC1 (%.2f%% of variance)', var(1)), 'FontSize', 13);
		ylabel(sprintf('PC2 (%.2f%% of variance)', var(2)), 'FontSize', 13);
		zlabel(sprintf('PC3 (%.2f%% of variance)', var(3)), 'FontSize', 13);
	else
		error('Please provide a valid number of dimensions.')
	end
end