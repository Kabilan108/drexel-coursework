<style>
	pre{
		border:1px solid red;
		padding:10px;
	}
</style>
<?
if(!strncmp(gethostname(),'sacan',5)) require_once getenv('AHMETLIBPHP').'/ahmet.php';


$MLEXE='matlab';
if(strtoupper(substr(PHP_OS, 0, 3)) === 'WIN'){
	if(file_exists($try='C:\Program Files\MATLAB\R2017a\bin\matlab.exe')) $MLEXE=$try;
	if(file_exists($try='C:\Program Files\MATLAB\R2018b\bin\matlab.exe')) $MLEXE=$try;
	
}
else{
	#On MAC, matlab is probably on the path already. So, nothing to do.
}

$cmd="\"$MLEXE\" -nosplash -logfile runmatlab.out -r \"disp(sample(5,6)); 
open "iamdonefile.txt"
write "yes" in that file
exit;\"";
echo "<p>Running Command: <pre>$cmd</pre></p>";
set_time_limit(60); #extend maximum run time for php so it doesn't terminate us.
$out=exec($cmd);
sleep(20); #wait some time for matlab to complete...
echo "<p>Output from matlab commandline:</p> <pre>$out</pre>";
echo "<p>Output from sample() is:</p> <pre>".file_get_contents('runmatlab.out')."</pre>";


echo "<hr><h2>Source Code</h2>"; show_source(__FILE__);
