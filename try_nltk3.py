# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 19:15:14 2017

@author: Niranjan
"""

from __future__ import division
import nltk,re,pprint
from nltk import word_tokenize
from urllib2 import Request
from urllib2 import urlopen
from bs4 import BeautifulSoup
import feedparser


#Accessing data from web
url = "http://www.gutenberg.org/files/2554/2554.txt"
response = urlopen(url)
raw = response.read().decode('utf-8')
type(raw)
raw[:75]

#Tokenization
tokens = word_tokenize(raw)
tokens[:10]
text = nltk.Text(tokens)
text.collocations()


#Reading from HTML
url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
html = urlopen(url).read().decode('utf-8')
raw = BeautifulSoup(html).get_text()
tokens = word_tokenize(raw)
tokens_1 = tokens[110:390]
text = nltk.Text(tokens_1)
text.concordance('gene')


#RS feed
llog = feedparser.parse("http://languagelog.ldc.upenn.edu/nll/?feed=atom")
llog['feed']['title']
post = llog.entries[2]
post.title
content = post.content[0].value
content[:70]
raw = BeautifulSoup(content).get_text()
word_tokenize(raw)

#Encoded text from file
path = nltk.data.find("corpora/unicode_samples/polish-lat2.txt")
f = open(path,encoding = "latin2")
for line in f:
    line = line.strip()
    print line
    

#Regular Expression
wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]    
wordlist    
[w for w in wordlist if re.search('ed',w)]


#Finding word stem
def stem(word):
    for suffix in ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's', 'ment']:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word  

stem("bushes")


re.findall(r'^.*(ing|ly|ed|ious|ies|ive|es|s|ment)$','Commintment')
re.findall(r'^(.*)(ing|ly|ed|ious|ies|ive|es|s|ment)$','Commintment')
  
