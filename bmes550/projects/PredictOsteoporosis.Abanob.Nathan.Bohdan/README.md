This file contains all the files that are associated with the Osteoporosis Predictor project along
with a description of what each file does.

Files include:

mainguiosteoporosispredictor.mlapp:
This is the main GUI that interacts with the user. This will ask the user for different parameters
associated to the patient and will allow the user to push a button to calculate a prediction for
osteoporosis. It generates a pie chart depending on the inputted parameters.

calculaterisk.m: 
This file takes in the inputs from the mainguiosteoporosispredictor.mlapp and calculates the
prediction. The outputs of this file is used to create the sections of the pie chart that is
portrayed in the GUI. This function also append the new patient data to the sql database.

Osteoporosis.sqlite:
This is the database table that stores all of the input parameters of the GUI. The calculaterisk.m
file uses this table to compare the patients information to the pre-existing patients in this table
and do the calculation.


To run this code you must have MATLAB installed and download the MATLAB app designer app. To run this file, 
you must have the designated "Osteoporosis.sqlite" in a bmes temp folder as well as access to the bmes functions 
created by Ahmet Sacan that are also found within the folder. 



