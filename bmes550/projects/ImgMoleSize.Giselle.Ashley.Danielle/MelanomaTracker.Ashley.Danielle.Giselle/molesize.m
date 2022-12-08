%% molesize.m
% This function will evaluate size of mole image uploaded. 
% Inputs to this function will include the RGB image matrix information. 
% Its output will be the diameter of the mole which is provided to molechanges.db (mole_info table).

function  [risk, diameter] = molesize(file)
diameter=[];
risk=[];
%% Extract Image from File Path
%% Read Image
img=imread(file);   % RGB matrix
figure(1)
imshow(img)
 title('Original Image')
%% Detect Edges of Mole  
% edgethreshold=0.9;
% amount=0.3;
% contrastimg = localcontrast(img,edgethreshold,amount);                   
% grayimg=rgb2gray(contrastimg);                                  % converts to grayscale image.
% sharpimg=imsharpen(grayimg,'Amount',2);                         % imsharpen sharpens the grayscale image by using the unsharp masking method. 
% inccontrast=imadjust(sharpimg);                                 % imadjust saturates the bottom 1% and the top 1% of all pixel values. This operation increases the contrast of the output image J
% binaryimg=imbinarize(inccontrast);                              % imbinarize replaces all values above a globally determined threshold with 1s and setting all other values to 0s.
% binaryimg=bwmorph(binaryimg,'diag',1000);
% edgeimg=bwmorph(binaryimg,'fill',1000);                       % bwmorph 'fill' fills isolated interior pixels and applies it 1000 times

grayimg=rgb2gray(img);                                      % converts to grayscale image.
binaryimg=imbinarize(grayimg);                          % imbinarize replaces all values above a globally determined threshold with 1s and setting all other values to 0s.
edgeimg=bwmorph(binaryimg,'diag',1000);
edgeimg=bwmorph(edgeimg,'fill',1000);                   % bwmorph 'fill' fills isolated interior pixels and applies it 1000 times
% edgeimg=edge(edgeimg,'sobel',0.04);
edgeimg= edge(edgeimg,'canny',[0.5 0.8]);                    % Finds edges at those points where the gradient of the image I is maximum, using the Sobel approximation to the derivative and determines threshold value.
edgeimg=edge(edgeimg,'canny',0.05); 

%  figure(2)
%  imshow(edgeimg)
%  title('Edge Image')
%% Dilate the Edges of the Mole
se90 = strel('line',1,90);                              
se0 = strel('line',1,0);
dilatedimg=imdilate(edgeimg,[se90 se0]);                % Dilates in the 90 degree and 0 degree direction with a length of 1
dilatedimg=bwmorph(dilatedimg,'spur',1000);             % bwmorph 'spur' removes random pixels jutting out
dilatedimg=bwmorph(dilatedimg,'fill',10000);            % bwmorph 'fill' fills isolated interior pixels
dilatedimg=bwmorph(dilatedimg,'diag',10000);            % bwmorph 'diag' fills corner pixels

%  figure(3)
%  imshow(dilatedimg)
%  title('Dilated Image')
%% Fill in the Holes Created by Edges
filledimg=imfill(dilatedimg,4,"holes");                    % Determines if 'holes' with connectivity pattern of 4 are holes and fills them in.
filledimg=bwmorph(filledimg,'fill',10000);                 % bwmorph 'fill' fills isolated interior pixels
filledimg=bwmorph(filledimg,'diag',10000);                 % bwmorph 'diag' fills corner pixels

%  figure(4)
%  imshow(filledimg)
%  title('Filled Image')
%% Remove Small Objects
cleanedimg = bwareaopen(filledimg,400);
% cleanedimg = bwareaopen(filledimg,900);

% figure(5)
% imshow(cleanedimg)
% title('Isolated Mole Image')

overlayimg=imfuse(cleanedimg,img);
figure()
imshow(overlayimg)
title('Your Mole')

saveas(gcf, [file '.overlay.jpg']);
%% Get Diameter
stats = regionprops(cleanedimg,'MajorAxisLength');
diameterinpixels = ([stats.MajorAxisLength]);
diameter=(diameterinpixels)*0.0615;                     % Ratio is the ratio of mm/pixels based on the 'aftermelanoma.jpg' image (source: https://www.skincancer.org/skin-cancer-information/melanoma/melanoma-warning-signs-and-images/)
%% Evaluate Risk
% Thresholds determined to be low (<6mm), moderate (between 6-8mm), and high (greater than 8mm)
% Source: https://www.cancer.gov/types/skin/moles-fact-sheet#:~:text=There%20is%20a%20change%20in,past%20few%20weeks%20or%20months. 
% Source: https://www.skincancer.org/risk-factors/atypical-moles/#:~:text=People%20with%20atypical%20mole%20syndrome,One%20or%20more%20atypical%20moles 
if diameter<=6
    risk='Low';
elseif diameter>6 & diameter<8
    risk='Moderate';
elseif diameter>=8
    risk='High';
end





