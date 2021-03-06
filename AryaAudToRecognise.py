# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 19:29:33 2018

@author: Panku
"""


import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

voiceData = None

def convertToText():
        
    # Instantiates a client
    client = speech.SpeechClient()
    
    # The name of the audio file to transcribe
    file_name ='demo.wav'
    
    # Loads the audio into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)
    
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code='en-US')
    
    # Detects speech in the audio file
    response = client.recognize(config, audio)
    
    for result in response.results:
        global voiceData
        voiceData = result.alternatives[0].transcript
        print('Transcript: {}'.format(result.alternatives[0].transcript))
    return voiceData
