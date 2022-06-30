function [smallest,largest,average,stddev]=xls_columnstats(file,field)
   % Takes a file or file path and field name or number and returns the
   % smallest, largest, average, and standard deviation of the numbers in
   % the column
	 % By Tony Kabilan Okeke - 20191126
	 
	 [~,~,raw] = xlsread(file);
	 
	 % Extract the data in the specified field
	 if isnumeric(field)
		 % If column number is specified
		 data =  raw( : , field );
	 else
		 % If column name is specified
		 data = raw( : , strcmpi( [ raw(1,:) ] , field ) );
	 end
	 
	 % Create a logical index of all the entries that are empty, texts, or
	 % NaN
	 I = zeros(numel(data),1); % Preallocating
	 for i = 1:numel(data)
		 if any( ischar(data{i}) || isempty(data{i}) || isnan(data{i}) )
			 I(i) = 1;
		 else
			 I(i) = 0;
		 end
	 end
	 data( logical(I) ) = []; % Select the data where the condition is satisfied
	 smallest = min([ data{:} ]);
	 largest = max([ data{:} ]);
	 average = mean([ data{:} ]);
	 stddev = std([ data{:} ]);
end