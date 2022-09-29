function lineNo = findfirstinfile(filename, search)
   % Takes in a filename and a search text as input and returns the line 
	 % number of the first line in that file that contains the search text.
	 % By Tony Kabilan Okeke (tko35) - 20191209
	 
	 % Load the text file
	   text = fileread( filename );
	 
	 % Determine the number of lines in the text
	   noOfLines = numel( strfind( text , newline ) ) + 1 ;
	 
	 % Break the text up into respective lines
	   lines = strsplit( text , newline );
	 
	 % Loop through each line
	   for line = 1:noOfLines
		   if numel( strfind( lines{line} , search ) ) > 0
			   lineNo = line;
			   break;
			 end
		 end
	 % If no match exists, then assign 0 to lineNo
	   if ~exist('lineNo','var')
		   lineNo = 0;
	   end
end