function [dt_hold] = ca3_fun2(data,ax_lbl)
%% Segmentation Function
   % This function takes user-chosen data as well as axis labels and
   % returns a numeric matrix of the data segmented from the time of
   % maximum load to the end. The function also shifts the time data so
   % that t(1) = 0.
% Input:
   % data - [Mx3] numeric matrix containing data
   % ax_lbl - [1x3] cell array for labeling axes
% Output:
   % dt_hold - [Mx3] numeric matrix that contains data
% -------------------------------------------------------------------------
% Author: Gabriella Grym
% Date:   10.08.2020
% Team:   A_03
   
%% Obtain the displacement and load axis labels from ax_lbl and ensure
%  that they are positive

% Assuming displacement is stored under "Disp (mm)"
  disp = abs(data(:, strcmp(ax_lbl,'Disp (mm)'))); 

% Assuming load is stored under "Load (N)"
  load = abs(data(:, strcmp(ax_lbl,'Load (N)'))); 
                                               
% Also extract time data, assuming it is stored under "Elapsed Time (sec)"
  time = abs(data(:, strcmp(ax_lbl,'Elapsed Time (Sec)')));
                                               
%% Determine Max Load and Segment Data
% The max function produces the maximum load and the coordinate at which it
% occurs
  [max_load,x] = max( load );

% Segmented displacement
  segDisp = disp(x:end);

% Segmented load
  segLoad = load(x:end);

% unshifted Segmented time
  ushiftTime = time(x:end);

% Shift Segmented time such that t(1) = 0 by % subtracting the time at 
% which the max occurs to shift data
  segTime = time(x:end) - time(x);

%% Create figure(2) that plots time vs load

fig = figure(2);
clf(fig);

% Adjust plot settings
	ax = gca;
	ax.XGrid = 'on';
	ax.XMinorGrid = 'on';
	ax.YGrid = 'on';
	ax.YMinorGrid = 'on';
	hold on
	title('Load (N) vs Time (Sec)', 'fontsize', 14);
  xlabel('Time (sec)', 'fontsize', 12);
  ylabel('Load (N)', 'fontsize', 12);

% Plot Shifted Data
  plot(segTime,segLoad,'-','LineWidth',2,'DisplayName',...
		'Time-Adjusted "Hold Data"','Color','#A2142F')
	
% Plot Unshifted Data
  plot(ushiftTime,segLoad,'k--','LineWidth',1,'DisplayName',...
		  'Unshifted "Hold" Data')
		
% Add maximum load point onto figure(2)
  plot(segTime(1), max_load, 'm*', 'DisplayName',...
		   sprintf('Max Load = %.2f',max_load),'MarkerSize',10);
	hold off

% Add legend
  legend
%% Assign output matrix
dt_hold = [segTime segDisp segLoad];