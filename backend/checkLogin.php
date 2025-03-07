<?php
require './auth.php';

header("Access-Control-Allow-Credentials: true");
header("Access-Control-Allow-Headers: Content-Type");
header('Content-type:application/json;charset=utf8');

if (authenticate()) {
    echo 'connecté avec succès';
} else {
    echo 'échec connexion';
}
?>
