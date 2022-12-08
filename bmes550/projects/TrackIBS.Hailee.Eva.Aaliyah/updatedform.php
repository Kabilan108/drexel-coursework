<!-- By Hailee Mayer--> 
<html>
<head>
    <title>IBS SYMPTOM TRACKER</title>

<style>
  body {background-color: powderblue;}
  
  p {
        color: blue;
        background-color: white;
        padding: 5px;
        border: 1px solid black;
    }

</style>
</head>

<body>
<?php

// do i need to start a session or do we assume one has started already when we reach this code

// Check if the form was submitted
if (isset($_POST['abpain'], $_POST['recpain'], $_POST['backpain'], $_POST['bodyache'], $_POST['headache'], $_POST['stooltype'], $_POST['stoolcolor'], $_POST['stoolpain'], $_POST['stooltype'], $_POST['bai1'], $_POST['bai2'],$_POST['bai3'],$_POST['bai4'],$_POST['bai5'],$_POST['bai6'],$_POST['bai7'],$_POST['bai8'],$_POST['bai9'],$_POST['bai10'],$_POST['bai11'],$_POST['bai12'],$_POST['bai13'],$_POST['bai14'],$_POST['bai15'],$_POST['bai16'],$_POST['bai17'],$_POST['bai18'],$_POST['bai19'],$_POST['bai20'],$_POST['bai21'])) {
	// Process form data 
	// Assign POST variables
	$abpain = $_POST['abpain'];
	$recpain = $_POST['recpain'];
	$backpain = $_POST['backpain'];
	$bodyache = $_POST['bodyache'];
	$headache = $_POST['headache'];
	$stooltype = $_POST['stooltype'];
    $stoolcolor = $_POST['stoolcolor'];
    $stoolpain = $_POST['stoolpain'];
    $bai1 = $_POST['bai1'];
    $bai2 = $_POST['bai2'];
    $bai3 = $_POST['bai3'];
    $bai4 = $_POST['bai4'];
    $bai5 = $_POST['bai5'];
    $bai6 = $_POST['bai6'];
    $bai7 = $_POST['bai7'];
    $bai8 = $_POST['bai8'];
    $bai9 = $_POST['bai9'];
    $bai10 = $_POST['bai10'];
    $bai11 = $_POST['bai11'];
    $bai12 = $_POST['bai12'];
    $bai13 = $_POST['bai13'];
    $bai14 = $_POST['bai14'];
    $bai15 = $_POST['bai15'];
    $bai16 = $_POST['bai16'];
    $bai17 = $_POST['bai17'];
    $bai18 = $_POST['bai18'];
    $bai19 = $_POST['bai19'];
    $bai20 = $_POST['bai20'];
    $bai21 = $_POST['bai21'];
    $otherpain = $_POST['otherpain'];
    $othersymptoms = $_POST['othersymptoms'];
    $notes = $_POST['notes'];

} 
else {
		<php>
			echo "Data not submitted";
		</php> 
	}
}
<p> Welcome to your daily IBS Symptom tracker</p> 
<form method="post" action="datadisplay.php">	

      <label for="date">
       Enter Today's Date:
        <input type="date" name="date">
    </label>
	

		<p>How would you rate your abdominal pain today?</p>
		
			<input type="radio" name="abpain" id="radio1" value=1>
			<label for="radio1">None/Minimal</label>
			<input type="radio" name="abpain" id="radio2" value=2>
			<label for="radio2">Mild</label>
			<input type="radio" name="abpain" id="radio3" value=3>
			<label for="radio3">Moderate</label>
			<input type="radio" name="abpain" id="radio4" value=4>
			<label for="radio4">Severe</label>
			<input type="radio" name="abpain" id="radio5" value=5>
			<label for="radio5">Very Severe</label>
	
		
        <p>How would you rate your rectal pain today?</p>
   		
		    <input type="radio" name="recpain" id="radio6" value=1>
		    <label for="radio6">None/Minimal</label>
		    <input type="radio" name="recpain" id="radio7" value=2>
		    <label for="radio7">Mild</label>
		    <input type="radio" name="recpain" id="radio8" value=3>
		    <label for="radio8">Moderate</label>
		    <input type="radio" name="recpain" id="radio9" value=4>
		    <label for="radio9">Severe</label>
		    <input type="radio" name="recpain" id="radio10" value=5>
		    <label for="radio10">Very Severe</label>
	

        <p>How would you rate your lower back pain today?</p>
   		
		    <input type="radio" name="backpain" id="radio11" value=1>
		    <label for="radio11">None/Minimal</label>
		    <input type="radio" name="backpain" id="radio12" value=2>
		    <label for="radio12">Mild</label>
		    <input type="radio" name="backpain" id="radio13" value=3>
		    <label for="radio13">Moderate</label>
		    <input type="radio" name="recpain" id="radio14" value=4>
		    <label for="radio14">Severe</label>
		    <input type="radio" name="backpain" id="radio15" value=5>
		    <label for="radio15">Very Severe</label>
		
        <p>How would you rate your Body Aches today?</p>
   		
		    <input type="radio" name="bodyache" id="radio16" value=1>
		    <label for="radio16">None/Minimal</label>
		    <input type="radio" name="bodyache" id="radio17" value=2>
		    <label for="radio17">Mild</label>
		    <input type="radio" name="bodyache" id="radio18" value=3>
		    <label for="radio18">Moderate</label>
		    <input type="radio" name="bodyache" id="radio19" value=4>
		    <label for="radio19">Severe</label>
		    <input type="radio" name="bodyache" id="radio20" value=5>
		    <label for="radio20">Very Severe</label>
		
        <p>How would you rate your Head Aches today?</p>
   		
		    <input type="radio" name="headache" id="radio21" value=1>
		    <label for="radio21">None/Minimal</label>
		    <input type="radio" name="headache" id="radio22" value=2>
		    <label for="radio22">Mild</label>
		    <input type="radio" name="bodyache" id="radio23" value=3>
		    <label for="radio23">Moderate</label>
		    <input type="radio" name="headache" id="radio24" value=4>
		    <label for="radio24">Severe</label>
		    <input type="radio" name="headache" id="radio25" value=5>
		    <label for="radio25">Very Severe</label>
		


