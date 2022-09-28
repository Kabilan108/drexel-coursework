% filter shared genes within 2 GSE sets.

% read 2 GSE sets with gene names.
GSE13425 = open('GSE13425.mat').gsedata;

GSE13351 = open('GSE13351.mat').gsedata;
%% 

% {overlappedgenes = 'empty';
% for i=1:numel(GSE13351.rownames)
	% for j=1:numel(GSE13425.rownames)
% 		if strcmpi(GSE13425.RowNames(j),GSE13351.RowNames(i))==1
		% 	overlappedgenes = [overlappedgenes; GSE13351.RowNames(i)];
	% 	end
% 	end
% end}
%% test intersect function.
GSE1genenames=GSE13425.rownames;
GSE2genenames=GSE13351.rownames;
testoverlap = intersect(GSE1genenames,GSE2genenames);
%%
mapgene = containers.Map(testoverlap, 1:numel(testoverlap));
filterGSE1=zeros(numel(GSE13425.RowNames),1);
filterGSE2=zeros(numel(GSE13351.RowNames),1);

for i=1:numel(GSE13425.RowNames)
if mapgene.isKey(GSE13425.RowNames{i})
   filterGSE1(i)=mapgene(GSE13425.RowNames{i}); 
end
end

%% 

	for i=1:numel(GSE13351.RowNames)
	 
		if mapgene.isKey(GSE13351.RowNames{i})
   filterGSE2(i)=mapgene(GSE13351.RowNames{i}); 
		end
	end

%% 
% GSEGenes1(find(filterGSE1)) = GSE1genenames(filterGSE1(find(filterGSE1)));
% GSEGenes2(find(filterGSE2)) = GSE2genenames(filterGSE2(find(filterGSE2)));
% gsedata1 = GSE13425.rownames(':',GSEGenes1);
% gsedata2 = GSE13351.rownames(':',GSEGenes2);
%% 
filterrow1=[0];
for i=1:numel(GSE1genenames)
 for t=1:numel(testoverlap)
	 if strcmpi(testoverlap{t},GSE1genenames{i})==1
		 filterrow1=[filterrow1;i];
	 end
 end
end

