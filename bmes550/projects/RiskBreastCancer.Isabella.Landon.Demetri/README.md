# BreastCancerRisk Application
### by Landon Leininger, Demetri Tsitsios, Isabella Spinelli - 2022.12.5

## Project Proposal
For our project, we propose a GUI that US women can use to assess their risk of developing breast cancer based on various risk factors. We used a database of mammography data of US women from 2005-2017 that shows the history of breast cancer in each woman that received a mammogram and the corresponding risk factors associated with that woman. Our GUI will allow users to input their corresponding risk factors and examine the percentage of women from this database with the same risk factors who have a history of breast cancer.

## Installation Instructions
This project utilizes the 2022b version of MATLAB, a programming language designed by Mathworks. The installation of MATLAB can be followed using this link: https://www.mathworks.com/store/. 
During installation, the only additional package required is the **Database Toolbox**. If MATLAB has aleady been installed on your computer follow these steps to install the packages. Open Matlab -> Apps -> Install App -> Search Database Toolbox -> Install.
In order to download or access the breast cancer data, please follow this link https://www.bcsc-research.org/data/rf/risk-factor-dataset-download. 

## Description of Each File
The BreastCancerRisk Application utilizes four different functions in order to calculate breast cancer risk based on 9 different risk factors inputted by the user.

1. dbconnection.m
This function creates a connection to the SQL database if it exists. If it does not exist, or is it exists and is empty, the function will call the dbcreation.m function.

2. dbcreation.m
This function downloads the data files from their associated URLs, unzips the, and stores them in a temporary folder. An SQL database in created using the data from the BCSC .csv files. 

3. riskcalc.m
This function takes the user inputted risk factors and returns the percentage of people within the database that have breast cancer history, no breast cancer history and unknown history with the same risk factors. The function uses the connection created from dbconnection.m to query the specified information.

4. maingui_breastcancerrisk.mlapp
The fourth function is a GUI created in Matlab's Appdesigner that allows the user to input answers to the 9 risk factors found in the BCSC data. After user selection, a pie chart outputs the calculated percentages taken from riskcalc.m