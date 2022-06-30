function [dt_pos, S_obj] = ca6_fun3(BW_hva)
  %% DESCRIPTION (filter image)
	%    This function takes in 'filtered image HSV data, and returns  
	%    the position and structure results of the image.
	%  INPUT
	%    imBW_in [MxNx1] - ‘final’ logical image (MxN) [hue&value&size]
	%  OUTPUT
	%    a) dt_pos - [1x2] x,y position of object, b) S_obj – Structure results for object analysis (for a given input)
	%  ----------------------------------------------------------------------
	%  Authors: Jessica Baggett
	%           Vrigav Narra
	%           Tony Okeke
	%           Jackie Tang
	%  Team: B02
	%  Date: 11/9/2020

%% Visualize the labeled objects as an image [imL] in figure 5, (bwlabel) {where the inputs would be the size filtered BW image [BW_sz]}
im_L = bwlabel(BW_hva);

%% Determine the centroid of an object in the labeled image [im_L] (regionprops)
S_obj = regionprops(im_L, 'centroid');

%% Provide centroid position (x,y) as your function output and report position to the command line in a formatted string (sprintf, disp)
dt_pos= S_obj.Centroid ;

fprintf( '%.3 \t %.3', dt_pos)
end

