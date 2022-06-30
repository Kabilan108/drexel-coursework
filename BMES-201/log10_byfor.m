function est = log10_byfor(x,inc)
   % Set the default value of inc as 0.01
	 if ~exist('inc','var')
		 inc = 0.01;
	 end
	 for est = 0:inc:x
		 if 10^est >= x
			 break;
		 end
	 end
end