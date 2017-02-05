# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 15:59:20 2017

@author: Niranjan
"""

import json
from nltk.tokenize import word_tokenize
import re,nltk
import operator
from collections import Counter
from nltk.corpus import stopwords
import string

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
with open("E:\\Coursera\\NLP\\trump_feed.json", 'r') as f:
    count_all = Counter()
    for line in f:
        data = str(line).strip("'<>()[]\"` ").replace('\'', '\"')
        tweet = json.loads(data)
        punctuations = list(string.punctuation)
        stop = stopwords.words('english')+punctuations + ['rt','via']
        term_stop = [term for term in preprocess(tweet['text'])]    


with open("E:\\Coursera\\NLP\\trump_feed.csv",'r') as f:
    for line in f:
        text = nltk.word_tokenize(line)
        pos_tag = nltk.pos_tag(text)
        print(pos_tag)
    
fp = open("E:\\Coursera\\NLP\\trump_feed.csv","r")
text = fp.read()
tokens = nltk.word_tokenize(text)
text = nltk.Text(tokens)
text.similar('trump')


def process(sentence):
    for (w1,t1),(w2,t2),(w3,t3) in nltk.trigrams(sentence):
        if (t1.startswith('V') and t2 == 'ban' and t3.startswith('V')):
            print(w1,w2,w3)

for sent in text:
    process(sent.lower()) 
    
