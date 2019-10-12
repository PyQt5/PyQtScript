#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2019年9月10日
@author: Irony
@site: https://pyqt5.com https://github.com/892768447
@email: 892768447@qq.com
@file: test
@description: 
"""
import argparse
import os
import sys

try:
    from pip._internal import main as _main  # @UnusedImport
except:
    from pip import main as _main  # @Reimport @UnresolvedImport

__Author__ = 'Irony'
__Copyright__ = 'Copyright (c) 2019 Irony'
__Version__ = 1.0

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--platform', default=None,
                    metavar='[Windows or Linux]',
                    choices=['Windows', 'Linux'],
                    required=True, help='System platform')
parser.add_argument('-a', '--arch', default=None, type=str.lower,
                    metavar='[x86 or x64]',
                    choices=['x86', 'x64'],
                    required=True, help='System Arch')
parser.add_argument('-v', '--version', default=None, type=str.lower,
                    required=True, help='PyQt5 Version')
parser.add_argument('-t', '--tags', default=['cp35', 'cp36', 'cp37', 'cp38'], nargs='+',
                    metavar='cp35 cp36 cp37 cp38', help='Python version')

args = parser.parse_args()

assert args.version != None
print('Platform:', args.platform)
print('Arch:', args.arch)
print('Version:', args.version)
Name = 'PyQtScript'
print('Name:', Name)
print(args.tags)
Tags = '.'.join(args.tags)
print('Tags:', Tags)
build_version = os.environ.get('APPVEYOR_BUILD_VERSION', '')
print('build_version :', build_version)

if args.platform == 'Windows':
    Tag = '{0}-none{1}'.format(Tags,
                               '-win32' if args.arch == 'x86' else '-win_amd64' if args.arch == 'x64' else '')
elif args.platform == 'Linux':
    Tag = '{0}-abi3-manylinux1_x86_64'.format(Tags)
else:
    Tag = '{0}-none'.format(Tags)

_main(['install', os.path.abspath(
    'dist/{0}-{1}-{2}.whl'.format(Name, build_version if build_version else args.version, Tag))])

if args.platform != 'Windows':
    # ln library
    import PyQt5
    from PyQt5 import QtCore

    dirpath = os.path.dirname(PyQt5.__file__)
    print('PyQt5 dir:', dirpath)
    os.chdir(dirpath)
    if not os.path.islink('libQt5Script.so'):
        os.system('ln -s libQt5Script.so.{0} libQt5Script.so'.format(QtCore.PYQT_VERSION_STR))
    if not os.path.islink('libQt5Script.so.5'):
        os.system('ln -s libQt5Script.so.{0} libQt5Script.so.5'.format(QtCore.PYQT_VERSION_STR))
    if not os.path.islink('libQt5Script.so.{0}'.format('.'.join(QtCore.PYQT_VERSION_STR.split('.')[:2]))):
        os.system('ln -s libQt5Script.so.{0} libQt5Script.so.{1}'.format(
            QtCore.PYQT_VERSION_STR, '.'.join(QtCore.PYQT_VERSION_STR.split('.')[:2])))
    if not os.path.islink('libQt5ScriptTools.so'):
        os.system('ln -s libQt5ScriptTools.so.{0} libQt5ScriptTools.so'.format(QtCore.PYQT_VERSION_STR))
    if not os.path.islink('libQt5ScriptTools.so.5'):
        os.system('ln -s libQt5ScriptTools.so.{0} libQt5ScriptTools.so.5'.format(QtCore.PYQT_VERSION_STR))
    if not os.path.islink('libQt5ScriptTools.so.{0}'.format('.'.join(QtCore.PYQT_VERSION_STR.split('.')[:2]))):
        os.system('ln -s libQt5ScriptTools.so.{0} libQt5ScriptTools.so.{1}'.format(
            QtCore.PYQT_VERSION_STR, '.'.join(QtCore.PYQT_VERSION_STR.split('.')[:2])))

# 加载模块是否正常
try:
    from PyQt5 import QtCore

    print(QtCore)
    print(QtCore.PYQT_VERSION_STR)
    print(QtCore.QT_VERSION_STR)
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtScript import QScriptEngine
    from PyQt5.QtScriptTools import QScriptEngineDebugger

    app = QApplication(sys.argv)
    print(QScriptEngine, QScriptEngine())
    print(QScriptEngineDebugger, QScriptEngineDebugger())
except Exception as e:
    print(e)
    sys.exit(-1)
