function [BW_out, BW_123] = ca4_fun2(imHSV, filt_opts)
  %% DESCRIPTION (filter image)
	%    This function takes in image HSV data, and filter parameters and
	%    returns filtered images based on the set parameters.
	%  INPUT
	%    imHSV -> [MxNx3] containing image HSV data
	%    filt_opts -> [3x2] filtering options
	%              -> row1 - min/max color
	%              -> row2 - min/max value
	%              -> row3 - min/max diameter
	%  OUTPUT
	%    BW_out -> [MxN] matrix with 'final' filtered image
	%    BW_123 -> [MxNx3] B/W images (1 - hue; 2 - value; 3 - size)
	%  ----------------------------------------------------------------------
	%  Author: Vrigav Narra, Tony Okeke
	%  Team:   B02
	%  Date:   10/28/2020

	%% Prompt the User to provide Filter Options if None were provided
	if ~exist('filt_opts','var')
		%% Prompt User to select Color Range from appropriate colorbar
		uiwait(msgbox('Please Select Start and End Points for the Color Range'))
		fig = figure(4);
		clf(fig)
		ax = axes;
		
		% Adjust plot settings
		fig.Position = [597   407   282   420];
		pos = [0.3 0.06 0.4 0.9];
		colormap hsv;
		colorbar(ax,'Position',pos);
		ax.Visible = 'off';
		ylim([0,1])
		
		% Collect Color Filter start and end points from user
		[~,y] = ginput(2);
		hue_thr = y;
		
		%% Prompt User to select 'Value' Range for filter from colorbar 2
		uiwait(msgbox('Please Select Start and End Points for the Value Range'))
		clf(fig)
		ax = axes;
		
		% Adjust plot settings
		fig.Position = [597   407   282   420];
		pos = [0.3 0.06 0.4 0.9];
		colormap hot;
		colorbar(ax,'Position',pos);
		ax.Visible = 'off';
		ylim([0,1])
		
		% Collect Value Filter Start and end points from user
		[~,y] = ginput(2);
		val_thr = y;
		
		% Close figure
		close(fig)
		
		%% Prompt User to Provide 'Size' Range for filter
		prompt = {'Minimum Diameter:','Maximum Diameter:'};
		dialogTitle = 'Filter Size Range';
		dims = [1 25];
		definput = {'10','1000'};
		siz_thr = str2double(inputdlg(prompt,dialogTitle,dims,definput));
		
		%% Print out user selected threshold values
		fprintf(2,'<strong>\nFilter Inputs\n</strong>')
		fprintf('<strong>hue_min\thue_max\tval_min\tval_max\tdia_min\tdia_max</strong>\n')
		fprintf('%.3f\t%.3f\t%.3f\t%.3f\t%5d\t%5d\n',min(hue_thr),...
			    max(hue_thr),min(val_thr),max(val_thr),min(siz_thr),max(siz_thr))
	else
		hue_thr = filt_opts(1,:);
		val_thr = filt_opts(2,:);
		siz_thr = filt_opts(3,:);
	end
	
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
	area_thr = floor(pi*(siz_thr/2).^2);
	area_thr = reshape(area_thr,[1 2]);
	
	% Remove smaller or larger objects based on area thresholds
	BW_out = bwareafilt(imBW_hv,area_thr);
	
	% Visualize Image
	nexttile
	imshow(BW_out)
	title('Hue, Value & Size Filters')
	
	% Create Output Arry
	BW_123(:,:,1) = imBW_c;
	BW_123(:,:,2) = imBW_v;
	BW_123(:,:,3) = imBW_hv;
end