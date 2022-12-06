<?php

// Create a class to manage the database connection
class MyDB extends SQLite3 {
    function __construct($dbfile) {
        // This will take the file path and create the database if it doesn't exist
        $this->open($dbfile);
    }

    // Check if a table exists
    function tableExists($table) {
        $results = $this->query('SELECT name FROM sqlite_master WHERE type="table" AND name="' . $table . '"');
        return (bool) $results->fetchArray();
    }

    // Drop a table
    function dropTable($table) {
        $this->exec('DROP TABLE IF EXISTS ' . $table);
    }
}

// Create a new database connection
$dbfile = __DIR__.'/test.db';
$db = new MyDB($dbfile);
if(!$db) {
    echo $db->lastErrorMsg();
} else {
    echo "Opened database successfully\n";
}

// Create a table
$sql =<<<EOF
    CREATE TABLE COMPANY
    (ID INT PRIMARY KEY  NOT NULL,
    NAME  TEXT  NOT NULL,
    AGE   INT  NOT NULL,
    ADDRESS  CHAR(50),
    SALARY  REAL);
EOF;

$ret = $db->exec($sql);
if(!$ret){
    echo $db->lastErrorMsg();
} else {
    echo "Table created successfully\n";
}
$db->close();
?>