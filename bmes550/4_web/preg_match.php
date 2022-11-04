<?php
echo (preg_match('#[/\x5c]dropbox[/\x5c]#i',$_SERVER['SCRIPT_FILENAME'])?1:2).(preg_match('#[/\x5c]bmes550web[/\x5c]#i',$_SERVER['SCRIPT_NAME'])?1:2);
?>