function dy = xorpathway(t, y, varargin)
  % This function is a more robust version of xorpathway_simple.
	% It allows the user to specify reaction rate constants.
	% INPUT:
	%   t - a vector indicating the time interval (for ode23s)
	%   y - initial concentrations
	%   varargin - additional model parameters
	% OUTPUT: dy - a vector containing rates of change
	% y, dy = [S1 R1 S1R1 S2 R2 S2R2 TF TFP]
	
	% Combine input options
	opt = mergeoptions(struct('kf', 50, 'kr', 2, 'Vmax', 4,...
										        'km', 2), varargin{:});
	
	%% Reactions
	re1 = opt.kf*y(1)*y(2) - opt.kr*y(3);
	re2 = opt.kf*y(4)*y(5) - opt.kr*y(6);
	re3 = opt.kf*y(3)*y(6) - opt.kr*y(9);
	E4 = (opt.Vmax*y(7)*y(3))/(opt.km + y(7));
	E5 = (opt.Vmax*y(7)*y(6))/(opt.km + y(7));
	E6 = (opt.Vmax*y(8)*y(9))/(opt.km + y(8));
	
	%% Rate of change in species
  dy = zeros(9,1);
	dy(2) = -re1 + re3;
	dy(3) = re1 - re3;
	dy(5) = -re2 + re3;
	dy(6) = re2 - re3;
	dy(7) = E6 - E4 - E5;
	dy(8) = E4 + E5 - E6;
	dy(9) = re3 - E6;
end