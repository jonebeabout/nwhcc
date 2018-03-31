<?php
if(!isset($_POST['submit'])) {
  echo "ERROR: you need to submit the form!";
}
$name = $_POST['name'];
echo $name;
$visitor_email = $_POST['email'];
$message = $_POST['msg'];

if(empty($name)||empty($visitor_email)) {
  echo "Name and email are necessary!";
  exit;
}

function IsInjected($str)
{
    $injections = array('(\n+)',
           '(\r+)',
           '(\t+)',
           '(%0A+)',
           '(%0D+)',
           '(%08+)',
           '(%09+)'
           );
               
    $inject = join('|', $injections);
    $inject = "/$inject/i";
    
    if(preg_match($inject,$str))
    {
      return true;
    }
    else
    {
      return false;
    }
}

if(IsInjected($visitor_email))
{
    echo "Bad email value!";
    exit;
}

$email = 'jonebeabout@gmail.com';
$subject = 'Contact from NWHCC.org';
$body = 'Here is a message from $name.\n'.
  'email: $visitor_email\n'.
  'Here is the message:\n$msg';
$headers = "From: $visitor_email \r\n";

mail($email,$subject,$body,$headers);

header('Location: ../contact.html');

?>
