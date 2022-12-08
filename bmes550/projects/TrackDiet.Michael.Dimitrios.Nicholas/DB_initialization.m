%% Data Initialization Script
% By Nick Fioravanti, Dimitri Dogias, and Michael Mathews
% Summary - downloads data files from FNDDS, establishes sqlite database,
% and deposits data into tables
%% Pull Data Files from Website
% Food and Beverage Data File Location
food_and_beverage_link = 'https://www.ars.usda.gov/ARSUserFiles/80400530/apps/2019-2020%20FNDDS%20At%20A%20Glance%20-%20Foods%20and%20Beverages.xlsx';

% Nutrient Data File Location
nutrients_link = 'https://www.ars.usda.gov/ARSUserFiles/80400530/apps/2019-2020%20FNDDS%20At%20A%20Glance%20-%20FNDDS%20Nutrient%20Values.xlsx';
if isfile('2019-202020FNDDS20At20A20Glance20-20FNDDS20Nutrient20Valuesapps80400530ARSUserFileswww.ars.usda.gov.xlsx')
    food_and_beverage_xls = readtable('2019-202020FNDDS20At20A20Glance20-20Foods20and20Beveragesapps80400530ARSUserFileswww.ars.usda.gov.xlsx');
else
    % Food and Beverage Download
    food_and_beverage_xls=bmes.downloadurl(food_and_beverage_link);
    food_and_beverage = readtable(food_and_beverage_xls);
end

if isfile('2019-202020FNDDS20At20A20Glance20-20FNDDS20Nutrient20Valuesapps80400530ARSUserFileswww.ars.usda.gov.xlsx')
    nutrients_xls = readtable('2019-202020FNDDS20At20A20Glance20-20FNDDS20Nutrient20Valuesapps80400530ARSUserFileswww.ars.usda.gov.xlsx');
else
    % Food and Beverage Download
    nutrients_xls=bmes.downloadurl(nutrients_link);
end

% Find size of text file to know number of rows to iterate through
[r,c] = size(food_and_beverage);

%% Database Initialization
% Append data directory with file name 
diet_database = [bmes.datadir()  '/diet_database.sqlite'];
fclose(fopen(diet_database,'a'));

% If database file exists 
if isfile(diet_database);
    
    % Make connection to database file 
    conn = sqlite(diet_database);
    
% If database file does not exist, create empty database file
else 
    % Create database file and make connection
    conn = sqlite(diet_database, 'create');
end

%% Food and Beverage Table
exec(conn, ['CREATE TABLE IF NOT EXISTS food_and_beverage_db ( '...
    'FoodCode TEXT, ' ...
    'MainFoodDescription TEXT, ' ...
    'AdditionalFoodDescription TEXT, ' ...
    'WWEIACategoryNumber TEXT, ' ...
    'WWEIACategoryDescription TEXT' ...
    ')'])


for n = 1:r

    % for each row, index the text within the miRNA variable equivalent of
    % Var1 and convert from table to cell to character
    strin1 = string(table2cell(food_and_beverage(n,1)));

    % for each row, index the text within the Target variable equivalent of
    % Var2 and convert from table to cell to character
    strin2 = string(table2cell(food_and_beverage(n,2)));
    strin3 = string(table2cell(food_and_beverage(n,3)));
    strin4 = string(table2cell(food_and_beverage(n,4)));
    strin5 = string(table2cell(food_and_beverage(n,5)));   
    
    % Correct for empty strings

    if strin1 == ""
        strin1 = 'Empty';
    end
    if strin2 == ""
        strin2 = 'Empty';
    end
    if strin3 == ""
        strin3 = 'Empty';
    end
    if strin4 == ""
        strin4 = 'Empty';
    end
    if strin5 == ""
        strin5 = 'Empty';
    end
    % Correct for Empty Parentheses in Strings
    strin1 = strrep(strin1, '"', "");
    strin2 = strrep(strin2, '"', "");
    strin3 = strrep(strin3, '"', "");
    strin4 = strrep(strin4, '"', "");
    strin5 = strrep(strin5, '"', "");

    % Create the instructional input that will be executed with the
    % connection to the database -- insert into the table mirdbfile
    % according to the columns of miRNA, Target, and Prediction Score
    % according to the values provided by the previous inputs that were
    % read from each row
    input1 = ['INSERT INTO food_and_beverage_db(FoodCode, MainFoodDescription, AdditionalFoodDescription, WWEIACategoryNumber, WWEIACategoryDescription) VALUES("' char(strin1) '","' char(strin2) '","' char(strin3) '","' char(strin4) '","' char(strin5) '")'];
    
    % Execute input with connection to database and complete data insertion
    exec(conn, input1);
end

