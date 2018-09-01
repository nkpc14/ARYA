# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 14:18:25 2018

@author: Nitish Kumar
"""

from subprocess import Popen
from pywinauto import Desktop
from pywinauto import Application
import time
from pywinauto.keyboard import SendKeys, KeySequenceError
import AryaWindowsUpdate

import speech_recognition as sr
import pyttsx3
#import AryaSpeechModule



class AryaAI:
    
    """ Pywin @params  """
    MyApplicationList= {'sublime':'C:\\Program Files\\Sublime Text 3\\sublime_text.exe',
                        'notepad':'notepad.exe',
                        'paint':'mspaint.exe',
                        'chrome':'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
                        }
    dlg = None
    app = None
    pxwindowclass = None
    menu_item = None
    def __init__(self):
        self.voiceModel = ""
        """ Starting Speech Recognisation  """

    def aryaSTT(self):
        
        """# obtain audio from the microphone
        AryaSpeechModule.main()
        self.voiceModel = AryaSpeechModule.voiceModelData
        print("Arya : " + self.voiceModel)
        """
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
        self.app = Application().Start(cmd_line=u'"C:\\Program Files\\Sublime Text 3\\sublime_text.exe"')
        self.app = Application().Connect(title=u'untitled (demo) - Sublime Text (UNREGISTERED)', class_name='PX_WINDOW_CLASS')
        self.pxwindowclass = app.PX_WINDOW_CLASS
        self.pxwindowclass.Wait('ready')
        menu_item2 = self.pxwindowclass.MenuItem(u'&File->&New File\tCtrl+N')
        menu_item2.ClickInput()
        
    def startChrome(self):
        app = Application().Start(cmd_line=u'"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" -- "http:\\www.msftconnecttest.com\\redirect"')
        chromewidgetwin = app.Chrome_WidgetWin_1
        chromewidgetwin.Wait('ready')
    
    def startPaint(self):
         self.app = Application(backend='uia').start(r'mspaint.exe')
         self.dlg = self.app.window(title_re='.* - Paint') 
        
    def startNotepad(self):
        app = Application().Start(cmd_line=u'"C:\\WINDOWS\\system32\\notepad.exe" ')
        self.notepad = app.Notepad
        self.notepad.Wait('ready')
         
    def openFile(self,param):
        if(param == "sublime"):
            self.menu_item = self.pxwindowclass.MenuItem(u'&File')
            self.menu_item.ClickInput()
        elif(param=="notepad"):
            self.menu_item = self.notepad.MenuItem(u'&File')
            self.menu_item.ClickInput()
        elif(param=="paint"):
            self.dlg.File_tab.click()
            self.dlg.child_window(title='Open', control_type='MenuItem', found_index=0).invoke()
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
            self.dlg.File_tab.click()
            self.dlg.child_window(title='New', control_type='MenuItem', found_index=0).invoke()

        elif(param=="chrome"):
            pass
        else:
            pass
    def exitProgramm(self):
        self.app = Application().Connect(title=u'untitled (demo) - Sublime Text (UNREGISTERED)', class_name='PX_WINDOW_CLASS')
        self.menu_item2 = self.pxwindowclass.MenuItem(u'&File->&Exit')
        self.menu_item2.ClickInput()
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
                self.app = Application().connect(title_re=".*Notepad", class_name="Notepad")
                self.app.notepad.menu_select("File->SaveAs")
                self.app.SaveAs.EncodingComboBox.select("UTF-8")
                self.app.SaveAs.edit1.set_edit_text("Example-utf8.txt")
                self.app.SaveAs.Save.close_click()
            elif(param =="paint"):
                self.dlg = self.app.window(title_re='.* - Paint') 
                self.dlg.File_tab.click()
                self.dlg.SaveAsGroup.child_window(title="Save as", found_index=1).invoke()
            elif(param =="chrome"):
                pass
            else:
                pass
    def selectAll(self,param):
        if(param == "sublime"):
            self.app = Application().connect(title_re=".*Notepad", class_name="Notepad")
            self.app.notepad.menu_select("File->SaveAs")
        elif param == "notepad":
            self.app = Application().connect(title_re=".*Notepad", class_name="Notepad")
            menu_item2 = self.app.notepad.menu_select("Edit->Select All\tCtrl+A")
            menu_item2.ClickInput()
            
    def copy(self,param):
        if(param == "sublime"):
            self.app = Application().connect(title_re=".*Notepad", class_name="Notepad")
            self.app.notepad.menu_select("File->SaveAs")
        elif param == "notepad":
            self.app = Application().connect(title_re=".*Notepad", class_name="Notepad")
            menu_item2 = self.app.notepad.menu_select("Edit->Copy\tCtrl+C")
            menu_item2.ClickInput()
            
    def paste(self,param):
        if(param == "sublime"):
            self.app = Application().connect(title_re=".*Notepad", class_name="Notepad")
            self.app.notepad.menu_select("File->SaveAs")
        elif param == "notepad":
            self.app = Application().connect(title_re=".*Notepad", class_name="Notepad")
            menu_item2 = self.app.notepad.menu_select("Edit->Paste\tCtrl+V")
            menu_item2.ClickInput()
            
    def exitApp(self,param):
        if param == "sublime":
           self.app = Application().connect(title_re=".*Notepad", class_name="Notepad")
           self.app.notepad.menu_select("File->Exit")
        elif param == "notepad":
           self.app = Application().connect(title_re=".*Notepad", class_name="Notepad")
           self.app.notepad.menu_select("File->Exit")
           
    def aryaVoiceModule(self,speech):
        engine = pyttsx3.init()
        engine.say(speech)
        engine.runAndWait()
    
    def openPaintMenuItem(self,param):
        if param == "new":    
            self.dlg.child_window(title='New', control_type='MenuItem', found_index=0).invoke()
        elif param =="open":
            self.dlg.child_window(title='Open', control_type='MenuItem', found_index=0).invoke()
        elif param =="exit":
            self.dlg.child_window(title='Exit', control_type='MenuItem', found_index=0).invoke()

    def fileName(self,FileName):
        file_name_edit = self.dlg.Open.child_window(title="File name:", control_type="Edit")
        file_name_edit.set_text(FileName+'.jpg')
        self.dlg.Open.child_window(title="Open", auto_id="1", control_type="Button").click()
    
    def resizePaint(self):
        self.dlg = self.app.window(title_re='.* - Paint')
        self.dlg.ResizeButton.click()
        self.dlg.ResizeAndSkew.Pixels.select()
        if self.dlg.ResizeAndSkew.Maintain_aspect_ratio.get_toggle_state() != 1:
            self.dlg.ResizeAndSkew.Maintain_aspect_ratio.toggle()
        self.dlg.ResizeAndSkew.HorizontalEdit1.set_text('100')
        self.dlg.ResizeAndSkew.OK.click()
        
    def saveImageType(self,param):
        self.dlg = self.app.window(title_re='.* - Paint')
        if param == "png":
            self.dlg.child_window(title='PNG picture', found_index=0).invoke()
            self.dlg.SaveAs.File_name_ComboBox.Edit.set_text('image.png')
            self.dlg.SaveAs.Save.click()
            if self.dlg.ConfirmSaveAs.exists():
                self.dlg.ConfirmSaveAs.Yes.click()
            #self.dlg.close()
        elif param == "jpg":
            self.dlg.child_window(title='JPEG picture', found_index=0).invoke()
            self.dlg.SaveAs.File_name_ComboBox.Edit.set_text('image.png')
            self.dlg.SaveAs.Save.click()
            if self.dlg.ConfirmSaveAs.exists():
                self.dlg.ConfirmSaveAs.Yes.click()
            #self.dlg.close()
        elif param == "bmp":
            self.dlg.child_window(title='BMP picture', found_index=0).invoke()
            self.dlg.SaveAs.File_name_ComboBox.Edit.set_text('image.png')
            self.dlg.SaveAs.Save.click()
            if self.dlg.ConfirmSaveAs.exists():
                self.dlg.ConfirmSaveAs.Yes.click()
            #self.dlg.close()
        elif param == "gif":
            self.dlg.child_window(title='GIF picture', found_index=0).invoke()
            self.dlg.SaveAs.File_name_ComboBox.Edit.set_text('image.png')
            self.dlg.SaveAs.Save.click()
            if self.dlg.ConfirmSaveAs.exists():
                self.dlg.ConfirmSaveAs.Yes.click()
            #self.dlg.close()

    def printPaint(self):
        self.dlg.SaveAsGroup.child_window(title="Print", found_index=1).invoke()
        self.dlg.child_window(title='Print', found_index=0).invoke()
        
    def close(self):
        self.dlg = self.app.window(title_re='.* - Paint')
        self.dlg.close()
    
    def calDemo(self):
        pass
    
    def startCal(self):
        self.app = self.Application(backend="uia").start('calc.exe')
        self.dlg = Desktop(backend="uia").Calculator
        self.dlg.type_keys('2*3=')
        self.dlg.print_control_identifiers()
    
    def exitNotepad(self):
        self.app = Application().connect(title_re=".*Notepad", class_name="Notepad")
        self.menu_item = self.notepad.MenuItem(u'&File')
        self.menu_item.ClickInput()

def startARYA():
    Arya = AryaAI()
    
    while 1:
        Arya.aryaVoiceModule("Arya is Online")
        Arya.aryaSTT() 
        if Arya.voiceModel == "start sublime":
            Arya.aryaVoiceModule("Opening Sublime Please Wait")
            Arya.startSublime()
            while 1:
                Arya.aryaVoiceModule("Sublime Opened")
                Arya.aryaSTT() 
                if Arya.voiceModel == "close window":
                    Arya.aryaVoiceModule("Terminating programm")
                    Arya.exitProgramm()
                    break
                elif Arya.voiceModel == "open new file":
                    Arya.aryaVoiceModule("Opening New File")
                    Arya.openNewFile("sublime")
                elif Arya.voiceModel == "type":
                    Arya.aryaVoiceModule("Please Type something!")
                    Arya.aryaSTT() 
                    Arya.typeSomething("sublime",Arya.voiceModel)
                elif Arya.voiceModel == "save":
                    """ please enter your filename"""
                    Arya.saveAs("sublime")
                else:
                    print("I didn't get you")
                    
        elif Arya.voiceModel == "start notepad":
            Arya.aryaVoiceModule("Opening Notepad Please Wait")
            Arya.startNotepad()
            while 1:
                Arya.aryaVoiceModule("Notepad Opened")
                Arya.aryaSTT()
                if Arya.voiceModel =="close window":
                    Arya.exitNotepad()
                    break
                elif Arya.voiceModel == "open new file":
                    Arya.aryaVoiceModule("Opening New File")
                    Arya.aryaSTT()
                    Arya.openNewFile("notepad")
                elif Arya.voiceModel == "type":
                    Arya.aryaVoiceModule("Please say something")
                    Arya.aryaSTT()
                    Arya.typeSomething("notepad",Arya.voiceModel)
                elif Arya.voiceModel == "save":
                    Arya.saveAs("notepad")
                elif Arya.voiceModel == "select all":
                    Arya.selectAll("notepad")
                elif Arya.voiceModel == "copy":
                    Arya.copy("notepad")
                elif Arya.voiceModel == "exit":
                    Arya.saveAs("notepad")
                    Arya.exitApp("notepad")
                    Arya.aryaVoiceModule("Exiting Notepad")
                else:
                    print("I did't get you")
        elif Arya.voiceModel == "start paint":
            Arya.aryaVoiceModule("Starting Microsoft Paint Please Wait")
            Arya.startPaint()
            while 1:
                Arya.aryaVoiceModule("MS Paint Started")
                Arya.aryaSTT()
                if Arya.voiceModel == "close window":
                    Arya.close()
                    break
                elif Arya.voiceModel == "open new file":
                    Arya.openNewFile("paint")
                elif Arya.voiceModel == "open file menu":
                    Arya.openFileMenu()
                elif Arya.voiceModel == "new menu":
                    Arya.openPaintMenuItem("new")
                elif Arya.voiceModel == "file menu":
                    Arya.openPaintMenuItem("file")
                elif Arya.voiceModel == "exit menu":
                    Arya.openPaintMenuItem("exit")
                elif Arya.voiceModel == "open file":
                    Arya.aryaSTT()#filename Arya
                    Arya.fileName("image")
                elif Arya.voiceModel == "resize":
                    Arya.resizePaint()
                elif Arya.voiceModel == "save as":
                    Arya.saveAs("paint")
                    Arya.aryaSTT()#file type Arya
                    if Arya.voiceModel == "png":
                        Arya.saveImageType("png")
                    elif Arya.voiceModel == "jpg":
                        Arya.saveImageType("jpg")
                    elif Arya.voiceModel == "bmp":
                        Arya.saveImageType("bmp")
                    elif Arya.voiceModel == "gif":
                        Arya.saveImageType("gif")
                    else:
                        Arya.saveImageType("png")
                elif Arya.voiceModel == "close window":
                    Arya.close()
                else:
                    pass #invalid command
        elif Arya.voiceModel == "show Updates":
            AryaWindowsUpdate.show()
        else:
            break
startARYA()
