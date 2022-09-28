function [approxPi] = eulerpi_withdefault(inVal)
   % Takes positive integer as input, and returns an approximate value of
   % pi with a default value of n=1000
	 % By Tony Kabilan Okeke - 20191023
   
	 % squaresOfInverses contains the squares of the inverses of numbers 1 
	 % through n 
	 if ~exist('inVal','var') 
		 inVal = 1000;
	 end
	 squaresOfInverses = [1:inVal] .^ -2;
	 sumOfSquares = sum(squaresOfInverses);
	 
	 approxPi = sqrt(6*sumOfSquares);
end