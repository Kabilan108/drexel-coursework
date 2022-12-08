% By: Corine Lontoc, Soham Patel, Sam Schonwald

function [] = RegisterEncrypted(username, encrypted, first_name, ...
                 last_name, ethnicity, gender, date_of_birth)

%{RegisterEncrypted is used to register a user, saving username,
% encrypted password, first name, last name, date of birth, 
% and demographic information into the User Database}%



% save registration info into a table
datatable = table(username, encrypted, first_name, ...
                 last_name, ethnicity, gender, date_of_birth);


% dbfile saves file path for the registration
dbfile = [bmes.tempdir() '/User_Database.sqlite'];



% Conn establishes connection to database
    conn = sqlite(dbfile);


% sqlwrite puts data into the SQL table
sqlwrite(conn, 'encrypted_registration', datatable);


end

