#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2019/10/12
@author: Irony
@site: https://pyqt5.com https://github.com/892768447
@email: 892768447@qq.com
@file: defaultprototypes
@description:
"""
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtScript import QScriptEngine
from PyQt5.QtScriptTools import QScriptEngineDebugger
from PyQt5.QtWidgets import QApplication, QListWidget, QMessageBox

__Author__ = 'Irony'
__Copyright__ = 'Copyright (c) 2019 Irony'
__Version__ = 1.0


class Window(QListWidget):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        # js 引擎
        self.engine = QScriptEngine(self)
        self.engine.installTranslatorFunctions()
        # debug window
        debugger = QScriptEngineDebugger(self)
        debugger.attachTo(self.engine)
        self.debugWindow = debugger.standardWindow()
        self.debugWindow.resize(800, 600)
        self.debugWindow.show()

        # 创建一个js访问的对象
        self.engine.globalObject().setProperty('listWidget', self.engine.newQObject(self))

        # 读取js
        contents = open('data/defaultprototypes.js', 'rb').read().decode()
        # 执行js
        result = self.engine.evaluate(contents, 'defaultprototypes.js')

        # 检查错误, 但是只能检查一些常规的执行的错误, 未执行的函数是没有办法得到错误, 需要通过debugger界面得到
        if self.engine.hasUncaughtException():
            QMessageBox.critical(self, 'defaultprototypes',
                                 '{0}:{1}: {2}'.format('defaultprototypes.js', result.property('line').toInt32(),
                                                       result.toString()))

    # ## 暴露方法

    @pyqtSlot(str)
    def addItem(self, text):
        super(Window, self).addItem(text)

    @pyqtSlot(list)
    def addItems(self, texts):
        super(Window, self).addItems(texts)

    @pyqtSlot(int)
    def setBackgroundColor(self, row):
        self.setStyleSheet(
            'QListWidget::item {background-color: %s;}\nQListWidget::item {selection-color: black;}' % self.item(
                row).text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
