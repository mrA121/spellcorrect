#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 10:12:59 2019

@author: shivank
"""

from spellcorrect.word_operations import NLP_COUNTS,common,exact,known,get_case,LOWERCASE
from spellcorrect.word_processing import Word


def spell(word):
    """most likely correction for everything up to a double typo"""
    w = Word(word)
    candidates = (common([word]) or exact([word]) or known([word]) or
                  known(w.typos()) or common(w.double_typos()) or
                  [word])
    correction = max(candidates, key=NLP_COUNTS.get)
    return get_case(word, correction)

swap = { "im":"i'm","its":"it's","thats":"that's","ill":"i'll","ure":"u're","hes":"he's","hesnt":"hesn't","shes":"she's","shesnt":"shesn't","shant": "shan't",
        "theyre":"they're","theyll":"they'll","cant":"can't","dont":"don't","wont":"won't","arent":"aren't","wouldnt":"wouldn't","shouldnt":"shouldn't",
        "couldnt":"couldn't","havent":"haven't","hasnt":"hasn't","oclock":"o'clock","iam":"i am", "youare":"you are","heis":"he is","sheis":"she is",
        "itis":"it is","weare":"we are","theyare":"they are", "arent": "aren't","couldve": "could've","didnt": "didn't","doesnt": "doesn't","dont": "don't",
        "hadnt": "hadn't","hed": "he'd","hell": "he'll","hes": "he's","howd": "how'd","howll": "how'll","hows": "how's","id": "i'd","ive": "i've",
        "isnt": "isn't","lets": "let's","mustnt": "mustn't","mustve": "must've","shed": "she'd","shell": "she'll","shouldve": "should've",
        "somebodys": "somebody's","someones": "someone's","somethings": "something's","thats": "that's","thatll": "that'll","theres": "there's",
        "theyve": "they've","wasnt": "wasn't","were": "we're","weve": "we've","werent": "weren't","whatll": "what'll","whats": "what's","whatve": "what've",
        "wholl": "who'll","whos": "who's","whove": "who've","youll": "you'll","youre": "you're","youve": "you've"
       }
LOWERCASE=list(LOWERCASE)
LOWERCASE += list(swap.keys())

def segment(word):
    word= word.lower()
    for i in range(len(word),-1,-1):
        h = word[0:i+1]
        if h in LOWERCASE:
            if len(h)==len(word):
                if h in swap:
                    return swap[h]
                else:
                    return h
            else:
                if h in swap:
                    h=swap[h]
                return h + " " + segment(word[i+1:])
    