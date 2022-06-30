function lines = countlies(file)
   data = fileread(file);
	 lines = strsplit(data,sprintf('\n'),'CollapseDelimiters',false);
	 lines = numel(lines);
end