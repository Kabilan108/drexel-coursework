function out = filterpatients_cell(data)
   % Takes patient data (in form of a cell array) as input and returns the
   % names of feamle patients whose ages fall in the closed interval
   % [30,40]
	 % By Tony Kabilan Okeke - 20191120
	 fields = data(1,:); % Cell array of the headings
	 data = data(2:end,:); % Cell Array of only data values
	 outID = 0; % This variable counts the number of elements that we are 
	            % going to have in our final output cell array
	 for i = 1:size(data,1)
		 % Create the two conditions necessary (between 30 & 40, and female)
		    % Condition 1 checks if the current patient is female
				cond1 = ( data{i,strcmp(fields,'gender')} == 'f' );
				
				% Condition 2 checks if the current patient is between 30 and 40
				% years old
				cond2 = ( data{i,strcmp(fields,'age')} >= 30 ) && ( data{i,strcmp(fields,'age')} <= 40 );
		 if  cond1 && cond2
			 outID = outID + 1;
			 out{outID} = data{i,strcmp(fields,'name')};
		 end
	 end
end