function [d_obj, S_obj] = ca5_fun3(BW_hva)  %[analyze blobs] 
% DESCRIPTION
%   This function takes in a 'filtred' BW image and returns a structure 
%   containing results for object analysis, and the estimated diameter (in
%   pix_ of all objects found.
% INPUT: 
%   BW_hva -> [MxN] matrix with 'final' logical image (hue, value & area)
% OUTPUT: 
%   d_obj -> [Mx1] “estimated” diameter (in pix) of all objects found 
%   S_obj -> [Mx1] Structure results for object analysis (for a given input)
% -------------------------------------------------------------------------
% By Jessica Baggett, Vrigav Narra, Tony Okeke, & Jackie Tang
% Team: B02
% Date: 11-2-2020

%% Create label image [im_L]
im_L = bwlabel(BW_hva);

% Visualize Image
figure(5)
clf
imshow(im_L)
title('Filtered Image')

%% Determine Function Outputs
% Determine object analysis struct
S_obj = regionprops(im_L);

% Calculate Equivalent Diameters for all objects in the filtered image
d_obj = sqrt( [S_obj.Area]*4/pi );

%% Prepare Formatted Output
% find the number of elements in S_obj
n = numel(S_obj);

% Calculate the mean
avgDia = mean(d_obj);

% caclulate the standard diviation
stdDia = std(d_obj);
 
%% Report to the command line:  
fprintf('\n')
fprintf('<strong>Number of Objects\tAverage Diameter\tStd-Dev Diameter</strong>\n')
fprintf('%12.3f\t%15.3f\t%19.3f\n',n,avgDia,stdDia)

end