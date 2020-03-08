'''
    p90
    4.3 70行的货币转换程序

    原汇率网址已失效,对getData()方法进行了重写：
    1. 采用requests库获取网页内容;
    2. 采用lxml库的xpath路径表达式从网页内容中提取所需信息.
'''

import sys
import requests
from lxml import etree
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QDialog, QLabel, QComboBox, QDoubleSpinBox, QGridLayout, QApplication

class Form(QDialog):
    def __init__(self):
        super().__init__()
        # 设置窗口
        self.setWindowTitle("Currency")

        # 获取数据
        data = self.getData()
        currenyTypes = sorted(self.rates.keys())   # 提取币种列表

        # 设置窗口部件
        dataLabel = QLabel(data)            # 标签部件
        self.fromComboBox = QComboBox()     # 下拉框(输入币种)
        self.fromComboBox.addItems(currenyTypes)
        self.fromSpinBox = QDoubleSpinBox() # 微调框（含上下两个调节按钮）
        self.fromSpinBox.setRange(0.01, 10000000.00)
        self.fromSpinBox.setValue(1.00)
        self.toComboBox = QComboBox()       # 下拉框（输入币种）
        self.toComboBox.addItems(currenyTypes)
        self.toLabel = QLabel("1.00")

        # 网格布局
        grid = QGridLayout()    # 创建网格布局
        grid.addWidget(dataLabel, 0, 0)
        grid.addWidget(self.fromComboBox, 1, 0)
        grid.addWidget(self.fromSpinBox, 1, 1)
        grid.addWidget(self.toComboBox, 2, 0)
        grid.addWidget(self.toLabel, 2, 1)
        
        self.setLayout(grid)    # 将布局设置在当前对象上

        # 关联信号与槽
        self.fromComboBox.currentIndexChanged.connect(self.updataUi)
        self.toComboBox.currentIndexChanged.connect(self.updataUi)
        self.fromSpinBox.valueChanged.connect(self.updataUi)     # python3只有float
        
        # self.connect(self.fromSpinBox, SIGNAL("valueChanged(float)"), self.updataUi)

    # 设置槽函数
    def updataUi(self):
        from_ = str(self.toComboBox.currentText())
        to = str(self.fromComboBox.currentText())
        amount = self.rates[to] / self.rates[from_] * self.fromSpinBox.value()
        self.toLabel.setText("%0.2f" % amount)

    # getData()函数，获取汇率数据
    def getData(self):
        self.rates = {}
        
        try:
            url = "https://www.bankofcanada.ca/rates/exchange/daily-exchange-rates"     # 汇率网站,书上的网址404
            respond = requests.get(url)         # 采用requests库对网站解析

            datas = etree.HTML(respond.text)    # 将respond转化为文本后,再转化为lxml的HTML对象

            date = datas.xpath(f'//thead[@class="bocss-table__thead"]//th[6]/text()')
            ratesCountries = datas.xpath(f'//tr[@class="bocss-table__tr"]/th/text()')   # 使用lxml库的xpath表达式提取国家和对应的汇率消息
            ratesNums = datas.xpath(f'//tr[@class="bocss-table__tr"]/td[5]/text()')     # xpath元素从1计数
        
            self.rates = dict(zip(map(str,ratesCountries), map(float,ratesNums)))
            return "Exchange Rate Date:" + date[0]      # 通过xpath选中日期时会自动变为重复的两个,原因不明
        except Exception as e:      # 'except Exception, e:'为python2用法,在python3中会报错
            return "Failed to download:\n%s" % e

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()