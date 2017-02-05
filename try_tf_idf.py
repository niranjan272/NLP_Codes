# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 16:15:46 2017

@author: Niranjan
"""

import math
from textblob import TextBlob as tb

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)


fp = open("E:/Coursera/Projects/KeywordExtraction-TF-IDF-master/description.txt","r")
txt = fp.read()
bloblist = [tb(txt)]
for i,blob in enumerate(bloblist):
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
for word, score in sorted_words[:10]:
    print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))