#!/bin/bash 

echo $@ > /home/dlwsadmin/shellargs.txt
cd /home/dlwsadmin/dlworkspace/src/ClusterBootstrap
# Copy ssh keys
../ARM/createconfig.py sshkey $@ > /home/dlwsadmin/sshkeycopy.txt
