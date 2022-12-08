# **READ ME**
## Cystic Fibrosis Survey
## By Corine, Sam, and Soham

### ***How to set up the survey***
This GUI system and files are all used together to create a symptom tracker for cystic fibrosis. To get you started, MATLAB will need to be installed at the mathworks website listed here: https://www.mathworks.com/. Once MATLAB is installed, the Database toolbox will need to be added. Go into MATLAB and under home click add-ons. Look up the Database toolbox and install. After that, MATLAB can be closed.

### ***How to fill out survey***
To get started, open the file Login_Screen.mlapp. This should be opened through the file explorer, and not from within MATLAB. A login screen will pop up, and after registering as a user, the survey can be filled out. Keep in mind that the SQL database file will be saved in a temporary directory.

### ***Code file descriptions***
A short description of every code that is involved in the symptom tracker is as follows:

**Login_Screen.mlapp:** Allows a user to input their username and password for a login attempt or to go to the user registration GUI if they are a new user.
**User_Registration.mlapp:** GUI that allows the user to create a new user.
**Symptom_Survey.mlapp:** GUI where the user fills in cystic fibrosis symptoms.
**Disp_Database.mlapp:** GUI that displays the table of symptoms that the user has inputted over a period of time.

**usermatch.m:** Used to determine if a user with the same username already exists.
**RegisterEncrypted.m:**  Used to register a user, saving inputted user registration information into the User Database.
**PassMatch.m:** Compares the username and password combination with a database of users and prompts the login screen to advance to the symptom survey if the combination exists or prompts the login screen to display an error.
**encrypt_pass.m:** Function that uses the md5 file function to encrypt inputted passwords
**ImportData.m:** Takes survey results and adds it to an SQL database.
**Database.m:** Pulls out symptoms from SQL database for the specific user logged in.
**md5.m:** Used to encrypt a given inputted text file, used in GUI to encrypt inputted passwords to prevent others from accessing stored user passwords from User Database.

### ***Disclaimers***
Our symptom tracker was loosely based on the following article:
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4371465/ 

Used md5 code from: 
Stefan Stoll (2022). MD5 signature of a file (https://www.mathworks.com/matlabcentral/fileexchange/5498-md5-signature-of-a-file), MATLAB Central File Exchange. Retrieved December 1, 2022.
