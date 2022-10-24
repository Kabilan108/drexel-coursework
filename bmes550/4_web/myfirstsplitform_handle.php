<?
# we assume that data is submitted from myfirstsplitform_webpage.html to this script.

	echo "<h3>_GET variable</h3><pre>"; print_r($_GET); echo "</pre>";

	echo "<li>You provided the name: ".$_GET['name']."</li>";

	echo "<hr>";

	echo "<h3>_POST variable</h3><pre>"; print_r($_POST); echo "</pre>";


	echo "<hr>";

	echo "<h3>_REQUEST variable</h3><pre>"; print_r($_REQUEST); echo "</pre>";


	echo "<hr>";
