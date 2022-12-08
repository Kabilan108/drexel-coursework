
# Heart Disease Risk Calculator

This Graphical User Interface (GUI) can be utilized by any individual to determine their risk of Atherosclerotic Cardiovascular Disease (ASCVD) based on several personal input factors. These user inputs include sex, race, age, presence of blood pressure medications, blood pressure values, cholesterol levels, high-density lipoprotein (HDL) cholesterol, smoking status, and presence of diabetes. After submitting these factors via text boxes or dropdown menus, the calculator will present a risk score of ASCVD as a percentage. The user can also input their current zip code, which will determine the three closest hospitals from their location.



## Create A New Environment with Streamlit

1. Open Anaconda Navigator application on your computer
2. Select a new environment, open a new terminal in the environment of your choice
![App Screenshot](https://i.stack.imgur.com/EiiFc.png)


## Installing Streamlit

Install streamlit in python terminal - used to create custom web applications

```bash
 pip install streamlit
```

Install geopy in python terminal - make it easy to locate coordinates of addresses, cities, using specified data sources

```bash
pip install geopy
```

Navigate to folder where all project files are located on computer

For example:
![App Screenshot](https://i.paste.pics/K8YXN.png)

To run the GUI

```bash
streamlit run cvdrisk.py
```

## GUI Files

## cvdrisk.py
This article (https://www.ahajournals.org/doi/full/10.1161/01.cir.0000437741.48606.98#d1e421) provides an estimation of an individual's 10-year risk of ASCVD based on the Pooled Cohort Equations (PCE). This file creates the user input section.

The "Sex" entry is a selectbox() that allows the user to choose their biological sex. The "Race" entry is a selectbox() that allows the user to choose from 5 different races. The "Age" entry is a number input box that allows the user to enter their age. The "Blood pressure treatment" entry is a selectbox() that allows the user to provide whether or not they are taking any medication to control their blood pressure. The "Blood pressure" entry is a number input box that allows the user to enter their most recent systolic blood pressure value. The "Total cholesterol" box is a number input box that allows the user to enter their most recent total cholesterol value. The "HDL cholesterol" entry is a number input box that allows the user to enter their most recent high-density lipoprotein (HDL) cholesterol value. The "Smoker" entry is a selectbox() that allows the user to choose whether or not they are currently a smoker. The "Diabetes" entry is a selectbox() that allows the user to choose whether or not they have been diagnosed with diabetes. The "Zip code" entry is a number input box that allows the user to enter their current zip code. The inputted personal information (zip code is not factored into this calculation) is run through the risk_calc.py file to determine an output risk score as a percentage. The user's zip code information is run through the close_hosp.py file to determine the locations of the three closest hospitals from their given location.

## risk_calc.py
Based on the user inputs (excluding zip code), this file determines the user's risk of ASCVD based on the PCE. Different user inputs (sex, race, BP treatment) will lead to modifications in the PCE calculation for risk.

## close_hosp.py
This file utilizes geopy, which has been installed to locate the coordinates and addresses of the hospitals in the database. This file creates the data directory, creates the zipcode based on the latitude and longitude reference table in the database, and establishes a connection between the cursor and the database. All of the zipcodes from the database are then put into the database and are converted to a panda data frame (import panda as pd). The specific latitude and longitude of each possible zip code are gathered. In the table includes the distance from between the user's location (given by user zip code input) and the three nearest hospitals.

## hosp.py
This file establishes a hospital data directory, creates a new database in the specified data folder, and establishes a cursor using a connection from sqlite to pull hospital information from all areas of the United States. A table is then created with the hospital information. The hospital data is taken from https://www.kaggle.com/datasets/andrewmvd/us-hospital-locations?resource=download. It is possible that the URL to this website may expire, so it is important to retrieve the data using the filepath specified if this happens. A temporary directory is created where the filepath is opened, the opened file is copied into the temporary directory, and all of the hospital locations (taken from the us_hospital_locations.csv which has been downloaded and extracted) are read into a data frame. The data frame is then converted into a table and is appended to the table containing the hospital data. The changes will be saved in the database and the connection to the database will close.

## zips.py
This file opens https://www.unitedstateszipcodes.org/, reads the United States zip code data, and prints the information. This file also creates a new database and establishes a cursor using a connection between sqlite and the us_hospital_locations.sqlite file. A table is created with the zip codes, and the zip_code_database.csv file is downloaded, which contains all of the zip codes and their corresponding latitudes and longitudes. This information is then put into a data frame and the data frame is converted to a table. This table is then appended to the table containing the zip code data. The changes will be saved in the database and the connection to the database will close.   

##zip_code_database.csv
This file contains all of the zip code information for the United States. It includes the states, counties, time zones, area codes, latitudes, and longitudes which are imported into the zips.py file. This information is used in correlation with the hospital location data to establish distances for the user after a zip code is entered in the GUI.
