#!/usr/bin/python2

import webbrowser,commands

try:
	x=raw_input("Enter 1st number: ")
	y=raw_input("Enter 2nd number: ")
	print int(x)+int(y)
except:
	print "Tujse na ho payega tu google pe karle"
	commands.getoutput("festival --tts tts_sample.txt")
	webbrowser.open_new_tab('http://www.google.com/search?q=calculator'

#finally:
#	print "sahi he bhai"
