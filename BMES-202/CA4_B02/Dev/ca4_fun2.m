function [BW_out, BW_123] = ca4_fun2(imHSV, filt_opts)
%--- Made by Vrigav Narra and team.
%--- Made on 10/28/2020

%% INPUT: a) imHSV [MxNx3] image (h-s-v) data, b) filt_opts [3x2] filtering options (row1 = min/max colr, row2 = min/max value, row3  = min/max diameter)

im_hue = imHSV(:,:,1);
im_val = imHSV(:,:,3);

%% OUTPUT: a) BW_out [MxN] ‘final’ filtered image; b) im123 [MxNx3] B/W images (1=hue, 2=value,3=size)


%% From the filter options input (filt_opts), create a variable for the hue thresholds [hue_thr], and use these hue thresholds in combination with logical operators to create a black/white image [imBW_c] based on a particular hue  (look at the colorbar from figure 2 to choose the hue threshold)
% purple = [0.75, 0.9; 0.3, 0.45; 10, 60];
% lightgreen = [0.25, 0.45; 0.95, 1; 10, 40];
% allgreen = [0.25, 0.45; 0, 1; 0, 200];
% largegreen = [0.25, 0.45; 0, 1; 50, 200];
% brightblue = [0.55, 0.75; 0.75, 0.9; 0, 200];
% allblue = [0.55, 0.75; 0, 1; 0, 200];
% yellow = [0.15, 0.25; 0.9, 1; 0, 200];
% orange = [0.05, 0.15; 0.9, 1; 0, 200];
% filt_opts = {allgreen, lightgreen, largegreen, allblue, brightblue, yellow, purple, orange};


figure
tiledlayout(2,2);

color=filt_opts{1,1};
thr= color(1,:);

nexttile
bwh = (im_hue > thr(1,1) & im_hue < thr(1,2));
imshow(bwh)
title('Hue Filtered')

%% From the filter options input (filt_opts), create a variable for the value thresholds [hue_thr], and use these thresholds in combination with logical operators to create a black/white image [imBW_v] based on a particular hue  (look at the colorbar from figure 3 to choose the hue threshold)

nexttile
bwv = (im_val > filt_opts(2,1) & im_val < filt_opts(2,2));
imshow(bwv)
title('Value Filtered')

%% Combine the hue and value BW image into a new BW image (imBW_hv) and calculate the min/max area based on the min/max diameters (filt_opts)

nexttile
imBW_hv = (bwh & bwv);
imshow(imBW_hv)
title('Hue & Value Filtered')


%% Remove small/large objects (BW_out) from this combined image by using bwareafilt function (where the inputs should be: the ‘combo’ imBW_hv, as well as, the min/max areas)

ar_min = round(pi*(filt_opts(3,1)^2));
ar_max = round(pi*(filt_opts(3,2)^2));

BW = bwareafilt(imBW_hv, [ar_min ar_max]);

%% In figure 4, visualize the four b/w image images for:  a) hue filter, b) value filter, c) hue & value filter, d) hue & value & size filter

nexttile
imshow(BW)
title('Hue, Value, & Size Filtered')

%% Combine the 3 BW images into a 3D array (BW_123(:,:,1) = hue, BW_123(:,:,2) = value, BW_123(:,:,3) = hue&value)

BW_123(:,:,1) = bwh;
BW_123(:,:,2) = bwv;
BW_123(:,:,3) = imBW_hv;
end