%% Master Script 
% Description 
% reads a data file, fits the hold-portion of the load-data  to the 
% following equation, L(t)= A exp ((-1/B) * t) + C 
% Where L(t) is the load at any time t, and A, B and C are the parameters 
% outputs the results    
% -------------------------------------------------------------------------
% Author: Benjamin Jennings
% Date:   10.13.2020
% Team:   A_03

%% Clear all variables
clear variables

%% Use outputs of function 1-2, as inputs for functions 3-4 
% to generate all necessary output variables

% Run Function 1 & Store Output
%   OUTPUT:
%     Data: [Mx3] numeric numbers
%     ax_lbl:[1x3] cell array of axis labels 
%     csv_file: [1xN] string array (path & file name)
[data,ax_lbl, csv_file] = ca3_fun1();
            
% Run Function 2 & Store Output
%   OUTPUT:
%     dt_hold: [Mx3] numeric matrix that contains data
[dt_hold] = ca3_fun2(data,ax_lbl);
            
% Run Function 3 using output from functions 1 & 2
[fit_params,y_est,y_mae] = ca3_fun3(dt_hold,ax_lbl);

%% Use output from functions 1-3 to create a formatted output

% Extract File Name from csv_file
[~,file,~] = fileparts(csv_file);

% (sprintf, disp):  'Filename, a (N), b (sec), c (N), y_mae (N)'
% creates header for the values printed next 
fprintf(['\n<strong> File Name           \t A (N) \t B (sec) \t C (N) '...
	       '\t y_mae \n</strong> '])

% Prints values of a, b, c, and y_mae using the outputs from function 3 
% for the user 
fprintf('%s\t%6.3f\t%8.3f\t%6.3f\t%6.3f\n\n',file, fit_params , y_mae)

