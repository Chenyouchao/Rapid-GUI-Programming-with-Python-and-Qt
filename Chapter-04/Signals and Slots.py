'''
    p95
    4.4 Signals and Slots
'''

import sys
from PyQt5.QtWidgets import QDialog, QDial, QSpinBox, QHBoxLayout, QApplication

class Form(QDialog):
    def __init__(self):
        super().__init__()

        self.dial = QDial()
        self.dial.setNotchesVisible(True)
        self.spinbox = QSpinBox()

        layout = QHBoxLayout()
        layout.addWidget(self.dial)
        layout.addWidget(self.spinbox)
        self.setLayout(layout)

        # 1. 型号参数数量 >= 槽参数数量
        # 2. 信号与槽, 对应参数类型要一致
        self.spinbox.valueChanged.connect(self.dial.setValue)
        self.dial.valueChanged.connect(self.spinbox.setValue)

        self.setWindowTitle("Signals and Slots")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()