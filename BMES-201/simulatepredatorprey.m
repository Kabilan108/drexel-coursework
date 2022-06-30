function [ popHistory ] =  simulatepredatorprey(x,y, a,b,c,d, T)
   % Takes the initial populations of predators(y) and prey(x), parameters
   % for their growth, and length of time in years and returns their
   % simulated population history
	 % By Tony Kabilan Okeke (tko35) - 20191209 
	 
	 % Preallocate the output vector
	   popHistory = [ x zeros(1,T) ; y zeros(1,T) ];
	 
	 % Loop runs T times
	   for i = 1:T
		   % Allocate the values of xt and yt from the popHistory matrix
		     xt = popHistory(1,i);
		     yt = popHistory(2,i);
		   % Calculate the populations for the next years
		     xt_1 = a*xt - b*xt*yt +xt;
		     yt_1 = c*xt*yt - d*yt +yt;
		   % replace the corresponding elements in popHistory with the new
		   % populations
		     popHistory(:,i+1) = [xt_1 yt_1];
	   end
end