#!/bin/bash

#SYNOPSIS :  条件 
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

echo 'NULL評価'
echo '${VAR:-expression} 値がセットされていない(NULL)場合、:-以降の式を評価結果を返す。'
echo '${VAR:+expression} 値がセットされている(NONE-NULL)場合、:+以降の式を評価結果を返す。'
echo '${VAR:=expression} 値がセットされていない(NULL)場合、:=以降の式を評価結果を返し、変数に代入。'
echo '${VAR:?[expression]} 値がセットされていない(NULL)場合、:式が標準エラーに出力。'
