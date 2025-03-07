<?php
require_once "config.php";

$dsn = "mysql:host=$host;dbname=$dbname;charset=$charset";
$pdo = new PDO($dsn, $user, $password);
$pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

?>
