function [days,hours,minutes,seconds] = convertsec(sTotal)
   % Takes one input 's = total number of seconds,' and returns...
	 % the number of days, hours, minutes, and seconds.
	 % By Tony Kabilan Okeke - 20190928
	 
	 % Divide sTotal by 60 using the mod function to obtain the number
	 % of seconds.
	   seconds = mod(sTotal,60);
		 
	 % Divide sTotal by 60 and round down using the floor function to obtain
	 % the total number of minutes, mTotal. Then, divide mTotal by 60 using
	 % the mod function to obtain the number of minutes.
	   mTotal = floor(sTotal/60);
		 minutes = mod(mTotal,60);
		 
	 % Divide mTotal by 60 and round down using the floor function to obtain
	 % the total number of minutes, hTotal. Then, divide hTotal by24 using 
	 % the mod function to obtain the number of hours.
	   hTotal = floor(mTotal/60);
		 hours = mod(hTotal,24);
		 
	 % Divide hTotal by 24 and round down using the floor function to obtain
	 % the number of days.
	   days = floor(hTotal/24);
end