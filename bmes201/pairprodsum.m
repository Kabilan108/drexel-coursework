function [prodSum] = pairprodsum(vec)
   % Takes a vector as input and returns the sum of the products of
   % consecutive terms
	 % By Tony Kabilan Okeke - 20191112
	 prodSum = 0; 
	 for i = 2:numel(vec) % iterates from the second to last element
		 % add the product of the prior element and the courrent element to the
		 % running product
		 prodSum = prodSum + vec(i-1)*vec(i);
	 end
end