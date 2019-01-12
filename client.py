#!usr/bin/env python2
#program to execute a command on server
import socket

ip = "127.0.0.1"     
port=9090  #port > 6000 are generally free to use

#calling UDP protocol
#              socket.AF_INET----->ipv4        ,  soxket.SOCK_DGRAM----->UDP

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#sending message to target
while True :
	data=raw_input("Send your command :")   #it will send data as well as create its own socket
	s.sendto(data,(ip,port))   #providing a way to connect
	#this is for receiving from sender
	print s.recvfrom(30) 
