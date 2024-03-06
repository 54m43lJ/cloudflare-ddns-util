#!/bin/sh
if [ -z $i4addr ]; then
    i4addr=$(curl -s "https://myip.ipip.net" | grep "当前 IP" | grep -E -o '([0-9]+\.){3}[0-9]+' | head -n1 | cut -d' ' -f1)
fi
if [ -z $i4addr ]; then
    i4addr=$(curl -s https://4.ident.me)
fi
if [ -z $i4addr ]; then
    i4addr=$(curl -s http://4.ipw.cn)
fi
echo $i4addr
