# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 15:16:15 2018

@author: Nitish Kumar
"""

import pyttsx3
engine = pyttsx3.init()
engine.say('Sally sells seashells by the seashore.')
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()


import pyttsx3
def onStart(name):
   print ('starting', name)
def onWord(name, location, length):
   print ('word', name, location, length)
def onEnd(name, completed):
   print ('finishing', name, completed)
engine = pyttsx3.init()
engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()


engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
   engine.setProperty('voice', voice.id)
   engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()


engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+90)
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()