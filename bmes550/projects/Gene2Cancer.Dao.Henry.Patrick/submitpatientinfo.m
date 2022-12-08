function [] = submitpatientinfo(F,L,E,P,G)
% by Patrick Chapagain 120722
% This function will insert new data into the database

% Create a temporary file and connect to the gene database that is stored
% in it
dbfile = [bmes.tempdir '/disgenet_2020.sqlite'];
db = bmes_db(dbfile,'database');

% Create a new table in the database that will be used to store patient info            
db.exec([ 'CREATE TABLE IF NOT EXISTS patientinfo ( ' ...
	      ' FirstName VARCHAR(30), ' ... 
	      ' LastName VARCHAR(30),  ' ...
	      ' Email VARCHAR(30), ' ...
          ' PhoneNumber VARCHAR(30),' ...
          ' GeneName VARCHAR(30),' ...
          ' CancerAssociation VARCHAR(255)' ...
          ' )' ]);

% Create and execute a SQL query that will pull out all cancer related
% diseases associated with inputted gene
txt = sprintf('Select Disease from compare_table where geneName = "%s"', upper(G));
x = db.query(txt);

% Convert the query struct to an array
y = struct2array(x);
% Remove unnecessary characters  
c = regexprep(y, {'[' ,']' , '"'} , {''});

% Create and execute a SQL statement that will input the patient data into the
% patientinfo table
txt2 = sprintf('INSERT INTO patientinfo (FirstName, LastName, Email, PhoneNumber, GeneName, CancerAssociation) VALUES ("%s","%s", "%s", "%s", "%s", "%s")', F, L, E, P, G, c);
db.exec(txt2);

