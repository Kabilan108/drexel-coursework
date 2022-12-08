%% By: Isabella Spinelli, Demetri Tsitsios, & Landon Leininger
% This function connects to the database if it exists; if the database
% does not exist, this function creates it by calling dbcreation.m; if the
% database exists and is empty, this function calls dbcreation.m to
% populate it

% Input: Path to database file
% Output: Connection to database file

function conn = dbconnection(dbfile)

% Define zip file URLs for dbcreation.m inputs
zipfile1 = 'https://www.bcsc-research.org/download_file/view/191/344';
zipfile2 = 'https://www.bcsc-research.org/download_file/view/192/344';
zipfile3 = 'https://www.bcsc-research.org/download_file/view/193/344';

% Check if database file exists
% Exist function outputs a 2 if the file exists
if exist(dbfile, 'file') == 2
	
	% Connect to file if it already exists
	conn = sqlite(dbfile);
	
	% If database exists but is empty
	% SQL query returns names of any tables that exist in the database file
  if isempty(fetch(conn, 'SELECT name FROM sqlite_schema WHERE type = "table"'))
		
    % Call dbcreation.m to populate existing database
	  dbfile = dbcreation(zipfile1, zipfile2, zipfile3);
		
		% Connect to existing database file
		conn = sqlite(dbfile);
		
  end
	
else
	
	% If database file does not exist, use dbcreation.m to create it
	dbfile = dbcreation(zipfile1, zipfile2, zipfile3);
	
	% Connect to newly created database file
	conn = sqlite(dbfile);
	
end
