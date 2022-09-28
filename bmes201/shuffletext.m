function [s] = shuffletext(pair,s)
   % Swaps characters of s as specified by the indices present in the pairs
   % variable
	 % By Tony Kabilan Okeke - 20191111
	 
	 % Set default value of s
	 if ~exist('s','var')
		 s = 'O0O0O0OO000OO0OO0O00OOOOO0OO00O0O0OOO0OO00OO0OO0OOOOO00O0O00000O';
	 end
	 
	 % determine the size of the matrix
	 [r] = size(pair,1);
	 
	 for i=1:r % loops through all the rows
		 % Get the index pairs from pairs variable and use them to index the
		 % string
		 tempVar = s( pair(i,1) );
		 s( pair(i,1) ) = s( pair(i,2) );
		 s( pair(i,2) ) = tempVar;
	 end
end