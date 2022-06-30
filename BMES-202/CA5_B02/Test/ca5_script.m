%% ca5_script - Script for end user
%  Authors: Jessica Baggett
%           Vrigav Narra
%           Tony Okeke
%           Jackie Tang
%  Team: B02
%  Date: 11/2/2020

%% Clears all existing parameters.
clear;

%% Prompt User to Select Image File
[imHSV, imRGB, img_file] = ca5_fun1;

%% Analyze 'Green' Objects
% Prompt the user to input thresholds for green objects
uiwait( msgbox("Please Input Thresholds For 'Green' Objects") )

% Print current color on command window
fprintf('\n(Green)')

[BW_hva] = ca5_fun2(imHSV);
%--- This function takes in image HSV data, and filter parameters and
%    returns filtered images based on the parameters, and the parameters
%    can be given by the user. There is also a suggested value filled in by
%    default.

[G_dia, S_obj.Green] = ca5_fun3(BW_hva);
%--- G_Dia -> contains the equivalent diameters for green objects
%--- S_obj.Green -> Structure Containing object analysis data

%% Analyze 'Orange' Objects
% Prompt the user to input thresholds for orange objects
uiwait( msgbox("Please Input Thresholds For 'Orange' Objects") )

% Print current color on command window
fprintf('\n(Orange)')

[BW_hva] = ca5_fun2(imHSV);
%--- This function takes in image HSV data, and filter parameters and
%    returns filtered images based on the parameters, and the parameters
%    can be given by the user. There is also a suggested value filled in by
%    default.

[O_dia, S_obj.Orange] = ca5_fun3(BW_hva);
%--- O_Dia -> contains the equivalent diameters for orange objects
%--- S_obj.Orange -> Structure Containing object analysis data

%% Perform Statistical Analysis
% Based on these outputs, determine if the diameters of the ‘green’ 
% (not infected cells) and ‘orange’ (infected) cells are different using 
% the matlab function (ttest2, where the inputs would be G_dia, O_dia, 
% 1-tailed, and ‘assume equal variance’, and a p<.005 as being significant)

[h,p] = ttest2(G_dia, O_dia, 'Alpha', 0.005, 'Tail', 'right', 'Vartype', 'equal');

%% Report to the command line:  p-value (#.###) (sprintf, disp)   
fprintf('\n<strong>p-value: </strong>%.3f\n', p);