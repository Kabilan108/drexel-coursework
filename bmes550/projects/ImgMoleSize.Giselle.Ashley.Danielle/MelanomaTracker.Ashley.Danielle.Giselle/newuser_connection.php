<?php

session_start();
// If "Create New User" was selected, store all variables using session
if(isset($_REQUEST['createnewuser'])) {
    $_SESSION['createnewuser']=$_REQUEST['createnewuser']; //store in session variable
    $_SESSION['firstname']=$_REQUEST['firstname'];
    $_SESSION['lastname']=$_REQUEST['lastname'];
    $_SESSION['username']=$_REQUEST['username'];
    $_SESSION['password']=$_REQUEST['password'];
    $userinput_password = $_SESSION['password'];
    $encrypt_pass = md5($userinput_password);
    $_SESSION['encrypt_pass']=$encrypt_pass;
    $_SESSION['loggedin']=1;
}

// If "Create New User" was not selected, unset it all variables?
if(!isset($_REQUEST['createnewuser'])) {
    unset($_SESSION['createnewuser']); //unset
    unset($_SESSION['firstname']);
    unset($_SESSION['lastname']);
    unset($_SESSION['username']);
    unset($_SESSION['password']);
} 
session_commit();

// If 'createnewuser' has not been selected, show the form
if(!isset($_SESSION['createnewuser'])) {
    echo "
        <html>
            <center>
                <body>
                    <h1><b>Melanoma Tracker</b></h1>
                    <h3><b>Create New User</b></h3>
                    <form id='newuser'>
                        <br>First Name: <input type=text name='firstname' required></br>
                        <br>Last Name: <input type=text name='lastname' required></br>
                        <br>Username: <input type=text name='username' required></br>
                        <br>Password: <input type='password' id='password' name='password' required></br>
                        <br><input type='checkbox' onclick='myFunction()'> Show Password </br>
                            <script>
                                function myFunction() {
                                  var x = document.getElementById('password');
                                  if (x.type === 'password') {
                                    x.type = 'text';
                                  } else {
                                    x.type = 'password';
                                  }
                                }
                            </script>
                        <br><input name='createnewuser' type=submit value='Create New User'></br>
                    </form>  
                </body>
            </center>
        </html>";
}

// If 'createnewuser' HAS been selected, display the "Submit Image" php page
if(isset($_SESSION['createnewuser'])) {

    $first_name=$_REQUEST['firstname'];
    $last_name =$_REQUEST['lastname'];
    $user_name =$_REQUEST['username'];
    $pass_word=$encrypt_pass;

##Trying to connect to the database 
$dir = dirname(__DIR__, 2);
$dbfile=$dir.'\MelanomaData.sqlite'; #if you are using a large database file (>10 MB), please keep it elsewhere on your computer.
echo "$dbfile";
####################################################
#create database connection
$db=new PDO("sqlite:$dbfile");
$db->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);

## Checking if userinfo exists --> not sure why it as name here and what to replace it with 
function doesdbtableexist($db){
#AND name='$userinfo'
    $results =$db->query("SELECT name FROM sqlite_master WHERE type='table' AND name='userinfo';'")->fetch();
	return $results['name'];

}

$results = doesdbtableexist($db);
#echo isset($results);

####################################################
#if table does not exist, create it and add sample entries.
#TODO: it would be nice to have a function that told us whether this table exists.
#if(!$db->query("SELECT User_ID FROM userinfo")->fetch()) {
if(!isset($results)) {  
    echo "line 89";
	$db->exec("BEGIN TRANSACTION"); #group statements that should work together in a transaction.
	$db->exec("CREATE TABLE IF NOT EXISTS userinfo(User_ID INTEGER PRIMARY KEY, firstname VARCHAR(255), lastname VARCHAR(255), username VARCHAR(255) UNIQUE, password VARCHAR(255))");
    $db->exec("COMMIT");
}

#Freestying this part
    $sqlquery="INSERT INTO userinfo(firstname, lastname, username, password) VALUES('$first_name', '$last_name', '$user_name', '$pass_word');";
    #echo "$sqlquery";
	$db->exec("INSERT INTO userinfo(firstname, lastname, username, password) VALUES('$first_name', '$last_name', '$user_name', '$pass_word');");

#Redirtect to test_submiting.php
  header("Location: test_submitting.php");
  exit();  
}

?>
