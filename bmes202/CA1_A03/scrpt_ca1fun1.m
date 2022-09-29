%% Calculate Temperature at Four Locations
% DESCRIPTION
%  This script determines the temperatures at different locations based on
%  the model y(t) = R.sin(2*pi/24*(t-t0)) + B
%  It returns plots of temperature against time at these locations
%-----------------------------------
% Authors: Tony Okeke
%          Nick Corrado
%          Ben Jennings
%          Gabriella Grym
% Date: 09.25.2020
% Team: A_03

% Define time variable
   t_data = (0:24)';
	 
% Define cnsts table containing constants at different locations
   location = {'Philadelphia, PA','Panama City, FL','Brewster, MA',...
		           'Enugu, Nigeria'}';
	 eq_cnst = [25 9 55 ; 10 9 72 ; 15 9 59 ; 13 9 73];
	 % eq_cnst(:,1) -> R (oF)
	 % eq_cnst(:,2) -> t0 (hrs)
	 % eq_cnst(:,3) -> B (oF)
	 cnsts = table(location,eq_cnst);
	 
% Use ca1_fun1 to determine temperatures and plot Temperature vs Time
% graphs for each location.

% Configure Plot Area
  figure
  ax = axes;
	% Color order for the various graphs
	ax.ColorOrder = [0 0.447058823529412 0.741176470588235;0.729411764705882 0 0;...
									 0.929411764705882 0.694117647058824 0.125490196078431;...
									 0.466666666666667 0.674509803921569 0.188235294117647];
	% Adjust plot settings
	ax.XGrid = 'on';
	ax.XMinorGrid = 'on';
	ax.YMinorGrid = 'on';
	ax.Parent.Position = [900 450 800 450]; % window size
	hold on
  title('Temperature (^oF) vs Time (hrs)','FontWeight','bold','FontSize',14)
  xlabel('Time (hrs)','FontWeight','bold','FontSize',12)
	ylabel('Temperature (^oF)','FontWeight','bold','FontSize',12)
			
% Generate Graphs
  for i = 1:numel(location)
	  % Calculate yt_data
	    yt_data = ca1_fun1(cnsts.eq_cnst(i,:),t_data);
	  % Plot Results
	    plot(t_data,yt_data,'-o','LineWidth',1.5,'MarkerSize',4)
	end
  legend(location,'Location','southeast','FontSize',10)
	hold off
	
%% Determining Constants from Figure 1 (In Problem Statement)
% Define Constants and t_data.
%   From Figure 1 (Problem Statement)
%     Max Temp - Min Temp = 40 oF
%     Range, R = 40/2 = ± 20 oF
%     Bias, B = Max Temp - R = 60 oF
%   To determine the appropriate t0 value, we test all possible values and 
%   select the one that produces a graph matching fig. 1
	R = 20; 
	t0 = (0:24)'; % range of values for testing
	B = 60; 
	
	t_data = (0:24)';
	
% Calculate yt_data, and plot graphs for each potential t0 value in a 5 x 5
% subplot grid.
	figure
	clf
	for i = 1:numel(t0)
		% Calculate temperature
		yt_data = ca1_fun1([R t0(i) B],t_data);
		
		% Plot Graphs
		subplot(5,5,i)
		hold on
		title(sprintf('t0 = %i',t0(i)))
		plot(t_data,yt_data,'-r')
		plot([15 15],[40 80],'-k') % Identifies peak from problem statement
		xticks(15)
		yticks([])
		hold off
	end
% The graph t0 = 9 best matches figure 1 as it has the same peak at 15 hrs,
% as well as matching the shape of figure 1.
%   Emphasize the plot t0 = 9
	  ax = subplot(5,5,10);
		box on
		ax.LineWidth = 1;
		ax.XColor = 'blue';
		ax.YColor = 'blue';
	
% Generate Figure 1 From The Problem Statement
%   Plot Graph
    figure
		ax = axes;
		hold on
		plot(t_data,ca1_fun1([R t0(10) B],t_data),'sr');
		ax.XGrid = 'on';
		ax.YGrid = 'on';
		title('Problem Statement Figure 1')
		xlabel('Time (hrs)')
		ylabel('Temperature (^oF)')
		xlim([0 24])
		xticks([0 3 6 9 12 15 18 21 24])
%   Include a text box containing the determined constants
    txt = sprintf('Constants\n\nR = %i ^oF \nt0 = %i hrs \nB = %i ^oF',...
			            R,t0(10),B);
    a = text(1,73,txt);
		a.EdgeColor = 'k';
		a.BackgroundColor = 'white';
		hold off