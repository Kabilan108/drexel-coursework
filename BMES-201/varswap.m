function [a,b] = varswap(a,b)
   % Takes two variables as input and swaps theit content
	 % By Tony Kabilan Okeke - 20191113
	 temp = b;
	 a = b;
	 b = temp;
end