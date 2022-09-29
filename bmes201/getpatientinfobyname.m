function query = getpatientinfobyname(excelOrCell, name, field)
   % Takes an excel file name or a cell array data; the name of a patient; 
	 % and the name of an information field as input and returns the
	 % requested information
	 % By Tony Kabilan Okeke (tko35) - 20191209
	 
	 % Check if first input is a cell array or an excel file, and read data
	 % accordingly
	   if iscell(excelOrCell)
		   fields = excelOrCell(1,:);
		   data   = excelOrCell(2:end,:);
		 else
		   [~,~,raw] = xlsread(excelOrCell);
		   fields = raw(1,:);
		   data = raw(2:end,:);
	   end
	 
	 % Obtain the requested information
	 % Select the rows where the name field is the same as name
	   rowCond = strcmpi( data( : , strcmpi(fields,'name')) , name );
	 % Select all the rows in the specified field
	   colCond = strcmpi(fields,field);
	 % If the name cannot be found, output NaN
	   if ~any(rowCond) 
		   query = nan;
		 else
		   query = data{ rowCond , colCond };
	   end
end