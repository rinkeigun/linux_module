#!/bin/bash
#SYNOPSIS : export def=456
echo "環境変数:def"
echo "exportを使って定義"
echo "シェル変数と環境変数との違いは"
echo "シェル変数はこのシェル内のみ有効に対して"
echo "環境変数は一度設定したらこれによって起動される子プロセスはすべて有効"
abc=123
export def=456
echo "abc=$abc, def=$def"
echo "003_variable_env_01.shを実行し、\$defが引き継がれることを確認してください"
./003_variable_env_01.sh
