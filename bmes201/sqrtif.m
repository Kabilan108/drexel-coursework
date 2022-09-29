function srt = sqrtif(x)
   % Takes a positive integer as input, and returns its square root. If the
   % number is negative, it tells the user that taking square roots of
   % negative numbers is not allowed, and returns NaN
	 % By Tony Kabilan Okeke
	 
	 if sign(x) == -1
		 disp('Taking the Square Root of Negative Numbers is Not Allowed')
		 srt = nan;
	 else
		 srt = sqrt(x);
	 end
end