#!/bin/bash
#SYNOPSIS :  while 真条件の間 
#SYNOPSIS :  do	
#SYNOPSIS :  		処理2 
#SYNOPSIS :  done 

while read READ_LINE;
do
	echo "<h1>$READ_LINE</h1>"
	echo "<pre>"
	TMP_LINE=`echo $READ_LINE | sed s/$//`
#	//echo `docker $TMP_LINE --help`
	echo -e "`docker $TMP_LINE --help`"
	echo "</pre>"
done < /mnt/share/docker.txt
