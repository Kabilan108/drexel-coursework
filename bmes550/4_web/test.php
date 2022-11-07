<?php
    error_reporting(E_ALL & ~E_NOTICE);
    session_start();

    #if furit is set:
    #store it $_SESSION['fruit']= $_REquest['fruit']

    $_SESSION['numvisits']=$_SESSION['numvisits']+1;

    session_commit();
?>

<html>
    <head>
        <style>
            pre{
                background-color:#ccccff;
                border: 1px dashed gray;
            }
            p.error{
                color:red;
                font-weight:bold;
            }
        </style>
    </head>

    <body>
        apple<br>

        <?php

            require 'helperfunctions.php';

            $x = 5;

            echo "<p style='color:red'>An apple is $x dollars.</p>";


            echo "<pre>";
            # print_r($_REQUEST['firstname']);
            echo "</pre>";

            echo "<p>You have visited this webpage ".$_SESSION['numvisits']." times.</b>";
            echo "<p>Your favorite fruit is: [".htmlspecialchars($_REQUEST['fruit'])."]</p>";

            echo "<a href='test.php'>Forget my fruit</a><br>";

            echo "".$_REQUEST['favoritefood']."<br>";
            echo "".($_REQUEST['favoritefood']=='pasta'? 'You like pasta': 'You hate pasta');

            echo "
            <form method=get>
                <input type=text name='fruit'>

                <select name=favoritefood>
                    <option>Select a food item</option>
                    <option value=pizza ".($_REQUEST['favoritefood']=='pizza'?'selected':'').">pizza</option>
                    <option value=pasta ".($_REQUEST['favoritefood']=='pasta'?'selected':'').">pasta</option>
                </select>
                <input type=submit>
            </form>
            "; 
        ?>


    </body>
</html>



