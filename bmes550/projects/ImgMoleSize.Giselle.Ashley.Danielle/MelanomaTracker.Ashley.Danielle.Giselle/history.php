<?php 
session_start();
if(!$_SESSION['loggedin'])die('This page requires login');
#Get the user name info
$user=$_SESSION['username']; 
if (isset($_REQUEST['mole_id'])){
	$moleID=$_REQUEST['mole_id']; 
} 
else {
	$moleID=1;
}
#echo $moleID;

#Make the database connection
#### PDO SQLITE
	##Connect to the database
	$dir = dirname(__DIR__, 2);
	$db = new PDO('sqlite:'.$dir.'/MelanomaData.sqlite');
	
	

	##Find what the UserID is for that username
	$results =$db->query("Select User_ID FROM userinfo WHERE username='$user'")->fetch();
	#print_r($results);
	$userid = $results['User_ID'];
	//echo $userid;


	$mole_ids = array();
	foreach($db->query("Select Mole_ID FROM moleinfo WHERE User_ID=\"$userid\"") as $row){
		if (!in_array($row['Mole_ID'],$mole_ids)){
			array_push($mole_ids, $row['Mole_ID']);
		}
	}
	#print_r($mole_ids);
	


	## Handle if user has no mole information printed

	## Get the associated mole information for a User_ID

	#Create an arrays to store information
	$img_dates = array();
	$mole_size = array();
	$mole_risk = array();
	#Loop through and display the select entries
	if (!is_null($moleID)){
		foreach($db->query("Select Img_Date, Mole_Size, Risk FROM moleinfo WHERE User_ID=\"$userid\" AND Mole_ID=\"$moleID\" ORDER BY Img_Date") as $row){
			array_push($img_dates, $row['Img_Date']);
			array_push($mole_size, $row['Mole_Size']);
			array_push($mole_risk, $row['Risk']);
			
		}
	}
	else {
		foreach($db->query("Select Img_Date, Mole_Size, Risk FROM moleinfo WHERE User_ID=\"$userid\" AND Mole_ID=1 ORDER BY Img_Date") as $row){
			array_push($img_dates, $row['Img_Date']);
			array_push($mole_size, $row['Mole_Size']);
			array_push($mole_risk, $row['Risk']);
			
		}
	}
	

	##



####


echo "
    <html>
	  <head>
    		<script src=\"lib/jquery/jquery.min.js\"></script>
    		
			<link href=\"history.css\" rel=\"stylesheet\">
			<script src=\"history.js\"></script>
			
		
	  </head>
        <body>
            <h1><b>Melanoma Tracker</b></h1>
            <center><b><div class='navbar'>
                <p>Hello $user!</p>
                <a class='active' href='test_submitting.php'>Submit Image</a>
                <a href='history.php'>View History</a>
            </div></b></center>

			<center>
			<div class=\"dropdown\">
				<button class=\"dropbtn\">Select a Mole</button>
					<div class=\"dropdown-content\" id=\"myDropDown\">
					</div> 
			</div>
			</center>

			<center><h2>Growth of Mole: $moleID</h2></center>
			
			<center><div style=\"max-height: 400px;max-width:1000px;overflow: scroll;margin:20px; display: flex; flex-direction: \"row\";\">
			<div style=\"margin-top:175px;margin-right:50px; font-size:24\">Mole Size (mm)</div>
			<canvas id=\"myCanvas\" height=\"390px\" width=\"1400px\" style=\"border:1px solid grey; \"></canvas>
			</div>
			<div style=\"font-size:24\">Image Date</div>
			</center>
			
			
			
			
	    	<script>
				var max_height=1400;
				var max_width=1000;
				var xArray =[\" ". implode('", "', $img_dates) ." \"];
				var yArray =[\" ". implode(', ', $mole_size) ." \"];
				var molArray=[\"". implode('", "', $mole_ids) ."\"];
				$(function() {
					// create your Grapher here within the #myCanvas canvas
					graph = new Grapher();
					graph.build('#myCanvas',max_height,max_width,xArray,yArray);

					// populate the dropdown menu based on the number of moles
					moleContent = new Mole();
					moleContent.populate('#myDropDown',\"$user\", molArray);
				});
        		
    		</script>
        </body>
    </html> ";


    

?>