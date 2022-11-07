<?php
    // Authors: Tony Okeke, Majo Garcia
    // Date: 2022-11-06

    // Check if form was submitted
    if ($_SERVER['REQUEST_METHOD'] == 'POST') {

        if (isset($_FILES['myfile']) && !empty($_FILES['myfile']['name'])) {
            // If a file was uploaded, show its name, size, and the first line
            $file = $_FILES['myfile'];
            $name = $file['name'];
            $size = $file['size'];
            $line = htmlspecialchars( file($file['tmp_name'])[0] );

            echo "
                <table>
                    <tr>
                        <td>File name:</td>
                        <td>$name</td>
                    </tr>
                    <tr>
                        <td>File Size:</td>
                        <td>$size</td>
                    </tr>
                    <tr>
                        <td>First Line:</td>
                        <td>$line</td>
                    </tr>
                </table>
            ";

            // Don't show form
            exit();
        } else {
            // If no file was uploaded, show error message and show form
            echo "
                <p style='color: red; font-weight: bold'>
                    ERROR: No file was uploaded
                </p>
            ";
        }
    }
?>

<html>
    <form method="post" enctype="multipart/form-data">
        <table>
            <tr>
                <td>Upload File</td>
                <td><input type="file" name="myfile" /><br></td>
            </tr>
            <tr>
                <td style="text-align:center">
                    <input type="submit" value="Upload"><br>
                </td>
            </tr>
        </table>
    </form>
</html>
