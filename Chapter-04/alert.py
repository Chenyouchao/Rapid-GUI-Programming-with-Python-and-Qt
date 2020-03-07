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