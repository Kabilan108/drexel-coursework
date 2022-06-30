function [result] = sumeveryothernegative(vec)
   % Takes a vector as input, and returns the sum of every other negative
   % value in the vector.
	 % By Tony Kabilan Okeke [tko35] - 20191030
	 
	 % Create a vector containing all the negative elements in vec
	 vec = vec( sign(vec) == -1 );
	 
	 % Take the sum of every other element in the vector created. These will
	 % occupy odd positions, so the iterator was used.
	 result = sum( vec( 1:2:end ) );
end