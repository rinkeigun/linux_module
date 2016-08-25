#!/bin/bash
#SYNOPSIS :  until 真条件の間 
#SYNOPSIS :  do	
#SYNOPSIS :  		処理2 
#SYNOPSIS :  done 

a=10

until [ $a -le 5 ];
do
	echo $a
	a=`expr $a - 1`
done

