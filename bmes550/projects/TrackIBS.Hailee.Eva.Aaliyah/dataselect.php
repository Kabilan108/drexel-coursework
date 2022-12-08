

<?php
session_start();
//require_once "configure.php";

//due to the problems with connection the session variable will not pull
//$username =  $_SESSION['username'];

$username = 'testuser';

//DIRECT FILEPATH DATABSE LINK due to lack of connection to database
$dir = 'sqlite:C:/Users/Administrator/Downloads/sqlitestudio-3.3.3/SQLiteStudio/ibstracker.db';

class MyDB extends SQLite3
{
   function __construct()
   {
      $this->open('C:/Users/Administrator/Downloads/sqlitestudio-3.3.3/SQLiteStudio/ibstracker.db');
   }
}
$db = new MyDB();
if(!$db){
   echo $db->lastErrorMsg();
} else {
   //echo "Opened database successfully\n";

}
///

//XX a query to pull all distinct months that contain data under the username
$sql =<<<EOF
      SELECT distinct(month) FROM symptoms WHERE username = $username;
EOF;

   $ret = $db->query($sql);

?>




<form action="" method="POST" style="text-align: center;">
<select name="month" size='1' style="font-family : monospace; font-size : 18pt">
    <?php
    //while there are results from the user's date query, assign the distinct values to the select via converting the value to a time value, then to its corosponding word and numeric value
    while ($row = $ret->fetchArray(SQLITE3_ASSOC)) {
        $time = strtotime(sprintf('%d months', $row['month']));   
        $label = date('F', $time);   
        $value = date('n', $time);
        echo "<option value='$value' >$label</option>";
    }
    ?>
</select>

<input type="submit" value="Submit" name="submit" style="font-family : monospace; font-size : 17pt">
</form>

<?php



//establish the different arrays for future graphs
$anxiety = array(); //nervous
$bmovement = array(); //stooltype
//$sleep = array();
$abpain = array();
$recpain = array();
$backpain = array();
$bodyache =array();
$headache = array();
//$username = 'testuser'; //CHANGE LATER

if(!isset($_REQUEST['submit'])){
   echo '<h1 style="text-align: center; font-size : 18pt; font-family: '."Hind Siliguri".';">
   
   Choose a Month for Summary </h1>';
}


if(isset($_REQUEST['submit'])){
   $mon = $_REQUEST['month'];
   $year = date('Y');

   echo '<h2 style="text-align: center; font-size : 28pt; font-family: '."Hind Siliguri".';">
   
         Showing Month Summary for ' . "$mon/$year", '</h2>';
   

   //query and store results CHANGE LATER
    $sql = "SELECT * FROM symptoms WHERE year = $year AND month = $mon AND username = $username";
    $result = $db->query($sql);  

    while($row = $result->fetchArray(SQLITE3_ASSOC) ){
      $datas[] = $row;
    }
    foreach ($datas as $i){
      $day[] = $i ['day'];
      $bmovement[] = $i['stooltype'];
      $anxiety[] = $i['bai10']; //nervousness
      //$sleep[] = $i['sleep'];
      $abpain[] = $i['abpain'];
      $recpain[] = $i['recpain'];
      $backpain[] = $i['backpain'];
      $bodyache[] =$i['bodyache'];
      $headache[] = $i['headache'];
     
    }
   } 
   $db->close();
?>

