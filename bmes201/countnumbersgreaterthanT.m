function [out] = countnumbersgreaterthanT( v , T )
   % Takes a vector v and a number T as input and returns the number of
   % elements in v that are greater than T
	 % By Tony Kabilan Okeke
	 if ~(exist('T','var')); T = 10; end
	 out = numel( v(v > T) );
end