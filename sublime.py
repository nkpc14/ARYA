# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 11:50:24 2018

@author: Panku
"""
from subprocess import Popen
from pywinauto import Desktop
from pywinauto import Application
import time
from pywinauto.keyboard import SendKeys, KeySequenceError
import speech_recognition as sr
import AryaSpeechModule
class AryaAI:
    
    """ Pywin @params  """
    MyApplicationList= {'sublime':'C:\\Program Files\\Sublime Text 3\\sublime_text.exe',
                        'notepad':'notepad.exe',
                        'paint':'mspaint.exe',
                        'chrome':'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
                        }
        
    app = None
    dlg = None
    pxwindowclass = None
    notepad  = None
    mspaintapp = None
    menu_item = None
    menu_item2 = None
        
    def __init__(self):
        self.voiceModel = ""
        """ Starting Speech Recognisation  """

    def aryaSTT(self):
        # obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
        # recognize speech using Google Speech Recognition
        try:
            self.voiceModel = r.recognize_google(audio)
            print("Google Speech Recognition thinks you said " + self.voiceModel )
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        self.voiceModel = self.voiceModel.lower()

    def startSublime(self):  
        app = Application().Start(cmd_line=u'"C:\\Program Files\\Sublime Text 3\\sublime_text.exe"')
        app = Application().Connect(title=u'untitled (demo) - Sublime Text (UNREGISTERED)', class_name='PX_WINDOW_CLASS')
        self.pxwindowclass = app.PX_WINDOW_CLASS
        self.pxwindowclass.Wait('ready')
        menu_item2 = self.pxwindowclass.MenuItem(u'&File->&New File\tCtrl+N')
        menu_item2.ClickInput()
        
    def startChrome(self):
        app = Application().Start(cmd_line=u'"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" -- "http:\\www.msftconnecttest.com\\redirect"')
        chromewidgetwin = app.Chrome_WidgetWin_1
        chromewidgetwin.Wait('ready')
    
    def startPaint(self):
        app = Application().Start(cmd_line=u'"C:\\WINDOWS\\system32\\mspaint.exe" ')
        self.dlg = app.window(title_re='.* - Paint')
        self.mspaintapp = app.MSPaintApp
        self.mspaintapp.Wait('ready')    
        
    def startNotepad(self):
        app = Application().Start(cmd_line=u'"C:\\WINDOWS\\system32\\notepad.exe" ')
        self.notepad = app.Notepad
        self.notepad.Wait('ready')
         
    def openFileMenu(self):
        if(self.voiceModel == "sublime"):
            self.menu_item = self.pxwindowclass.MenuItem(u'&File')
            self.menu_item.ClickInput()
        elif(self.voiceModel=="notepad"):
            self.menu_item = self.notepad.MenuItem(u'&File')
            self.menu_item.ClickInput()
        elif(self.voiceModel=="paint"):
            pass
        elif(self.voiceModel=="notepad"):
            pass
        else:
            pass
        
    def openNewFile(self,param):
        if(param == "sublime"):
            self.menu_item2 = self.pxwindowclass.MenuItem(u'&File->&New\tCtrl+N')
            self.menu_item2.ClickInput()
        elif(param=="notepad"):
            self.menu_item = self.notepad.MenuItem(u'&File->&New File\tCtrl+N')
            self.menu_item.ClickInput()

        elif(param=="paint"):
            pass
        elif(param=="notepad"):
            pass
        else:
            pass
    
    def typeSomething(self,param,message):
        
        if(param == "sublime"):
            self.pxwindowclass.type_keys(message, with_spaces = True)
        elif(param =="notepad"):
            self.notepad.type_keys("Hello welcome to ARYA!", with_spaces = True)
        else:
            pass
    
    def saveAs(self,param):
            if(param == "sublime"):
                self.menu_item = self.pxwindowclass.MenuItem(u'&File->Save &As\u2026\tCtrl+Shift+S')
                self.menu_item.ClickInput()
                SendKeys('{ENTER 2}')
            elif(param =="notepad"):
                self.app.notepad.menu_select("File->SaveAs")
                self.app.SaveAs.EncodingComboBox.select("UTF-8")
                self.app.SaveAs.edit1.set_edit_text("Example-utf8.txt")
                self.app.SaveAs.Save.close_click()
            elif(param =="paint"):
                pass
            elif(param =="notepad"):
                pass
            else:
                pass
    
                
Arya = AryaAI()

while 1:
    Arya.aryaSTT() 
    if Arya.voiceModel == "start sublime":
        Arya.startSublime()
        while 1:
            Arya.aryaSTT() 
            if Arya.voiceModel == "a i terminate":
                break
            elif Arya.voiceModel == "open new file":
                Arya.openNewFile("sublime")
            elif Arya.voiceModel == "type":
                Arya.aryaSTT() 
                Arya.typeSomething("sublime",Arya.voiceModel)
            elif Arya.voiceModel == "save":
                Arya.saveAs("sublime")
            else:
                print("I didn't get you")
                
    elif Arya.voiceModel == "start notepad":
        Arya.startNotepad()
        while 1:
            Arya.aryaSTT()
            if Arya.voiceModel =="a i terminate":
                break
            elif Arya.voiceModel == "open new file":
                Arya.aryaSTT()
                Arya.openNewFile("notepad")
            elif Arya.voiceModel == "type":
                Arya.aryaSTT()
                Arya.typeSomething("notepad",Arya.voiceModel)
            elif Arya.voiceModel == "save":
                Arya.saveAs("notepad")
            else:
                print("I did't get you")


    
    
