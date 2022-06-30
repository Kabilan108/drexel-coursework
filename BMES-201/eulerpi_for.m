function estPi = eulerpi_for(n)
   % Takes a number n as input and returns an approximate value of pi
	 % By Tony Kabilan Okeke - 20191112
	 
	 % Set default value of n
	 if ~exist('n','var'); n = 1000; end
	 estPi = 0;
	 for i = 1:n
		 estPi = estPi + 1/(i^2);
	 end
	 % finish evaluating pi
	 estPi = sqrt( 6*estPi );
end