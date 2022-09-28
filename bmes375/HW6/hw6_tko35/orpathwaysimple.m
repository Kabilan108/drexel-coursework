function dy = orpathwaysimple(t, y, kf, Vmax)
  % This function defines the rates of change for the OR pathway
  % simulation.
	% INPUT:
	%   t - a vector indicating the time interval (for ode23s)
	%   y - initial concentrations
	%   kf - rate of the forward reaction
	%   Vmax - maximum micheals menten rate
	% OUTPUT: dy - a vector containing rates of change
	% Species in y: S1, R1, S1R1, S2, R2, S2R2, TF, TFP
	
	% Define arbitrary constants
	if ~exist('kf', 'var'); kf = 1; end
	if ~exist('Vmax', 'var'); Vmax = 1; end
	kr = 2;
	km = 2;
	
	% Define reaction rates
	re1 = kf*y(1)*y(2) - kr*y(3);
	re2 = kf*y(4)*y(5) - kr*y(6);
	re3 = (Vmax*y(7)*(y(3)+y(6))) / (km + y(7));
	
	% Define dy vector
	dy = zeros(8,1);
	dy(2) = -re1;
	dy(3) = re1;
	dy(5) = -re2;
	dy(6) = re2;
	dy(7) = -re3;
	dy(8) = re3;
end