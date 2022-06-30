function bacteriaKilled = killbacteria_2d_noedgecase(M,R,C)
   % Returns the total number of bacteria killed in the matrix, assuming
   % that no antibiotic was dropped on the edge dishes
	 % By Tony Kabilan Okeke - 20191110
	 
	 % All the bacteria were killed in the cell in row R, column C
	 allDead = M(R,C);
	 
	 % Store the cells to the left of the drop in lCol
	 lCol = M(R-1:R+1,C-1);
	 
	 % Store the cells above and below the drop in mCol
	 % Set the second term to zero, because bacteria in this cell are all
	 % killed, not partially.
	 mCol = M(R-1:R+1,C);
	 mCol(2) = 0;
	 
	 % Store the cells to the right of the drop in rCol
	 rCol = M(R-1:R+1,C+1);
	 
	 halfKilled = sum(lCol+mCol+rCol)/2;
	 bacteriaKilled = allDead + halfKilled;
end