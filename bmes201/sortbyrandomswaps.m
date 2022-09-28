function [vec] = sortbyrandomswaps(vec)
   % Takes a row vecor as input and returns the sorted vector (in ascending
   % order). Takes two random elements of the vector and swaps them
   % repeatedly, until a sorted vector is produced.
	 % By Tony Kabilan Okeke - 20191106
	 
	 % Determine the length of the vector
		 n = length(vec);
		 
	 while ~all(diff(vec)>0)
		 % Create two random vectors to represnt the random positions in the
		 % input, and assign the values at these positions to vectors
		 pos1 = randi(n);
		 pos2 = randi(n);
		 one = vec(pos1);
		 two = vec(pos2);
		 % Swap the contents to the two positions
		 vec(pos1) = two;
		 vec(pos2) = one;
	 end
end