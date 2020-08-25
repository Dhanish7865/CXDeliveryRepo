<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<body>
<?php
$hostname = "localhost";
$username = "users_site";
$password = "JxSLRkdutW";
$db = "users";

$dbconnect=mysqli_connect($hostname,$username,$password,$db);

if ($dbconnect->connect_error) {
  die("Database connection failed: " . $dbconnect->connect_error);
}

?>

<h1>Web Form</h1>

<form action="data.php" method="post">
  <label for="fname">First name:</label><br>
  <input ty id="fname" name="fname"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname"><br>
  <label for="age">Age:</label></label><br>
  <input type="text" id="age" name="age"><br>
  <label for="location">Location:</label><br>
  <input type="text" id="location" name="location"><br>
  <label for="shoesize">Shoe Size:</label><br>
  <input type="text" id="shoesize" name="shoesize"><br><br>
  <input type="submit" value="Submit">
</form>

<table border="1" align="center">
<tr>
  <td>First Name</td>
  <td>Last Name</td>
  <td>Age</td>
  <td>Location</td>
  <td>Shoe Size</td>
</tr>
<?php

$query = mysqli_query($dbconnect, "SELECT * FROM user_information")
  or die (mysqli_error($dbconnect));

while ($row = mysqli_fetch_array($query)) {
  echo
  "<tr>".
    #<td>{$row['id']}</td>
    "<td>{$row['first_name']}</td>
    <td>{$row['last_name']}</td>
    <td>{$row['age']}</td>
    <td>{$row['location']}</td>
    <td>{$row['shoe_size']}</td>
  </tr>";
  
}

?>
</table>
</body>
</html>