function [S_clr, dt_out] = ca4_fun3(imBW_in)
  %% DESCRIPTION (Analyze objects in BW image)
	%    This function takes in a 'filtred' BW image and returns a structure
	%    containing results for object analysis, and an object summary
	%  INPUT
  %    imBW_in -> [MxN] matrix with 'final' filtered image
	%  OUTPUT
	%    S_clr  -> Struct containing results for object analysis
	%    dt_out -> object summary containing n (# of objects), minimum eq.
	%              diameter, max eq. diameter, average eq. diameter, standard
	%              deviation eq. diameter.
	%  ----------------------------------------------------------------------
	%  Author: Tony Okeke
	%  Team:   B02
	%  Date:   10/28/2020
	
	%% Create Label Image
	im_L = bwlabel(imBW_in);
	
	% Visualize Image
	figure(5)
	imshow(im_L)
	title('Filtered Image')
	
	%% Determine Outputs
	% Determine object analysis struct
	S_clr = regionprops(im_L);
	
	% Calculate Equivalent Diameters
	eqDia = sqrt( [S_clr.Area]*4/pi );
	
	% Prepare Output struct
	n = numel(S_clr);
	minDia = min( eqDia );
	maxDia = max( eqDia );
	avgDia = mean( eqDia );
	stdDia = std( eqDia );
	dt_out = struct('n',n,'minDia',minDia,'maxDia',maxDia,'avgDia',avgDia,'stdDia',stdDia);
	%% Report Formatted Output
	fprintf('\n')
	fprintf(2,'Outputs\n')
	fprintf('<strong>Number of Objects\tMinimum Diameter\tMaximum Diamter\t Average Diameter\t Std-Dev Diameter</strong>\n')
	fprintf('%12.3f\t%15.3f\t%19.3f\t%16.3f\t%15.3f\n',n,minDia,maxDia,avgDia,stdDia)
	
end