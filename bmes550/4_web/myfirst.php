<style>
    pre{
        background-color:#ffffcc;
    }
</style>
<!-- by AhmetSacan -->

<?
echo sys_get_temp_dir();
#require_once getenv('AHMETLIBPHP').'/ahmet.php';
$dbfile=sys_get_temp_dir( ) .'/mydb.sqlite';

#create database connection
$db=new PDO("sqlite:$dbfile"); # "sqlite:".$dbfile
$db->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);


# if table does not exist, create it and add sample entries.
if(!$db->query("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='students'")->fetch()){
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

$stmt=$db->query("SELECT * FROM students");
$fields=[];
for($i=0;$i<$stmt->columnCount();$i++) $fields[]=$stmt->getColumnMeta($i)['name']; #fields{end+1}=
echo "<h3>Fields:</h3><pre>"; print_r($fields); echo "</pre>";

$rows=$stmt->fetchAll();
echo "<h3>Rows:</h3><pre>"; print_r($rows); echo "</pre>";


echo "<table border=1>\n";
echo "<tr>";
#for($i=0;$i<sizeof($fields);$i++){
foreach($fields as $f){
    echo "<th>$f</th>"; 
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

echo "<hr><h2>Source Code</h2>"; show_source(__FILE__);
