#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2019/10/11
@author: Irony
@site: https://pyqt5.com https://github.com/892768447
@email: 892768447@qq.com
@file: helloscript
@description:
"""
import sys

from PyQt5.QtScript import QScriptEngine
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QMessageBox

__Author__ = 'Irony'
__Copyright__ = 'Copyright (c) 2019 Irony'
__Version__ = 1.0


class Window(QWidget):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        layout = QVBoxLayout(self)
        button = QPushButton(self)
        layout.addWidget(button)

        # js 引擎
        self.engine = QScriptEngine(self)
        self.engine.installTranslatorFunctions()

        # 创建一个js访问的按钮对象
        scriptButton = self.engine.newQObject(button)
        self.engine.globalObject().setProperty('button', scriptButton)

        # 读取js
        contents = open('data/helloscript.js', 'rb').read().decode()
        # 执行js
        result = self.engine.evaluate(contents, 'helloscript.js')

        # 检查错误, 但是只能检查一些常规的执行的错误, 未执行的函数是没有办法得到错误, 需要通过debugger界面得到
        if result.isError():
            QMessageBox.critical(self, 'Hello Script',
                                 '{0}:{1}: {2}'.format('helloscript.js', result.property('line').toInt32(),
                                                       result.toString()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
