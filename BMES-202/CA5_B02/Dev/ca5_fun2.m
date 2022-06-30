function [BW_hva] = ca5_fun2(imHSV)
  %% DESCRIPTION (filter image)
	%    This function takes in image HSV data, and filter parameters and
	%    returns filtered images based on the set parameters.
	%  INPUT
	%    imHSV -> [MxNx3] containing image HSV data
	%   (Not an actual input to the function but prompts the user for it when the function is called) 
	%   filt_opts -> [3x2] filtering options
	%              -> row1 - min/max color
	%              -> row2 - min/max value
	%              -> row3 - min/max diameter
	%  OUTPUT
	%    BW_out -> [MxN] matrix with 'final' filtered image
	%    BW_123 -> [MxNx3] B/W images (1 - hue; 2 - value; 3 - size)
	%  ----------------------------------------------------------------------
	%  Author: Everyone
	%  Team:   B02
	%  Date:   11/2/2020
		%% Prompt User to enter Filter Parameters
		uiwait(msgbox('Please Enter Filter Parameters using the colorbar in the HUE and Value figures'));
		prompt = {'Minimum Hue:', 'Maximum Hue:',...
			'Minimum Value:', 'Maximum Value:', ...
			'Minimum Diameter:','Maximum Diameter:'};
		dialogTitle = 'Filter Parameters';
		dims = [1 30];
		definput = {'0.25','0.45','0.25','0.6','1','1000'};
		% Green = 0.25, 0.45, 0.25, 0.6, 5, 1000
		% Orange = 0, 0.15, 0.6, 1, 5, 1000
		filt_thrs = str2double(inputdlg(prompt,dialogTitle,dims,definput));
		hue_thr = [filt_thrs(1,1),filt_thrs(2,1)];
		val_thr = [filt_thrs(3,1),filt_thrs(4,1)];
		dia_thr = [filt_thrs(5,1),filt_thrs(6,1)];
		%% Print out user selected threshold values
		fprintf(2,'<strong>\nFilter Inputs\n</strong>')
		fprintf('<strong>hue_min\thue_max\tval_min\tval_max\tdia_min\tdia_max</strong>\n')
		fprintf('%.3f\t%.3f\t%.3f\t%.3f\t%5d\t%5d\n',min(hue_thr),...
			    max(hue_thr),min(val_thr),max(val_thr),min(dia_thr),max(dia_thr))	
	%% Create Black and White Image based on hue thresholds
	% Extract hue data from input
	imHue = imHSV(:,:,1);
	
	% Segment hue data based on thresholds
	imBW_c = (imHue > min(hue_thr)) & (imHue < max(hue_thr));
	
	% Visualize Image
	figure(4)
	clf
	nexttile
	imshow(imBW_c)
	title('Hue Filter')
	
	%% Create Black and White Image based on value thresholds
	% Extract value data from input
	imVal = imHSV(:,:,3);
	
	% Segment hue data based on thresholds
	imBW_v = (imVal > min(val_thr)) & (imVal < max(val_thr));
	
	% Visualize Image
	nexttile
	imshow(imBW_v)
	title('Value Filter')
	
	%% Combine hue and value BW images into new BW image
	imBW_hv = imBW_c & imBW_v;
	
	% Visualize Image
	nexttile
	imshow(imBW_hv)
	title('Hue & Value Filters')
	
	%% Create hue, value and size filtered BW image
	% Calculate min/max area
	area_thr = floor(pi*(dia_thr/2).^2);
	area_thr = reshape(area_thr,[1 2]);
	
	% Remove smaller or larger objects based on area thresholds
	BW_hva = bwareafilt(imBW_hv,area_thr);
	
	% Visualize Image
	nexttile
	imshow(BW_hva)
	title('Hue, Value & Size Filters')
end