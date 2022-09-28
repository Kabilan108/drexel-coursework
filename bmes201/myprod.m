function prod = myprod(vec)
   % Takes a vector as input and returns product of all the elements in the
   % vector
	 % By Tony Kabilan Okeke - 20191112
	 prod = 1;
	 for i = 1:numel(vec)
		 prod = prod * vec(i);
	 end
end