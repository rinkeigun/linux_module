#!/bin/bash
# 配列をどうやって作るの？
#abc=`du | wc -l`
abc=(`du`) 
printf '${abc[0]}=%d\n' ${abc[0]}
printf '${abc[1]}=%d\n' ${abc[1]}
printf '${abc[2]}=%d\n' ${abc[2]}
