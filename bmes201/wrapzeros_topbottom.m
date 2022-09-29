function M = wrapzeros_topbottom(M)
   % Wraps the input matrix with zeros on the top and bottom
	 % By Tony Kabilan Okeke - 20191110
	 
	 % Obtain the size of the matrix
	 [R,C] = size(M);
	 
	 % Creates row vector of zeros equal in length to the number of columns C
	 wrap = zeros(1,C);
	 
	 % Wrap M by creating a new matrix with zeros above and below M
	 M = [wrap;M;wrap];
end