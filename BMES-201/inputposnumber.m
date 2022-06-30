function [num] = inputposnumber()
   % Asks the user for an input and checks if the input is strictly a
   % positive integer. If not, it will continue to ask for the number.
   num = input('Enter a positive integer: ');
	 while ~( num > 0 && floor(num) == num )
		 num = input('Invalid! Enter a POSITIVE INTEGER: ');
	 end
	 disp('OK!')
end