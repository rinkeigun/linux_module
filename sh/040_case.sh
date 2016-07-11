#!/bin/bash
#SYNOPSIS :  case 変数 in 
#SYNOPSIS :  	値a) 
#SYNOPSIS :  		処理1;; 
#SYNOPSIS :  	値b) 
#SYNOPSIS :  		処理2;; 
#SYNOPSIS :  	*) 
#SYNOPSIS :  		a, b の他の処理;; 
#SYNOPSIS :  esac 

a=2
case $a in
	1)
		echo '1';;
	2)
		echo '2';;
	*)
		echo 'そのほか、これはｃ言語のdefault見たいに最初に配置するのはだめ';;
esac
