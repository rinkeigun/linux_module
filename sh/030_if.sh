#!/bin/bash

#SYNOPSIS :  if 条件; then ... [elif 条件; then] ... [elif]...fi 
echo  'if 条件; then ... [elif 条件; then] ... [elif]...fi'
echo  '条件:文字列比較'
echo  '     a == b'
echo  '     a != b'
echo  '条件:数値比較'
echo  '     a -eq b'
echo  '     a -ne b'
echo  '     a -ge b'
echo  '     a -le b'
echo  '     a -gt b'
echo  '     a -lt b'
echo  '条件:test'
echo  '     -f ファイル名:通常ファイル'
echo  '     -d ファイル名:ディレクトリ'
echo  '     -e ファイル名:ファイルが存在'
echo  '     -L ファイル名:シンボリックリンク'
echo  '     -r ファイル名:読み取り可能'
echo  '     -w ファイル名:書き込み可能'
echo  '     -x ファイル名:ファイルが存在し、実行権限あり'
echo  '     -s ファイル名:サイズ０より大きい'

echo '複数条件'
echo '      [ 条件A -a 条件B -a 条件C ]   <- a = and'
echo '      [ 条件A ] && [ 条件B ] && [ 条件C ]'
echo '      [ 条件A -o 条件B -o 条件C]   <- o = or'
echo '      [ 条件A ] || [ 条件B ] || [ 条件C ]'
echo '      [  ] スペースを必ずいれること'
USER_ID=`/usr/bin/id -u`
 
#if [ $USER_ID -ne 0 ]; then
#    echo "You must be super-user to execute $0"
#    exit 1
#fi
 
a=5
b=7

if [ $a == $b ]; then
	echo "a=b"
elif [ $a == 5 -a $b == 6 ] ; then
#elif [ $a == 5 ] && [ $b == 6 ] ; then
	echo "$a=5, $b=6"
else
	echo "else"
fi

nowtime=`date +%u`
if [ $nowtime -le  4 ]
then
	echo "You have to work..."
elif [ $nowtime -eq 5 ]
then
	echo "You can drink many beer soon!"
else
	echo "Have a relax day."
fi

#$cが定義していなければ$aを出力
echo ${c:-$a}
#$aが定義してあれば$bを出力
echo ${a:+$b}
echo ${a+$b}
#$cが定義していなければ$aを$cに代入
echo ${c:=$a}
echo $c
echo ${d:?'$dが定義されていないためこのメッセージが標準エラーとして出力'}
