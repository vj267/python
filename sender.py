#!usr/bin/env python2

import socket

ip = "192.168.10.101"
port=9090  #port > 6000 are generally free to use

#calling UDP protocol
#              socket.AF_INET----->ipv4        ,  soxket.SOCK_DGRAM----->UDP

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#sending message to target

s.sendto("abcd",(ip,port))
