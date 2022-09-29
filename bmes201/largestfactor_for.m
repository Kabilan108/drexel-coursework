function [factor] = largestfactor_for(num)
   % Takes a positive integer greater than one as input and returns its
   % largest factor
	 % By Tony Kabilan Okeke - 20191112
	 for i = 1:num
		 if mod(num,i) == 0 && i < num
			 factor = i;
		 end
	 end
end