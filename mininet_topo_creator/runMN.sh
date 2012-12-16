#!/bin/sh
if [ "$1" = "m2" ]
then
sudo mn --custom ~/Dropbox/Project_OpenFlow/mininet_topo_creator/hhsshh.py --topo mytopo
fi
if [ "$1" = "m1" ]
then
sudo mn --custom ~/Dropbox/Project_OpenFlow/mininet_topo_creator/hssh.py --topo mytopo
fi
if [ "$1" = "o" ]
then
sudo mn --topo single,5 --mac --switch ovsk --controller remote
fi
