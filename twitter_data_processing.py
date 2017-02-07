# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 15:59:20 2017

@author: Niranjan
"""

import json,simplejson
from nltk.tokenize import word_tokenize
import re,nltk
import operator
from collections import Counter
from nltk.corpus import stopwords
import string
import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob
import codecs

emoticons_str = """
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
    
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]   

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)

def tokenize(s):
    return tokens_re.findall(s)

def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

#processing all the tweets
#Read input file of all text
tweets_data = []
tweets_file = open("E:\\Coursera\\NLP\\trump_feed.json", 'r') 
for line in tweets_file:
    #tweet = json.loads(codecs.decode(line,'utf-8'))
    tweet =simplejson.loads(line.replace('\r\n', ''))
    #tweets_data.append(tweet)

with open("E:\\Coursera\\NLP\\trump_feed.json", 'r') as f:
    line = f.readlines()
    line1 = line.read()
    tweet = json.loads(line1)
        
    
print(tweet)
    
tweets = pd.DataFrame()
tweets["text"] = map(lambda tweet:tweet['text'],tweets_data)
tweets["lang"] = map(lambda tweet:tweet['lang'],tweets_data)
tweets["country"] = map(lambda tweet:tweet['place']['country'],tweets_data)

tweets_by_country = tweets['country'].value_counts()

fig.ax = plt.subplots()
ax.tick_params(axis = 'x',labelsize = 15)
ax.tick_params(axis = 'y',labelsize = 15)
ax.set_xlable('Country',fontsize = 15)
ax.set_ylable('No of tweets',fontsize = 15)
ax.set_title('Top 5 Countries',fontsize = 15, fontweight ='bold')
tweets_by_country[:10].plot(ax = ax, kind = 'bar',color = 'red')
plt.show()




