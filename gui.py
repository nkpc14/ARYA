import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout,QLabel, QApplication
from PyQt5.QtGui import QPixmap, QMovie
from PyQt5.QtWidgets import QPushButton

app=QApplication(sys.argv)
w=QWidget()
l1=QLabel(w)
l2=QLabel(w)
l4=QLabel(w)
pixmap2=QPixmap('pics.png')
l2.setPixmap(pixmap2)
l2.move(400,500)
l2.resize(200,200)
pixmap1=QPixmap('arya_logo.jpg')
l1.setPixmap(pixmap1)
l1.move(-70,-70)
l1.resize(1500,500)

w.setStyleSheet("background-color:#08000c")
b2=QPushButton("ARYA",w)
b2.move(500,500)
b2.setStyleSheet("background-color: white;border-style: outset;border-radius: 10px;border-color: beige;font: bold 30px;padding: 6px;height:100px;width:200px;")
#b2.clicked.connect(Arya1.startARYA())
w.show()
app.exec_()