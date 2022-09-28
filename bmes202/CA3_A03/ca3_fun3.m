function [fit_params,y_est,y_mae] = ca3_fun3(dt_hold,ax_lbl)
  % DESCRIPTION -> Analysis Function
	%  This function takes the segmented hold data and axes labels as input
	%  and returns a figure showing the hold data fitted to the equation 
	%  L(t) = A exp(-1/B * t) + C. It also returns the fit parameters
	%  (A,B,C), estimated load values, and mean absolute error of the fit.
	% INPUT
	%  dt_hold  -> [Mx3] numeric matrix containing data
	%  ax_lbl   -> [1x3] cell array of axis labels
	% OUTPUT
	%  fit_params -> [1x3] vector containing best fit parameters
	%       y_est -> [Mx1] vector containing estimated load values
	%       y_mae -> [1x1] vector containing mean-absolute-error of the fit
	% -----------------------------------------------------------------------
	% Author: Tony Okeke
	% Date:   10.08.2020
	% Team:   A03
	
	%% Extract data
	segTime = dt_hold(:, strcmp(ax_lbl,'Elapsed Time (Sec)') );
	segLoad = dt_hold(:, strcmp(ax_lbl,'Load (N)') );
	
	%% Plot Raw Load vs. Time Data Points
	fig = figure(3);
	clf(fig)
	
	% Adjust plot settings
	  ax = gca;
	  ax.XGrid = 'on';
	  ax.XMinorGrid = 'on';
	  ax.YGrid = 'on';
	  ax.YMinorGrid = 'on';
		
  % Plot data points
	  hold on
		title([ax_lbl{3} ' vs. ' ax_lbl{1}],'FontWeight','bold','FontSize',14)
		xlabel(ax_lbl{1},'FontWeight','bold','FontSize',12)
		ylabel(ax_lbl{3},'FontWeight','bold','FontSize',12)
		plot(segTime,segLoad,'x','Color','#A2142F','MarkerSize',4,...
			   'MarkerFaceColor','#A2142F')
		hold off
		
	%% Estimate model parameters
	
	% Determine initial estimates
	C_est = min(segLoad);
	A_est = max(segLoad) - C_est;
	%    Extract a point roughly in the center of the graph and use that to
	%    evaluate an estimate of B
	     t = segTime( round(numel(segTime)/2) );
	     L = segLoad(segTime == t);
	B_est = t / ( log(A_est) - log(L - C_est) );
	
	% fit the data to the load model
	opts = optimset('Display','off');
	lb = [0 0 0]; % parameters that would generate a straight line
	ub = [60 100 60];
	fit_params = lsqcurvefit(@cartilage_fun,[A_est B_est C_est],segTime,...
		                       segLoad,lb,ub,opts);
	
	%% Estimate load values based on the model, and add to figure 3
	y_est = cartilage_fun(fit_params,segTime);
	
	figure(3)
	hold on
	plot(segTime,y_est,'-','Color','#77AC30','LineWidth',3)
	hold off
	
	% add legend
	legend({'Experimental Data','Fitted Curve'})
	
	% mean absolute error
	y_mae = mean( abs( y_est - segLoad ) );
end