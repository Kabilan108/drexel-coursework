function studyresponsetime_xorpathway( dyfun )
  % This function is used to
	% INPUT: dyfun - a function that defines the pathway rates
	% OUTPUT: rTime - response time corresponding to unit input
	% Define Initial Conditions
	Yi = zeros(9, 1);
	Yi([2, 5, 7]) = 10; % [R1 R2 TF]
	
	checks = linspace(0.1, 10, 20); % Various input concentrations
	rtimes = zeros(size(checks)); % Response times
	
	for i = 1:length(checks)
		Yi(1) = checks(i); % S1
		[T, Y] = ode23s(dyfun, [0 10], Yi);
		pos = find(Y(:,8) >= 8, 1, 'first');
		% Get corresponding response times if requirement is met
		if isempty(pos); rtimes(i) = nan;
		else;            rtimes(i) = T(pos); end
	end
	
	% Plot results
	figure;
	plot(checks, rtimes, '-', 'Color', '#A2142F', 'LineWidth', 2);
	xlabel('Input Concentration')
	ylabel('Response Time (sec)')
	ylim([0.2 1.2])
	hold on;
	plot([1, 1], ylim, 'k--')
	plot([0, 10], [1, 1], 'k--')
	hold off
end