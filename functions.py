# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 01:03:24 2018

@author: Panku
"""

from pywinauto import Application
import time

def open(application_name):
    app  = Application()
    app.start(application_name)


def editMenu():
    app.Notepad.menu_select("File->Exit")

def write(text):
    app.Notepad.edit.Type_keys(text,with_spaces=True)

#open("Notepad.exe")
#editMenu()
#write("Hello My Name is Arya")

def move(x,y):
    app.mouse.click(button="left",coords=(0,0))
#move(0,0)

def setUp():
    """Start the application set some data and ensure the application is in the state we want it."""
    app = subprocess.Popen("exec " + _test_app(), shell=True)
    time.sleep(0.1)
    mouse.click(coords=(300, 300))
    time.sleep(0.1)
setUp()6

