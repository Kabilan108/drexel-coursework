# Dietary Tracking Database (DB) and Graphical User Interface (GUI)
##### Contributions from Nicholas Fioravanti (nef46), Dimitri Dogias (dnd56), and Michael Mathews (mjm678)

**Summary:**

The dietary tracker aims to establish a connection between data from the Food and Nutrient Database for Dietary Studies (FNDDS) and an end-user. By developing a database for the .xlsx files provided by the US Deparatment of Agriculture, this project establishes a fast data resource that can be used with a graphical user interface (GUI), allowing for ease-of-use in end-user utilization. The database is kept in a temporary directory outside the project folder.Large data files are kept in a separate location within the local computer. Database and GUI combination do not assume that the user already has access to the data files. Instead it pulls the files directly from the website. 

**Installation Instructions:**

- The only necessary installation is MATLAB. The data files will be downloaded within the MATLAB scripts. 
- It is imperative to ensure that you have access to the bmes folder, which includes various functions for matlab using object oriented programming, that was shared by the professor. 

**Notes:**

- This project does not require the use of passwords, tokens, or external web applications. 
- Database installations found at food and beverages (https://www.ars.usda.gov/ARSUserFiles/80400530/apps/2019-2020%20FNDDS%20At%20A%20Glance%20-%20Foods%20and%20Beverages.xlsx) and FNDDS Nutrient Values (https://www.ars.usda.gov/ARSUserFiles/80400530/apps/2019-2020%20FNDDS%20At%20A%20Glance%20-%20FNDDS%20Nutrient%20Values.xlsx)

**File 1- README.md:**

- This file is the file that you are currently within. It serves as a summary of the project as well as all of the associated files. 

**File 2- README.pdf:**

- This is the pdf version of the README.md file 

**File 3- Thumb.png:**

- This file serves as the cover image for the project. 

**File 4- index.yml:**

- This file summarizes the project's title, contributors, and abstract for public availability. 

**File 5- DB_initialization.m**

- This MATLAB script downloads the .xls files from the FNDDS website if they don't exist, creates a sqlite file in the data directory, then establishes a connection with the sqlite database file to incorporate all of the data into separate tables to later be conjoined and initializes the DataEntry.mlapp application. 

**File 6- DataEntry.mlapp:**

- This MATLAB appdesigner file (.mlapp) utilizes the MATLAB software to generate a graphical user interface that preloads the distinct food descriptions so that the user may submit with autocomplete
- Inputs:
    - Date (mm/dd/yyyy)
    - Food Name/Description
    - Portion (g)
    - Height (ft)
    - Weight (lbs.)

**File 7- DataAnalysis.mlapp:**

- This MATLAB appdesigner file (.mlapp) utilizes the MATLAB software to generate a graphical user interface that queries the sqlite database based on the user's inputs to determine the caloric intakes of food and graph them over time. The GUI also calculates the user's BMI based on previous user input.

**File 8- report.docx**

- This file represents the formal report that discusses the project need

**File 9- design.pptx**

- This design slideshow presents the general breakdown of the database tables, the SQLite perspective, the queries and the script functionalities. 

**File 10- sketch.jpg**

- This file provides a preliminary example of what we expect the GUI to look like. 

