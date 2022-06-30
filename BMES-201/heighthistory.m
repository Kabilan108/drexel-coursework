function [maxWeight] = heighthistory(data)
   % Plots a graph of height against time, and returns the maximum weight
	 % By Tony Kabilan Okeke - 20191016
	 
	 % Obtain the maximum of each column, the third value is the maximum
	 % weight
	 maxima = max(data,[],1);
	 maxWeight = maxima(3);
	
	 % Obtain the heights and ages from the second and first columns
	 % respectively
	 heights = data(:,2);
	 ages = data(:,1);
	 
	 % Plot the graph, and set the xlabel,ylabel, and title values. Also show
	 % the grid
	 plot(ages,heights,'r-o','linewidth',2)
	 xlabel('Age (Years)');
	 ylabel('Height (cm)');
	 title('Height vs. Age');
	 grid on;
end