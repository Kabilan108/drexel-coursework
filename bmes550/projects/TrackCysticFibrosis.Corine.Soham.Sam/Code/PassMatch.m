% By: Corine Lontoc, Soham Patel, Sam Schonwald

function [Pass] = PassMatch(User_In,Pass_In)

% Predetermines Pass as 0
Pass = 0;

% Sets a temporary directory for the database
dbfile = [bmes.tempdir() '/User_Database.sqlite'];

% If the database file does not exist, then Pass = 0
% Useful for the first user to use the GUI
if ~isfile(dbfile)
    Pass = 0;

% If database exists, then call the database as a table
else
    conn = sqlite(dbfile);


data = sqlread(conn, 'encrypted_registration');

datasize = size(data);

% Runs through each line of the database and compares against username and
% password combinations
for i = 1:datasize(1)
    if User_In == data.username(i) && Pass_In == data.encrypted(i)
        Pass = 1;
    end
end
end