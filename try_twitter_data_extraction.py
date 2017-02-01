# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 14:09:53 2017

@author: Niranjan
"""

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

#API Authentication
app_key = "StVMHhyoj2Hdk1gOX6fSS9c9G"
app_secret = "ul4bdLxYDJLIqMtknE6uIXutbBltCuvBIXwaJ3X2Snk2a7b4xT"
oauth_token = "2249397456-8V4H8ACDqqEqdFtPcF9BemcOmuJ5UNUUaC7PvW9"
oauth_token_secret= "CDlM6JdiqDIH869q5M8moqkyD7xYPfwcBscbzF4mpVB6i"

auth = OAuthHandler(app_key,app_secret)
auth.set_access_token(oauth_token,oauth_token_secret)

api = tweepy.API(auth)

#StreamListener
class MyListener(StreamListener):
    
    def on_data(self,data):
        try:
            with open("E:\\Coursera\\NLP\\trump_feed.json",'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on data: %s",str(e))
    
    def on_error(self,status):
        print(status)
        return True 

twitter_stream = Stream(auth,MyListener())
twitter_stream.filter(track=['#trump'])       
            