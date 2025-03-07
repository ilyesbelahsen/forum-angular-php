<?php

session_start();
require 'mysqlConnect.php';

if (isset ($_SERVER['HTTP_ORIGIN'])) {
  header("Access-Control-Allow-Origin: " . $_SERVER['HTTP_ORIGIN']);
}


function authenticate(){
    global $pdo;
    if (!(array_key_exists('username', $_POST) && array_key_exists('mdp', $_POST))) {
        return false;
    }

    $username = $_POST['username'];
    $mdp = $_POST['mdp'];

    $stmt = $pdo->prepare("SELECT * FROM users WHERE username = :username");
    $stmt->execute(['username' => $username]);
    $user = $stmt->fetch(PDO::FETCH_ASSOC);

    if ($user['username'] !== $username  || $user['mdp'] !== $mdp ) {
        return false;
    }

    $_SESSION['username'] = $username;
    return true;
}

function isAuthenticate(){
    return (isset($_SESSION['username']));
}
?>