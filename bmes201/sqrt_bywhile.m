function [estRt] = sqrt_bywhile(x,inc)
   % Takes two numbers as input. X is the number whose root is being
   % evaluated, and inc is the increment
	 % By Tony Kabilan Okeke - 20191106
	 
	 % Set the default value of inc as 0.01
	 if ~exist('inc','var')
		 inc = 0.01;
	 end
	 
	 % let the estimate start from 0 and increase each time until estimate^2
	 % is less than or equal to x
	 estRt = 0;
	 while estRt^2 < x
		 estRt = estRt + inc;
	 end
	 % If the estimate is not exactly equal to the square root of x, then it
	 % should be smaller
	 if estRt^2 ~= x
		 estRt = estRt - inc;
	 end
end