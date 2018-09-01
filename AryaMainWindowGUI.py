# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 20:30:52 2018

@author: Panku
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout,QLabel, QApplication
from PyQt5.QtGui import QPixmap, QMovie
from PyQt5.QtWidgets import QPushButton

import Arya1
def start():
    Arya1.startARYA()
    
def aryaGUI():
    app=QApplication(sys.argv)
    w=QWidget()
    l1=QLabel(w)
    l2=QLabel(w)
    l4=QLabel(w)
    
    t="Aastha Sharma\nAastha Sharma\nAastha Sharma\nAastha Sharma\nAastha Sharma\nAastha Sharma\nAastha Sharma\n"
    l3=QLabel("Suggestions:\n"+t,w)
    l3.move(20,400)
   # l3.resize(200,200)
    l3.setWordWrap(True)
    l3.setStyleSheet("color:white;border:0px;font:20px")
    pixmap = QPixmap('arya_logo.jpg')
    l1.setPixmap(pixmap)
    l1.move(-70,-70)
    #l1.resize(1500,600)0

    pixmap1=QPixmap('pics.png')
    l2.setPixmap(pixmap1)
    l2.move(400,400)
   # l2.resize(50,50)

    b2=QPushButton("ARYA",w)
    b2.move(700,500)
    b2.setStyleSheet("background-color: white;border-style: outset;border-radius: 10px;border-color: beige;font: bold 30px;padding: 6px;height:100px;width:200px;")
    b2.clicked.connect(start)
    # l5=QLabel(w)
    # movie=QMovie("v_gif.gif")
    # l5.setMovie(movie)
    # l5.move(300,500)
   # l5.resize(1280,720)
    #l5.setStyleSheet("border-radius:30px;")
    #movie.start()
    w.resize(600,400)
    w.setGeometry(10,10,600,400)
    w.setStyleSheet("background-color:#08000c;")
    w.show()
    app.exec_()
aryaGUI()