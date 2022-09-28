function mySum = mymatsumifpos(mat)
   % Takes a matrix as input and returns the sum of all positive emelemts
   % in the matrix
	 % By Tony Kabilan Okeke - 20191115
	 % [R,C] = size(mat); - part of less efficient method
	 mySum = 0;
	 for i = 1:numel(mat)
		 if mat(i) > 0
			 mySum = mySum + mat(i);
		 end
	 end
	 
	 %{
	 less efficient method
	 for r = 1:R
		 for c = 1:C
			 if mat(r,c) > 0
				 mySum = mySum + mat(r,c);
			 end
		 end
	 end
	 %}
end