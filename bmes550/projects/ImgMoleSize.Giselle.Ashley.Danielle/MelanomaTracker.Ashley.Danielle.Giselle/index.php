<?php

session_start();

#// If "Login" was selected, store all variables using session
if(isset($_REQUEST['login'])) {
    $_SESSION['login']=$_REQUEST['login']; //store in session variable
    $_SESSION['username']=$_REQUEST['username'];
    $_SESSION['password']=$_REQUEST['password'];
    $userinput_password = $_SESSION['password'];
    $encrypt_pass = md5($userinput_password);
    $_SESSION['encrypt_pass']=$encrypt_pass;
    $_SESSION['loggedin']=1;
    #echo "$encrypt_pass";
    #echo "$userinput_password";
}
session_commit();



// If nothing has been pressed, display the form.
echo "
    <html>
        <center>
            <body>
                <h1><b>Melanoma Tracker</b></h1>
                <h3><b>Login</b></h3>
                <form id='login'>
                    <br>Username: <input type=text name='username'></br>
                    <br>Password: <input type='password' id='password' name='password'></br>
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
                    <br><input name='login' type=submit value='Login'>
                    <a href='newuser_connection.php'><button type='button'>Create New User</button></a></br>
                </form>  
            </body>
        </center>
</html>
";

# If login button was selected, verify entries with userinfo table in database
if(isset($_REQUEST['login'])) { 
   
    # save user entries for username and password into variables
    $username = $_SESSION['username'];
    $encrypt_pass = $_SESSION['encrypt_pass'];
    #echo "$encrypt_pass";

########## Connect to Database ##############################

    ##Trying to connect to the database 
    $dir = dirname(__DIR__, 2);
    $dbfile=$dir.'/MelanomaData.sqlite'; #if you are using a large database file (>10 MB), please keep it elsewhere on your computer.
    
    # If the database file doesn't exist
    if (!file_exists($dbfile)) {
        touch($dbfile);
    }
    #create database connection
    $db=new PDO("sqlite:$dbfile");
    $db->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
    
    ## Checking if userinfo exists --> not sure why it as name here and what to replace it with 
    function doesdbtableexist($db, $tablename){
    	$results = $db->query("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='$tablename'")->fetch();
        return $results['count(*)'];
    }

######### Creating 'userinfo' Table if does not exist ##############

    $tbexist = doesdbtableexist($db,'userinfo');

    # If userinfo table does not exist, create it.
    if($tbexist==0){
        echo "<center><br><p style='color:red; font-weight:bold'>No users exist. Create a New User.</p></br></center>";
    }
    else{

###### Obtain userid based on username which was input to previous php page (home.php or newuser.php) #############

    ## Find corresponding userid for the username 
    $results=$db->query("SELECT COUNT(username) AS count FROM userinfo WHERE username='$username' AND password='$encrypt_pass'")->fetch();
    #print_r($results);
	$count = $results['count'];
    echo "$count";

    # If incorrect username/password, display error and form.
    if($count==1) {
        $results2=$db->query("SELECT firstname, lastname FROM userinfo WHERE username='$username' AND password='$encrypt_pass';")->fetch();
        print_r($results2);
        #session_start();
        $_SESSION['firstname'] = $results2['firstname'];
        $_SESSION['lastname'] = $results2['lastname'];
        $_SESSION['loggedin']=1;
        header("Location: test_submitting.php");
        exit(); 

    # If correct username/password, redirect to history.php.
    } elseif($count==0) {
        echo "<center><br><p style='color:red; font-weight:bold'>Incorrect Username or Password!</p></br></center>";   
    }
    }

}

?>