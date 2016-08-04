#!/bin/sh
while true
do
#ここではftpdのプロセス監視
#isAlive=`ps -ef | grep "receiver.exe" | \
#isAlive=`ps -ef | grep "defunct" | \
isAlive=`ps -ef | grep "a.out" | \
grep -v grep | wc -l`
if [ $isAlive -gt 1 ]; then
echo "プロセスは生きています"
ps -ef | grep "a.out" | grep -v grep
else
echo "プロセスは死んでいます"
fi
sleep 1
done
