<?php
$name = $_POST['name'];
$email = $_POST['email'];
$message = $_POST['message'];

$subject = "Message";
$body = "From $name, $email,  \n\n$message";

$to = "yourdomain@example.com";

mail($to, $subject, $body);
?>