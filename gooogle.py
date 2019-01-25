#!/usr/bin/env python2

import time
import requests
from bs4 import BeautifulSoup
from googlesearch import search
#now put a keyword
whattosearch=raw_input("What do you want to search\n")
webdata=search(whattosearch,num=3,tld="co.in")
#generator type iterable
#print type(webdata)
for url in webdata:
	response = requests.get(url)
	response_content= BeautifulSoup(response.content,"html.parser")
	print url
	complete_page=""
	for data in response_content.find_all('p') :
                complete_page=complete_page+ data.text
	print complete_page
