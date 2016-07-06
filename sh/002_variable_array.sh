#!/bin/bash
#SYNOPSIS : abc[0]=111 , echo ${abc[0]}
echo "変数:abc[0]=111"
echo "変数:abc[1]=112"
echo "変数:abc[2]=abcde"
echo "表示:echo \${abc[1]}"
echo "結果:112"
abc[0]=111
abc[1]=112
abc[2]=abcde
printf  '${abc[1]}=%d\n' ${abc[1]}
printf '${#abc} =%d\n' ${#abc}
printf '${abc[@]}=%s\n' ${abc[@]}
printf '${abc[*]}=%s\n' ${abc[*]}
printf '${#abc[@]}=%d\n' ${#abc[@]}
printf '${#abc[2]}=%d\n' ${#abc[2]}
