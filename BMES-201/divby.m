function [output] = divby(v,n)
   if ~exist('n','var')
		 n = 2;
	 end
	 Cond = (mod(v,n) == 0);
	 output = sum( v(Cond) ); 
end