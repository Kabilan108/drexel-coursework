<!-- by AhmetSacan -->
<style>
	pre{
		border:1px solid red;
		padding:10px;
	}
</style>

<?
					
if(!strncmp(gethostname(),'sacan',5)) require_once getenv('AHMETLIBPHP').'/ahmet.php';


$PYEXE='python';
if(strtoupper(substr(PHP_OS, 0, 3)) === 'WIN'){
	if(file_exists($try='C:\ProgramData\Anaconda3\python.exe')) $PYEXE=$try;
}
else{
	#On MAC, python is probably on the path already. So, nothing to do.
}

$cmd="\"$PYEXE\"  sample.py 5 6 2>&1";
echo "<p>Running Command: <pre>$cmd</pre></p>";
$out=[]; exec($cmd, $out);
echo "<p>Output from sample.py is:</p> <pre>"; print_r($out); echo "</pre>";

//echo "<hr><h2>Source Code</h2>"; show_source(__FILE__);
