<?php
    // Authors: Tony Okeke, Majo Garcia
    // Date: 2022-11-06

    if (isset($_REQUEST['submit'])) {
        // Define variables for python script
        $family = isset($_REQUEST['history']) ? 'Yes' : 'No';
        $europe = $_REQUEST['europe'];
        $ar_ggc = $_REQUEST['ar_ggc'];
        $haplotype = $_REQUEST['haplotype'];

        // Create path to python executable
        if (strtoupper(substr(PHP_OS, 0, 3)) === 'WIN') {
            if (file_exists($try='C:\ProgramData\Anaconda3\python.exe')) {
                $PYEXE = $try;
            } elseif (file_exists($try=getenv("USERPROFILE") . "\anaconda3\python.exe")) {
                $PYEXE = $try;
            } else {
                echo "<p style='color:red'>Cannot find python.exe</p>";
                exit();
            }
        } else {
            if (shell_exec("python --version") != '') {
                $PYEXE = 'python';
            } elseif (shell_exec("python3 --version") != '') {
                $PYEXE = 'python3';
            } else {
                echo "<p style='color:red'>Cannot find python</p>";
                exit();
            }
        }

        // Create command and run python script
        $cmd = "\"$PYEXE\" prostaterisk.py $family $europe $ar_ggc $haplotype";
        $risk = shell_exec($cmd);

        // Print the output
        echo "
            <p style='font-weight:bold'>Prostate Risk: $risk</p>
        ";
        exit();
    } else {

        // Show the form if it hasn't been submitted
        echo "
            <form method='post' enctype='multipart/form-data'>
                <table>
                    <tr>
                        <td>Family History of Prostate Cancer:</td>
                        <td><input type='checkbox' name='history'/><br></td>
                    </tr>
                    <tr>
                        <td>Amount of European Ancestry:</td>
                        <td><input type='textbox' name='europe'/><br></td>
                    </tr>
                    <tr>
                        <td>Number of AR_GGC Repeats:</td>
                        <td><input type='textbox' name='ar_ggc'/><br></td>
                    </tr>
                    <tr>
                        <td>CYP3A4/CYP3A5 Haplotype:</td>
                        <td>
                            <select name='haplotype'>
                                <option value='AA'>AA</option>
                                <option value='GA'>GA</option>
                                <option value='AG'>AG</option>
                                <option value='GG'>GG</option>
                            </select><br>
                        </td>
                    </tr>
                    <tr>
                        <td style='text-align:center'>
                            <input type='submit' name='submit' value='Submit'><br>
                        </td>
                    </tr>
                </table>
            </form>
        ";
    }
?>
