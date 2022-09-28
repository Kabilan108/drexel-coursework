function [avg] = averageageofmales(data)
   % Takes a 2-column matrix as input, where the first column indicates
   % gender, and the second indicates age, and returns the average age of
   % male patients
	 % By Tony Kabilan Okeke (tko35) - 20191101
	 
	 % Create a vector I to index all the male patients, i.e. where column one
	 % entries are 1
	 I = data(:,1) == 1;
	 
	 % Evaluate the average ages (column 2 entries) using the mean function,
	 % if there are no male patients, the the output will be nan
	 if ( data(:,1) == 1 ) == 0
		 avg = nan;
	 else
		 avg = mean( data( I , 2 ) );
	 end
end