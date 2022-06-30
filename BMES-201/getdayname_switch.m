function day = getdayname_switch(n)
   % Takes an integer between 1 and 7 as input and returns the equivalent
   % day
	 % By Tony Kabilan Okeke - 20191025
	 
	 switch n
		 case 1
			 day = 'Sun';
		 case 2
			 day = 'Mon';
		 case 3
			 day = 'Tue';
		 case 4
			 day = 'Wed';
		 case 5
			 day = 'Thur';
		 case 6
			 day = 'Fri';
		 case 7
			 day = 'Sat';
		 otherwise 
			 day = 'Invalid Input';
	 end
end