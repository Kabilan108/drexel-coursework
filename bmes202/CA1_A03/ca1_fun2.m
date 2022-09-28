function [yt_data] = ca1_fun2(eq_cnst,t_data)
  % DESCRIPTION
	%  This function models how the heart rate slows as it returns to
	%  'normal' after exercise based on the model y(t) = D*exp(-t/tau) + B
	% INPUT
	%  eq_cnst -> [1x3] vector containing model constants [D,tau,B] in order.
	%      D   -> Increase in heart-rate (BPM)
  %      tau -> decay constant (sec)
	%      B   -> base-line heart-rate (BPM)
	%  t_data  -> [Nx1] vector containig times (sec)
	% OUTPUT
	%  yt_data -> Heart-rate (BPM)
	%-----------------------------------
  % Authors: Tony Okeke
	%          Nick Corrado
	%          Ben Jennings
	%          Gabriella Grym
	% Date: 09.25.2020
	% Team: A_03
	
	% Extract constants from eq_cnst
	  D = eq_cnst(1,1); % Assuming col 1 = D
		tau = eq_cnst(1,2); % Assuming col 2 = tau
		B = eq_cnst(1,3); % Assuming col 3 = B
		
	% Calculate yt_data
	  yt_data = D * exp(-t_data/tau) + B;
end

