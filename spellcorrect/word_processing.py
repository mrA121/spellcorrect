#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 09:10:13 2019

@author: shivank
"""

import re, os, tarfile
from contextlib import closing
from itertools import chain

PATH = os.path.abspath(os.path.dirname(__file__))
BZ2 = 'words.bz2'
RE = '[A-Za-z]+'
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'



def words_from_archive(filename, include_dups=False, map_case=False):
    bz2 = os.path.join(PATH, BZ2)
    tar_path = '{}/{}'.format('words', filename)
    with closing(tarfile.open(bz2, 'r:bz2')) as t:
        with closing(t.extractfile(tar_path)) as f:
            words = re.findall(RE, f.read().decode(encoding='utf-8'))
    if include_dups:
        return words
    elif map_case:
        return {w.lower():w for w in words}
    else:
        return set(words)
    
def concat(*args):
    try:
        return ''.join(args)
    except TypeError:
        return ''.join(chain.from_iterable(args))
    
class Zero(dict):

    def __getitem__(self, key):
        return self.get(key)

    def get(self, key):
        try:
            return super(Zero, self).__getitem__(key)
        except KeyError:
            return 0

zero_default_dict = Zero
    
class Word(object):
    """container for word-based methods"""

    def __init__(self, word):
        word_ = word.lower()
        slice_range = range(len(word_) + 1)
        self.slices = tuple((word_[:i], word_[i:])
                            for i in slice_range)
        self.word = word

    def _deletes(self):
        """th"""
        return {concat(a, b[1:])
                for a, b in self.slices[:-1]}

    def _transposes(self):
        """teh"""
        return {concat(a, reversed(b[:2]), b[2:])
                for a, b in self.slices[:-2]}

    def _replaces(self):
        """tge"""
        return {concat(a, c, b[1:])
                for a, b in self.slices[:-1]
                for c in ALPHABET}

    def _inserts(self):
        """thwe"""
        return {concat(a, c, b)
                for a, b in self.slices
                for c in ALPHABET}

    def typos(self):
        """letter combinations one typo away from word"""
        return (self._deletes() | self._transposes() |
                self._replaces() | self._inserts())

    def double_typos(self):
        """letter combinations two typos away from word"""
        return {e2 for e1 in self.typos()
                for e2 in Word(e1).typos()}
