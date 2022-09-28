function [imHSV, imRGB, img_file]= ca4_fun1(img_file)
%Jackie Tang
%Takes an input image file and shows it. Converts the original rgb image
%file into a HSV image file and plots the Hue and Value in separate
%figures, using the 'HSV', and 'hot' colormap with a color axis from 0-1.

% If file name not provided by user, prompt user to select a file
if (nargin<1)
	%promput user to select file
	[file_name, pth] = uigetfile('*.PNG', 'Choose Image file', 'default.PNG');
	%join file name and path
	png_file = fullfile(pth, file_name);
else
	fprintf('using given filename: %',png_file)
end

%Read the image file
imRGB = imread(png_file);

%Plot the original image
figure
imagesc(imRGB);
colorbar
title('Original Image')

%Convert from RGB to HSV
imHSV = rgb2hsv(imRGB);
%Create separate image matrices of only the Hue
imH = imHSV(:,:,1);
%Create a separate image matrices of only the Value
imV = imHSV(:,:,3);

%Plot the Hue image with a "HSV" colormap and color axis from 0-1
figure
imagesc(imH);
colormap HSV;
caxis([0,1]);
title('Hue Image')
colorbar

%Plot the Hue image with a "hot" colormap and color axis from 0-1
figure
imagesc(imV);
colormap hot
caxis([0,1]);
title('Value Image')
colorbar

img_file = png_file;
end