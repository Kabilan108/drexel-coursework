%Script combines the scripts from previous functions and outputs the final results produced in function 3.
%Jessica Baggett
%10-31-2020
%TEAM B02

%clears all the parameters and limits to the function
clear;

%Create original image, hue, and value plots
[imHSV, imRGB, img_file] = ca4_fun1;

% Filter Image based on user-selected filter parameters
% Some recommended user select values, categories like largegreen and 
% brightgreen are subjective to each user 
% purple = [0.75 0.95; 0.3 0.45; 10 80];
% lightgreen = [0.25 0.45; 0.60 1; 10 150];
% allgreen = [0.225 0.45; 0 1; 10 200];
% largegreen = [0.25, 0.45; 0, 1; 35, 200];
% brightblue = [0.55 0.75; 0.75 0.9; 0 200];
% allblue = [0.55 0.75; 0, 1; 0, 200];
% yellow = [0.15 0.25; 0.9 1; 0 200];
% orange = [0.05 0.15; 0.9 1; 0 200];
% (If no filter options are selected, the user will be prompted to select them)
[BW_out, BW_123] = ca4_fun2(imHSV);

%Analyze Image and Return Object Summary
[S_clr, dt_out] = ca4_fun3(BW_out);