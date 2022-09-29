function [BW_hva, BW_123] = ca6_fun2(imHSV)
  %% DESCRIPTION (filter image)
	%    This function takes in image HSV data, and returns filtered images 
	%    based on the set parameters.
	%  INPUT
	%    imHSV -> [MxNx3] containing image HSV data
	%  OUTPUT
	%    BW_hva -> [MxNx3] matrix containing 'final' b/w images (combo
	%              filter, value filter & color filter)
	%  ----------------------------------------------------------------------
	%  Authors: Jessica Baggett
	%           Vrigav Narra
	%           Tony Okeke
	%           Jackie Tang
	%  Team: B02
	%  Date: 11/9/2020
	
	%% Prompt User to enter Filter Parameters
	% Dialog box parameters
	prompt = {'Minimum Hue:','Maximum Hue:','Minimum Value:',...
		        'Maximum Value:','Minimum Diameter:','Maximum Diameter:'};
	dialogTitle = 'Filter Parameters';
	dims = [1 30];
	% Filter ranges: 
	%   Green:  [0.25, 0.45, 0.25, 0.6, 5, 1000] (Default)
  %   Orange: [0, 0.15, 0.6, 1, 5, 1000]
	definput = {'0.25','0.45','0.25','0.6','1','1000'};
	filt_thr = str2double( inputdlg(prompt, dialogTitle, dims, definput) );
	
	% Extract specific filter thresholds
	hue_thr = filt_thr(1:2);
	val_thr = filt_thr(3:4);
	dia_thr = filt_thr(5:6);
	
	%% Print out user selected threshold values
	fprintf(2,'<strong>\nFilter Inputs\n</strong>')
	fprintf('<strong>hue_min\thue_max\tval_min\tval_max\tdia_min\tdia_max</strong>\n')
	fprintf('%.3f\t%.3f\t%.3f\t%.3f\t%5d\t%5d\n',min(hue_thr),...
	        max(hue_thr),min(val_thr),max(val_thr),min(dia_thr),max(dia_thr))	

	%% Create Black and White Image based on hue thresholds
	% Extract hue data from input
	imHue = imHSV(:,:,1);
	
	% Segment hue data based on thresholds
	if abs(diff(hue_thr)) > 0.5
		BW_h = (imHue < min(hue_thr)) | (imHue > max(hue_thr));
	else
		BW_h = (imHue > min(hue_thr)) & (imHue < max(hue_thr));
	end
	
	% Visualize Image
	figure(4)
	clf
	nexttile
	imshow(BW_h)
	title('Hue Filtered Image')
	
	%% Create Black and White Image based on value thresholds
	% Extract value data from input
	imVal = imHSV(:,:,3);
	
	% Segment hue data based on thresholds
	BW_v = (imVal > min(val_thr)) & (imVal < max(val_thr));
	
	% Visualize Image
	nexttile
	imshow(BW_v)
	title('Value Filtered Image')
	
	%% Combine hue and value BW images into new BW image
	imBW_hv = BW_h & BW_v;
	
	% Visualize Image
	nexttile
	imshow(imBW_hv)
	title('Hue & Value Filtered Image')
	
	%% Create hue, value and size filtered BW image
	% Calculate min/max area
	area_thr = sort( floor(pi*(dia_thr/2).^2) )';
	
	% Remove smaller or larger objects based on area thresholds
	BW_hva = bwareafilt(imBW_hv,area_thr);
	
	% Visualize Image
	nexttile
	imshow(BW_hva)
	title('Hue, Value & Size Filtered Image')
	
	% Create Output Array
    
    BW_123 = [];
    
	BW_123(:,:,1) = BW_h;
	BW_123(:,:,2) = BW_v;
	BW_123(:,:,3) = imBW_hv;
end