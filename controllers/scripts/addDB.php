<!DOCTYPE html>
<html>
<?php

error_reporting(E_ALL);
ini_set("display_error", true);

try
{
  $barcode= $_POST['barcode'];
  $name = $_POST['name'];
  $category = $_POST['category'];
  $count = $_POST['count'];

// FIX ME!! \/ \/ \/
  exec("/usr/bin/python sudo /var/www/html/add.py", $barcode);

  header('Location: myHTML.html');
  exit();
}

catch (Exception $e)
{
  echo 'Caught exception: ',  $e->getMessage(), "\n";
}
?>

</html>
