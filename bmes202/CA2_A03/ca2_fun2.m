function [dt_seg] = ca2_fun2(data, col_lbls)
  % DESCRIPTION -> Segmentation Function
	%   This function takes experimental data and column labels as input, and
	%   returns a numeric data of a segmented linear region of the user's
	%   choice. The user identifies the linear region from a plot of load
	%   against displacement generated from the experimental data
	% INPUT
	%  data     -> [M1 x N1] matrix of numerical data
	%  col_lbls -> [1 x N1] cell-array containing data labels decribing data
	%              contained within columns
	% OUTPUT
	%  dt_seg -> [MxN] matrix of numeric data of 'segmented' linear region
	% -----------------------------------------------------------------------
	% Author: Tony Okeke
	% Date:   10.03.2020
	% Team:   A_03
	
	% Extract the Load and Displacement columns from col_lbls, and use them
	% to index data.
	% Assuming:
	%    * Displacement data is stored under 'Disp (mm)'
	%    * Load data is stored under 'Load (N)'
	disp = data(:, strcmp(col_lbls,'Disp (mm)') );
	load = data(:, strcmp(col_lbls,'Load (N)') );
	
	% Create Load-Displacement Plot
	fig = figure(2);
	clf(fig)
	  % Adjust Plot Settings
		ax = gca;
	  ax.XGrid = 'on';
	  ax.XMinorGrid = 'on';
	  ax.YGrid = 'on';
	  ax.YMinorGrid = 'on';
		% Plot Data Points
		hold on
		title('Load (N) vs Displacement (mm)','FontWeight','bold','FontSize',14)
		xlabel('Displacement (mm)','FontWeight','bold','FontSize',12)
		ylabel('Load (N)','FontWeight','bold','FontSize',12)
		plot(disp,load,'-o','Color','#A2142F','LineWidth',1,'MarkerSize',4,'MarkerFaceColor','y')
		hold off
		
  % Prompt user to select points for linear region
	%  prompt formatting
	   createmode.WindowStyle = 'Modal';
		 createmode.Interpreter = 'tex';
		 message = [newline '\fontsize{12}\bfPlease Selet Linear Region by'...
			          ' Identifying The Start and End Points' newline...
								newline '\fontsize{10}Select start point first, then end point, '...
								'then hit "Enter"'];
	uiwait( msgbox(message,createmode) );
	
	% Collect start and end points of segmented region
	[x,y] = getpts(fig);
	% Ensure x(1) < x(2)  && y(1) < y(2)
	p_1 = [x(1) y(1)];
	p_2 = [x(2) y(2)];
	while ~all( p_1 < p_2 )
		% Create an error prompt if point1 is not > point 2
		  createmode.WindowStyle = 'Modal';
			createmode.Interpreter = 'tex';
			message = [newline '\fontsize{12}\bfERROR!' newline...
					       'Please Ensure the Start Point Preceeds the End Point'...
								 newline 'i.e. x(1) > x(2) AND y(1) > y(2)' newline];
		uiwait( msgbox(message,createmode) );
		% Collect new start and end points
		[x,y] = getpts(fig);
		p_1 = [x(1) y(1)];
		p_2 = [x(2) y(2)];
	end
	% Plot user-selected points
	figure(2)
	hold on
	plot(x,y,'og','LineWidth',2,'MarkerFaceColor','#0000FF')
	hold off
	
	% Create bolean and use it to identify points in data between p_1 and p_2
	disp_bool = (disp > x(1) & disp < x(2));
	load_bool = (load > y(1) & load < y(2));
	I = disp_bool & load_bool;
	
	% Extract segmented data
	dt_seg = data(I,3:5);
	disp_seg = dt_seg(:,2);
	load_seg = dt_seg(:,3);
	
	% Plot segmented region in figure 2
	figure(2)
	hold on
	plot(disp_seg,load_seg,'s','Color','#0072BD','LineWidth',2,'MarkerSize',5)
	lgd = {'Experimental Data','User-Selected Points','Segmented Data'};
	legend(lgd,'Location','northwest');
	hold off
end