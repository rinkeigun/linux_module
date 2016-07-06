#!/bin/bash
#SYNOPSIS : printf format abc 
echo "printf %s aaa"
echo "printf %s aaa bbb"
echo "printf \"%s %s\" aaa bbb ccc"
printf "%s\n" 1.aaa
printf "%s\n" 2.aaa bbb
printf "%s %s\n" 3.aaa bbb ccc
