function [Kel, y_err] = ca2_fun3(dt_linear)
  % Code written by Nicolas Corrado 9302020
  % Team 3A for the project ca2_fun3
	% -----------------------------------------------------------------------
	% OVERVIEW (Analysis Function)
	%   This funtion takes the output of funtion two (dt_linear) and 'fits' 
	%   the line using polyfit.  This data will then be used to estimate load 
	%   values (y_est) using polyval. The line produced will be overlayed on 
	%   to the graph. Finally, the average absoluter error between the y_est 
	%   and the y data will be expressed as y_err
  % OUTPUT
  %  Kel   -> [1x1] matrix containing stiffness of the material tested
	%  y_err -> [1x1] matrix containing average-absolute-error between linear
	%           model and data
  % INPUT
	%  dt_linear -> [Mx3] matrix of data from the linear region of data

	% This fits the displacement and load data (x and y) to a line assuming:
	%  displacement (x) = dt_linear(:,2)
	%  load data (y) = dt_linear(:,3)
	p_line= polyfit(dt_linear(:,2), dt_linear(:,3),1);

	% Kel is the slope of the polyfit of the data.
	Kel= p_line(1);

	% Load values are estimated using the previous data and polyval assuming:
	%  displacement (x) = dt_linear(:,2)
	y_est= polyval(p_line, dt_linear(:,2));

	% The line produced is overlayed on the figure 2 (generated by ca2_fun2)
	% assuming:   displacement (x) = dt_linear(:,2)
	figure(2)
	hold on
	plot(dt_linear(:,2), y_est, '-m','LineWidth',3,'DisplayName',...
		   'Linear Estimate')
	hold off
	
	% Caclulation of the average absolute error in the fit assuming:
	%  load data (y) = dt_linear(:,3)
	y_err = mean(abs(y_est - dt_linear(:,3)));
return