


<?php

$dbfile = (__DIR__.'/ibstracker.db');

class MyDB extends SQLite3
{
   function __construct()
   {
      $this->open(__DIR__.'/ibstracker.db');
   }
}

if(!$dbfile){
    $db = new MyDB();
   echo $dbfile->lastErrorMsg();
} else {
   //echo "Opened database successfully";
    // remove the commented line above and run the file to see that a database connection was established 

}




/* Not working code based on downloaded db.php
$dbfile=__DIR__.'/ibstracker.db'; #if you are using a large database file (>10 MB), please keep it elsewhere on your computer.
#$dbfile = "...";

####################################################
#create database connection
$db=new PDO("sqlite:$dbfile");
$db->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);


function doesdbtableexist($db, $tablename){
	return $db->query("SELECT users FROM ibstracker WHERE type='table' AND name='$tablename'")->fetch();
}

####################################################
#if table does not exist, create it and add sample entries.
#TODO: it would be nice to have a function that told us whether this table exists.
if(!$db->query("SELECT username FROM ibstracker WHERE type='table' AND name='users'")->fetch()){
	$db->exec("BEGIN TRANSACTION"); #group statements that should work together in a transaction.

	$db->exec("CREATE TABLE   IF NOT EXISTS   users (
	username VARCHAR(50), 
	password VARCHAR(50)");

	$db->exec("INSERT INTO users(username, password) VALUES ('testuser', '')");


	$db->exec("COMMIT");
}



*/
?>


