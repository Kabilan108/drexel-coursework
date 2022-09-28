function bmes_progress(title,percentcomplete)


try
	% If zozanidb is installed, use the gui_progress available there.
	 % gui_progress shows time estimates, whereas Matlab's waitbar doesn't.
	gui_progress(title,percentcomplete);
catch me
	if numel(percentcomplete)==2; percentcomplete=percentcomplete(1)/percentcomplete(2); end
	h = findall(0,'Name',title,'Type','Figure','Tag','TMWWaitbar');
	if percentcomplete==1
		if ~isempty(h); delete(h); end
	else
		if isempty(h)
			h=waitbar(percentcomplete,title);
			h.Name=title;
		else
			waitbar(percentcomplete,h,title);
		end
	end
end