%% Ingredient Nutrient Table
% Take text file and convert to database file 
% Read Text File into Matlab 
FNDDS_nutrient_values_xls = readtable(nutrients_xls);
% Find size of text file to know number of rows to iterate through
[r,c] = size(FNDDS_nutrient_values_xls);

% Create new table if it does not already exist
exec(conn, ['CREATE TABLE IF NOT EXISTS FNDDS_nutrient_values_db ( '...
    'FoodCode TEXT,'...
    'MainFoodDescription TEXT,' ...
    'WWEIACategoryNumber TEXT,' ...
    'WWEIACategoryDescription TEXT,' ...
    'Energy_kcal FLOAT,' ...
    'Protein_grams FLOAT,' ...
    'Carbohydrate_grams FLOAT,' ...
    'Sugars_total_grams FLOAT,' ...
    'TotalFiber_grams FLOAT,' ...
    'TotalFat_grams FLOAT,' ...
    'SaturatedFattyAcids_total_grams FLOAT,'...
    'MonoSaturatedFattyAcids_total_grams FLOAT,' ...
    'PolySaturatedFattyAcids_total_grams FLOAT,' ...
    'Cholesterol_milligrams FLOAT,' ...
    'Calcium_milligrams FLOAT,' ...
    'Phosphorus_milligrams FLOAT,' ...
    'Magnesium_milligrams FLOAT,'...
    'Iron_milligrams FLOAT,' ...
    'Zinc_milligrams FLOAT,'...
    'Copper_milligrams FLOAT,' ...
    'Selenium_micrograms FLOAT,' ...
    'Potassium_milligrams FLOAT,' ...
    'Sodium_milligrams FLOAT,' ...
    'Caffeine_milligrams FLOAT,' ...
    'Alcohol_grams FLOAT'...
    ')'])

