function [fortynines, sevens, ones] = converttobase7(number)
   % Returns the input in base 7, as powers of 7
	 % By Tony Kabilan Okeke - 20190410
	 
	 % Obtain the number of fortynines by dividing by 49 using the fix
	 % function and obtain the remainder with the mod function
	   fortynines = fix(number/49);
		 remainder = mod(number,49);
		 
	 % Obtain the number of sevens by dividing remainder by 7 and, using fix,
	 % the number of ones
	   sevens = fix(remainder/7);
		 ones = mod(remainder,7);
end	 