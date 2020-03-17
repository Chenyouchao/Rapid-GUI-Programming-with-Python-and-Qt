'''
    P83 4.1 25行的弹出式闹钟
    1. 在当前目录输入一下指令运行：
        "python alert.py 10:00 WakeUp"
        (书上的指令不含python，无法运行)
    2. sys.argv的参数从0开始计数，sys.argv[0]代表"python"
    3. pyqt5的模块做了调整，按照书上的模块导入会发生错误
'''

import sys
import time
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

try:
    due = QTime.currentTime()
    message = "Alert!"
    # 检查参数个数
    if len(sys.argv) < 2:   # len()从1计数
        raise ValueError
    # 检查参数有效性
    hours, mins = sys.argv[1].split(":")
    due = QTime(int(hours), int(mins))
    if not due.isValid():
        raise ValueError
    # 检查是否输入message参数
    if len(sys.argv) > 2:
        message = " ".join(sys.argv[2:])
except ValueError:
    message = "Usage:alert.pyw HH:MM [optional message]"

while QTime.currentTime() < due:
    time.sleep(1)

label = QLabel("<font color=red size=72><b>" + message + "</b></font>")
label.setWindowFlags(Qt.SplashScreen)
label.show()
QTimer.singleShot(10000, app.quit)
app.exec_()