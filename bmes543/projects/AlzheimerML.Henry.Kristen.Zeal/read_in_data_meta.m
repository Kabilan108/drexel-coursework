function [data, meta, data_numerical, rownames,colnames] = read_in_data_meta(datadir, geo)
%%
%function gets expr and meta data processed from R
%inputs datadir: base path that has files in it
%       geo: geo acc number in string

%%
data_file = [datadir '/' geo '_z_intersectGenes.csv' ]; %path of expr data

matfile=[data_file '.mat'];
if isfile(matfile)
	load(matfile);
else
	opts = detectImportOptions(data_file);
	opts.DataLines = 3;
	opts.VariableNamesLine = 2;
	data = readtable(data_file, opts);   %read in as table
	%extract numerical data, rownames, column names.
	data_numerical = table2array(data(:,2:end));
	rownames = data.Properties.RowNames;
	colnames = data.Properties.VariableNames;
	save(matfile,'data','data_numerical','rownames','colnames');
end

meta = readtable([datadir '/' geo '_subject_data.csv']); %read meta data