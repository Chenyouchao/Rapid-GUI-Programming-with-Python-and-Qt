'''
    p97
    ZeroSpinBox
'''

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class ZeroSpinBox(QSpinBox):
    zeros = 0
    atzero = pyqtSignal(object)     # 1. 定义信号

    def __init__(self):
        super().__init__()

        self.valueChanged.connect(self.checkzero)
        self.atzero.connect(self.test)      # 2. 关联信号与槽

    def checkzero(self):
        if self.value() == 0:
            self.zeros += 1
            self.atzero.emit(self.zeros)    # 3. 触发信号

    def test(self, num):
        print(num)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    box = ZeroSpinBox()
    box.show()
    app.exec_()