<!--page 2-->

   <p> Please rate your stool type today</p>
	
			<input type="radio" name="stooltype" id="radio26" value=1>
			<label for="radio26">Severe Constispation</label>
			<input type="radio" name="stooltype" id="radio27" value=2>
			<label for="radio27">Mild Constipation</label>
			<input type="radio" name="stooltype" id="radio28" value=3>
			<label for="radio28">Normal</label>
			<input type="radio" name="stooltype" id="radio29" value=4>
			<label for="radio29">Mild Diarrhea</label>
			<input type="radio" name="stooltype" id="radio30" value=5>
			<label for="radio30">Severe Diarrhea</label>
    </div>
        <p>What color was your stool today?</p>
 
            <input type="radio" name="stoolcolor" id="radio31" value=1>
			<label for="radio31">Brown</label>
			<input type="radio" name="stooltype" id="radio32" value=2>
			<label for="radio32">Green</label>
			<input type="radio" name="stooltype" id="radio33" value=3>
			<label for="radio33">Bright Red</label>
			<input type="radio" name="stooltype" id="radio34" value=4>
			<label for="radio34">Black/Dark Brown</label>
			<input type="radio" name="stooltype" id="radio35" value=5>
			<label for="radio35">White/Clay-like</label>
            
        <p>Did you have any pain associated with your bowel movement today?</p>
     
            <input type="radio" name="stoolpain" id="radio36" value=1>
			<label for="radio36">None/minimal</label>
			<input type="radio" name="stoolpain" id="radio37" value=2>
			<label for="radio37">Mild Discomfort</label>
			<input type="radio" name="stoolpain" id="radio38" value=3>
			<label for="radio38">Moderate Discomfort</label>
			<input type="radio" name="stoolpain" id="radio39" value=4>
			<label for="radio39">Severe Discomfort</label>
			<input type="radio" name="stoolpain" id="radio40" value=5>
			<label for="radio40">Very Severe Discomfort</label>
    


<!---pg 3--->
<!--beck anxiety inventory-->

  
<p>Please rate the following symptoms you have experienced today<br>
    The scoring is as follows:<br>
    Not at All: 0<br>
    Mildly, but it did not bother me much: 1<br>
    Moderately, it wasn not pleasant at times: 2<br>
    Severly, it bothered me alot: 3 <br>
