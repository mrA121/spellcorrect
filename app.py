#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 07:25:43 2019

@author: shivank
"""

from flask import Flask
from spellcorrect import spellcorrector
import json

app = Flask(__name__)

@app.route("/spellCorrect/<word>/")
def spellCorrect(word):
    return json.dumps(spellcorrector(word))


if __name__ == "__main__": 
    app.run()