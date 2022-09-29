%Script combines the scripts from previous functions and outputs results.

%clears all the parameters and limits to the function
clear;

%the outputs coming from functions 1 and 2 will be used as inputs for
%functions 3 and 4. Successfully generate all output variables
[imHSV, imRGB, img_file]= ca4_fun1;

purple = [0.75, 0.85; 0.3, 0.45; 10, 40];
lightgreen = [0.25, 0.45; 0.95, 1; 10, 40];
allgreen = [0.25, 0.45; 0, 1; 0, 200];
largegreen = [0.25, 0.45; 0, 1; 50, 200];
brightblue = [0.55, 0.75; 0.75, 0.9; 0, 200];
allblue = [0.55, 0.75; 0, 1; 0, 200];
yellow = [0.15, 0.25; 0.9, 1; 0, 200];
orange = [0.05, 0.15; 0.9, 1; 0, 200];
filt_opts = {allgreen, lightgreen, largegreen, allblue, brightblue, yellow, purple, orange};


[BW_out, BW_123] = ca4_fun2(imHSV, filt_opts);

%Change BW_out to imBW_in so it can be recognized by the input for function
%3
imBW_in=BW_out;

[S_clr, dt_out] = ca4_fun3(imBW_in);

%Formatted output created using all the outputted values from functions 1,
%2, and 3; 'Filename, a (N), b (sec), c (N), y_mae (N)'
fprintf('%s \t %.3f (N) \t %.3f (N) \t %.3f (N) \t %.3f (N)', number, mindia, maxdia, avgdia, stddia);