</p>

    <p>Numbness or Tingling</p>

            <input type="radio" name="bai1" id="radio41" value=0>
			<label for="radio41">0</label>
			<input type="radio" name="bai1" id="radio42" value=1>
			<label for="radio42">1</label>
			<input type="radio" name="bai1" id="radio43" value=2>
			<label for="radio43">2</label>
			<input type="radio" name="bai1" id="radio44" value=3>
			<label for="radio44">3</label>
        
        <p>Feeling Hot</p>

            <input type="radio" name="bai2" id="radio45" value=0>
			<label for="radio45">0</label>
			<input type="radio" name="bai2" id="radio46" value=1>
			<label for="radio46">1</label>
			<input type="radio" name="bai2" id="radio47" value=2>
			<label for="radio47">2</label>
			<input type="radio" name="bai2" id="radio48" value=3>
			<label for="radio48">3</label>
        
    <p>Wobliness in Legs</p>
   
            <input type="radio" name="bai3" id="radio49" value=0>
			<label for="radio49">0</label>
			<input type="radio" name="bai3" id="radio50" value=1>
			<label for="radio50">1</label>
			<input type="radio" name="bai3" id="radio51" value=2>
			<label for="radio51">2</label>
			<input type="radio" name="bai3" id="radio52" value=3>
			<label for="radio52">3</label>
        
    <p>Unable to Relax</p>
    
            <input type="radio" name="bai4" id="radio53" value=0>
			<label for="radio53">0</label>
			<input type="radio" name="bai4" id="radio54" value=1>
			<label for="radio54">1</label>
			<input type="radio" name="bai4" id="radio55" value=2>
			<label for="radio55">2</label>
			<input type="radio" name="bai4" id="radio56" value=3>
			<label for="radio56">3</label>
       
    <p>Fear of Worst Happening</p>
     
            <input type="radio" name="bai5" id="radio57" value=0>
			<label for="radio57">0</label>
			<input type="radio" name="bai5" id="radio58" value=1>
			<label for="radio58">1</label>
			<input type="radio" name="bai5" id="radio59" value=2>
			<label for="radio59">2</label>
			<input type="radio" name="bai5" id="radio60" value=3>
			<label for="radio60">3</label>
       
    <p>Dizzy or Lightheaded</p>
     
            <input type="radio" name="bai6" id="radio61" value=0>
			<label for="radio61">0</label>
			<input type="radio" name="bai6" id="radio62" value=1>
			<label for="radio62">1</label>
			<input type="radio" name="bai6" id="radio63" value=2>
			<label for="radio63">2</label>
			<input type="radio" name="bai6" id="radio64" value=3>
			<label for="radio64">3</label>
        
    <p>Heart pounding/racing</p>
   
            <input type="radio" name="bai7" id="radio65" value=0>
			<label for="radio65">0</label>
			<input type="radio" name="bai7" id="radio66" value=1>
			<label for="radio66">1</label>
			<input type="radio" name="bai7" id="radio67" value=2>
			<label for="radio67">2</label>
			<input type="radio" name="bai7" id="radio68" value=3>
			<label for="radio68">3</label>
       
    <p>Unsteady</p>
      
            <input type="radio" name="bai8" id="radio69" value=0>
			<label for="radio69">0</label>
			<input type="radio" name="bai8" id="radio70" value=1>
			<label for="radio70">1</label>
			<input type="radio" name="bai8" id="radio71" value=2>
			<label for="radio71">2</label>
			<input type="radio" name="bai8" id="radio72" value=3>
			<label for="radio72">3</label>
       
    <p>Terrified or Afraid</p>
     
            <input type="radio" name="bai9" id="radio73" value=0>
			<label for="radio73">0</label>
			<input type="radio" name="bai9" id="radio74" value=1>
			<label for="radio74">1</label>
			<input type="radio" name="bai9" id="radio75" value=2>
			<label for="radio75">2</label>
			<input type="radio" name="bai9" id="radio76" value=3>
			<label for="radio76">3</label>
       
    <p>Nervous</p>
    
            <input type="radio" name="bai10" id="radio77" value=0>
			<label for="radio77">0</label>
			<input type="radio" name="bai10" id="radio78" value=1>
			<label for="radio78">1</label>
			<input type="radio" name="bai10" id="radio79" value=2>
			<label for="radio79">2</label>
			<input type="radio" name="bai10" id="radio80" value=3>
			<label for="radio80">3</label>
       
    <p>Feeling of Choking</p>
    
            <input type="radio" name="bai11" id="radio81" value=0>
			<label for="radio81">0</label>
			<input type="radio" name="bai11" id="radio82" value=1>
			<label for="radio82">1</label>
			<input type="radio" name="bai11" id="radio83" value=2>
			<label for="radio83">2</label>
			<input type="radio" name="bai11" id="radio84" value=3>
			<label for="radio84">3</label>
      
    <p>Hands Trembling</p>
   
            <input type="radio" name="bai12" id="radio85" value=0>
			<label for="radio85">0</label>
			<input type="radio" name="bai12" id="radio86" value=1>
			<label for="radio86">1</label>
			<input type="radio" name="bai12" id="radio87" value=2>
			<label for="radio87">2</label>
			<input type="radio" name="bai12" id="radio88" value=3>
			<label for="radio88">3</label>
       
    <p>Shaky/Unsteady </p>
     
            <input type="radio" name="bai13" id="radio89" value=0>
			<label for="radio89">0</label>
			<input type="radio" name="bai13" id="radio90" value=1>
			<label for="radio90">1</label>
			<input type="radio" name="bai13" id="radio91" value=2>
			<label for="radio91">2</label>
			<input type="radio" name="bai13" id="radio92" value=3>
			<label for="radio92">3</label>
        
    <p>Fear of Losing Control</p>
      
            <input type="radio" name="bai14" id="radio93" value=0>
			<label for="radio93">0</label>
			<input type="radio" name="bai14" id="radio94" value=1>
			<label for="radio94">1</label>
			<input type="radio" name="bai14" id="radio95" value=2>
			<label for="radio95">2</label>
			<input type="radio" name="bai14" id="radio96" value=3>
			<label for="radio96">3</label>
      
    <p>Difficulty Breathing</p>
       
            <input type="radio" name="bai15" id="radio97" value=0>
			<label for="radio97">0</label>
			<input type="radio" name="bai15" id="radio98" value=1>
			<label for="radio98">1</label>
			<input type="radio" name="bai15" id="radio99" value=2>
			<label for="radio99">2</label>
			<input type="radio" name="bai15" id="radio100" value=3>
			<label for="radio100">3</label>
      
    <p>Fear of Dying</p>
     
            <input type="radio" name="bai16" id="radio101" value=0>
			<label for="radio101">0</label>
			<input type="radio" name="bai16" id="radio102" value=1>
			<label for="radio102">1</label>
			<input type="radio" name="bai16" id="radio103" value=2>
			<label for="radio103">2</label>
			<input type="radio" name="bai16" id="radio104" value=3>
			<label for="radio104">3</label>
       
    <p>Scared</p>
    
            <input type="radio" name="bai17" id="radio105" value=0>
			<label for="radio105">0</label>
			<input type="radio" name="bai17" id="radio106" value=1>
			<label for="radio106">1</label>
			<input type="radio" name="bai17" id="radio107" value=2>
			<label for="radio107">2</label>
			<input type="radio" name="bai17" id="radio108" value=3>
			<label for="radio108">3</label>
     
    <p>Indigestion</p>
        
            <input type="radio" name="bai18" id="radio109" value=0>
			<label for="radio109">0</label>
			<input type="radio" name="bai18" id="radio110" value=1>
			<label for="radio110">1</label>
			<input type="radio" name="bai18" id="radio111" value=2>
			<label for="radio111">2</label>
			<input type="radio" name="bai18" id="radio112" value=3>
			<label for="radio112">3</label>
     
    <p>Faint/Light-headed</p>
     
            <input type="radio" name="bai19" id="radio113" value=0>
			<label for="radio113">0</label>
			<input type="radio" name="bai19" id="radio114" value=1>
			<label for="radio114">1</label>
			<input type="radio" name="bai19" id="radio115" value=2>
			<label for="radio115">2</label>
			<input type="radio" name="bai19" id="radio116" value=3>
			<label for="radio116">3</label>
    
    <p>Face Flushed</p>
        
            <input type="radio" name="bai20" id="radio117" value=0>
			<label for="radio117">0</label>
			<input type="radio" name="bai20" id="radio118" value=1>
			<label for="radio118">1</label>
			<input type="radio" name="bai20" id="radio119" value=2>
			<label for="radio119">2</label>
			<input type="radio" name="bai20" id="radio120" value=3>
			<label for="radio121">3</label>
      
    <p>Hot/Cold Sweats</p>
        
            <input type="radio" name="bai21" id="radio122" value=0>
			<label for="radio122">0</label>
			<input type="radio" name="bai21" id="radio123" value=1>
			<label for="radio123">1</label>
			<input type="radio" name="bai21" id="radio124" value=2>
			<label for="radio124">2</label>
			<input type="radio" name="bai21" id="radio125" value=3>
			<label for="radio125">3</label>
     


<p> Please record any other symptoms, pain, or notes you'd like to note from today. </p>
    <label for="otherpain">Other Pain:</label><br>
    <input type="text" id="otherpain" name="otherpain"><br>
    <label for="othersymptoms">Other Symptoms:</label><br>
    <input type="text" id="othersymptoms" name="othersymptoms"><br>
    <label for="notes">Additional Notes:</label><br>
    <input type="text" id="notes" name="notes"><br>
    
<input type="submit" value="Submit" name="submit" style="font-family : monospace; font-size : 17pt">

		</form>


	</body>
</html>
