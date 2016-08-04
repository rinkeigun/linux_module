#!/bin/bash
# grabtty.sh

rootpid="$1"
newtty=$(tty)

if [[ $(whoami) != "root" ]]; then
    echo "must be root."
    exit 1
fi

if [[ -z "$rootpid" ]]; then
    echo "Usage: $0 PID"
    exit 1
fi

grabpid() {
    local pid="$1"
    local children=$(ps --ppid=$pid -o pid --no-headings)
    for child in $children; do
        grabpid "$child"
    done

    gdb -q -p "$pid" &>/dev/null <<__EOF__
p close(0)
p open("$newtty", 0)
p close(1)
p open("$newtty", 1)
p close(2)
p open("$newtty", 1)
__EOF__
}

grabpid "$rootpid"

tpgid="ps --pid=$rootpid -o tpgid --no-headings"
if [[ $($tpgid) -eq -1 ]]; then
    trap "kill -SIGTERM $rootpid" SIGINT
else
    trap "kill -SIGINT -\$((\$($tpgid)))" SIGINT
fi

while ps --pid=$rootpid >/dev/null; do
    sleep 1
done
