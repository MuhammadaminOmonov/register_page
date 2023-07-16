from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from os import system as sys
sys("cls")

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.move(600, 200)
        self.setFixedSize(600, 500)
        self.setWindowTitle("Register page")
        self.setWindowIcon(QIcon("C:\\Users\\HP\\Desktop\\calculator\\calculator.png"))
        self.setStyleSheet("background-color: #000000;")
        self.main_box = QVBoxLayout(self)
        self.userName_label = QLabel("Username", self)
        self.userName_label.setStyleSheet("""
    color: #FF0000;
    font-size: 25px;
    background-color: #124589;
    font-weight: bold;
    padding: 0.5em;
""")
        self.userName_Input = QLineEdit(self)
        self.userName_Input.setStyleSheet("""
    color: #0000FF;
    font-size: 25px;
    font-family: monospace;
    background-color: #FFFFFF;
    padding: 0.5em
""")
        self.password_label = QLabel("Password", self)
        self.password_label.setStyleSheet("""
    color: #FF0000;
    font-size: 25px;
    background-color: #124589;
    font-weight: bold;
    padding: 0.5em;
""")
        self.password_Input = QLineEdit(self)
        self.password_Input.setPlaceholderText("Kamida 8 belgidan iborat bo'lishi kerak")
        self.password_Input.setStyleSheet("""
    color: #0000FF;
    font-size: 25px;
    font-family: monospace;
    background-color: #FFFFFF;
    padding: 0.5em
""")
        self.check_box = QCheckBox("Quyidagi shartlarga rozimisiz?", self)
        self.check_box.setStyleSheet("color: #FFFFFF;")

        self.radio_button_box = QVBoxLayout(self)
        self.radio_button_1 = QRadioButton("Erkak", self)
        self.radio_button_1.setStyleSheet("color: white;")
        self.radio_button_2 = QRadioButton("Ayol", self)
        self.radio_button_2.setStyleSheet("color: white;")
        self.radio_button_box.addWidget(self.radio_button_1)
        self.radio_button_box.addWidget(self.radio_button_2)

        self.button_box = QHBoxLayout(self)
        self.button_clear = QPushButton("CLEAR", self)
        self.button_clear.setStyleSheet("background-color: yellow;")
        self.button_clear.clicked.connect(lambda: func_clear(self.userName_Input, self.password_Input))
        self.button_submit = QPushButton("SUBMIT", self)
        self.button_submit.setStyleSheet("background-color: yellow;")
        self.button_submit.clicked.connect(lambda: func_submit(self))
        def func_clear(userName_Input, password_Input):
            userName_Input.clear()
            password_Input.clear()

        def func_submit(self):
            if len(self.userName_Input.text()) > 0 and len(self.password_Input.text()) > 8:
                self.notice_blank = QMessageBox(self)
                self.notice_blank.setWindowTitle("Eslatma")
                self.notice_blank.setText("Ro'yxatdan o'tdingiz")
                self.notice_blank.setStyleSheet("background-color: white;")
                self.notice_blank.exec_()
            else:
                self.notice_blank = QMessageBox(self)
                self.notice_blank.setWindowTitle("Eslatma")
                self.notice_blank.setText("Ro'yxatdan o'tmadingiz")
                self.notice_blank.setStyleSheet("background-color: white;")
                self.notice_blank.exec_()

        self.button_box.addWidget(self.button_clear)
        self.button_box.addWidget(self.button_submit)

        self.main_box.addWidget(self.userName_label)
        self.main_box.addWidget(self.userName_Input)
        self.main_box.addWidget(self.password_label)
        self.main_box.addWidget(self.password_Input)
        self.main_box.addWidget(self.check_box)
        self.main_box.addLayout(self.radio_button_box)
        self.main_box.addLayout(self.button_box)

app = QApplication([])
window = Window()
window.show()
app.exec_()