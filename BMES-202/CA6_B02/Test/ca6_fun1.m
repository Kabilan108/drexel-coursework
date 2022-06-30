function [imHSV, imRGB, img_file] = ca6_fun1(img_file)
%% DESCRIPTION (Import & Convert Data)
%    This function imports image data, visualizes it, and converts it from
%    RGB to HSV data. It also visualizes the eu and Value Channels of the
%    image.
%  INPUT
%    img_file -> [1xN] string containing full image file name
%    * function can be called with no inputs
%  OUTPUT
%    imHSV    -> [MxNx3] array containing HSV data
%    imRGB    -> [MxNx3] array containing RGB data
%    img_file -> [1xN] string containing full image file name
%  ------------------------------------------------------------------------
%  Author: Tony Kabilan Okeke
%          Jessica Baggett
%          Vrigav Narra
%          Jackie Tang
%  Team: B02
%  Date: 11/10/2020

%% Prompt User to select file if none was provided
   if ~exist('img_file','var') || ~exist(img_file,'file') %-- no file provided
		 %% Set default name to be the file the user previously selected. 
		 %  Assuming the previously selected file name is stored in the
		 %  'FileName' handle of the figure tagged 'Original Object'
		 defname = get( findobj('Tag','Original Image'), 'FileName' );
		 if ~isempty(defname) %-- if a file was found, combine it appropriately
			 [~,fnm,ext] = fileparts(defname);
			 defname = [fnm ext];
		 end
		 
		 %% Prompt User to select file
		 [fnm, pth] = uigetfile('*.jpg','Please Select Image File',defname);
		 
		 %% Combine fnm & pth
		 img_file = fullfile(pth,fnm);
	 else %-- the file was provided as a function input
		 [~,fnm] = fileparts(img_file);
		 %-- extact file name from input for storage in image handles
	 end
	 
%% Read & Visualize RGB data from File
   imRGB = imread(img_file);
	 
	 % Visualize Data in Figure 1 & Store File Name & Tag
	 fig = figure(1);
	 fig.Name = fnm;
	 fig.Tag = 'Original Image';
	 fig.FileName = img_file;
	 imagesc(imRGB)
	 title('Original Image')
	 
%% Convert RGB data to HSV & Visualize the Hue & Value Channels
   imHSV = rgb2hsv(imRGB);
	 imHue = imHSV(:,:,1);
	 imVal = imHSV(:,:,3);
	 
	 % Visualize Hue Channel & Store Tag
	 fig = figure(2);
	 fig.Name = ['Hue Channel: ' fnm];
	 fig.Tag = 'Hue Channel';
	 imagesc(imHue)
	 title('Hue Channel')
	 colormap hsv;
	 colorbar;
	 caxis([0 1]);
	 
	 % Visualize Value Channel & Store Tag
	 fig = figure(3);
	 fig.Name = ['Value Channel: ' fnm];
	 fig.Tag = 'Value Channel';
	 imagesc(imVal);
	 title('Value Channel')
	 colormap hot;
	 colorbar;
	 caxis([0 1])
	 
end