for n = 1:r

    % for each row, index the text within the miRNA variable equivalent of
    % Var1 and convert from table to cell to character
    strin1 = string(table2cell(FNDDS_nutrient_values_xls(n,1)));
    strin2 = string(table2cell(FNDDS_nutrient_values_xls(n,2)));
    strin3 = string(table2cell(FNDDS_nutrient_values_xls(n,3)));
    strin4 = string(table2cell(FNDDS_nutrient_values_xls(n,4)));
    strin5 = string(table2cell(FNDDS_nutrient_values_xls(n,5)));  
    strin6 = string(table2cell(FNDDS_nutrient_values_xls(n,6)));
    strin7 = string(table2cell(FNDDS_nutrient_values_xls(n,7)));
    strin8 = string(table2cell(FNDDS_nutrient_values_xls(n,8)));
    strin9 = string(table2cell(FNDDS_nutrient_values_xls(n,9)));
    strin10 = string(table2cell(FNDDS_nutrient_values_xls(n,10)));
    strin11 = string(table2cell(FNDDS_nutrient_values_xls(n,11)));
    strin12 = string(table2cell(FNDDS_nutrient_values_xls(n,12)));
    strin13 = string(table2cell(FNDDS_nutrient_values_xls(n,13)));
    strin14 = string(table2cell(FNDDS_nutrient_values_xls(n,14)));
    strin15 = string(table2cell(FNDDS_nutrient_values_xls(n,38)));
    strin16 = string(table2cell(FNDDS_nutrient_values_xls(n,39)));  
    strin17 = string(table2cell(FNDDS_nutrient_values_xls(n,40)));
    strin18 = string(table2cell(FNDDS_nutrient_values_xls(n,41)));
    strin19 = string(table2cell(FNDDS_nutrient_values_xls(n,42)));
    strin20 = string(table2cell(FNDDS_nutrient_values_xls(n,43)));
    strin21 = string(table2cell(FNDDS_nutrient_values_xls(n,44)));
    strin22 = string(table2cell(FNDDS_nutrient_values_xls(n,45)));
    strin23 = string(table2cell(FNDDS_nutrient_values_xls(n,46)));
    strin24 = string(table2cell(FNDDS_nutrient_values_xls(n,47)));
    strin25 = string(table2cell(FNDDS_nutrient_values_xls(n,49)));

    % Account for empty inputs
    if strin1 == ""
        strin1 = 'Empty';
    end
    if strin2 == ""
        strin2 = 'Empty';
    end
    if strin3 == ""
        strin3 = 'Empty';
    end
    if strin4 == ""
        strin4 = 'Empty';
    end
    if string(strin5) == "" | string(strin5) == '' | isnan(FNDDS_nutrient_values_xls{n,5}) == 1
        strin5 = 'Empty';
    end
    if string(strin6) == "" | string(strin6) == '' | isnan(FNDDS_nutrient_values_xls{n,6}) == 1
        strin6 = 'Empty';
    end
    if string(strin7) == "" | string(strin7) == '' | isnan(FNDDS_nutrient_values_xls{n,7}) == 1
        strin7 = 'Empty';
    end
    if string(strin8) == "" | string(strin8) == '' | isnan(FNDDS_nutrient_values_xls{n,8}) == 1
        strin8 = 'Empty';
    end
    if string(strin9) == "" | string(strin9) == '' | isnan(FNDDS_nutrient_values_xls{n,9}) == 1
        strin9 = 'Empty';
    end
    if string(strin10) == "" | string(strin9) == '' | isnan(FNDDS_nutrient_values_xls{n,10}) == 1
        strin10 = 'Empty';
    end
    if string(strin11) == "" | string(strin11) == '' | isnan(FNDDS_nutrient_values_xls{n,11}) == 1
        strin11 = 'Empty';
    end
    if string(strin12) == "" | string(strin12) == '' | isnan(FNDDS_nutrient_values_xls{n,12}) == 1
        strin12 = 'Empty';
    end
    if string(strin13) == "" | string(strin13) == '' | isnan(FNDDS_nutrient_values_xls{n,13}) == 1
        strin13 = 'Empty';
    end
    if string(strin14) == "" | string(strin14) == '' | isnan(FNDDS_nutrient_values_xls{n,14}) == 1
        strin14 = 'Empty';
    end
    if string(strin15) == "" | string(strin15) == '' | isnan(FNDDS_nutrient_values_xls{n,38}) == 1
        strin15 = 'Empty';
    end
    if string(strin16) == "" | string(strin16) == '' | isnan(FNDDS_nutrient_values_xls{n,39}) == 1
        strin16 = 'Empty';
    end
    if string(strin17) == "" | string(strin17) == '' | isnan(FNDDS_nutrient_values_xls{n,40}) == 1
        strin17 = 'Empty';
    end
    if string(strin18) == "" | string(strin18) == '' | isnan(FNDDS_nutrient_values_xls{n,41}) == 1
        strin18 = 'Empty';
    end
    if string(strin19) == "" | string(strin19) == '' | isnan(FNDDS_nutrient_values_xls{n,42}) == 1
        strin19 = 'Empty';
    end
    if string(strin20) == "" | string(strin20) == '' | isnan(FNDDS_nutrient_values_xls{n,43}) == 1
        strin20 = 'Empty';
    end
    if string(strin21) == "" | string(strin21) == '' | isnan(FNDDS_nutrient_values_xls{n,44}) == 1
        strin21 = 'Empty';
    end
    if string(strin22) == "" | string(strin22) == '' | isnan(FNDDS_nutrient_values_xls{n,45}) == 1
        strin22 = 'Empty';
    end
    if string(strin23) == "" | string(strin23) == '' | isnan(FNDDS_nutrient_values_xls{n,46}) == 1
        strin23 = 'Empty';
    end
    if string(strin24) == "" | string(strin24) == '' | isnan(FNDDS_nutrient_values_xls{n,47}) == 1
        strin24 = 'Empty';
    end
    if string(strin25) == "" | string(strin25) == '' | isnan(FNDDS_nutrient_values_xls{n,49}) == 1
        strin25 = 'Empty';
    end

    % Replace empty quotations
    strin1 = strrep(strin1, '"', "");
    strin2 = strrep(strin2, '"', "");
    strin3 = strrep(strin3, '"', "");
    strin4 = strrep(strin4, '"', "");
    
    % Generate input for data entry
    input5 = ['INSERT INTO FNDDS_nutrient_values_db(FoodCode, MainFoodDescription, WWEIACategoryNumber, WWEIACategoryDescription, Energy_kcal, Protein_grams, Carbohydrate_grams, Sugars_total_grams, TotalFiber_grams, TotalFat_grams, SaturatedFattyAcids_total_grams, MonoSaturatedFattyAcids_total_grams, PolySaturatedFattyAcids_total_grams, Cholesterol_milligrams, Calcium_milligrams, Phosphorus_milligrams, Magnesium_milligrams, Iron_milligrams, Zinc_milligrams, Copper_milligrams, Selenium_micrograms, Potassium_milligrams, Sodium_milligrams, Caffeine_milligrams, Alcohol_grams) VALUES("' char(strin1) '","' char(strin2) '","' char(strin3) '","' char(strin4) '","' char(strin5) '","' char(strin6) '","' char(strin7) '","' char(strin8) '","' char(strin9) '","' char(strin10) '","' char(strin11) '","' char(strin12) '","' char(strin13) '","' char(strin14) '","' char(strin15) '","' char(strin16) '","' char(strin17) '","' char(strin18) '","' char(strin19) '","' char(strin20) '","' char(strin21) '","' char(strin22) '","' char(strin23) '","' char(strin24) '","' char(strin25) '")'];
    
    % Execute input with connection to database and complete data insertion
    exec(conn, input5);
end


%% Data Entry GUI
DataEntry()
