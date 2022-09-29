function day = getdayname(n)
   % Takes an integer between 1 and 7 as input and returns the equivalent
   % day
	 % By Tony Kabilan Okeke - 20191025

   if n == 1
		 day = 'Sun';
	 elseif n==2
		 day = 'Mon';
	 elseif n == 3
		 day = 'Tue';
	 elseif n == 4
		 day = 'Wed';
	 elseif n == 5
		 day = 'Thur'
	 elseif n == 6
		 day = 'Fri'
	 elseif n == 7
		 day = 'Sat'
	 else
		 day = 'Invalid Output';
	 end
end