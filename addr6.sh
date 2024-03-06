#!/bin/sh
device=$(ip -br l | grep -v -E '(lo|vir|tun)' | grep -E '^\w+\s+UP' | awk '{print $1; NR=1}')
i6addr=$(ip a show dev $device | grep -e 'inet6.*global' | awk 'NR<2 {print $2}' | cut -d '/' -f 1)
echo $i6addr
