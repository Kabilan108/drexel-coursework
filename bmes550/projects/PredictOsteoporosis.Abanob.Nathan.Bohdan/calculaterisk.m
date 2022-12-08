function riskpercentages = calculaterisk( info )
%Example input structure
%info.name = {'Sasha'}; info.gender = {'Female'}; info.age = {'78'}; info.height = {'52'}; info.weight = {'90'}; info.ethnicity = {'Non hispanic white'}; info.mhf = {'Yes'};info.smoker = {'Yes'}; info.grip = {'25'}; info.vitamin = {'No'}; info.fractures = {'2+'};
%info.name = {'Marco'}; info.gender = {'Male'}; info.age = {'96'}; info.height = {'52'}; info.weight = {'98'}; info.ethnicity = {'Asian'}; info.mhf= {'Yes'};info.smoker = {'Yes'}; info.grip = {'25'}; info.vitamin = {'Yes'}; info.fractures = {'3'};

%Download external database and save as a variable
%dbfile = fullfile(pwd,"Osteoporosis.sqlite");
dbfile = [bmes.tempdir '/Osteoporosis.sqlite'];
conn = sqlite(dbfile);

%Extract structure cells into variables
patientname = char(info.name);
patientagechar = char(info.age);
patientage = str2double(patientagechar);
patientgender = char(info.gender);
patientheight = char(info.height);
patientweight = char(info.weight);
patientethnicity = char(info.ethnicity);
patientmaternalfracture = char(info.mhf);
patientsmoker = char(info.smoker);
patientgripstrengthchar = char(info.grip);
patientgripstrength = str2double(patientgripstrengthchar);
patientvitamin = char(info.vitamin);
patientfracturehistory = char(info.fractures);

%Use sprintf command to create sql command with new variables
%Use INSERT INTO to append the new patient data to the bottom of the
%existing database
new = sprintf('INSERT INTO Osteoporosis_Patient_Data(Name, Gender, Age, Height, Weight, Ethnicity, MaternalFractureHistory, Smoker, GripStrength, Vitamin, FractureHistory, Distance) VALUES("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s",0)',patientname, patientgender, patientagechar, patientheight, patientweight, patientethnicity, patientmaternalfracture, patientsmoker, patientgripstrengthchar, patientvitamin, patientfracturehistory);

%Execute command to add new patient data
exec(conn, new)

%Calculate BMI for distance calculation

%Convert height and weight structure cells to variables for use in
%calculation
BMIweight = str2double(info.weight);
BMIheight = str2double(info.height);

%BMI equation based on weight (pounds) and height (total inches)
BMI = ((BMIweight)/(BMIheight*BMIheight))*703;

%Create a distance variable and set at 0 before calculating risk
Distance = 0;

%Patient Gender
if strcmpi(patientgender,{'female'}) == 1
    Distance = Distance + 10;
end

%Patient Age
if patientage >20 & patientage <=30
    Distance = Distance + 2.5;
elseif patientage > 30 & patientage <=40
    Distance = Distance + 5;
elseif patientage > 40 & patientage <=50
    Distance = Distance + 10;
elseif patientage > 50 & patientage <=60
    Distance = Distance + 15;
elseif patientage > 60 & patientage <=70
    Distance = Distance + 20;
else Distance = Distance + 25;
end

%Patient BMI
if BMI < 20
    Distance = Distance + 7.5;
end

%Patient Ethnicity
if strcmpi(patientethnicity,{'Non hispanic white'})==1
    Distance = Distance + 5;
elseif strcmpi(patientethnicity,{'Asian'})==1
    Distance = Distance + 7.5;
elseif strcmpi(patientethnicity,{'Hispanic'})==1
    Distance = Distance + 2.5;
end

%Patient Maternal Fracture History
if strcmpi(patientmaternalfracture,{'Yes'})==1
    Distance = Distance + 12.5;
end

%Patient Smoking
if strcmpi(patientsmoker,{'Yes'})==1
    Distance = Distance + 5;
end

%Patient Grip Strength
if patientgripstrength <48.5
    Distance = Distance + 7.5;
elseif patientgripstrength >=48.5 & patientgripstrength <61.73
    Distance = Distance + 4;
end

%Patient Vitamin
if strcmpi(patientvitamin,{'Yes'})==1
    Distance = Distance + 10;
end

%Patient History of Fractures
if patientfracturehistory == '1'
    Distance = Distance + 5;
elseif patientfracturehistory == '2'
    Distance = Distance + 10;
elseif strcmpi(patientfracturehistory,{'2+'})==1
    Distance = Distance + 15;
end

newDistance = sprintf('UPDATE Osteoporosis_Patient_Data SET Distance = %d WHERE (Name = "%s")', Distance, patientname);
exec(conn,newDistance)


dbTable = fetch(conn, 'SELECT * FROM Osteoporosis_Patient_Data');
s = size(dbTable);

Alldistances = [];
positive = [];
negative = [];
undetermined = [];
for i=1:s(1)
    Alldistances(end+1) = dbTable{i,12};
end


for j = 1:s(1)
    if abs(Distance-Alldistances(j))<=20 & strcmpi(dbTable{j,13},{'Positive'}) == 1
        positive(end+1) = [j];
    elseif abs(Distance-Alldistances(j))<=20 & strcmpi(dbTable{j,13},{'Negative'}) == 1
        negative(end+1) = [j];
    elseif abs(Distance-Alldistances(j))<=20
           if strcmpi(dbTable{j,13},{'Undetermined'}) == 1 | strcmpi(dbTable{j,13},{''}) == 1
                undetermined(end+1) = [j];
           end
    end
end
p = size(positive);
n = size(negative);
u = size(undetermined);

totalpositive = p(2);
totalnegative = n(2);
totalundetermined = u(2);
total = totalpositive + totalnegative + totalundetermined;

positiverisk = totalpositive./total;
negativerisk = totalnegative./total;
undeterminedrisk = totalundetermined./total;
riskpercentages = [positiverisk, negativerisk,undeterminedrisk];
%Distance

close(conn);



