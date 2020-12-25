# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 10:07:24 2020

@author: SURYA
"""


import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

paragraph = """Rohit Gurunath Sharma is an Indian cricket player.
               Rohit is also the captain of IPL team Mumbai Indians. 
               Sharma currently holds the record for highest individual 
               score in One Day Internationals.He scored a record 264 
               off 173 balls against Srilanka on November 13, 2014. 
               Rohit is also the only player to score two double 
               centuries in One Day Internationals. He is also the 
               only person to score 250+ in ODI innings."""
               
            
sentences = nltk.sent_tokenize(paragraph)            
            
stemmer = PorterStemmer()

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i] = ' '.join(words)
