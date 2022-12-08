% By: Corine Lontoc, Soham Patel, Sam Schonwald

function [datatable] = Database(username)
%DATABASE used to pull data out of database to put onto GUI table

% dbfile saves file path for the symptoms
%dbfile = fullfile(pwd,'User_Database.sqlite');
dbfile = [bmes.tempdir() '/User_Database.sqlite'];

% Conn establishes connection to database
conn = sqlite(dbfile);

% fetch fill create matlab table from selected fields if username matches
datatable = fetch(conn, ['SELECT date, height, weight, sputum_color, ' ...
    'stool_consist, stool_color, cough_freq, effort_breath, ' ...
    'level_activity, amount_sputum, stomach_pain, appetite_level ' ...
    'FROM symptoms WHERE user = "' username{1} '"' ]);

end