function [imHSV, imRGB, img_file] = ca5_fun1(img_file)

% Everyone
% TEAM B02
% Takes an input image file and shows it. Converts the original rgb image
% file into a HSV image file and plots the Hue and Value in separate
% figures, using the 'HSV', and 'hot' colormap with a color axis from 0-1.
%  INPUT
%    img_file -> [1xN] string containing full image file name
%    function can be called with no inputs
%  OUTPUT
%    imHSV -> [MxNx3] matrix containing image H-S-V data
%    imRGB -> [MxNx3] matrix containing imahe R-G-B data
%    img_file -> [1xN] string containing full image file name


% If file name not provided by user, prompt user to select a file
if (nargin<1)
	%promput user to select file
	[file_name, pth] = uigetfile('*.jpg', 'Choose Image file', 'default.jpg');
	%join file name and path
	img_file = fullfile(pth, file_name);
end

%Read the image file
imRGB = imread(img_file);

%Plot the original image
fig1 = figure(1);
clf(fig1)
imagesc(imRGB);
title('Original Image')
colorbar

%Convert from RGB to HSV
imHSV = rgb2hsv(imRGB);
%Create separate image matrices of only the Hue
imH = imHSV(:,:,1);
%Create a separate image matrices of only the Value
imV = imHSV(:,:,3);

%Plot the Hue image with a "HSV" colormap and color axis from 0-1
fig2 = figure(2);
clf(fig2)
imagesc(imH);
colormap HSV;
caxis([0,1]);
title('Hue Image')
colorbar;

%Plot the Value image with a "hot" colormap and color axis from 0-1
fig3 = figure(3);
clf(fig3)
imagesc(imV);
colormap hot
caxis([0,1]);
title('Value Image')
colorbar;

%Print Image Name to Command Window
fprintf('\nFile: %s\n',file_name)
return