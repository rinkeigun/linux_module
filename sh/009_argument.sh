#!/bin/bash
#SYNOPSIS : script arg0 arg1 arg2 
echo 'プログラム名 $0:' $0 
echo '1番目引数 $1:' $1 
echo '2番目引数 $2:' $2 
echo '3番目引数 $3:' $3 
echo '9番目引数 $9:' $9 
echo '10番目引数 $10:' $10 
echo '10番目引数 ${10}:' ${10} 
echo '引数の個数 $#:' $# 
echo 'すべての引数$*:' $* 
echo 'すべての引数$@:' $@ 
echo '直前に実行したコマンドのexit値$?:' $? 
echo 'シェル自身のプロセスID$$:' $$ 
echo 'シェル起動時のフラグの一覧$-:' $- 
echo 'シェルが最後に起動したバックグラウンドプロセスのプロセスID$!:' $! 
echo '$LINENO:' $LINENO 
echo '${PIPESTATUS[@]}:' ${PIPESTATUS[@]}

