<?php
require_once getenv('AHMETLIBPHP').'/ahmet.php';
(@include_once glob('/Users/*/Dropbox/bmes.ahmet')[0].'/bmes.php') or (@include_once glob('/Users/*/Dropbox/share/bmes.ahmet')[0].'/bmes.php') or die('<b>ERROR while running '.basename(__DIR__).'/'.basename(__FILE__).'</b>: Failed to load bmes.php, make sure you have a copy of bmes.php and have set the BMESAHMETDIR environment variable.');

#from pathlib import Path; import sys,os; sys.path.append(str(Path.home())+'/Dropbox/bmes.ahmet'); #import bmes

echo "<li>".explode('.',gethostbyname('sacan.biomed.drexel.edu'))[0];


echo "<li>".(preg_match('#[/\x5c]dropbox[/\x5c]#i',$_SERVER['SCRIPT_FILENAME'])?1:2).(preg_match('#[/\x5c]bmes550web[/\x5c]#i',$_SERVER['SCRIPT_NAME'])?1:2);


ve($_SERVER);
