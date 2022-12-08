# Melanoma Tracker: Image Processing Application for Tracking Changes in Mole Size
## By: Ashley Bishop, Danielle Shoshany, Giselle Matlis
### School of Biomedical Engineering, Drexel University, USA
### Course: BMES550
### Instructor: Ahmet Sacan
### Date: 2022-12-07

## Project Description: Melanoma is a rapidly growing and fatal cancer. However, if caught early, 
it can be treated. Early detection and self monitoring is crucial to decrease mortality. 
With melanoma’s prevalence in the United States on the rise, there is a need for a self 
monitoring app that can track the growth and assess the risk of potentially malignant moles. 
Therefore, a series of linked web pages,  Matlab code, and a database were created for individuals 
to track the progression or advancement of a potentially malignant mole that could be diagnosed as 
Melanoma.   The web pages were created in PHP, where users login or create an account which compares 
and/or stores this  user information into a table in SQLite database. Then able to upload an image of 
a suspicious mole. The image was then evaluated in Matlab based on diameter with a qualitative (i.e.,
 high, moderate, or low) risk based on the diameter. The image, diameter, and risk were then presented 
to the user on a new page where they can also evaluate the growth history of the given mole. This mole 
information was also stored in the database. This process can be used for multiple users and multiple 
moles per user. In conclusion, the hope for this project is to assist patients in self-assessment of suspicious 
 moles to potentially increase the detection rate, which could reduce unnecessary melanoma related deaths due to
late-stage diagnosis. 

###

## index.php 
Creates the html interface and takes the username and password as inputs. 
If you are a new user, click the 'create new user' button this will send the user to newuser_connected.php 
If you are a returning user, fill in the username and password and click the 'submit button'. Once the submit is clicked, the username and password will be compared to the stored values. 
The show password checkbox allows the user to choose if they want to see the password text. 
If the correct username and password are inputed, the user will be taken to test_submitting.php. 
If the incorrect combination is input, an error will be displayed directing the user to input the correct username and password.

## newuser_connection
Creates the html interface(including four text boxes and a submit button) asks the user for their  first name, last name, username and password as inputs and adds them to the database. 
The show password checkbox allows the user to choose if they want to see the password text.
Once the user clicks the 'create new user button', the data is then stored into the database and the user is redirected to the 'test_submitting.php'.

## test_submitting.php
Creates the html interface that asks the user for the date of the image, mole number, and for them to upload the image. This information is then sent to molesize.m where it is processed. Once the submit button is pressed, the can either submit another image or choose to click the "view history' button to to redirect to history.php where results can be viewed.

## mole.m 
This matlab script take the submitted image and analyzes it to determine the mole's diameter and risk (based on diameter) this data is then stored in molesize_export.m. 

## molesize_export.m
This script saves the risk and diameter in a temporary file that can be assessed and printed by history.php

## history.php 
Displayed the analyzed image from molesize.m as well as the diameter for a given mole indicated by its mole id. This page also includes a graph tracking the past diameter of the same mole. 
Other mole histories can be displayed on the plot using the hover-over drop down menu. 
Please make sure the folder named 'lib' is in the directory.  These include a javascript library to jQuery (which can be downloaded from: https://jquery.com/download/) 
## MelanomaData 
The database created with two tables that are linked via user ID. 
The 'userinfo' table stores the user information including 'User_ID' as an INTEGER and PRIMARY KEY, 'firstname' as a VARCHAR(255), 'lastname' as a VARCHAR(255), 'username' as a VARCHAR(255) and UNIQUE character so that two users cannot have the same username, and 'password' as a VARCHAR(255). The second table, 'moleinfo' stores the mole information including the 'id' as a PRIMARY KEY, 'User_ID' as an INTEGER, 'Img_Date' as a VARCHAR(255), 'Mole_Size' as a FLOAT(6), 'Risk' as a VARCHAR(255), and 'Mole_ID' as an INTEGER. This information is stored and access by the above listed .php pages and. 







 

