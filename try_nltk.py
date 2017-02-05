# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 18:14:57 2017

@author: Niranjan
"""

import nltk
from nltk.book import *
import re
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import word_tokenize,pos_tag
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.models import Word2Vec
from textblob.classifiers import NaiveBayesClassifier as NBC
from textblob import TextBlob

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
print(text_without_re)


#Lemmatization
lem= WordNetLemmatizer()
word= "Multiplying"
word_lemmaztization = lem.lemmatize(word,"v")
print(word_lemmaztization)


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
print(text_tagging)


#generate n-gram
def generate_ngram(input_text,n):
    words = input_text.split()
    output = []
    for i in range(len(words)- n+1):
        output.append(words[i:i+n])
    return output

output_ngram = generate_ngram('this is a simple text',3) 
print(output_ngram)  

#tf-idf
def tf_idf(input_text):
    obj = TfidfVectorizer()
    x = obj.fit_transform(input_text)
    print(x)
    
tf_idf(['This is sample document.', 'another random document.', 'third sample document text'])   

#Word Embedding
sentences = [['data', 'science'], ['vidhya', 'science', 'data', 'analytics'],['machine', 'learning'], ['deep', 'learning']]
model = Word2Vec(sentences, min_count = 1)
print(model.similarity)
print(model['learning'])


#Text Classification
training_corpus = [
                   ('I am exhausted of this work.', 'Class_B'),
                   ("I can't cooperate with this", 'Class_B'),
                   ('He is my badest enemy!', 'Class_B'),
                   ('My management is poor.', 'Class_B'),
                   ('I love this burger.', 'Class_A'),
                   ('This is an brilliant place!', 'Class_A'),
                   ('I feel very good about these dates.', 'Class_A'),
                   ('This is my best work.', 'Class_A'),
                   ("What an awesome view", 'Class_A'),
                   ('I do not like this dish', 'Class_B')]
test_corpus = [
                ("I am not feeling well today.", 'Class_B'), 
                ("I feel brilliant!", 'Class_A'), 
                ('Gary is a friend of mine.', 'Class_A'), 
                ("I can't believe I'm doing this.", 'Class_B'), 
                ('The date was good.', 'Class_A'), ('I do not enjoy my job', 'Class_B')]


model = NBC(training_corpus)
print(model.classify("Their codes are amazing."))
print(model.accuracy(test_corpus))

#Text Similarity - Levenshtein Distance
def levenshtein(s1,s2):
    if len(s1) > len(s2):
        s2,s1 = s1,s2
        
    distances = range(len(s1) + 1)
    for index2, char2 in enumerate(s2):
        newDistances = [index2 + 1]
        for index1, char1 in enumerate(s1):
            if char1 == char2:
                newDistances.append(distances[index1])
            else:
                newDistances.append(1 + min(distances[index1],distances[index1 + 1],newDistances[-1]))
    
    distances = newDistances
    return distances[-1]

text_sim = levenshtein("analyse","analyze")
print(text_sim)  

#text4 analysis
text4.dispersion_plot(['citizens','democracy','freedom','duties','America'])


          
                    
            
            


