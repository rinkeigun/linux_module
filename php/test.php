<?php
echo "a" ;
$con = mysql_connect('127.0.0.1', 'root', 'Keigun690920');
/*
#$con = mysql_connect('localhost', 'root', 'Keigun690920');
echo "a" ;
if (!$con) {
  exit('データベースに接続できませんでした。');
}

$result = mysql_select_db('hardware_info', $con);
if (!$result) {
  exit('データベースを選択できませんでした。');
}

$result = mysql_query('SET NAMES utf8', $con);
if (!$result) {
  exit('文字コードを指定できませんでした。');
}

$result = mysql_query('SELECT * FROM feature', $con);
while ($data = mysql_fetch_array($result)) {
  echo  $data['a'].$data['b'] ;
}

$con = mysql_close($con);
if (!$con) {
  exit('データベースとの接続を閉じられませんでした。');
}
*/

?>
