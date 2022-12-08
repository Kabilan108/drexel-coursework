<?php
 session_start();
 include 'dataselect.php';



//CODE FOR AVERAGING ARRAYS
//Below all pain types are filtered for just numerical values, averaged, then counted to create an ordered pair of type, count
if(isset($_REQUEST['submit'])){

	$recpain = array_filter($recpain);
	$recavg = array_sum($recpain)/count($recpain);
	$recnum= round($recavg, 0);
	$recdata = array("label"=> "Rectal", "y"=> $recnum);

	$abpain = array_filter($abpain);
	$abavg = array_sum($abpain)/count($abpain);
	$abnum= round($abavg, 0);
	$abdata = array("label"=> "Abdominal", "y"=> $abnum);

	$backpain = array_filter($backpain);
	$backavg = array_sum($backpain)/count($backpain);
	$backnum= round($backavg, 0);
	$backdata = array("label"=> "Back", "y"=> $backnum);

	$bodyache = array_filter($bodyache);
	$bodyavg = array_sum($bodyache)/count($bodyache);
	$bodynum= round($bodyavg, 0);
	$bodydata = array("label"=> "Body", "y"=> $bodynum);

	$headache = array_filter($headache);
	$headavg = array_sum($headache)/count($headache);
	$headnum= round($headavg, 0);
	$headdata = array("label"=> "Head", "y"=> $headnum);

	//PAIN DATA POINTS
	$dataPoints = array(
		$abdata,
		$bodydata,
		$backdata,
		$headdata,
		$recdata
	);

	//CODE FOR COUNTS OF VALUES
	//Stool type charted over the month is filtered, coutned, then filed through to sort into the corrosponding stool types in a similar type, count ordered pair
	$bmovement = array_filter($bmovement);
	$bmcount = count($bmovement);
	$typecount = array();

	$sevconst = 0;
	$mildconst = 0;
	$norm = 0;
	$milddia = 0;
	$sevdia = 0;

	for($i = 0; $i < $bmcount; $i++){
		if ($bmovement[$i] == 1){
			$sevconst += 1;}
		if ($bmovement[$i] == 2){
			$mildconst += 1;}
		if ($bmovement[$i] == 3){
			$norm += 1;}
		if ($bmovement[$i] == 4){
			$milddia += 1;}
		if ($bmovement[$i] == 5){
			$sevdia += 1;}	
		}
	//prep ordered pairs and store in data array	
	$sevconst = array("label"=> "Severe Constipation", "y"=> $sevconst);
	$mildconst = array("label"=> "Mild Constipation", "y"=> $mildconst);
	$norm = array("label"=> "Normal", "y"=> $norm);
	$milddia = array("label"=> "Mild Diarreha", "y"=> $milddia);
	$sevdia = array("label"=> "Severe Diarreha", "y"=> $sevdia);
	$stoolcount = array($sevconst, $mildconst, $norm, $milddia, $sevdia);




	//LINE GRAPH
	//array is turned into float values and made into ordered pair arrays for given line graphs of day vs value
	$anxiety = array_filter($anxiety);
	$anxcount = count($anxiety);


	for($i = 0; $i < $anxcount; $i++){
		$y = floatval($anxiety[$i]); 
		$x = floatval($day[$i]);
		$pair = array("x" => $x, "y" => $y);
		//print_r($pair);
		$anxdata[] = $pair;
		}
		sort($anxdata);
		
	/*
	//LINE FOR SLEEP
	$sleep = array_filter($sleep);
	$slecount = count($sleep);


	for($i = 0; $i < $slecount; $i++){
		$y = floatval($sleep[$i]); 
		$x = floatval($day[$i]);
		$spair = array("x" => $x, "y" => $y);
		//print_r($pair);
		$sleepdata[] = $spair;
	}
	*/




}
?>

<!DOCTYPE HTML>
<html>
<head> 
    <title>Month Sumary</title>
<script>
window.onload = function () {

var painchar = new CanvasJS.Chart("chartContainer", {
	animationEnabled: true,
	theme: "light1", // "light1", "light2", "dark1", "dark2"
	title:{
		text: "Average Pain Ratings Over Chosen Month"
	},
	axisX:{
		title: "Pain Area",
	},
	axisY:{
		title: "Pain Rating, Low to High",
	},
	data: [{
		type: "column", //change type to bar, line, area, pie, etc
		indexLabelFontColor: "#5A5757",
		indexLabelPlacement: "outside",   
		dataPoints: <?php echo json_encode($dataPoints, JSON_NUMERIC_CHECK); ?>
	}]
});
painchar.render();

//NERVES LINE GRAPH
var anxiouschar = new CanvasJS.Chart("chartContainer1", {
	animationEnabled: true,
	theme: "light1", // "light1", "light2", "dark1", "dark2"
	title:{
		text: "Nervousness Over Chosen Month"
	},
	axisX:{
		title: "Day of the Month",
	},
	axisY:{
		title: "Nerve Rating, Low to High",
	},
	data: [{
		type: "line",
		indexLabelFontColor: "#5A5757",
		lineColor: "red",
		indexLabelPlacement: "outside",   
		dataPoints: <?php echo json_encode($anxdata, JSON_NUMERIC_CHECK); ?>
		
	}]
});
anxiouschar.render();

/*
//SLEEP LINE GRAPH
var sleepchar = new CanvasJS.Chart("chartContainer2", {
	animationEnabled: true,
	//exportEnabled: true,
	theme: "light1", // "light1", "light2", "dark1", "dark2"
	title:{
		text: "Sleep Quality Over Chosen Month"
	},
	axisX:{
		title: "Day of the Month",
	},
	axisY:{
		title: "Sleep Quality, Low to High",
	},
	data: [{
		type: "line", 
		indexLabelFontColor: "#5A5757",
		indexLabelPlacement: "outside",   
		dataPoints: <?php echo json_encode($sleepdata, JSON_NUMERIC_CHECK); ?>
		
	}]
});
sleepchar.render();
*/

//STOOL COUNT
var stoolchar = new CanvasJS.Chart("chartContainer3", {
	animationEnabled: true,
	theme: "light1", // "light1", "light2", "dark1", "dark2"
	title:{
		text: "Stool Types Over Chosen Month"
	},
	data: [{
		type: "pie",
		indexLabel: "{label} ({y})",   
		dataPoints: <?php echo json_encode($stoolcount, JSON_NUMERIC_CHECK); ?>
	}]
});
stoolchar.render();
}

</script>
</head>
<body style="background-color: #1abc9c;">
<div id="chartContainer" style="height: 370px; width: 100%;"></div>
<div id="chartContainer3" style="height: 370px; width: 100%;"></div>
<div id="chartContainer1" style="height: 370px; width: 100%;"></div>
<script src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>
</body>
</html>    