<?php
    // Authors: Tony Okeke, Majo Garcia
    // Date: 2022-11-06

    // Start the session
    session_start();

    // Store name in session if provided by POST or GET request
    if (isset($_REQUEST['myname'])) {
        $_SESSION['name'] = $_REQUEST['myname'];
        session_commit();
    }

    // Erase name from session if forgetme is set
    if (isset($_REQUEST['forgetme']) && $_REQUEST['forgetme'] == 1) {
        unset($_SESSION['name']);
        session_commit();
    }

    if (isset($_SESSION['name'])) {
        // If name is in session, show it
        $name = $_SESSION['name'];
        echo "
            <p>$name</p>
            <a href='session.php?forgetme=1'>Forget Me</a>
        ";
    } else {
        // If no name is in session, show the form
        echo "
            <form method='post'>
                <table>
                    <tr>
                        <td>User Name:</td>
                        <td><input type='text' name='myname'/><br></td>
                    </tr>
                    <tr>
                        <td style='text-align:center'>
                            <input type='submit' value='Submit'><br>
                        </td>
                    </tr>
                </table>
            </form>
        ";
    }
?>
