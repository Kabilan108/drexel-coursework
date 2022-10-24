<?
	echo "<form>
	a: <input name='a' value='$_REQUEST[a]'><br>
	b: <input name='b' value='$_REQUEST[b]'><br>
	<input type='submit'><br>
</form>
<hr>
";
					
$PYEXE='python';
if(strtoupper(substr(PHP_OS, 0, 3)) === 'WIN'){
	if(file_exists($try='C:\ProgramData\Anaconda3\python.exe')) $PYEXE=$try;
}
else{
	#On MAC, python is probably on the path already. So, nothing to do.
}
$cmd="\"$PYEXE\"  sample2.py ".escapeshellarg($_REQUEST['a'])." ".escapeshellarg($_REQUEST['b']);
echo "Running command: $cmd";

exec($cmd, $out);
$out = implode("\n", $out);

echo "<pre>"; print_r($out); echo "</pre>";
#echo "Output from python was: $out";
