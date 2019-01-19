#!usr/bin/python

from googlesearch import search
#now put a keyword
webdata=search('hello',num=3,stop=2,pause=1)
#generator type iterable
print type(webdata)
for i in webdata:
	print i

