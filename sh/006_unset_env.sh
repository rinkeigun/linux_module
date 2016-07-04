#!/bin/bash
#SYNOPSIS : unset env_variable 
echo "unset env_variable" 
export abc=aaa
echo "abc=$abc"
unset abc
echo "unset abc"
echo "abc=$abc"
