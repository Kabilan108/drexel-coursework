<?php #hwweb_tester.php by AhmetSacan.

session_start();
$basehref=&$_SESSION['basehref'];
if(isset($_REQUEST['basehref'])) $basehref=$_REQUEST['basehref'];
//automatically determine the URL folder of this tester:
if(!$basehref){
    if(isset($_SERVER['SCRIPT_URI'])) $selfurl=$_SERVER['SCRIPT_URI'];
    else{
     $uri=$_SERVER['REQUEST_URI'];
     list($selfurl)=explode('?',$uri);
    }
    $basehref=dirname($selfurl);
}
//todo: in the future, move this into the if statement above.
if(!preg_match('#https?://#',$basehref)){
	$basehref=($_SERVER['REQUEST_SCHEME']?:'http')."://$_SERVER[SERVER_NAME]:$_SERVER[SERVER_PORT]$basehref";
}
session_commit();


echo "
<html>
	<head>
	<title>Homework: Web Programming in Php: Tester</title>
	</head>
<body>
View this web page in Chrome Browser. Print into PDF file when done.
<form method='POST'>
	Enter the URL of the folder for your hwweb assignment:<br>
	<input type='text' name='basehref' value='$_SESSION[basehref]' size=64>
	<input type='submit' name='submit'>
</form>
<hr>
	
	<h3>Periodic Table of Elements</h3>
	<iframe src='$basehref/periodictable.html' height=460px width='100%'></iframe>";


function hwweb_testphpfile($phpfile,$params=null){
	echo "Getting webpage [$phpfile";
	if($params){
		$ss=[];
		foreach($params as $name=>$val){
			if(is_a($val,'CURLFile')){
				$ss[]="$name=@".basename($val->getFilename());
			}
			else $ss[]="$name=$val";
		}
		echo "?".implode('&',$ss);
	}
	echo "] ...<br>";
	$curl = curl_init();
	curl_setopt($curl, CURLOPT_URL, $_SESSION['basehref']."/$phpfile");
	curl_setopt($curl, CURLOPT_RETURNTRANSFER,1);
	$cookiefile=sys_get_temp_dir()."/hwweb_tester_cookies.bin";
	curl_setopt($curl, CURLOPT_COOKIEFILE, $cookiefile);
	curl_setopt($curl, CURLOPT_COOKIEJAR, $cookiefile);
	if($params){
	  curl_setopt($curl, CURLOPT_POST,1);
	  curl_setopt($curl, CURLOPT_POSTFIELDS, $params);
	}
	$s=curl_exec($curl);
	curl_close($curl);
	$s=str_replace("&","&amp;",$s);
	$s=str_replace("\"","&quot;",$s);
	return $s;
}

echo "<h3>File Upload: before upload</h3>";
echo "<iframe src='$basehref/fileupload.php' height=50px width='100%'></iframe>";

echo "<h3>File Upload: after upload (submit with no file)</h3>";
$s=hwweb_testphpfile('fileupload.php',['submit'=>1]);
echo "<iframe srcdoc=\"$s\" height=80px width='100%'></iframe>";

echo "<h3>File Upload: after upload</h3>";
$s=hwweb_testphpfile('fileupload.php',['myfile'=>curl_file_create(__FILE__), 'submit'=>1]);
echo "<iframe srcdoc=\"$s\" height=80px width='100%'></iframe>";


echo "<h3>Using Sessions: set myname</h3>";
$s=hwweb_testphpfile('session.php',['myname'=>'Ahmet Sacan']);
echo "<iframe srcdoc=\"$s\" height=100px width='100%'></iframe>";

echo "<h3>Using Sessions: revisit</h3>";
$s=hwweb_testphpfile('session.php');
echo "<iframe srcdoc=\"$s\" height=100px width='100%'></iframe>";

echo "<h3>Using Sessions: forgetme</h3>";
$s=hwweb_testphpfile('session.php',['forgetme'=>1]);
echo "<iframe srcdoc=\"$s\" height=100px width='100%'></iframe>";

echo "<h3>Using Sessions: revisit</h3>";
$s=hwweb_testphpfile('session.php');
echo "<iframe srcdoc=\"$s\" height=100px width='100%'></iframe>";


echo "<h3>Running Python from php: Before Submit</h3>";
$s=hwweb_testphpfile('prostaterisk.php');
echo "<iframe srcdoc=\"$s\" height=340px width='100%'></iframe>";

echo "<h3>Running Python from php: After Submit</h3>";
$s=hwweb_testphpfile('prostaterisk.php',['history'=>1,'europe'=>5,'ar_ggc'=>5,'haplotype'=>'AA','submit'=>1]);
echo "<iframe srcdoc=\"$s\" height=100px width='100%'></iframe>";

echo "<h3>Running Python from php: After Submit</h3>";
$s=hwweb_testphpfile('prostaterisk.php',['history'=>1,'europe'=>30,'ar_ggc'=>5,'haplotype'=>'GA','submit'=>1]);
echo "<iframe srcdoc=\"$s\" height=100px width='100%'></iframe>";


	echo "
</body>
</html>
";

        
