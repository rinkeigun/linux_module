#!/bin/sh
while true
do
#ここではftpdのプロセス監視
#isAlive=`ps -ef | grep "receiver.exe" | \
#isAlive=`ps -ef | grep "defunct" | \
free -h | grep Mem
sleep 3
done
