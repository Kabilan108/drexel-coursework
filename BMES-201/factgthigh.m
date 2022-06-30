function [n,f] = factgthigh(high)
% n=1; f =1;   1!=1
% so long as (while) f<high
   %increase n by 1
	 % calculate the new factorial
   %repeat till f ~< high
	 n=1; f=1;
	 
	 while f<high
		 n = n+1;
		 f = f*n;
	 end
end