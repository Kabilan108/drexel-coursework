<?
#if user has submitted something
if(isset($_REQUEST['gene']))
{
	echo "<h3>_GET variable</h3><pre>"; print_r($_GET); echo "</pre>";

	echo "<li>You provided the name: ".$_GET['name']."</li>";

	echo "<hr>";

	echo "<h3>_POST variable</h3><pre>"; print_r($_POST); echo "</pre>";


	echo "<hr>";

	echo "<h3>_REQUEST variable</h3><pre>"; print_r($_REQUEST); echo "</pre>";


	echo "<hr>";
}

#if form has not been submitted before
if(!isset($_REQUEST['gene']))
{
?>
<form method="get">

	<table>
		<tr>		
			<td>Gene Name:</td>
			<td><input type="text" name="gene"><br></td>
		</tr>
		<tr>
			<td>Species:
			<td><input type="text" name="species"><br>
		</tr>
		<tr>
			<td>
			<td style="text-align:right"><input type="submit" value="Submit"><br>
		</tr>
	</table>
	
</form>

<?
}
?>