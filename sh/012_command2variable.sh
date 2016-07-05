#!/bin/bash
#SYNOPSIS : 変数=$(コマンド) 
#SYNOPSIS : 変数=`コマンド` 
abc=$(pwd)
bcd=`date +%y%m%d_%H%M%S`
echo '$(pwd):'$abc 
echo '`date...`:'$bcd 

