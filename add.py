#!/usr/bin/env python2

import cgi

web_data = cgi.FieldStorage()
print "Content-type:text/html"
print ""
username= web_data.getvalue("nm")
password= web_data.getvalue("pass")

if password== "qwe" :
	print "Login successfully"
else :
	print "Login failed,password incorrect"


