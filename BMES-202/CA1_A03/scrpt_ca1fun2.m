%% Calculate Heart-rate Decays for Three Subjects
% DESCRIPTION
%  This function models how the heart rate slows as it returns to
%  'normal' after exercise based on the model y(t) = D*exp(-t/tau) + B
%  It plots the return to baseline for three subjects (fit,average,unfit).
%-----------------------------------
% Authors: Tony Okeke
%          Nick Corrado
%          Ben Jennings
%          Gabriella Grym
% Date: 09.25.2020
% Team: A_03

% Define time variable
   t_data = (0:60)';
	 
% Define cnsts table containing constants for the different subjects
   fitness = {'Unfit','Average','Fit'}';
	 eq_cnst = [120 20 75;60 10 60;40 5 40];
	 % eq_cnst(:,1) -> D (BPM)
	 % eq_cnst(:,2) -> tau (sec)
	 % eq_cnst(:,3) -> B (BPM)
	 cnsts = table(fitness,eq_cnst);
	 
% Use ca1_fun2 to determine heart-rates and plot Heart-rate vs Time
% graphs for each subject.

% Configure Plot
  figure
  ax = axes;
	% Color order for the various graphs
	ax.ColorOrder = [0 0.447058823529412 0.741176470588235;0.729411764705882 0 0;...
									 0.929411764705882 0.694117647058824 0.125490196078431];
	% Adjust plot settings
	ax.XGrid = 'on';
	ax.XMinorGrid = 'on';
	ax.YMinorGrid = 'on';
	hold on
  title('Heart-rate (BPM) vs Time (s)','FontWeight','bold','FontSize',14)
  xlabel('Time (s)','FontWeight','bold','FontSize',12)
	ylabel('Heart-rate (BPM)','FontWeight','bold','FontSize',12)
	yticks([20 40 60 80 100 120 140 160 180 200 220])
	
% Generate Graphs
  for i = 1:numel(fitness)
	  % Calculate yt_data
	    yt_data = ca1_fun2(cnsts.eq_cnst(i,:),t_data);
	  % Plot Results
		plot(t_data,yt_data,'-','LineWidth',1.5)
	end
	ylim([20 200])
  legend(fitness,'Location','northeast','FontSize',10)
	hold off
	
%% Determining Constants from Figure 2 (In Problem Statement)
% Define Constants and t_data.
%   From Figure 2 (Problem Statement)
%     Increase in HR, D = Max HR - Min HR = 120 BPM
%     Base-line HR, B = Min HR = 60 BPM
%   To determine the appropriate tau value, we test four different tau
%   values (based on the values for fit,unfit,and average subjects). The
%   tau value that produces a graph matching figure 2 is then selected.
	D = 120;
	tau = (5:5:20)'; % t0 contains a range of values for testing
	B = 60;
	
	t_data = (0:60)';
	
% Calculate yt_data, and plot graphs for each potential tau value 
% overlaying figure 2 in a 2 x 2 subplot grid.
	figure
	clf
	for i = 1:numel(tau)
		% Calculate heart rate
		yt_data = ca1_fun2([D tau(i) B],t_data);
		
		% Plot Graphs
		subplot(2,2,i)
		hold on
		title(sprintf('tau = %i',tau(i)))
		plot(t_data,yt_data,'-r','LineWidth',1.5)
		ylim([40 200])
		
		% Add graph from fig.2 to the background of the plots
		I = imread('Figure2.png');
		h = image([0 60],[200 40],I);
		uistack(h,'bottom')
		xticks([0 60])
		yticks([50 200])
		hold off
	end
% The graph tau = 5 matches fig.2 the best out of all values tested.
%   Emphasize the plot tau = 5
	  ax = subplot(2,2,1);
		box on
		ax.LineWidth = 3;
		ax.XColor = 'blue';
		ax.YColor = 'blue';
		
% Generate Figure 2 From The Problem Statement
%   Plot Graph
    figure
		ax = axes;
		hold on
		plot(t_data,ca1_fun2([D tau(1) B],t_data),'-r','LineWidth',1.5);
		ax.XGrid = 'on';
		ax.YGrid = 'on';
		title('Problem Statement Figure 2')
		xlabel('Time (s)')
		ylabel('Heart-rate (BPM)')
		ylim([40 200])
%   Include a text box containing the determined constants
	  txt = sprintf('Constants\n\nD = %i BPM \n\\tau = %i s \nB = %i BPM',...
		              D,tau(1),B);
		a = text(45,170,txt);
		a.EdgeColor = 'k';
		a.BackgroundColor = 'white';
		hold off