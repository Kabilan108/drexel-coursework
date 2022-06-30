function [d_obj, S_obj] = ca5_fun3(BW_hva)  %[analyze blobs] 
%By Jessica Baggett, Vrigav Narra, Tony Okeke, & Jackie Tang
%11-2-2020
 %This function takes in a 'filtred' BW image and returns a structure containing results for object analysis, and an object summary
%% INPUT: a) BW_hva [MxN] - final logical image (hue & value & area)
%BW_hva -> [MxN] matrix with 'final' filtered image
%% OUTPUT: a) d_obj [Mx1] “estimated” diameter (in pix) of all objects found, b) S_obj [Mx1]– Structure results for object analysis (for a given input)
%S_obj  -> Struct containing results for object analysis
%d_obj  -> Matrix with esitmated diameters of all objects found in BW_hva
%% Create label image [im_L] using the bwlabel function (where the inputs would be the input logical image [BW_hva]) and display label image in figure 5
%Create Label Image
im_L = bwlabel(BW_hva);

% Visualize Image
figure(5)
imshow(im_L)
title('Filtered Image')

%% Determine the areas of all objects in the labeled image (im_L) using the function regionprops  (the output of that function should be a structure, S_obj)

% Determine object analysis struct
S_obj = regionprops(im_L);

%% Use the structure [S_obj] to calculate the equivalent diameter (sqrt(area*4/pi)) for all objects in the structure

% Calculate Equivalent Diameters using the circle area equation
eqDia = sqrt( [S_obj.Area]*4/pi );

%% Extract the area of the objects, calculate the equivalent diameter into a vector [d_obj] and output

d_obj=transpose(eqDia);
%rotate the matrix eqDia because it was in the wrong format

% Prepare Output struct
n = numel(S_obj);
%finds the number of elements in S_obj
avgDia=mean(eqDia);
%Calculate the mean
stdDia=std(eqDia);
%caclulate the standard diviation 

%% Report to the command line:  number of objects, diameter average, diametre standard deviation in a formatted string (sprintf, disp)

fprintf('%12.3f\t%16.3f\t%15.3f\n',n,avgDia,stdDia)

end

