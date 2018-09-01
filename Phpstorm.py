# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 00:56:38 2018

@author: Panku
"""

"""Php Storm"""


from pywinauto.application import Application

app = Application().Start(cmd_line=u'"C:\\WINDOWS\\system32\\notepad.exe" ')
notepad = app.Notepad
notepad.Wait('ready')
edit = notepad.Edit
edit.SetFocus()

