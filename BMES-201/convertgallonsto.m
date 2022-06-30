function [output] = convertgallonsto(amt,unit)
   % Converts amt to the specified unit using IF and ELSEIF statements
	 % By Tony Kabilan Okeke - 20191023
	 
	 % Check what unit was input by the user, and produce the appropriate
	 % output. If the input does not correspond to any of the specified
	 % cases, output nan, and ask  them for a valid unit
   if unit == 'q'
		 output = 4 * amt;
	 elseif unit == 'p'
		 output = 8 * amt;
	 elseif unit == 'c'
		 output = 16 * amt;
	 elseif unit == 'o'
		 output = 128 *amt;
	 else
		 output = nan;
		 disp('Please Input a Valid Unit!')
	 end
end