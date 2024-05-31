function rna_plot(locs,pairs)
% by AhmetSacan

% if a row-vector is given, convert to a 3-column format.
if size(locs,1)==1;	locs=reshape(locs,3,[])'; end

plot3(locs(:,1),locs(:,2),locs(:,3),'r*-','LineWidth',3,'MarkerSize',5);

if exist('pairs','var')&&~isempty(pairs)
	hold on;
	args={};
	for i=1:size(pairs,1)
		args=[args {locs(pairs(i,:),1)', locs(pairs(i,:),2)', locs(pairs(i,:),3)', 'b-'}];
	end
	plot3(args{:},'LineWidth',2);
	hold off;
end
title(sprintf('Plotted on [%s]',bmes.computername))