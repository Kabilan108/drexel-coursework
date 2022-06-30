%% Master SCRIPT / System Check
% Description
%   This script returns the file, slope, and fit error of the data based on
%   fuction 1 that produces numeric data in a matrix and labels describing
%   that data. This then gets put into function 2 which outputs
%   numeric data of segmented linear data. Finally, the numeric data of
%   segmented linear data is the input for function 3 which then outputs
%   the stiffness of the material and average-absolute-error between the 
%   linear model and data.
%--------------------------------------------------------------------------
% Author: Gabriella Grym
% Date:   09.30.2020
% Team:   A_03

%% Clear all variables
clear variables

%% Import & Visualize Data (ca2_fun1)
%     data - [M1 x N1] numeric data matrix
%     col_lbls - labels describing data contained within columns
%     csv_file - path and file name
[data, col_lbls, csv_file] = ca2_fun1();

%% Data Segmentation (ca2_fun2)
%     dt_linear - numeric data of segmented linear data
[dt_linear] = ca2_fun2(data, col_lbls);

%% Data Analysis (ca2_fun3)
%     kel - stiffness of the material
%     y_err - average-absolute-error between linear model and data
[Kel, y_err] = ca2_fun3(dt_linear);

%% Get file name
[~,file,~] = fileparts(csv_file);

%% Provide Formatted Output
% Display output in a way that the client can copy and paste it into excel.
% Since they did not specify significant digits, provide 2, 3, and 4 for
% their choosing.

txt = ['<strong>      File Name  \t   Slope (N/mm)  \t    Fit-Error (N)'...
	     '</strong>\n%s\t%15.3f\t%21.3f\n'];
fprintf(txt, file, Kel, y_err);