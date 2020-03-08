'''
    P86
    4.2 30行的表达式求值程序

    1. python3中,'/'为真除,无需引入'__future__'模块;
    2. Python3中,unicode()更换换为 str();
    3. PE8规范：import避免使用'*'.(*会导入包下的全部模块，降低程序运行速度)
'''

from math import *
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QDialog, QTextBrowser, QLineEdit, QVBoxLayout, QApplication

class Form(QDialog):
    def __init__(self):     # 作为主窗口,parent = none,可省略不写
        super().__init__()  # super()方法在python3中的新写法,更简洁

        # 定义元件
        self.browser = QTextBrowser()
        self.lineedit = QLineEdit("Type an expression and press Enter")
        self.lineedit.selectAll()

        # 布局
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)

        self.setWindowTitle("Calculate")
        self.lineedit.setFocus()

        # 关联信号与槽
        self.lineedit.returnPressed.connect(self.updataUi)

        # 槽函数
    def updataUi(self):
        try:
            text = str(self.lineedit.text())
            self.browser.append("%s = <b>%s</b>" % (text, eval(text)))
        except:
            self.browser.append("<font color=red>%s is invalid!</font>" % text)

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()