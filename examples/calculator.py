#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2019/10/12
@author: Irony
@site: https://pyqt5.com https://github.com/892768447
@email: 892768447@qq.com
@file: calculator
@description:
"""
import sys

from PyQt5.QtScript import QScriptEngine
from PyQt5.QtScriptTools import QScriptEngineDebugger
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.uic import loadUi

__Author__ = 'Irony'
__Copyright__ = 'Copyright (c) 2019 Irony'
__Version__ = 1.0


class Window(QWidget):

    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        loadUi('data/calculator/calculator.ui', self)

        # js 引擎
        self.engine = QScriptEngine(self)
        self.engine.installTranslatorFunctions()

        # debug window
        debugger = QScriptEngineDebugger(self)
        debugger.attachTo(self.engine)
        self.debugWindow = debugger.standardWindow()
        self.debugWindow.resize(800, 600)

        # 读取js
        contents = open('data/calculator/calculator.js', 'rb').read().decode()
        # 执行js
        self.engine.evaluate(contents, 'calculator.js')

        # 执行刚刚js中的一个函数
        ctor = self.engine.evaluate('Calculator')
        scriptUi = self.engine.newQObject(self, QScriptEngine.ScriptOwnership)
        # 创建一个新的Object并使用创建的对象作为“this”对象并将参数作为参数传递，将此QScriptValue作为构造函数调用。如果构造函数调用的返回值是一个对象，则返回该对象。否则，将返回默认的构造对象。
        ctor.construct([scriptUi])

        # 绑定输入框信号
        self.display.returnPressed.connect(self.debugWindow.show)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
