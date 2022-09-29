%% Project gse reader
clear;clc;close all
%% Download data
% Download GSE data
GSE = bmes_downloadandparsegse('GSE13351');
% Store GSE data to variable gsedata
gsedata = GSE.Data;
% Obtain GPL platform id
GPLid = GSE.Header.Series.platform_id;
% Download GPL data
GPL = bmes_downloadandparsegpl(GPLid);

%% Convert probes into corresponded gene symbol
% Store ID into variable GPLProbes
GPLProbes = GPL.Data(:,strcmp(GPL.ColumnNames,'ID'));
% Obtain gene symbol from gpl data and store them into variable GPLGenes
GPLGenes = GPL.Data(:,strcmp(GPL.ColumnNames,'Gene Symbol'));
% Obtain row names in gse data
GSEProbes = gsedata.rownames;
MAP_GSE_GPL = zeros(numel(GSEProbes),1);

% The following step is to match gse probes with gpl probes, then to obtain
% corresponded gene symbol
map = containers.Map(GPLProbes,1:numel(GPLProbes));
% Create "address book"
for i=1:numel(GSEProbes)
if map.isKey(GSEProbes{i})
   MAP_GSE_GPL(i)=map(GSEProbes{i}); 
end
end

GSEGenes(find(MAP_GSE_GPL)) = GPLGenes(MAP_GSE_GPL(find(MAP_GSE_GPL)));

gsedata = gsedata.rownames(':',GSEGenes);

%% Convert col names
groupnames = {'T ALL' 'B ALL'};
colname = gsedata.ColNames;
colname(1:36)=groupnames(1);
colname(37:end)=groupnames(2); 
gsedata = set(gsedata,'ColNames',colname);

Data_TALL = strcmp(colname,'T ALL');
Data_BALL = strcmp(colname,'B ALL');

%% Mat test
[gsepvals]=mattest(gsedata(:,Data_TALL),...
    gsedata(:,Data_BALL), 'permute',10);

% Sort to get top 10 minimum
pvalssort = gsepvals.sortrows('p-values');

% Display check
        disp(pvalssort(1:10,:))