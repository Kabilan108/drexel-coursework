function avgTime = mytimer(myFunction)
   allTimes = zeros(1,10000);
	 for i = 1:10000
		 tic;
		 myFunction;
		 allTimes(i) = toc;
	 end
	 avgTime = mean(allTimes);
end