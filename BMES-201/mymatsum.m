function total = mymatsum(mat)
   % Takes a matrix as input and returns the sum of all elements in the
   % matrix
	 total = 0;
	 for i = 1:numel(mat)
		 total = total + mat(i);
	 end
end