# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 13:43:30 2018

@author: Nitish Kumar
"""

from pywinauto import Desktop, Application

app = Application(backend="uia").start('calc.exe')

dlg = Desktop(backend="uia").Calculator
dlg.type_keys('2*3=')
dlg.print_control_identifiers()

dlg.minimize()
Desktop(backend="uia").window(title='Calculator', visible_only=False).restore()