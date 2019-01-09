#!/usr/bin/python

import webbrowser
import commands     #to imports commands of the operating system on python


		
options = '''
Press 1 to check your os version :
Press 2 to login your fb account :
Press 3 to check RAM and CPU  in your current machine :
Press 4 to search google engine  :
Press 5 to list out all IP and mac address in your network zone :
'''

print options
#to take input from user interface in python2
choice = raw_input()

if int(choice) == 1 :
	print "My OS is RHEL 7.5"

elif choice == "2" :
	execfile('fblogin.py')

elif choice == "3" :
	execfile('ramandcpu.py')

elif int(choice) == 4 :
	data=raw_input("What do you want to search on google : ")
	webbrowser.open_new_tab('http://www.google.com/search?q='+data)
else:
	print "Please select a valid option"
