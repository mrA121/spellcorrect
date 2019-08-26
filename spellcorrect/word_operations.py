#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 09:20:33 2019

@author: shivank
"""
from spellcorrect.word_processing import words_from_archive,zero_default_dict

def parse(lang_sample):
    words = words_from_archive(lang_sample, include_dups=True)
    counts = zero_default_dict()
    for word in words:
        counts[word] += 1
    return set(words), counts

NLP_WORDS,NLP_COUNTS=parse("big.txt")

LOWERCASE = words_from_archive('en_US_GB_CA_lower.txt')

CASE_MAPPED = words_from_archive('en_US_GB_CA_mixed.txt',map_case=True)

MIXED_CASE = set(CASE_MAPPED.values())


LOWERED = set(CASE_MAPPED.keys())

KNOWN_WORDS = LOWERCASE | LOWERED | NLP_WORDS



def common(words):
    return set(words) & NLP_WORDS

def exact(words):
    return set(words) & MIXED_CASE

def known(words):
    return {w.lower() for w in words} & KNOWN_WORDS

def known_as_lower(words):
    return {w.lower() for w in words} & LOWERCASE

def get_case(word, correction):
    if word.istitle():
        return correction.title()
    if word.isupper():
        return correction.upper()
    if correction == word and not word.islower():
        return word
    if len(word) > 2 and word[:2].isupper():
        return correction.title()
    if not known_as_lower([correction]): #expensive
        try:
            return CASE_MAPPED[correction]
        except KeyError:
            pass
    return correction