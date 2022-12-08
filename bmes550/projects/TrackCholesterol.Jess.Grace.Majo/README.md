# **Cholesterol Tracker**
## Jess Baggett, Grace Fan, Majo Garcia

### To run these functions MATLAB will need to be installed, it can be installed via the MathWorks website (mathworks.com). The Database toolbox will need to be installed as well.

### How to run: open login.mlapp first and run the program. Insert a username and password (doesn't matter what) and click new user. Next gui, cholesterol_tracker.mlapp should open. Fill in all data and hit submit. Results should be shown on the right.
### DISCLAIMER: Currently the input date is already set for you (set as 'today'), so you will not see multiple dates displayed on the graph unless you run the tracker on separate days.

### Functions

#### recommendations.m
##### takes the user input from cholesterol_tracker.mlapp and returns if their ldl, hdl, and total choleserol are low, high, or normal

#### md5.m
##### takes the original password that was prepped by encrypt.m and returns the encrypted version. Downloaded from https://www.mathworks.com/matlabcentral/fileexchange/5498-md5-signature-of-a-file

#### login.mlapp
##### GUI where user inputs username and password. If user is new makes sure username isn't taken and adds them to the database table users. If user is existing makes sure username and password are correct

#### history.m
##### adds the new data from cholesterol_tracker.mlapp and adds them to the SQL database table data. Outputs the last 10 data points for that user.

#### heart_risk.m
##### based on user input from cholesterol_tracker.mlapp returns the 10 year risk for developing hard coronary heart disease.


#### encrypt.m
##### preps the password the user inputed in login.mlapp and runs md5.m. md5.m only takes in text files, so it puts the password in a text file, runs md5.m and then deletes the text file.

#### cholesterol_tracker.mlapp
##### GUI where user inputs their cholesterol data, if they have diabetes, are a smoker, are taking blood pressure meds and output the results from heart_risk.m, recommendations_m, and history.m





