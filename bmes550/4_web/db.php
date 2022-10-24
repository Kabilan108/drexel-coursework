<?
#by AhmetSacan

$dbfile=__DIR__.'/mydb.sqlite'; #if you are using a large database file (>10 MB), please keep it elsewhere on your computer.

####################################################
#create database connection
$db=new PDO("sqlite:$dbfile");
$db->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);


function doesdbtableexist($db, $tablename){
	return $db->query("SELECT name FROM sqlite_master WHERE type='table' AND name='$tablename'")->fetch();
}

####################################################
#if table does not exist, create it and add sample entries.
#TODO: it would be nice to have a function that told us whether this table exists.
if(!$db->query("SELECT name FROM sqlite_master WHERE type='table' AND name='students'")->fetch()){
	$db->exec("BEGIN TRANSACTION"); #group statements that should work together in a transaction.

	$db->exec("CREATE TABLE   IF NOT EXISTS   students (
	id INTEGER PRIMARY KEY,
	name VARCHAR(30), 
	birth DATE, 
	gpa FLOAT, 
	grad INTEGER)");

	$db->exec("INSERT INTO students(name, birth, gpa, grad) VALUES ('Anderson', '1987-10-22', 3.9, 2009)");
	$db->exec("INSERT INTO students(name, birth, gpa, grad) VALUES ('Jones', '1990-4-16', 2.4, 2012)");
	$db->exec("INSERT INTO students(name, birth, gpa, grad) VALUES ('Hernandez', '1989-8-12', 3.1, 2011)");
	$db->exec("INSERT INTO students(name, birth, gpa, grad) VALUES ('Chen', '1990-2-4', 3.2, 2011)");

	$db->exec("COMMIT");
}

####################################################
$stmt=$db->query("SELECT * FROM students");
$fields=[];
for($i=0;$i<$stmt->columnCount();$i++) $fields[]=$stmt->getColumnMeta($i)['name']; #fields{end+1}=
echo "<h3>Fields:</h3><pre>"; print_r($fields); echo "</pre>";

$rows=$stmt->fetchAll();
echo "<h3>Rows:</h3><pre>"; print_r($rows); echo "</pre>";

//echo "<hr><h2>Source Code</h2>"; show_source(__FILE__);


####################################################
# Print Results as a Table:
echo "<h3>Rows shown as HTML table</h3";
echo "<table border=1>\n";
echo "<tr>";
#for($i=0;$i<sizeof($fields);$i++){
foreach($fields as $f){
	echo "<td>$f</td>"; 
}
echo "</tr>";

foreach($rows as $r){
	echo "<tr>\n";
	foreach($fields as $f){
		echo "    <td>".$r[$f]."</td>\n"; 
	}
	echo "</tr>\n";
	
}
echo "</table>";


