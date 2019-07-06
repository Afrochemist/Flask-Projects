#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 09:36:49 2019

@author: Afrochemist
"""

#This is the first flask application I have created
#This application will print "Helo World"

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ =='__main__':
    app.run()
