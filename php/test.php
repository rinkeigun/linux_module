<?php
ini_set("display_errors", On);
error_reporting(E_ALL);

#$con = mysql_connect();
#$con = mysql_connect('127.0.0.1', 'root', 'Keigun690920');
#$con = mysql_connect('localhost', 'root', 'Keigun690920');
#$conn = new PDO("mysql:host=localhost;dbname=hardware_info", "root", "keigun690920");
$con = mysqli_connect("localhost", "root", "Keigun690920", "hardware_info");
if (!$con) {
  exit('データベースに接続できませんでした。');
}

#$result = mysql_select_db('hardware_info', $con);
#$result = mysqli_select_db('hardware_info', $con);
#if (!$result) {
#  exit('データベースを選択できませんでした。');
#}

#$result = mysql_query('SET NAMES utf8', $con);
#$result = mysqli_query('SET NAMES utf8', $con);
#if (!$result) {
#  exit('文字コードを指定できませんでした。');
#}

#$result = mysql_query('SELECT * FROM feature', $con);
$result = mysqli_query($con, 'SELECT * FROM feature');
while ($data = mysqli_fetch_array($result)) {
  echo  $data['a'].$data['b'] ;
}

#$con = mysql_close($con);
$con = mysqli_close($con);
if (!$con) {
  exit('データベースとの接続を閉じられませんでした。');
}

?>
