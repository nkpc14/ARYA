# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 15:21:46 2018

@author: Nitish Kumar
"""

def show():
    from __future__ import print_function
    from pywinauto import Application
    
    # Open "Control Panel"
    Application().start('control.exe')
    app = Application(backend='uia').connect(path='explorer.exe', title='Control Panel')
    
    # Go to "Programs"
    app.window(title='Control Panel').ProgramsHyperlink.invoke()
    app.wait_cpu_usage_lower(threshold=0.5, timeout=30, usage_interval=1.0)
    
    # Go to "Installed Updates"
    app.window(title='Programs').child_window(title='View installed updates', control_type='Hyperlink').invoke()
    app.wait_cpu_usage_lower(threshold=0.5, timeout=30, usage_interval=1.0)
    
    list_box = app.InstalledUpdates.FolderViewListBox
    
    # list all updates
    items = list_box.descendants(control_type='ListItem')
    all_updates = [item.window_text() for item in items]
    print('\nAll updates ({}):\n'.format(len(all_updates)))
    print(all_updates)
    
    # list updates from "Microsoft Windows" group only
    windows_group_box = list_box.child_window(title_re='^Microsoft Windows.*', control_type='Group')
    windows_items = windows_group_box.descendants(control_type='ListItem')
    windows_updates = [item.window_text() for item in windows_items]
    print('\nWindows updates only ({}):\n'.format(len(windows_updates)))
    print(windows_updates)