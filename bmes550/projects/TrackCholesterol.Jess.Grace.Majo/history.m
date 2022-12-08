function [output] = history(user, tot_chol, LDL, HDL, trig, in_date)

% By: Grace Fan
% inputs: username, total cholesterol, LDL, HDL, Triglycerides 
% 
% writes input data from GUI into sql db
% & takes current and past LDL, HDL, and total cholesterol measurements and
% plots the history on GUI

%% writes input data from GUI into sql db
% connect to sqlite
db_file=[bmes.tempdir() '/userinfo.db'];
conn=sqlite(db_file);

% convert input data from GUI into strings
tot_chol=num2str(tot_chol);
LDL=num2str(LDL);
HDL=num2str(HDL);
trig=num2str(trig);
in_date=char(in_date);
% writes data into sql db
exec(conn, ['INSERT INTO data(username, total_chol, LDL, HDL, Triglycerides, input_date) VALUES (''', user,''', ''', tot_chol,''', ''',LDL,''', ''', HDL,''', ''', trig,''', ''',in_date, ''')']);

%sort data based on username then date to get last 10 inputs
output=fetch(conn, ['SELECT total_chol, LDL, HDL, Triglycerides, input_date FROM data WHERE username=''',user,''' ORDER BY input_date LIMIT 10 ']);