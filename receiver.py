#!usr/bin/env python2

import socket

recv_ip = "127.0.0.1"
recv_port=9090  #port > 6000 are generally free to use

#calling UDP protocol
#              socket.AF_INET----->ipv4        ,  soxket.SOCK_DGRAM----->UDP

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#above code is same for sender as well as receiver

#rec side only
#binding ip and port

s.bind((recv_ip,recv_port))        #providing way to connect
while True :
	rec_data=s.recvfrom(100)#here 100 is the buffer size in char
	print "Data Received ",rec_data[0]
#  here rec_data[1] is the combo of sender ip and port
	s.sendto("ok got it",rec_data[1]) 
