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
from nltk.corpus import gutenberg
import codecs


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
    print(line)
    

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


s = input("enter some input:")
print("You entered",len(nltk.word_tokenize(s))," words")
  
#String Manipulation
a = [6,5,4,3,2,1,1,2,3,4,5,6]
b = [' ' *2*(7-i) + 'very' * i for i in a]
for i in b:
    print(b)
    
    
statement = "Akshay the sexy bouy"
for c in statement:
    print(c)    


raw = gutenberg.raw("melville-moby_dick.txt")
fdist = nltk.FreqDist(ch.lower() for ch in raw if ch.isalpha())
fdist.keys()
fdist.plot()


#Data Encoding
path = nltk.data.find("corpora/unicode_samples/polish-lat2.txt") 
f = codecs.open(path,encoding= 'latin2')
for line in f:
    line = line.strip()
    print(line.encode('unicode_escape'))

#Regular Expression
wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]
wordlist1 = [w for w in wordlist if re.search('ed$',w) ]    
print(wordlist1)    
[w for w in wordlist if re.search('^..j..t..$',w)]
[w for w in wordlist if re.search('..j..t..',w)]
[w for w in wordlist if re.search('^[ghi][mno][jlk][def]$',w)]


chart_words = sorted(set(w for w in nltk.corpus.nps_chat.words()))
[w for w in chart_words if re.search('^m+i+n+e$',w)]
[w for w in chart_words if re.search('^[ha]+$',w)]
wsj = sorted(set(nltk.corpus.treebank.words()))
[w for w in wsj if re.search('[0-9]+\.[0-9]+$',w)]
[w for w in wsj if re.search('^[A-Z]+\$$',w)]
[w for w in wsj if re.search('^[0-9]{4}$',w)]
[w for w in wsj if re.search('^[0-9]+-[a-z]{3,5}$',w)]
[w for w in wsj if re.search('^[a-z]{5,}-[a-z]{2,3}-[a-z]{,6}$', w)]
[w for w in wsj if re.search('(ed|ing)$',w)]
word = 'supercalifragilisticexpialidocious'
fd = nltk.FreqDist(vs for word in wsj for vs in re.findall(r'[aeiou]{2,}',word))
fd.items()


rotokas_word =  nltk.corpus.toolbox.words('rotokas.dic')
cvs = [cv for w in rotokas_word for cv in re.findall(r'[ptksvr][aeiou]',w)]
cdf = nltk.ConditionalFreqDist(cvs)
cdf.tabulate()
cv_wordpair = [(cv,w) for w in rotokas_word for cv in re.findall(r'[ptksvr][aeiou]',w)]
cv_index = nltk.Index(cv_wordpair)
cv_index['su']
cv_index['po']

def stem(word):
    
    regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$'
    stem, suffix = re.findall(regexp, word)[0]
    return stem

#Tokenizer
raw = """DENNIS: Listen, strange women lying in ponds distributing swords is no basis for a system of government. Supreme executive power derives from a mandate from the masses, not from some farcical aquatic ceremony."""
tokens = nltk.word_tokenize(raw)
[stem(t) for t in tokens]

from nltk.corpus import brown
hobbies = nltk.Text(brown.words(categories = ['hobbies','learned']))
hobbies.findall(r"<\w*> <and> <other> <\w*s>")


#Stemmer
porter = nltk.PorterStemmer()
lancster = nltk.LancasterStemmer()
[porter.stem(t) for t in tokens]
[lancster.stem(t) for t in tokens]

#Lemmatization
wnl = nltk.WordNetLemmatizer()
[wnl.lemmatize(t) for t in tokens]

#Tokenization
raw = """'When I'M a Duchess,' she said to herself, (not in a very hopeful tone though), 'I won't have any pepper in my kitchen AT ALL. Soup does very well without--Maybe it's always pepper that makes people hot-tempered,'"""
re.split(r' ',raw)
re.split(r'[ \t\n]+',raw)

text = 'That U.S.A. poster-print costs $12.40...'


raw = 'Red lorry, yellow lorry, red lorry, yellow lorry.'
text = nltk.word_tokenize(raw)
fdist = nltk.FreqDist(text)
list(fdist)
for key in fdist:
    print(fdist[key])
    
#Splitting Sentence
text = nltk.corpus.nps_chat.words()    
cut = int(0.9*len(text))
training_data,test_data = text[:cut],text[cut:]
text == training_data + test_data
len(training_data)/len(test_data)


#Combine
words = "I turned off the television".split()
wordlens = [(len(word),word) for word in words]
wordlens.sort()
" ".join(w for (_,w) in wordlens)


fd = nltk.FreqDist(nltk.corpus.brown.words())
cumalative = 0
for rank, word in enumerate(fd):
    cumalative +=fd[word]*100/fd.N()
    print("%3d %6.2f%% %s" %(rank+1,cumalative,word))
    if cumalative > 25:
        break;
        
text = nltk.corpus.gutenberg.words('milton-paradise.txt')        
longest = ''        
for word in text:
    if len(word) > len(longest):
        longest = word
print(longest)   


maxlen = max(len(word)for word in text)     
[word for word in text if len(word) == maxlen]


print("a\nb\nc\n".split())
