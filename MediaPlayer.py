# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 00:49:49 2018

@author: Panku
"""


"""Some automation of Windows Media player"""
from __future__ import unicode_literals
from __future__ import print_function

#import os
import time
import sys

try:
    from pywinauto import application
except ImportError:
    import os.path
    pywinauto_path = os.path.abspath(__file__)
    pywinauto_path = os.path.split(os.path.split(pywinauto_path)[0])[0]
    sys.path.append(pywinauto_path)
    from pywinauto import application


def windows_media():

    app = application.Application()

    try:
        app.start(   # connect_(path =
            r"C:\Program Files\Windows Media Player\wmplayer.exe")
    except application.ProcessNotFoundError:
        print("You must first start Windows Media "\
            "Player before running this script")
        sys.exit()

    app.WindowsMediaPlayer.menu_select("View->GoTo->Library")
    app.WindowsMediaPlayer.menu_select("View->Choose Columns")

    #for ctrl in app.ChooseColumns.children():
    #    print ctrl.class_name()


    print("Is it checked already:", app.ChooseColumsn.ListView.is_checked(1))

    # Check an Item in the listview
    app.ChooseColumns.ListView.check(1)
    time.sleep(.5)
    print("Shold be checked now:", app.ChooseColumsn.ListView.is_checked(1))

    # Uncheck it
    app.ChooseColumns.ListView.uncheck(1)
    time.sleep(.5)
    print("Should not be checked now:", app.ChooseColumsn.ListView.is_checked(1))

    # Check it again
    app.ChooseColumns.ListView.check(1)
    time.sleep(.5)

    app.ChooseColumsn.Cancel.click()

    app.WindowsMediaPlayer.menu_select("File->Exit")


def main():
    start = time.time()

    windows_media()

    print("Total time taken:", time.time() - start)

if __name__ == "__main__":
    main()