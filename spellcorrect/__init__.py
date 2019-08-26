#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 09:02:40 2019

@author: shivank
"""
from spellcorrect.unit_operations import spell,segment
import re
from itertools import chain

def spellcorrector(word):
    word=re.sub("[^a-zA-Z]","",word)
    wordlist=word.split()
    wordlist=list(map(lambda x: list(map(lambda y: spell(y),segment(x).split())),wordlist))
    return list(chain.from_iterable(wordlist))
    
