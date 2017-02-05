# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 20:30:19 2017

@author: Niranjan
"""

from nltk.book import *
from __future__ import division
#Searching a word
text1.concordance("monstrous")
text1.concordance("array")

# Similar words
text1.similar("monstrous")
text2.similar("monstrous")

#Context
text2.common_contexts(["monstrous","very"])
text1.common_contexts(["pictures","size"])

#Location of a word
text4.dispersion_plot(["citizens","democracy","freedom","duties","America","liberty","constitution"])

#Random text
text3.generate()

#Count number of words
len(text3)

#Elements of vocabulary
sorted(set(text3))
len(set(text3))
len(set(text3))/len(text3)

#count of a word
text3.count("smote")
100 * text4.count("a")/len(text4)

#Lexical Diversity
def lexical_diversity(text):
    return (len(set(text))/len(text))

lexical_diversity(text3)


saying = ['After', 'all', 'is', 'said', 'and', 'done','more', 'is', 'said', 'than', 'done']
tokens = set(saying)
tokens = sorted(saying)
tokens[-2]

#Frequency Distribution
freq_distribution = FreqDist(text1)
print(freq_distribution)
freq_distribution.most_common(20)
freq_distribution["he"]

#Filtering
V = set(text1)
long_words = [w for w in V if len(w) >15]
print(long_words)

fdist5 = FreqDist(text1)
fdist = [w for w in V if len(w) > 10 and  fdist5[w] > 10]
print(sorted(fdist))

#Collocation
text4.collocations()

#For loop
set1 = ["call","me","Isabel"]
for xyz in set1:
    if xyz.endswith("l"):
        print(xyz)
