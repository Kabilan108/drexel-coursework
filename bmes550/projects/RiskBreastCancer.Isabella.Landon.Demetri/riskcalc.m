%% By: Isabella Spinelli, Demetri Tsitsios, & Landon Leininger 
% This function takes input risk factors from the user input and returns
% the percentage of people within the database with the same risk factors
% that have breast cancer history, no breast cancer history, and unknown
% breast cancer history. This function utilizes the connection to the SQL
% database to calculate these percentages. 
function [percentages] = riskcalc(conn, fs, vals)

% age: 1-13 grouped bins based on years of age [1: ages 18-29, 2: ages
% 30-34, 3: ages 35-39, 4: ages 40-44, 5: ages 45-49, 6: ages 50-54, 7:
% ages 55-59, 8: ages 60-64, 9: ages 65-69, 10: ages 70-74, 11: ages 75-79,
% 12: ages 80-84, 13: ages 85 and up] 
% db col name: age_group_5_years 

% race: 1-9 grouped bins based on ethnicity [1: Non-Hispanic white, 2:
% Non-Hispanic black 3: Asian/Pacific Islander, 4: Native American, 5:
% Hispanic, 6: Other/mixed, 9: Unknown]
% db col name: race_eth 

% fdhistory: indicates whether the patient has a first degree relative with
% breast cancer [0: No history, 1: Yes history, 9: Unknown history]
% db col name: first_degree_hx 

% menarche: Age at menarche (first menstrual cycle) [0: Ages >14, 1: ages
% 12-13, 2: age <12, 9: Unknown] 
% db col name: age_menarche

% birth_age: Age where first birth was given [0: age <20, 1: age 20-24, 2:
% Age 25-29, 3: Age >30, 4: Nulliparous, 9: Unknown] 
% db col name: age_first_birth

% birads: BI-RADS breast density [1: Almost entirely fat, 2: Scattered
% fibroglandular densities, 3: Heterogeneously dense, 4: Extremely dense,
% 9: Unknown or different measurement system] 
% db col name: BIRADS_breast_density

% hormone_therapy: Use of hormone replacement therapy [0: No, 1: Yes, 9:
% Unknown] 
% db col name: current_hrt

% menopause: Menopausal status [1: Pre- or peri-menopausal, 2:
% Post-menopausal, 3: Surgical menopause, 9: Unknown] 
% db col name: menopaus

% bmi: BMI of patient (kg/m^2) [1: 10-24.99, 2: 25-29.99, 3: 30-34.99, 4:
% 35 or more, 9: Unknown] 
% db col name: bmi_group

% First the vals and fs variables need to be edited so that they only
% include the values and field names that the user inputted noui is an
% index that is returned when there is an empty character in the vals
% variable

noui = ismember(vals, ''); 
vals = vals(~noui); 
fs = fs(~noui); 

% if the values array is not empty, continue with the code as normal 
if ~isempty(vals)

% create the initial sqlquery string, first create the base  
initquery = sprintf(['select breastcancer.breast_cancer_history, ' ...
    'breastcancer.count from breastcancer where ']); 
% then create the body of the query by iterating through the fields and
% values cell arrays 
for i = 1:numel(fs)
    if i>1 
        initquery = [initquery ' AND ']; 
    end 
    initquery = [initquery sprintf('%s = %s', fs{i}, vals{i})]; 
end 



% Query the database to find breast cancer counts based on the user's input
bcc = fetch(conn, initquery); 

% Check if the table fetched by the particular user input is empty 
% If the table is empty, that means there were no matches in the database
% and an estimated risk needs to be calculated based on the closest match
% to the user input 
if isempty(bcc)
    % Need to create a new sql query for the empty database case, first
    % create the base of the query 
    % The query utilizes a nested query so that a distance column (dist)
    % can be created and added to the database
    % Then, the column number (id) breast cancer history indication (0,1,9)
    % and count (frequency) is returned
    emptyquery = sprintf(['select bc.id, breast_cancer_history, count from breastcancer as bc ' ...
        'INNER JOIN ( Select id, (']); 
    for i = 1:numel(fs)
        if i > 1
            emptyquery = [emptyquery '+ ']; 
        end 
        % The query is calculating a distance by first finding the absolute
        % value of the difference between the age group of the user
        % selected age and the values of the database rows provided, this
        % difference serves as a distance between the user input and the
        % database value
        if ismember(fs{i}, 'age_group_5_years')
            emptyquery= [emptyquery sprintf(' ABS(%s - %s) ', fs{i}, vals{i})]; 
        % When the user selects any other risk factor, the distance is
        % arbituary, so sql only checks whether the user inputted value is
        % not equal to the database value, if so, then a value of 1 is
        % returned and added to the total distance
        else 
            emptyquery= [emptyquery sprintf(' (%s!=%s) ', fs{i}, vals{i})]; 
        end 
    end 
    % With the first part of the query complete, create the rest of the
    % query where the distances are captured as 'dist' from the database
    % and the first 10,000 rows are collected ordered in ascending order.
    % This way, an accurate estimate of the percentages will be displayed
    % to the user whose selected combination of risk factors do not exist
    % in the database
    distsqlquery = [emptyquery ') as dist from breastcancer ) d ON bc.id = d.id order by dist limit 10000'];

    % Fetch the distances, where the first column is the row number (id),
    % the second column is the breast cancer diagnosis
    % (breast_cancer_history), and the third is the frequency (count)
    dists = fetch(conn, distsqlquery);
    
 
    % Return the rows of dists where the user has unknown breast
    % cancer history, known breast cancer history, and no breast cancer
    % history and capture the freqency to calculate the total number of
    % patients that do not know they have breast cancer, that know they had
    % breast cancer, and know they did not have breast cancer
    unknowns_I = dists{:, 2}==9;
    unknowns = sum(dists{unknowns_I,3}); 

    nobc_I = dists{:, 2}==0; 
    nobc = sum(dists{nobc_I,3});

    yesbc_I = dists{:, 2}==1; 
    yesbc = sum(dists{yesbc_I,3});
    
    totalsum = sum([unknowns nobc yesbc]); 
    unknown_history = unknowns/totalsum; 
    nbc_history = nobc/totalsum; 
    bc_history = yesbc/totalsum;


% if the table is not empty, then breast_cancer_history and count should be
% returned, therefore the frequencies of people who have a previous breast
% cancer diagnosis, who don't have a previous breast cancer diagnosis, and
% those who do not know will be returned. 
else 
    unknowns_I = bcc{:,1}==9; 
    unknowns = sum(bcc{unknowns_I,2});
    
    nobc_I = bcc{:,1}==0;
    nobc = sum(bcc{nobc_I,2}); 
    
    yesbc_I = bcc{:,1}==1;
    yesbc = sum(bcc{yesbc_I, 2}); 
    
    totalsum = sum([unknowns nobc yesbc]); 
    unknown_history = unknowns/totalsum; 
    nbc_history = nobc/totalsum; 
    bc_history = yesbc/totalsum;
    
end
% Finally, output these percentages in a vector which the pie function will
% use to populate the GUI pie chart. 
percentages = [bc_history nbc_history unknown_history]; 

% if the vals array is empty, produce a percentages vector that is empty,
% this will return an error message in our GUI if this result is obtained
else 
    percentages = []; 
end 
end