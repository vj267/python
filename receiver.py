#!usr/bin/env python2

import socket

ip = "192.168.10.101"
port=9090  #port > 6000 are generally free to use

#calling UDP protocol
#              socket.AF_INET----->ipv4        ,  soxket.SOCK_DGRAM----->UDP

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#above code is same for sender as well as receiver

#rec side only
#binding ip and port

s.bind((ip,port))        #providing way to connect

print s.recvfrom(100)#here 100 is the buffer size in char