function M = wrapzeros_leftright(M)
   % Wraps the input matrix with zeros on the left and right
	 % By Tony Kabilan Okeke - 20191110
	 
	 % Obtain the size of the matrix
	 [R,C] = size(M);
	 
	 %Create a column vector of zeros equal in length to the number of rows R
	 wrap = zeros(R,1);
	 
	 % Wrap M by creating a new matrix with zeros on the left and right od M
	 M = [wrap,M,wrap];
end