# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 11:34:43 2018

@author: Nitish Kumar

"""

from subprocess import Popen
from pywinauto import Desktop
from pywinauto import Application
import time
from pywinauto.keyboard import SendKeys, KeySequenceError
import speech_recognition as sr

    
        app.PageSetupDlg.Ok.close_click() #close dialog
        app.Notepad.Edit.right_click() #right click edit
        app.Popup.menu_item("Right To Left Reading Order").click() #popup menu item click on RIght to left reading order

#saving process trigger
    app.Notepad.menu_select("File->SaveAs")
    app.SaveAs.EncodingComboBox.select("UTF-8")
    app.SaveAs.FileNameEdit.set_edit_text("Example-utf8.txt")
    app.SaveAs.Save.close_click()
    
    
    zulip_api
    
    
    

app = application.Application()
app.start(r"notepad.exe")
app = Application().connect(title_re=".*Notepad", class_name="Notepad")
#app.Notepad.menu_select("File->PageSetup")

app.Notepad.Edit.right_click()
app.Popup.menu_item("Right To Left Reading Order").click()

app.Notepad.Edit.type_keys(u"{END}{ENTER}SendText d\xf6\xe9s "
u"s\xfcpp\xf4rt \xe0cce\xf1ted characters!!!", with_spaces = True)

# Try and save
app.Notepad.menu_select("File->SaveAs")
app.SaveAs.EncodingComboBox.select("UTF-8")
app.SaveAs.edit1.set_edit_text("Example-utf8.txt")
app.SaveAs.Save.close_click()


app.UntitledNotepad.menu_select("File->SaveAs")
app.SaveAs.ComboBox5.select("UTF-8")
app.SaveAs.edit1.set_text("Example-utf8.txt")
app.SaveAs.Save.click()