function bmes_fig( name )


%if there are figures with name "name"
h = findobj('Name',name,'Type','Figure');
if isempty ( h ) 
	h = figure;
	h.Name = name; %set(h,'Name',name)
end

set(0,'CurrentFigure', h);
