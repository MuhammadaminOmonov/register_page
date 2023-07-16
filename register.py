from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from os import system as sys
sys("cls")

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.move(600, 200)
        self.setFixedSize(600, 700)
        self.setWindowTitle("Register page")
        self.setWindowIcon(QIcon("C:\\Users\\HP\\Desktop\\calculator\\calculator.png"))
        self.setStyleSheet("background-color: #000000;")
        self.userName_label = QLabel("Username", self)
        self.userName_label.setGeometry(20, 10, 550, 50)
        self.userName_label.setStyleSheet("""
    color: #FF0000;
    font-size: 25px;
    background-color: #124589;
    font-weight: bold;
    padding: 0.5em;
""")
        self.userName_Input = QLineEdit(self)
        self.userName_Input.setGeometry(20, 75, 550, 60)
        self.userName_Input.setStyleSheet("""
    color: #0000FF;
    font-size: 25px;
    font-family: monospace;
    background-color: #FFFFFF;
    padding: 0.5em
""")
        self.userName_label = QLabel("Password", self)
        self.userName_label.setGeometry(20, 150, 550, 50)
        self.userName_label.setStyleSheet("""
    color: #FF0000;
    font-size: 25px;
    background-color: #124589;
    font-weight: bold;
    padding: 0.5em;
""")
        self.userName_Input = QLineEdit(self)
        self.userName_Input.setGeometry(20, 215, 550, 60)
        self.userName_Input.setStyleSheet("""
    color: #0000FF;
    font-size: 25px;
    font-family: monospace;
    background-color: #FFFFFF;
    padding: 0.5em
""")


app = QApplication([])
window = Window()
window.show()
app.exec_()