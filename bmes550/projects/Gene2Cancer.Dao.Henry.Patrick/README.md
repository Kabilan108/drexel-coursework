--------------Gene2Cancer------------
[[Henry Nguyen, Dao Lin, Pratik Chapagain]]


Install Software:


--MATLAB : https://www.mathworks.com/?s_tid=mlh_gn_logo


--MATLAB appdesigner: Package part of MATLAB


--SQLiteStudio(optional if you want to see patient info): https://sqlitestudio.pl


--Disgenet_2020 Database: (Located privately in Drexel OneDrive) 
https://drexel0-my.sharepoint.com/:u:/g/personal/hhn33_drexel_edu/Edbvf5tdev9KovNhrHvzA14B1lDPXbAPNjUkb_flzEQQ-w?e=qw2bkq
* Place the database file into C:\Users\[Username]\AppData\Local\Temp\bmes
* Add director to Ahmet BMES folder in Set path






##InsertPatientData.mlapp
This is the GUI that the user interacts with to input patient information and desired gene. After pressing submit, a table with associated cancer types, and a tree diagram of gene and cancer type correlations will appear.


##diagram.m 
When the submit button is pushed on the GUI, the information will be sent to this function. 
This function creates the associated cancer types table, and tree diagram that InsertPatientData.mlapp extracts for display.




##submitpatientinfo.m
When the submit is pushed on the GUI, the patient info will be given to this function to create a table and store it into the degenet_2020.sqlite for future reference. The columns of the labels are FirstName, LastName, Email, PhoneNumber, GeneName, and CancerAssociation. 




##NoData.m 
If the inputted gene from the GUI does not exist in degenet_2020.sqlite database, it will tell 
InsertPatientData.mlapp to make the graph disappear. It will tell the user that the gene has no association within the database.  




##Degenet_2020.sqlite
This is the database that has all the tables with different types of diseases. We used a query to extract geneName and cancer types into another table. Compare_table table will store the correlation of different cancer types to a single gene. Compare_table2 stores the correlation of different genes to a single cancer type. Patient info table will also be stored into this database. 














-----------------------------DO NOT NEEDED IF YOU ARE DOWNLOADING FROM THE ONE DRIVE LINK!------------------------------
##Compare_table Query: 
-Step 1: CREATE TABLE compare_table( geneName TEXT, count INTEGER, Disease TEXT );


-Step 2: with dnv as (SELECT diseaseAttributes.diseaseName, variantDiseaseNetwork.variantNID FROM diseaseAttributes join variantDiseaseNetwork on diseaseAttributes.diseaseNID = variantDiseaseNetwork.diseaseNID where diseaseName like '%Cancer%' or diseaseName like '%cancer%'), dnvg as (select diseaseName, geneNID from dnv join variantGene on dnv.variantNID = variantGene.variantNID), 


dngn as (select distinct diseaseName, geneName from dnvg join geneAttributes on dnvg.geneNID = geneAttributes.geneNID) 


dngn1 join dngn as dngn2 on dngn1.geneName = dngn2.geneName;


INSERT INTO compare_table select geneName, count(diseaseName) as cancersPerGene, json_group_array(diseaseName) as cancerNames from dngn group by geneName




##Compare_table2 Query: 
-Step 1:  CREATE TABLE compare_table( geneName TEXT, count INTEGER, Disease TEXT )


-STEP 2: with dnv as (SELECT diseaseAttributes.diseaseName, variantDiseaseNetwork.variantNID FROM diseaseAttributes join variantDiseaseNetwork on diseaseAttributes.diseaseNID = variantDiseaseNetwork.diseaseNID where diseaseName like '%Cancer%' or diseaseName like '%cancer%'), dnvg as (select diseaseName, geneNID from dnv join variantGene on dnv.variantNID = variantGene.variantNID), 


dngn as (select distinct geneName, diseaseName from dnvg join geneAttributes on dnvg.geneNID = geneAttributes.geneNID


join dngn as dngn2 on dngn1.geneName = dngn2.geneName; 


INSERT INTO compare_table select diseaseName, count(geneName) as cancersPerGene, json_group_array(geneName) as geneNames from dngn group by diseaseName