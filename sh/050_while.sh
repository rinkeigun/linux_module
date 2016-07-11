#!/bin/bash
#SYNOPSIS :  while 真条件の間 
#SYNOPSIS :  do	
#SYNOPSIS :  		処理2 
#SYNOPSIS :  done 

a=0

while [ $a -le 5 ];
do
	echo $a
	a=`expr $a + 1`
done

while read READ_LINE;
do
	echo $READ_LINE
done < $1
echo '$1は読み込みファイル名を指定'
