function [BW_hva, BW_123] = ca6_fun2(imHSV,filt_opts)
%% DESCRIPTION (Filter Image)
%    This function takes image HSV data and filters out objects based on
%    the provided filter options
%  INPUT
%    imHSV -> [MxNx3] array containing HSV data
%    filt_opts -> [3x2] matrix containing filtering options
%        (1,:) -> min & max hue
%        (2,:) -> min & max value
%        (3,:) -> min & max diameter
%  OUTPUT
%    BW_out -> [MxN] matrix containing 'final' filtered image
%    BW_123 -> [MxNx3] matrix containing logical images
%              (1 -> hue; 2 -> value; 3 -> size)
%  ------------------------------------------------------------------------
%  Author: Tony Kabilan Okeke
%          Jessica Baggett
%          Vrigav Narra
%          Jackie Tang
%  Team: B02
%  Date: 11/10/202

%% Provide Input Dialog For User if Filter Options were not Provided
   if ~exist('filt_opts','var')
		 % Create the input dialog
		 prompt = {'Hue Min:','Hue Max:','Value Min:','Value Max:',...
			         'Diameter Min:','Diameter Max'};
		 dlgtitle = 'Filter Parameters';
		 dims = [1 35];
		 % default inputs would filter out all green objects
		 definput = {'0.25','0.42','0.5','1','10','1000'};
		 thr = str2double( inputdlg(prompt,dlgtitle,dims,definput) );
		 
		 % Extract thresholds from inputs
		 hue_thr = thr(1:2);
		 val_thr = thr(3:4);
		 dia_thr = thr(5:6);
	 else
		 % Extract thresholds from filt_opts
		 hue_thr = filt_opts(1,:);
		 val_thr = filt_opts(2,:);
		 dia_thr = filt_opts(3,:);
	 end
	 
	 % Calculate area thresholds (make sure its in ascending order (for
	 % bwareafilt)
	 area_thr = sort(reshape( pi * (dia_thr/2).^2 , [1 2]));
	 
	 % Extract hue & value data from imHSV
	 imHue = imHSV(:,:,1);
	 imVal = imHSV(:,:,3);
	 
%% Create Filtered Logical Images
	 % Hue Filtered Image
	 if hue_thr(1) > hue_thr(2) %---Red
		 BW_h = ( imHue > hue_thr(1) ) | ( imHue < hue_thr(2) );
	 elseif hue_thr(1) < hue_thr(2) %---Other Colors
		 BW_h = ( imHue > min(hue_thr) ) & ( imHue < max(hue_thr) );
	 end
	 
	 % Value Filtered Image
	 BW_v = ( imVal > min(val_thr) ) & ( imVal < max(val_thr) );
	 
	 % Combined Hue & Value Filtered Image
   BW_hv = BW_h & BW_v;
	 
	 % Remove smaller or larger objects based on area thresholds
	 BW_hva = bwareafilt(BW_hv,area_thr);
	 
%% Visualize Logical Images
	 fig = figure(4);
	 clf(fig)
	 
	 % Hue Filter
	 nexttile
	 imshow(BW_h)
	 title('Hue Filter')
	 
	 % Value Filter
	 nexttile
	 imshow(BW_v)
	 title('Value Filter')
	 
	 % Hue & Value Filter
	 nexttile
	 imshow(BW_hv)
	 title('Hue & Value Filter')
	 
	 % Hue, value & Size Filter
	 nexttile
	 imshow(BW_hva)
	 title('Hue, Value & Size Filter')

%% Combine BW images
   BW_123(:,:,1) = BW_h;
	 BW_123(:,:,2) = BW_v;
	 BW_123(:,:,3) = BW_hv;
	 
end