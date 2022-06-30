function table = multtable(R,C)
   % Produces a matrix in which each element is the product of its indicies
	 % By Tony Kabilan Okeke - 201181115
	 table = zeros(R,C);
	 for r = 1:R
		 for c = 1:C
			 table(r,c) = r*c;
		 end
	 end
end