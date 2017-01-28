# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 15:50:31 2017

@author: Niranjan
"""

import nltk
from nltk.corpus import gutenberg
from nltk.corpus import webtext
from nltk.corpus import nps_chat

nltk.corpus.gutenberg.fileids()

emma = nltk.corpus.gutenberg.words('austen-emma.txt')
len(emma)

for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
    print (round(num_chars/num_words), round(num_words/num_sents), round(num_words/num_vocab), fileid)
    
    
#Sentences
macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')    
macbeth_sentences

#webdata
for fileid in webtext.fileids():
    print (fileid , webtext.raw(fileid)[:65],"...")

#Chat Application
chat_room = nps_chat.posts('10-19-20s_706posts.xml')    
chat_room[123]
