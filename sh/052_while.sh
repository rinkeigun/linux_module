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

du > test.txt

while read READ_LINE;
do
	echo $READ_LINE
done <  test.txt 
