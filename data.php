<?php
$conn = mysqli_connect("localhost", "users_site", "JxSLRkdutW");
if (!$conn) { 
    die('Connection Failed: ' . mysqli_error());
}

mysqli_select_db($conn, "users");

$sql = "INSERT INTO user_information (first_name, last_name, age, location, shoe_size) VALUES ('".$_POST['fname']."','".$_POST['lname']."','".$_POST['age']."','".$_POST['location']."','".$_POST['shoesize']."')";

echo $sql;

if (!mysqli_query($conn, $sql)) { 
    die('Error: ' . mysqli_error()); 
}

echo "Your information was added to the database.";
mysqli_close($conn);

header ("Location:index.php");

?>

