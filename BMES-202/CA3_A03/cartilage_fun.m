function load_est = cartilage_fun(eq_cnst, time_data)
  % DESCRIPTION
	%  This function models the applied load as a function of time based on
	%  the equation: L(t) = A exp(-1/B * t) + C. It takes the equation
	%  constants (A,B and C) and time data as inputs and returns the load
	%  estimates.
	% INPUT
	%  eq_cnst   -> [1x3] vector of equation constants (A,B and C in order)
	%  time_data -> [Nx1] vector of experimental time data
	% OUTPUT
	%  load_est  -> [Nx1] vector of estimated load values
	% -----------------------------------------------------------------------
	% Author: Tony Okeke
	% Date:   10.08.2020
	% Team:   A03
	
	% Extract equation constants
	A = eq_cnst(1);
	B = eq_cnst(2);
	C = eq_cnst(3);
	
	% Evaluate function
	load_est = A * exp( -1/B * time_data ) + C;
end