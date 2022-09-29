function [factor] = largestfactor(num)
   % Takes an integer greater than one as input and returns the largest
   % factor of that number, other than itself
	 % By Tony Kabilan Okeke - 20191106
	 
	 % let x be equal to the input. using a while loop, decrease x by one ech
	 % time, and check if it is a factor of the input. When x is a factor of
	 % the input, break the if statement assign that value to the output
	 factor = num - 1;
	 while factor < num
		 if mod(num,factor)==0
			 break;
		 end
		 factor = factor -1;
	 end
end