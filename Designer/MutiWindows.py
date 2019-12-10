"""
多窗口交互（1）：不使用信号和槽
Win1
Win2
"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from DateDialog import DateDialog

class MultiWindow1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("多窗口1")

        self.lineEdit = QLineEdit(self)
        self.button1 = QPushButton("弹出对话框1")
        self.button1.clicked.connect(self.onButton1Click)

