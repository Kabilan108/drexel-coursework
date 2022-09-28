function bacteriaKilled = killbacteria_2d(M,y,x)
   % Returns the total number of bacteria killed in the matrix,
   % irrespective of where the antibiotic was dropped
	 % By Tony Kabilan Okeke - 20191110
	 
	 % First wrap the input by zeros
	 [R,C] = size(M);
	 wrap = zeros(R,1);
	 M = [wrap,M,wrap];
	 [R,C] = size(M);
	 wrap = zeros(1,C);
	 M = [wrap;M;wrap];
	 
	 y=y+1;
	 x=x+1;
	 % All the bacteria were killed in the cell in row R, column C
	 allDead = M(y,x);
	 
	 % Store the cells to the left of the drop in lCol
	 lCol = M(y-1:y+1,x-1);
	 
	 % Store the cells above and below the drop in mCol
	 % Set the second term to zero, because bacteria in this cell are all
	 % killed, not partially.
	 mCol = M(y-1:y+1,x);
	 mCol(2) = 0;
	 
	 % Store the cells to the right of the drop in rCol
	 rCol = M(y-1:y+1,x+1);
	 
	 halfKilled = sum(lCol+mCol+rCol)/2;
	 bacteriaKilled = allDead + halfKilled;
end