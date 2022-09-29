function [yt_data] = ca1_fun1(eq_cnst,t_data)
  % DESCRIPTION
  %  This function calculates the temperature on earth's surface at
  %  different locations using the model y(t) = R.sin(2*pi/24*(t-t0)) + B
	% INPUT
	%  eq_cnst -> [1x3] vector containing model constants [R,t0,B] in order.
	%       R  -> range in daily temperature (deg F)
  %       t0 -> 'off-set' time of day (hrs)
	%       B  -> 'bias' temperature (deg F)
	%  t_data  -> [Nx1] vector containig times (hrs)
	% OUTPUT
	%  yt_data -> temperature (deg F)
	%-----------------------------------
  % Authors: Tony Okeke
	%          Nick Corrado
	%          Ben Jennings
	%          Gabriella Grym
	% Date: 09.25.2020
	% Team: A_03
	
	% Extract constants from eq_cnst
	  R = eq_cnst(1,1); % Assuming col 1 = R
		t0 = eq_cnst(1,2); % Assuming col 2 = t0
		B = eq_cnst(1,3); % Assuming col 3 = B
		
	% Calculate yt_data
	  yt_data = R * sin(2 * pi/24 * (t_data-t0)) + B;
end