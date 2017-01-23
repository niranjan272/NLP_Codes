# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 18:14:57 2017

@author: Niranjan
"""

import nltk
import re
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize,pos_tag

noise_list = ['this','is','a','an'];
             
def remove_noise(input_text):
    
    words = input_text.split()
    noise_free_words = [word for word in words if word not in noise_list ]
    noise_free_text = " ".join(noise_free_words)
    return noise_free_text

filtered_text = remove_noise("this is a simple text")
print(filtered_text)


#remove regular expression

def remove_regular_exp(input_text,regular_exp):
    
    url = re.finditer(regular_exp,input_text)
    for i in url:
        input_text_re = re.sub(i.group().strip(),'',input_text)
    
    return input_text_re


regular_exp = "#[\w]*"
text_without_re = remove_regular_exp("Barack Obama was the 44th President of #USA",regular_exp)
print text_without_re


#Lemmatization
lem= WordNetLemmatizer()
word= "Multiplying"
word_lemmaztization = lem.lemmatize(word,"v")
print word_lemmaztization


#Object Standardization
lookup_dict = {'rt':'Retweet', 'dm':'direct message', "awsm" : "awesome", "luv" :"love"}

def lookup_words(input_text):
    words = input_text.split()
    new_words = []
    for word in words :
        if word.lower() in lookup_dict:
            word = lookup_dict[word.lower()]
        
        new_words.append(word) 
        new_text = " ".join(new_words)
    return new_text

obj_standard = lookup_words("RT this is a retweeted tweet by Shivam Bansal")   
print(obj_standard) 

#POS Tagging
def pos_tagging(input_text):
    
    tokens = word_tokenize(input_text)
    return pos_tag(tokens)

text_tagging = pos_tagging("I am learning Natural Language Processing on Analytics Vidhya" )
print text_tagging


#generate n-gram
def generate_ngram(input_text,n):
    words = input_text.split()
    output = []
    for i in range(len(words)- n+1):
        output.append(words[i:i+n])
    return output

output_ngram = generate_ngram('this is a simple text',3) 
print output_ngram   
        
            
            


