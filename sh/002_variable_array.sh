#!/bin/bash
#SYNOPSIS : abc[0]=111 , echo ${abc[0]}
echo "変数:abc[0]=111"
echo "変数:abc[1]=112"
echo "表示:echo \${abc[1]}"
echo "結果:112"
abc[0]=111
abc[1]=112
echo ${abc[1]}
