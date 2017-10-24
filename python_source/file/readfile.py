#!/usr/bin/python3
#coding:UTF-8

f = open('passwd')
#data1 = f.read()
# lines = f.readlines()
lineWithEnd = f.readline()
f.close()
print(lineWithEnd.split('\n')[0])
