#!/bin/bash
#SYNOPSIS : 'この間は文字列'
#SYNOPSIS : "この間は変数展開" 
#SYNOPSIS : `コマンドがあると実行し、結果展開` 
abc=pwd
echo 引用符：文字列'$abc'
echo 引用符：変数"$abc" 
echo 引用符：実行`$abc` 

