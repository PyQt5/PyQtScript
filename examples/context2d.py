#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2019/10/14
@author: Irony
@site: https://pyqt5.com https://github.com/PyQt5
@email: 892768447@qq.com
@file: context2d
@description: 
"""
import sys

from PyQt5.QtWidgets import QApplication, QWidget

__Author__ = 'Irony'
__Copyright__ = 'Copyright (c) 2019'
__Version__ = 'Version 1.0'


class Window(QWidget):

    def __init__(self, *args, **kwarg):
        super(Window, self).__init__(*args, **kwarg)
        self.m_env = Environment(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.sohw()
    sys.exit(app.exec_())
