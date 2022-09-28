function [data,ax_lbl, csv_file] = ca3_fun1(csv_file)
% Writen by Nick Corrado 10/16/2020 Group A_03 

% Description: This file gives the user the option on how to chose their
% data and the fuction will give back the data, titles (w/ units), and the
% choosen file for further use. The funtion will also give back 2 figures
% that are subplots of eachother. 

% Input: The input will be the chosen csv_file. The fuction can also take
% no input and will prompt the user to select a file.

% Output: The output will give the nessicary data in a numeric matrix to be further
% used. It will also give out the titles coorisoponding to each column. The selectd file
% will also be output for further use.
% 2 graphs of the data will also be output.

%% File Selection

if (nargin<1)
    % Have the user select file if one isn't given
    [fnm,pth] = uigetfile('*.CSV','Choose Data file');
    csv_file = fullfile(pth,fnm);
else
    %If there is a file, then prompt message
    disp('Using preselected file')
end 

%% Read string lines into matlab

% Open file
fID = fopen(csv_file);
% max times the while can loop
loop_max= 10000;
% starting count for loop
loop_count= 0;
% flag for while loop
flg_go=1;

% This while loop goes through the data so it can be read in matlab
while(flg_go)
    loop_count = loop_count + 1 ;
    txt_line = fgetl (fID);
    c_lines(loop_count,1) = {txt_line};
    if(txt_line == -1)
        flg_go= 0;
    else
        flg_go = (loop_count < loop_max);
    end
end

% There is an empty row at the bottom that is extraneous
c_lines(end)= [];

% Close file
fclose(fID);

%% Store header information in a cell array, and numeric data into a numeric matrix

% reset loop_count
loop_count=0;
% reset flg_go
flg_go=1;

% This while loop finds what row the data starts at
while(flg_go)
   loop_count= loop_count + 1 ; 
   flg_go= isempty(str2num(c_lines{loop_count}));
        
end 

% Using the loop_count, the wanted numeric data is putinto a [Mx3] matrix
all_data= str2num( [c_lines{loop_count:end}]);
ncol = numel( str2num( [c_lines{loop_count}] ) );
data = reshape(all_data,ncol,[])';
data = [data(:,2) data(:,[4 5])];

% Using the nature data, the loop_count goes back two rows 
% to find the header. 
header = c_lines{loop_count-2,1};
header = strsplit(header( regexp(header,'[^"]')),',');
header(end)= [];

% Using the nature data, the loop_count goes back one row 
% to find the units
units= c_lines{loop_count-1,1};
units = strsplit(units( regexp(units,'[^"]')),',');
units(end)= [];

% A [1x3] blank cell is created
ax_lbl= cell(1,3);

% The information is combineded and put into the cell
ax_lbl{1}= [header{2}  ' ('  units{2} ')'];
ax_lbl{2}= [header{4} ' ('  units{4} ')'];
ax_lbl{3}= [header{5} ' ('  units{5} ')'];
    
%% Visualize raw data (time vs load, time vs displacement)

%The figure is created
subplots = figure(1);
clf(subplots)

% The first subpolt is made with the first two columns of data
subplot(2,1,1)
hold on
plot(data(:,1),data(:,2),'r')
xlabel(ax_lbl{1})
ylabel(ax_lbl{2})
title([ax_lbl{2} ' vs ' ax_lbl{1}])
grid on
hold off

% The second subpolt is made with the first and thrid columns of data
% The graph is positioned under the provious subplot
subplot(2,1,2)
hold on
plot(data(:,1),data(:,3),'m')
xlabel (ax_lbl{1})
ylabel (ax_lbl{3})
title ([ax_lbl{3} ' vs ' ax_lbl{1}])
grid on
hold off

return