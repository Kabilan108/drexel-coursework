function SQL()
%% Creating SQL Database
%Dimitri Kounis

%Create dbfile  if it does not exist 
delete sql.sqlite
dbfile = [pwd '\sql.sqlite']
%dbfile = [bmes.datadir() '/bmes550.sqlite'];
if isfile(dbfile)
    conn = sqlite(dbfile);
else                
    conn = sqlite(dbfile, 'create');
end
db = bmes_db(dbfile,'database');

%% Age
a_file = readtable("age.csv")
a_file.Total = sum(a_file{:,2:end},2)
exec(conn, [ 'CREATE TABLE IF NOT EXISTS age ( ' ...
	' id INTEGER PRIMARY KEY, ' ... 
	' ages VARCHAR(30),  ' ...
	' other INTEGER, ' ...
    ' men INTEGER, ' ...
    ' trans_men INTEGER, ' ...
    ' trans_women INTEGER, ' ...
    ' women INTEGER, ' ...
    ' total INTEGER ' ...
    ')' ])

for i = 1:length(a_file.web_age_grp)
    exec(conn, ["INSERT INTO age(ages, other, men, trans_men, trans_women, women, total) VALUES ('"+a_file.web_age_grp{i}+"',"+a_file.AnotherSex_gender(i)+","+a_file.Men(i)+","+a_file.TransgenderMen(i)+","+a_file.TransgenderWomen(i)+","+a_file.Women(i)+","+a_file.Total(i)+")"]);
end
    
exec(conn, ["INSERT INTO age(ages, other, men, trans_men, trans_women, women, total) VALUES ('Total',"+sum(a_file.AnotherSex_gender)+","+sum(a_file.Men)+","+sum(a_file.TransgenderMen)+","+sum(a_file.TransgenderWomen)+","+sum(a_file.Women)+","+sum(a_file.Total)+")"]);
exec(conn, ['SELECT * FROM age']) 

%% Ethnicity
e_file = readtable("ethnicity.csv")
e_file = e_file(:,2:end)
e_file_total = {mean(e_file.AmericanIndianOrAlaskaNative) mean(e_file.Asian) mean(e_file.BlackOrAfricanAmerican) mean(e_file.HispanicOrLatino) mean(e_file.MultipleRaces) mean(e_file.NativeHawaiianOrOtherPacificIslander) mean(e_file.OtherRace) mean(e_file.White) }
e_file = [e_file; e_file_total]
e_file.Total = sum(e_file{:,2:end},2)
exec(conn, [ 'CREATE TABLE IF NOT EXISTS ethnicity (' ...
	' id INTEGER PRIMARY KEY,' ... 
	' race VARCHAR(50), ' ...
	' percent INTEGER' ...
    ')' ])
races = e_file.Properties.VariableNames;
for i = 1:length(races)
    exec(conn, ["INSERT INTO ethnicity(race, percent) VALUES ('"+races{i}+"',"+e_file{end,i}+")"])
end

exec(conn, ['SELECT * FROM ethnicity']) 

%% Regions
r_file = readtable("regions.csv")
exec(conn, [ 'CREATE TABLE IF NOT EXISTS region (' ...
	' id INTEGER PRIMARY KEY,' ... 
	' state VARCHAR(50),' ...
	' cases INTEGER,' ...
    ' range VARCHAR(50)' ...
    ')' ])

for i = 1:length(r_file.Location)
    exec(conn, ["INSERT INTO region(state, cases, range) VALUES ('"+r_file.Location{i}+"',"+r_file.Cases(i)+",'"+r_file.Case_Range{i}+"')"])
end

exec(conn, ['SELECT * FROM region']) 

%% Vaccine
v_file = readtable("vaccine.csv")
v_file = v_file(:,2:end)
v_file_total = [round(sum(v_file.Vaccinated)) round(sum(v_file.Unvaccinated)) round(sum(v_file.Vaccinated))+round(sum(v_file.Unvaccinated))]
exec(conn, [ 'CREATE TABLE IF NOT EXISTS vaccine (' ...
	' id INTEGER PRIMARY KEY,' ... 
	' status VARCHAR(30),' ...
	' cases INTEGER' ...
    ')' ])

stat = v_file.Properties.VariableNames;
stat{3} = 'Total'

for i = 1:length(stat)
    exec(conn, ["INSERT INTO vaccine(status, cases) VALUES ('"+stat{i}+"',"+v_file_total(i)+")"])
end

exec(conn, ['SELECT * FROM vaccine']) 

end

end