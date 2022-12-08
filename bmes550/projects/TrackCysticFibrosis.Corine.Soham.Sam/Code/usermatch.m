% By: Corine Lontoc, Soham Patel, Sam Schonwald

function [User] = usermatch(username)

%{usermatch is used to determine if a user with the same 
% username already exists}%


% Predefines as 0 for the case this is first time user being created
User = 0;

% dbfile = fullfile(pwd,'User_Database.sqlite');
dbfile = [bmes.tempdir() '/User_Database.sqlite'];

% Isfile checks for the SQL file, if not created, then create
% Conn establishes connection to database
if ~isfile(dbfile)
    conn = sqlite(dbfile,'create');

% Create table in which to load results
exec(conn, ['CREATE TABLE IF NOT EXISTS encrypted_registration' ...
    '(username VARCHAR(30),' ...
    'encrypted VARCHAR(30), ' ...
    'first_name VARCHAR(30),' ...
    'last_name VARCHAR(30),' ...
    'ethnicity VARCHAR(30),' ...
    'gender VARCHAR(30),' ...
    'date_of_birth VARCHAR(30))'])
else
    conn = sqlite(dbfile);

% sqlwrite puts data into the SQL table
data = sqlread(conn, 'encrypted_registration');

% determine if there is a username that matches inputted username
User_Match = find(data.username == username);

%determine size of the data
datasize = size(data);

%create a for loop to match each username in the database list
%determine if there is a match or not 
    for i = 1:datasize(1)
        if isempty(User_Match) == 1
        User = 0;
        else
        User = 1;
        end

    end

end

end

