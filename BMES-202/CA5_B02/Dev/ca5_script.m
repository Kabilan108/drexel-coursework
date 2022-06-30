%% ca5_script   - script for end user
    %  Author: Everyone
    %  Team:   B02
    %  Date:   11/2/2020
%% Use your code (functions 1 -> 3), to analyze ‘green’ objects, being sure to store the final output diameter for green (G_dia).  {You and your team will have to decide on the proper filter thresholds}
clear;
%--- Clears all existing parameters.

[imHSV, imRGB, img_file] = ca5_fun1;
%--- Prompts udswer to select an image file in order to give an input.

[BW_hva] = ca5_fun2(imHSV);
%--- This function takes in image HSV data, and filter parameters and
%    returns filtered images based on the parameters, and the parameters
%    can be given by the user. There is also a suggested value filled in by
%    default.

[d_obj, S_obj] = ca5_fun3(BW_hva);
%--- We need the diameter which is the d_obj.
G_dia = d_obj;


%% Use your code (functions 1 -> 3), to analyze ‘ORANGE’ objects, being sure to store the final output diameter for orange (O_dia)

%--- Clears all existing parameters.

[imHSV, imRGB, img_file] = ca5_fun1;
%--- Prompts udswer to select an image file in order to give an input.

[BW_hva] = ca5_fun2(imHSV);
%--- This function takes in image HSV data, and filter parameters and
%    returns filtered images based on the parameters, and the parameters
%    can be given by the user. There is also a suggested value filled in by
%    default.

[d_obj, S_obj] = ca5_fun3(BW_hva);
%--- We need the diameter which is the d_obj.
O_dia = d_obj;

%% Based on these outputs, determine if the diameters of the ‘green’ (not infected cells) and ‘orange’ (infected) cells are different using the matlab function (ttest2, where the inputs would be G_dia, O_dia, 1-tailed, and ‘assume equal variance’, and a p<.005 as being significant)
[h, p] = ttest2(G_dia, O_dia, 'Alpha', 0.005, 'Tail', 'right');

%% Report to the command line:  p-value (#.###) (sprintf, disp)   
fprintf('P-value = %.4f', p);

return
