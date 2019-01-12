#!usr/bin/env python2
#program to get command from cliennt and run it

import socket
import os   #to check for command       
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
	data=s.recvfrom(100)#here 100 is the buffer size in char
	check= os.system(data[0]) 		#os.system() reply 0 as exit value if command is present else a non zero number is returned 
	#print check	
	if check == 0 :
		s.sendto("Success",data[1])
	else :
		s.sendto(data[0]+" Command not found",data[1])
