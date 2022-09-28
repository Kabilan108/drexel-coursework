function runSum = runningsum(from,to)
   % Returns the sum of numbers from 'from' to 'to'
	 % By Tony Kabilan Okeke - 20191112
	 
	 if ~exist('to','var') % allow function to run with only one input argument
		 to = from;
		 from = 1;
	 end
	 
	 if to < from % allow input arguments to be specified in any order
		 temp = to;
		 to = from;
		 from = temp;
	 end
	 
	 runSum = 0;
	 for i=from:to
		 runSum = runSum + i;
	 end
end