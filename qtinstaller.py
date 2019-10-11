#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2019/10/10
@author: Irony
@site: https://pyqt5.com https://github.com/892768447
@email: 892768447@qq.com
@file: qtinstaller
@description:
"""

import argparse
import os
import subprocess

import requests

__Author__ = 'Irony'
__Copyright__ = 'Copyright (c) 2019 Irony'
__Version__ = 1.0

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--platform', default=None,
                    metavar='[Windows or Linux]',
                    choices=['Windows', 'Linux'],
                    required=True, help='System platform')
parser.add_argument('--qtver', default=None, type=str.lower, required=True, help='qt5 version')
parser.add_argument('--dir', default='', required=True, help='qt5 install to dir')

args = parser.parse_args()

print('Platform:', args.platform)
print('Qt:', args.qtver)

args.dir = args.dir or r'C:\Qt\{0}'.format(args.qtver)
print('Dir:', args.dir)


def download(url, name):
    req = requests.get(url, stream=True)
    with open(name, 'wb') as fp:
        for chunk in req.iter_content(chunk_size=1024):
            if chunk:
                fp.write(chunk)
                fp.flush()
        fp.flush()


path = os.path.join(args.dir, args.qtver, 'msvc2017' if args.platform == 'Windows' else 'gcc_64')
print('check path: ', path)
if not os.path.exists(path):
    os.environ['INSTALLDIR'] = args.dir
    if args.platform == 'Windows':
        os.environ['PACKAGES'] = 'qt.qt5.{0}.win32_msvc2017,qt.qt5.{0}.win64_msvc2017_64,qt.qt5.{0}.qtscript,' \
                                 'qt.qt5.{0}.qtscript.win32_msvc2017,qt.qt5.{0}.qtscript.win64_msvc2017_64'.format(
            args.qtver.replace('.', ''))
        name = 'qt-opensource-windows-x86-{0}.exe'.format(args.qtver)
        url = 'http://download.qt.io/archive/qt/{1}/{0}/qt-opensource-windows-x86-{0}.exe'.format(args.qtver, '.'.join(
            args.qtver.split('.')[:2]))
        cmd1 = 'curl -fsS -o qt-opensource-windows-x86-{0}.exe http://mirrors.ustc.edu.cn/qtproject/archive/qt/{1}/{' \
               '0}/qt-opensource-windows-x86-{0}.exe'.format(args.qtver, '.'.join(args.qtver.split('.')[:2]))
        cmd2 = 'qt-opensource-windows-x86-{0}.exe -v --script qtinstaller.js'.format(args.qtver)
    else:
        os.environ['PACKAGES'] = 'qt.qt5.{0}.gcc_64,qt.qt5.{0}.qtscript,qt.qt5.{0}.qtscript.gcc_64'.format(
            args.qtver.replace('.', ''))
        name = 'qt-opensource-linux-x64-{0}.run'.format(args.qtver)
        url = 'http://download.qt.io/archive/qt/{1}/{0}/qt-opensource-linux-x64-{0}.run'.format(args.qtver, '.'.join(
            args.qtver.split('.')[:2]))
        cmd1 = 'curl -fsS -o qt-opensource-linux-x64-{0}.run http://mirrors.ustc.edu.cn/qtproject/archive/qt/{1}/{' \
               '0}/qt-opensource-linux-x64-{0}.run'.format(args.qtver, '.'.join(args.qtver.split('.')[:2]))
        cmd2 = 'chmod +x qt-opensource-linux-x64-{0}.run && ./qt-opensource-linux-x64-{0}.run -v --script ' \
               'qtinstaller.js'.format(args.qtver)

    if not os.path.exists(name):
        print(url)
        download(url, name)
        # print(cmd1)
        # retcode = subprocess.check_call(cmd1, shell=True, stderr=subprocess.STDOUT)
        # print('download qt retcode:', retcode)
        # assert retcode == 0

    assert os.path.exists(name)

    print(cmd2)
    retcode = subprocess.check_call(cmd2, shell=True, stderr=subprocess.STDOUT)
    print('install qt retcode:', retcode)
    assert retcode == 0
