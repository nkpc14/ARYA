# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 01:42:07 2018

@author: Panku
"""

from pywinauto import Application
import time

start(self, cmd_line, timeout=app_start_timeout)  # instance method:
connect(self, **kwargs)  # instance method:
app = Application().start(r"c:\path\to\your\application -a -n -y --arguments")

app = Application().connect(process=2341)#process id
app = Application().connect(handle=0x010f0c) #handle
app = Application().connect(path=r"c:\windows\system32\notepad.exe")#path


""" pywinauto.findwindows.find_elements() """
app = Application().connect(title_re=".*Notepad", class_name="Notepad")


""" How to specify a dialog of the application """
dlg = app.Notepad
dlg = app['Notepad']
dlg = app.top_window()
findwindows.find_windows() 
dlg = app.window(title_re="Page Setup", class_name="#32770")
dialogs = app.windows() #this will return a list of all the visible, enabled,
# top level windows of the application
app.window(handle=win) #we can use the handle like this once we have it 
app.window(title_re=".*Part of Title.*") # if title of the dialog is very long


"""How to specify a control on a dialog """
app.dlg.control
app['dlg']['control']

"""Once a set of identifiers has been created for all controls in the dialog we disambiguate them.
use the WindowSpecification.print_control_identifiers() method"""
app.YourDialog.print_control_identifiers()


"""How to Access the System Tray"""
import pywinauto.application
app = pywinauto.application.Application().connect(path="explorer")
systray_icons = app.ShellTrayWnd.NotificationAreaToolbar


ClickSystemTrayIcon(button)

RightClickSystemTrayIcon(button)

"""Often, when you click/right click on an icon, you get a popup menu. 
The thing to remember at this point is that the popup menu is a part of the application being automated not part of explorer."""

# connect to outlook
outlook = Application.connect(path='outlook.exe')

# click on Outlook's icon
taskbar.ClickSystemTrayIcon("Microsoft Outlook")

# Select an item in the popup menu
outlook.PopupMenu.Menu().get_menu_path("Cancel Server Request")[0].click()





app.wait_cpu_usage_lower(threshold=5) # wait until CPU usage is lower than 5%


# call ensure_text_changed(ctrl) every 2 sec until it's passed or timeout (4 sec) is expired

@always_wait_until_passes(4, 2)
def ensure_text_changed(ctrl):
    if previous_text == ctrl.window_text():
        raise ValueError('The ctrl text remains the same while change is expected')
        
        
        
""" 
        Cross-platform module to emulate mouse events like a real user

pywinauto.mouse.click(button='left', coords=(0, 0))
Click at the specified coordinates

pywinauto.mouse.double_click(button='left', coords=(0, 0))
Double click at the specified coordinates

pywinauto.mouse.move(coords=(0, 0))
Move the mouse

pywinauto.mouse.press(button='left', coords=(0, 0))
Press the mouse button

pywinauto.mouse.release(button='left', coords=(0, 0))
Release the mouse button

pywinauto.mouse.right_click(coords=(0, 0))
Right click at the specified coords

pywinauto.mouse.scroll(coords=(0, 0), wheel_dist=1)
Do mouse wheel

pywinauto.mouse.wheel_click(coords=(0, 0))
Middle mouse button click at the specified coords
"""


import pywinauto.application

app = pywinauto.application.Application()
comapp = app.connect_(path = "explorer")

for i in comapp.windows_():
    if "Progman" == i.FriendlyClassName():
        i.ClickInput(coords=(900, 50))
        
        
import win32api
x, y = win32api.GetCursorPos()