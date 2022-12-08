<?php

session_start();
if(!$_SESSION['loggedin'])die('This page requires login');

// If "submit" was pressed, store all user input variables using session
if(isset($_REQUEST['submit'])) {
    $_SESSION['submit']=$_REQUEST['submit']; //store in session variable
    $_SESSION['imgdate']=$_REQUEST['imgdate'];
    $_SESSION['moleid']=$_REQUEST['moleid'];
    
}
session_commit();

// If submit was not pressed, display the form.
if(!isset($_REQUEST['submit'])) {
    echo "
    <html>
        <body>
            <h1><b>Melanoma Tracker</b></h1>
            <center><b><div class='navbar'>
                <p> Hello ".$_SESSION['username']."!</p>
                <a class='active' href='test_submitting.php'>Submit Image</a>
                <a href='history.php'>View History</a>
            </div></b></center>
            <form id='submitimg' method='post' enctype='multipart/form-data'>
                <br>Date of Image: <input type=date name='imgdate' required></br>
                <br>Please assign a number to this mole. All images for one mole should be assigned the same number.</br>
                <br>Mole Number: <input type='number' name='moleid' min='1' required></br>
                <br><br>Please upload an image. (Accepted file type:.jpg, .png)</br></br> 
		    <br><input type='file' name='myImage' accept='.jpeg, .jpg' required></br>
                <br><input type='submit' name='submit'></br>
            </form>
        </body>
    </html> ";
}

// If 'submit' HAS been selected, display the "history" php page and upload date to moleinfo table in database
#Save user entries to php page as variables
elseif(isset($_REQUEST['submit'])) {
    $image_date=$_REQUEST['imgdate'];
    $mole_id=$_REQUEST['moleid'];

#### LINK TO MATLAB #################################

	#Check that the file uploaded is only a jpeg/png
    $temp_file = $_FILES['myImage']['tmp_name'];
    
    # Local computer testing
	#Using __DIR__ -> don't have to check system
    #set_time_limit(300);
	$cmd="matlab.exe -wait -nosplash -nodesktop -r \"cd('".__DIR__."'); molesize_export('".$temp_file."'); quit;\"  ";
    
    exec($cmd);

    # Get risk and molesize from molesize.
    $outfile="$temp_file.out";
    if(!file_exists($outfile)){
        die("Matlab failed to produce an output file. Something went wrong...");
    }

    $s = file_get_contents($outfile);
    #echo "Filecontents: [$s]";
    $ss = explode("\n",$s);
    #echo "<pre>"; print_r($ss); echo "</pre>";
    $diameter = $ss[0];
    $risk = $ss[1];
    #dbtable: overlayfiles [ id, path]
    $path="$temp_file.overlay.jpg";
    #"INSERT into overlayfiles(path) VALUES('$path')"

	#Allow the user to resubmit an image
    echo "
    <html>
        <body>
            <h1><b>Melanoma Tracker</b></h1>
            <center><b><div class='navbar'>
                <p>Hello ".$_SESSION['username']."!</p>
                <a class='active' href='submitting.php'>Submit Image</a>
                <a href='history.php'>View History</a>
            </div></b></center>
            <form id='submitimg' method='post' enctype='multipart/form-data'>
                <br>Date of Image: <input type=date name='imgdate' required></br>
                <br>Please assign a number to this mole. All images for one mole should be assigned the same number.</br>
                <br>Mole Number: <input type='number' name='moleid' min='1' required></br>
                <br><br>Please upload an image. (Accepted file type:.jpg, .png)</br></br> 
		    <br><input type='file' name='myImage' accept='.jpeg, .jpg' required></br>
                <br><input type='submit' name='submit'></br>
            </form>
        </body>
    </html> ";

    echo "<center><p><b>Your risk is: $risk and the calculated diameter is $diameter mm</b></p></center>";
    echo "<center><img src='showoverlay.php?path=$path'></center>";

#### Link to Database ##########################
   #require_once 'init.php';
   #$db=connectdb();

    ##Trying to connect to the database 
    $dir = dirname(__DIR__, 2);
    $dbfile=$dir.'\MelanomaData.sqlite'; #if you are using a large database file (>10 MB), please keep it elsewhere on your computer.
    #echo "$dbfile";

    #create database connection
    $db=new PDO("sqlite:$dbfile");
    $db->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
    #return $db;

    set_time_limit(300);
######### Creating 'moleinfo' Table if does not exist ##############
    function doesdbtableexist($db,$tablename){
    #AND name='$userinfo'
        $results =$db->query("SELECT name FROM sqlite_master WHERE type='table' AND name='$tablename';'")->fetch();
	    return $results['name'];
    
    }
    
    $results = doesdbtableexist($db,'moleinfo');
    #echo isset($results);

    # If moleinfo table does not exist, create it.
    if(!isset($results)) {
	    $db->exec("BEGIN TRANSACTION"); #group statements that should work together in a transaction.
	    $db->exec("CREATE TABLE IF NOT EXISTS moleinfo(id PRIMARY KEY, User_ID INTEGER, Img_Date VARCHAR(255) ,Mole_Size FLOAT(6), Risk VARCHAR(255), Mole_ID INTEGER)");
        $db->exec("COMMIT");
    }

###### Obtain userid based on username which was input to previous php page (home.php or newuser.php) #############

    ## Pull username from previous php page (or from url)
    # 1) Determine the previous php page that directed you to test_submitting.php
    # 2) Extract the username variable that was stored on that page
    $username=$_SESSION['username']; #get from createnewuser.php or home.php
    
    ## Find corresponding userid for the username 
    $userinfo_userid= $db->query("Select User_ID FROM userinfo WHERE username='$username'")->fetch();
	$userid = $userinfo_userid['User_ID'];

##### Populating moleinfo table ###############################

    $sqlquery="INSERT INTO moleinfo(User_ID,Img_Date, Mole_Size, Risk, Mole_ID) VALUES('$userid','$image_date', '$diameter','$risk', '$mole_id');";
    #echo "$sqlquery";
	$db->exec($sqlquery);

##### Redirecting to history.php page ####################
 # prevent redirect here and just show image with risk and diameter value
 
#  header("Location: history.php");
 # exit();  



}  

?>