function [S_clr, dt_out] = ca4_fun3(imBW_in) % [Analyze objects in BW image] 
%% INPUT: a) imBW_in [MxNx1] - ‘final’ filtered image (MxN) [hue&value&size]
%% OUTPUT: a) S_clr – Structure results for object analysis (for a given input), b) dt_out - object summary (n, min eq.dia, max eq.dia, avg eq.dia, stddev eq.dia)
%% Create label image [im_L] using the bwlabel function (where the inputs would be the size filtered BW image [BW_sz]) and display label image in figure 5
BW_sz=
im_L=bwlabel(
colorbar;
%% Determine the areas of all objects in the BW labeled image (im_L) using the function regionprops to get the area of all objects (the output of that function should be a structure, S_clr)
S_object=regionprops(im_L);

%% Use the structure [S_clr] to calculate the equivalent diameters (sqrt(area*4/pi)) for all objects in the structure, and summarize the statistics (dt_out = # objects, min dia, max dia, avg dia, sd dia)

%% Report, in a formatted string (sprintf, disp) to the command line, a summary of the objects:  number, min dia, max dia, average diameter, std-dev diameter

dt_out=sprintf(

end 