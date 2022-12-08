% Corine Lontoc, Soham Patel, & Sam Schonwald
% Group 22

function [encrypted] = encrypt_pass(password)
%function that uses the md5 file function to encrypt inputted passwords

% opens a text file to store user password
fileID = fopen('user_pass.txt','w');
%stores user password
fprintf(fileID, password);
%creates a variable to store encrypted password
encrypted = md5('user_pass.txt');

%closes file
fclose('all');

%deletes file with password that is not encrypted
delete('user_pass.txt')