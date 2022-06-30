function [output] = avgpositive7multiples(input)
   % Returns the average of the positive multiples of 7 in the input
	 % By Tony Kabilan Okeke - 20191023
	 
	 % Create and index for the problem
	 I = (mod(input,7) == 0) & (sign(input) == 1);
	
	 % Use the mean function to take the average of the numbers that satisfy
	 % the condition
	 output = mean( input(I) );
end