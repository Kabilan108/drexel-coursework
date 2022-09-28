function estLog = log10_bywhile(x,inc)
   % takes two numbers as input. X is the number whose logarithm we want to
   % evaluate, and inc in the increment. Returns an estimate value of the
   % logarithm.
	 % By Tony Kabilan Okeke - 20191106
	 
	 % Set the default value of inc as 0.01
	 if ~exist('inc','var')
		 inc = 0.01;
	 end
	 
	 % Let the estimate start at zero and increase each time until
	 % 10^estimate is equal to or greater than x
	 estLog = 0;
	 while (10^estLog) < x
		 estLog = estLog + inc;
	 end
end