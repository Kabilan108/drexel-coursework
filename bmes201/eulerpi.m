function [approxPi] = eulerpi(n)
   % Takes positive integer as input, and returns an approximate value of
   % pi
	 % By Tony Kabilan Okeke - 20191016
   
	 % squaresOfInverses contains the squares of the inverses of numbers 1 
	 % through n 
	 squaresOfInverses = [1:n] .^ -2;
	 sumOfSquares = sum(squaresOfInverses);
	 
	 approxPi = sqrt(6*sumOfSquares);
end