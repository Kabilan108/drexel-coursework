function max = mymax(vec)
   % Takes a vector as input and returns the maximum value in the
   % vector
	 % By Tony Kabilan Okeke -  20191112
	 max = vec(1);
	 for i = 1:numel(vec)
		 if max < vec(i)
			 max = vec(i);
		 end
	 end
end