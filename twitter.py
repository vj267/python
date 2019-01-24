#!/usr/bin/python

import tweepy
import sys

from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

consumer_key='ejeq7Xwx1FG8QvAI941ZqGewy'
consumer_sec='FvYa7gl2uqLHGlsyaQSkdGmQnM1PabRlIeNmau9U48FJWfIxuq'

#by using above keys we are going to check auth handler

auth=tweepy.OAuthHandler(consumer_key,consumer_sec)
#here auth is token by consumer key and sec
access_key='1081470947712892928-QKYQBzH5IcYuPTZ5b2NPIkToguGhNn'
secret_key='y8j5LJoWNblVVlchUFEGduLnrS1HTGDlgHJh4lQh1tEfk'

#connecting data server with access and secret key by using above token
auth.set_access_token(access_key,secret_key)
#connecting to twitter api with token stored in auth
connected=tweepy.API(auth)
#explore


#searching topics
res=""
tweet=connected.search(sys.argv[1])
for i in tweet:
	res=res+i.text
f=open("tweets.txt","w")
f.write(res)

