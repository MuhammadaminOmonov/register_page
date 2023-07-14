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
        self.userName_label = QLabel("Username", self)
        self.userName_label.setStyleSheet("""
    color: #FF0000;
    font-size: 25px;
    

""")

app = QApplication([])
window = Window()
window.show()
app.exec_()