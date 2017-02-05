# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 13:59:00 2017

@author: Niranjan
"""

from __future__ import division
import nltk,re,pprint
from nltk import word_tokenize
from nltk.corpus import gutenberg
from nltk.corpus import brown

text = nltk.word_tokenize("And now for something completely different")
nltk.pos_tag(text)

text = nltk.word_tokenize("They refuse to permit us to obtain the refuse permit")
nltk.pos_tag(text)

#Similarity
text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
text.similar('woman')
text.similar("bought")


#Tagged Corpora
tagged_token = nltk.tag.str2tuple("fly/NN")
tagged_token
tagged_token[0]
tagged_token[1]

#common tags
brown_news_tagged = brown.tagged_words(categories='news',tagset = 'universal')
tag_fd = nltk.FreqDist(tag for (word,tag) in brown_news_tagged)
tag_fd.keys()

def findtags(tag_prefix,tag_text):
    cfd = nltk.ConditionalFreqDist((tag,word) for (tag,word) in tag_text if tag.startswith(tag_prefix))
    return dict((tag,cfd[tag].keys()[:5]) for tag in cfd.conditions())

tagdict = findtags('NN',nltk.corpus.brown.tagged_words(categories = 'news'))
for tag in sorted(tagdict):
    print(tag,tagdict[tag])


#searching for 3 word phrase
def process(sentence):
    for (w1,t1),(w2,t2),(w3,t3) in nltk.trigrams(sentence):
        if (t1.startswith('V') and t2 == 'TO' and t3.startswith('V')):
            print(w1,w2,w3)

for sent in brown.tagged_sents():
    process(sent) 
    
#Automatic Tagging
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')       
tags = [tag for (word,tag) in brown.tagged_words(categories = "news")]
nltk.FreqDist(tags).max()
           
            



