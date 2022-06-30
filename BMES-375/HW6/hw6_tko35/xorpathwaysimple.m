function dy = xorpathwaysimple(t, y, kf, Vmax)
  % This function defines the rates of change for the XOR pathway
  % simulation.
	% INPUT:
	%   t - a vector indicating the time interval (for ode23s)
	%   y - initial concentrations
	%   kf - rate of the forward reaction
	%   Vmax - maximum micheals menten rate
	% OUTPUT: dy - a vector containing rates of change
	% Species in y: S1, R1, S1R1, S2, R2, S2R2, TF, TFP, S1R1S2R2
	
	% Define arbitrary constants
	if ~exist('kf', 'var'); kf = 50; end
	if ~exist('Vmax', 'var'); Vmax = 4; end
	kr = 2;
	km = 2;
	
	% Define reaction rates
	re1 = kf*y(1)*y(2) - kr*y(3);
	re2 = kf*y(4)*y(5) - kr*y(6);
	re3 = kf*y(3)*y(6) - kr*y(9);
	E4 = (Vmax*y(7)*y(3))/(km + y(7));
	E5 = (Vmax*y(7)*y(6))/(km + y(7));
	E6 = (Vmax*y(8)*y(9))/(km + y(8));
	
	% Define dy vector
  dy = zeros(9,1);
	dy(2) = -re1 + re3;
	dy(3) = re1 - re3;
	dy(5) = -re2 + re3;
	dy(6) = re2 - re3;
	dy(7) = E6 - E4 - E5;
	dy(8) = E4 + E5 - E6;
	dy(9) = re3 - E6;
end