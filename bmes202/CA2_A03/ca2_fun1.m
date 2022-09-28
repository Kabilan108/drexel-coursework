function [dt, col_lbls, csv_file] = ca2_fun1()
%By Ben Jennings
% 10/06/2020
  % DESCRIPTION -> Import & Visualization Function
	%   This function imports experimental data from a file of the users 
	%   choice, and plots a figure containing a graph of time (x-axis) 
	%   against displacement (y-axis).
	% INPUT
	%   None
	% OUTPUT
	%   data     -> [M1 x N1] matrix of numerical data
	%   col_lbls -> [1 x N1] cell-array containing labels decribing data
	%               contained within columns
	%   csv_file -> [1 x N2] string containing the path and file name
	%------------------------------------------------------------------------
	% Author: Ben Jennings
	% Date:   10.03.2020
	% Team:   A_03
	
	% Provide GUI for user to select data file
	[fnm,pth]=uigetfile('*.csv','Choose Data file');
	% Create full file name variable including name & path
	csv_file = fullfile(pth,fnm);
	
	% Search the csv_file to determine where the column headers start
	literal = 'Points'; % Key word being searched for in the file
	fid = fopen(csv_file); % creates a file identifer variable for the file 
	                       % user is calling 
	y = 0; % sets variable y to equal zero for use in while loop 
	tline = fgetl(fid); % Reads the file selected by the user line by line 
	line = 0; % sets the starting line to zero 
	while y < 1 
		% Each time The function goes through the loop a line is read.
		% for 'Points'once 'Points is found the m value is updated which
		% causes the y value to be updated to the line the file found the
		% word Points on
		matches = strfind(tline, literal);
		% This searches for the word 'Points' once 'Points is found the
		% m value is updated which causes the y value to be updated
		% to the line the file found the word Points on
		line = line +1 ;
		if matches > 0
			y = y + line;
		end
		tline = fgetl(fid);
	end
	
  % Read numerical data and header information
  S_data = importdata(csv_file,',',y+1);
	dt = S_data.data;
	
	% Create a cell-array to label ALL columns
	col_lbls{1,1}='Points';
	col_lbls{1,2}='Elapased Time (sec)';
	col_lbls{1,3}='Scan Time (sec)';
	col_lbls{1,4}='Disp (mm)';
	col_lbls{1,5}='Load (N)';

	% Create figure
	fig = figure(1);
	clf(fig)
	fig.OuterPosition = [208,208,1120,420];
	fig.InnerPosition = [200,200,1136,513];
	
	% Disp-Time Subplot
	  subplot(1,2,1)
	  % Adjust Plot Settings
	    ax = gca;
	    ax.XGrid = 'on';
			ax.XMinorGrid = 'on';
			ax.YGrid = 'on';
			ax.YMinorGrid = 'on';
		% Plot Data Points
		  hold on
			title([col_lbls{4} ' vs. ' col_lbls{2}],'FontWeight','bold','FontSize',14)
			xlabel(col_lbls{2},'FontWeight','bold','FontSize',12)
			ylabel(col_lbls{4},'FontWeight','bold','FontSize',12)
			plot(dt(:,2),dt(:,4),'-','Color','#A2142F','LineWidth',2)
			hold off
	
	% Load-Time Subplot
	  subplot(1,2,2)
	  % Adjust Plot Settings
	    ax = gca;
			ax.XGrid = 'on';
			ax.XMinorGrid = 'on';
			ax.YGrid = 'on';
			ax.YMinorGrid = 'on';
	  % Plot Data Points
	    hold on
			title([col_lbls{5} ' vs. ' col_lbls{2}],'FontWeight','bold','FontSize',14)
			xlabel(col_lbls{2},'FontWeight','bold','FontSize',12)
			ylabel(col_lbls{5},'FontWeight','bold','FontSize',12)
			plot(dt(:,2),dt(:,5),'-','Color','#A2142F','LineWidth',2)
			hold off
end