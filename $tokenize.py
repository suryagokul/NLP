# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 18:15:01 2020

@author: SURYA
"""


import nltk

nltk.download()

paragraph = """Rohit Gurunath Sharma is an Indian cricket player.
               Rohit is also the captain of IPL team Mumbai Indians. 
               Sharma currently holds the record for highest individual 
               score in One Day Internationals.He scored a record 264 
               off 173 balls against Srilanka on November 13, 2014. 
               Rohit is also the only player to score two double 
               centuries in One Day Internationals. He is also the 
               only person to score 250+ in ODI innings."""
               

#converting paragraph into sentences               
sentences = nltk.sent_tokenize(paragraph)   

            
#converting paragraph into words               
words = nltk.word_tokenize(paragraph)