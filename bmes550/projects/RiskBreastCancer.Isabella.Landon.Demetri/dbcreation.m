%% By: Isabella Spinelli, Demetri Tsitsios, & Landon Leininger
% This function downloads the files from their URLs, unzips them, stores
% them in a temporary folder, and then creates an SQL database with the
% data stored in them

% Inputs: 3 URLs for data files
% Output: Path to database file

function dbfile = dbcreation(zipfile1, zipfile2, zipfile3)

%% Download and unzip inputted URLs, and store in a temporary directory
% Use char function to convert cell cell arrays to character arrays
% File #1
bcfile1 = char(unzip(bmes.downloadurl(zipfile1), bmes.datadir()));

% File #2
bcfile2 = char(unzip(bmes.downloadurl(zipfile2), bmes.datadir()));

% File #3
bcfile3 = char(unzip(bmes.downloadurl(zipfile3), bmes.datadir()));


%% Read data into MATLAB tables
table1 = readtable(bcfile1);
table2 = readtable(bcfile2);
table3 = readtable(bcfile3);

% Combine table1, table2, and table3 data into one table (bctable)
bctable = [table1; table2; table3];


%% Create and connect to breastcancer database
% Create database file and store it in a temporary directory
dbfile = [bmes.tempdir()  '/breastcancerdb.sqlite'];

% If database file exists, this connects to it and populates it
% Will only be called by dbconnection.m if database is empty
% Exist function outputs a 2 if the file exists
if exist(dbfile, 'file') == 2
	
	% Connect to existing database file
	conn = sqlite(dbfile);
	
else
	
	% Otherwise, create and connect to database file
  conn = sqlite(dbfile, 'create');
	
end

%% Create table in database file
% Use an SQL query to drop the table if it already exists
exec(conn, 'DROP TABLE IF EXISTS breastcancer');

% Use an SQL query to create a new breast cancer table
exec(conn, ['CREATE TABLE breastcancer ' ...
    '(id INTEGER PRIMARY KEY, year NUMERIC, age_group_5_years NUMERIC, race_eth NUMERIC, ' ...
		'first_degree_hx NUMERIC, age_menarche NUMERIC, ' ...
		'age_first_birth NUMERIC, BIRADS_breast_density NUMERIC, ' ...
		'current_hrt NUMERIC, menopaus NUMERIC, bmi_group NUMERIC, ' ...
		'biophx NUMERIC, breast_cancer_history NUMERIC, count NUMERIC)']);

% Create column names for breast cancer table
columnnames = {'year', 'age_group_5_years', 'race_eth', 'first_degree_hx', 'age_menarche', 'age_first_birth', 'BIRADS_breast_density', 'current_hrt', 'menopaus', 'bmi_group', 'biophx', 'breast_cancer_history', 'count'};
    
% Insert bctable data into breastcancer table in database file
% Use columnnames defined above
insert(conn, 'breastcancer', columnnames, bctable);

% Close database connection
close(conn);
