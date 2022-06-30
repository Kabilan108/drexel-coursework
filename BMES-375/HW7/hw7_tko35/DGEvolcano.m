function DGEvolcano(log2fc, pval, varargin)
  % This function generates a volcano plot given the fold change and
  % pvalues of a specific comparisob
	% INPUT: log2fc -> log2(fold change)
	%        pval -> pvalues
	
	% Merge Plot Options
	opt = mergeoptions(struct('p_thr', 0.1, 'fc_thr', 2,...
		                        'main', 'Group 1 vs Group 2',...
														'figsize', [600 400]), varargin{:});
  
  % Create figure
	figure('Name', 'DGE Volcano Plot', 'Position', [0 0 opt.figsize]);
	scatter(log2fc, -log10(pval), 25, 'filled',...
		      'MarkerFaceColor', 	'#A2142F', 'MarkerFaceAlpha', 0.2);
	xlabel('log_2(Fold Change)', 'FontSize', 13);
	ylabel('-log_{10}(p-value)', 'FontSize', 13);
	title(opt.main, 'FontSize', 14);
	hold on;
	% Plot indicators for x2 or x1/2 greater/lower
	plot(log2([0.5 0.5]), ylim, log2([2 2]), ylim,... 
		   'Color', '#77AC30', 'LineWidth', 1); 
	% Plot significance threshold
	plot(xlim, -log10([.01 .01]), 'Color', '#77AC30', 'LineWidth', 1);
	hold off;
end