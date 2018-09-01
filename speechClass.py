# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 14:37:53 2018

@author: Panku
"""

import os
import re

import transcribe_streaming

RESOURCES = os.path.join(os.path.dirname(__file__), 'resources')


def test_transcribe_streaming(capsys):
    transcribe_streaming.transcribe_streaming(
        os.path.join(RESOURCES, 'audio.raw'))
    out, err = capsys.readouterr()

    assert re.search(r'how old is the Brooklyn Bridge', out, re.DOTALL | re.I)