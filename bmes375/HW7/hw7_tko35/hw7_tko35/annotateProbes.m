function probeAnnot = annotateProbes(gse, gpl, varargin)
  % This function adds annotation information from a GPL object to a GSE
  % object.
	% INPUT: GSE & GPL data objects, strings specifying GPL columns to
	%        annotate probes with
	% OUTPUT: a table with probe annotations
	
	% Input checking
	if isempty(varargin) 
		cols = 'Gene Symbol'; 
	else
		cols = strjoin(varargin(cellfun(@(x) ischar(x), varargin)), '|');
	end
	
	% Create a containers.Map object for GPL
	gpl_map = containers.Map(gpl.Data(:, 1), 1:size(gpl.Data,1));
	
	% Map probes in gse to gpl
	probe_mask = cellfun(@(x) gpl_map(x), gse.Data.rownames);
	
	% Create table with annotated probes
	col_mask = ~cellfun(@isempty,...
		                  regexp(gpl.ColumnNames, ['(^ID|' cols ')']));
	probeAnnot = cell2table(gpl.Data(probe_mask, col_mask),...
		                      'VariableNames', gpl.ColumnNames(col_mask));
end