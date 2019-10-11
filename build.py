#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2019年9月10日
@author: Irony
@site: https://pyqt5.com https://github.com/892768447
@email: 892768447@qq.com
@file: build
@description: 
"""
import argparse
import os
import shutil
import subprocess
import sys
import urllib.request
from tarfile import TarFile

__Author__ = 'Irony'
__Copyright__ = 'Copyright (c) 2019 Irony'
__Version__ = 1.0

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--platform', default=None,
                    metavar='[Windows or Linux]',
                    choices=['Windows', 'Linux'],
                    required=True, help='System platform')
parser.add_argument('-a', '--arch', default=None, type=str.lower,
                    metavar='[x86 or x64]', choices=['x86', 'x64'],
                    required=True, help='System Arch')
parser.add_argument('-b', '--build', default=None,
                    metavar='[sip or pyqt5]', type=str.lower, required=True, help='Build Target')
parser.add_argument('--sipver', default=None, type=str.lower, required=True, help='sip version')
parser.add_argument('--pyqtver', default=None, type=str.lower, required=True, help='pyqt5 version')
parser.add_argument('--qmake', default='', required=True, help='qmake tools')
parser.add_argument('--delete', default='True', type=str, help='Delete src files')
parser.add_argument('--skipdown', default='', type=str, help='skip download')

args = parser.parse_args()

assert args.build in ('sip', 'pyqt5')

print('Platform:', args.platform)
print('Arch:', args.arch)
make = 'make'
if args.platform == 'Windows':
    make = 'nmake'
print('Make:', make)
print('Build:', args.build)
print('Qmake:', args.qmake)
print('Del:', args.delete)
print('sip version:', args.sipver)
print('pyqt5 version:', args.pyqtver)
print('skipdown:', args.skipdown)

os.makedirs('src', exist_ok=True)
os.makedirs('{0}/{1}/PyQt5/Qt/bin'.format(args.platform, args.arch), exist_ok=True)
os.makedirs('{0}/{1}/PyQt5/Qt/lib'.format(args.platform, args.arch), exist_ok=True)


def buildSip():
    # 编译sip
    if args.delete:
        try:
            shutil.rmtree('sip-{0}'.format(args.sipver), ignore_errors=True)
        except Exception as e:
            print('remove sip', e)

        path = 'src/sip-{0}.tar.gz'.format(args.sipver)

        def reporthook(a, b, c):
            per = 100.0 * a * b / c
            if per > 100:
                per = 100
            print('download sip-%s.tar.gz %.2f%%' % (args.sipver, per))

        if not args.skipdown:
            url = 'https://www.riverbankcomputing.com/static/Downloads/sip/{0}/sip-{0}.tar.gz'.format(args.sipver)
            if args.platform == 'Windows':
                urllib.request.urlretrieve(url, path, reporthook)
            else:
                os.system('wget %s -O %s' % (url, path))

        with TarFile.open(path, 'r:*') as tf:
            tf.extractall(path='src')

        print('extractall sip ok')

    # 切换目录
    os.chdir('src/sip-{0}'.format(args.sipver))

    try:
        retcode = subprocess.check_call(
            sys.executable +
            ' configure.py && {0}'.format(make),
            shell=True, stderr=subprocess.STDOUT
        )
        print('retcode:', retcode)
        assert retcode == 0
        print('\nbuild sip ok\n')
    except subprocess.CalledProcessError as e:
        print(e)
        sys.exit(-1)


def patchConfigure():
    tpl1 = "\n    'QtScript':             ModuleMetadata(qmake_QT=['script', '-gui']),\n    'QtScriptTools':        " \
           "ModuleMetadata(qmake_QT=['scripttools', 'script', 'widgets']),\n"
    tpl2 = "    check_module(target_config, disabled_modules, verbose, 'QtScript',\n            'qscriptengine.h', " \
           "'new QScriptEngine()')\n    check_module(target_config, disabled_modules, verbose, 'QtScriptTools'," \
           "\n            'qscriptenginedebugger.h', 'new QScriptEngineDebugger()')\n "

    data = open(r'configure.py', 'rb').read().decode()
    if data.find('QScriptEngine') > -1:
        return

    index = data.find('QtSensors')
    start = data[:index - 6]
    end = data[index - 5:]
    data = start + tpl1 + end

    index = data.find('new QXmlName()')
    start = data[:index + 17]
    end = data[index + 17:]
    data = start + tpl2 + end

    open(r'configure.py', 'wb').write(data.encode())


def buildPyQt5():
    # 编译PyQt5
    if args.delete:
        try:
            shutil.rmtree('PyQt5_gpl-{0}'.format(args.pyqtver), ignore_errors=True)
        except Exception as e:
            print('remove PyQt5', e)

        path = 'src/PyQt5_gpl-{0}.tar.gz'.format(args.pyqtver)

        def reporthook(a, b, c):
            per = 100.0 * a * b / c
            if per > 100:
                per = 100
            print('download PyQt5_gpl-%s.tar.gz %.2f%%' % (args.pyqtver, per))

        if not args.skipdown:
            url = 'https://www.riverbankcomputing.com/static/Downloads/PyQt5/{0}/PyQt5_gpl-{0}.tar.gz'.format(
                args.pyqtver)
            if args.platform == 'Windows':
                urllib.request.urlretrieve(url, path, reporthook)
            else:
                os.system('wget %s -O %s' % (url, path))

        with TarFile.open('src/PyQt5_gpl-{0}.tar.gz'.format(args.pyqtver), 'r:*') as tf:
            tf.extractall(path='src')

        print('extractall PyQt5 ok')

    # 复制 QtScript sip
    try:
        shutil.copytree('sip/QtScript', 'src/PyQt5_gpl-{0}/sip/QtScript'.format(args.pyqtver))
        shutil.copytree('sip/QtScriptTools', 'src/PyQt5_gpl-{0}/sip/QtScriptTools'.format(args.pyqtver))
    except Exception as e:
        print(e)
    os.chdir('src/PyQt5_gpl-{0}'.format(args.pyqtver))
    # 修改 configure.py
    patchConfigure()

    try:
        cmd = '{0} configure.py ' \
              '--confirm-license ' \
              '--verbose ' \
              '--no-tools ' \
              '--no-designer-plugin ' \
              '--no-qml-plugin ' \
              '--disable=dbus ' \
              '--disable=QAxContainer ' \
              '--disable=QtAndroidExtras ' \
              '--disable=QtBluetooth ' \
              '--disable=QtDBus ' \
              '--disable=QtDesigner ' \
              '--disable=Enginio ' \
              '--disable=QtGui ' \
              '--disable=QtHelp ' \
              '--disable=QtLocation ' \
              '--disable=QtMacExtras ' \
              '--disable=QtMultimedia ' \
              '--disable=QtMultimediaWidgets ' \
              '--disable=QtNetwork ' \
              '--disable=QtNetworkAuth ' \
              '--disable=QtNfc ' \
              '--disable=QtOpenGL ' \
              '--disable=QtPositioning ' \
              '--disable=QtPrintSupport ' \
              '--disable=QtQml ' \
              '--disable=QtQuick ' \
              '--disable=QtQuickWidgets ' \
              '--disable=QtRemoteObjects ' \
              '--disable=QtSensors ' \
              '--disable=QtSerialPort ' \
              '--disable=QtSql ' \
              '--disable=QtSvg ' \
              '--disable=QtTest ' \
              '--disable=QtWebChannel ' \
              '--disable=QtWebKit ' \
              '--disable=QtWebKitWidgets ' \
              '--disable=QtWebSockets ' \
              '--disable=QtWinExtras ' \
              '--disable=QtX11Extras ' \
              '--disable=QtXml ' \
              '--disable=QtXmlPatterns ' \
              '--disable=_QOpenGLFunctions_1_0 ' \
              '--disable=_QOpenGLFunctions_1_1 ' \
              '--disable=_QOpenGLFunctions_1_2 ' \
              '--disable=_QOpenGLFunctions_1_3 ' \
              '--disable=_QOpenGLFunctions_1_4 ' \
              '--disable=_QOpenGLFunctions_1_5 ' \
              '--disable=_QOpenGLFunctions_2_0 ' \
              '--disable=_QOpenGLFunctions_2_1 ' \
              '--disable=_QOpenGLFunctions_3_0 ' \
              '--disable=_QOpenGLFunctions_3_1 ' \
              '--disable=_QOpenGLFunctions_3_2_Compatibility ' \
              '--disable=_QOpenGLFunctions_3_2_Core ' \
              '--disable=_QOpenGLFunctions_3_3_Compatibility ' \
              '--disable=_QOpenGLFunctions_3_3_Core ' \
              '--disable=_QOpenGLFunctions_4_0_Compatibility ' \
              '--disable=_QOpenGLFunctions_4_0_Core ' \
              '--disable=_QOpenGLFunctions_4_1_Compatibility ' \
              '--disable=_QOpenGLFunctions_4_1_Core ' \
              '--disable=_QOpenGLFunctions_4_2_Compatibility ' \
              '--disable=_QOpenGLFunctions_4_2_Core ' \
              '--disable=_QOpenGLFunctions_4_3_Compatibility ' \
              '--disable=_QOpenGLFunctions_4_3_Core ' \
              '--disable=_QOpenGLFunctions_4_4_Compatibility ' \
              '--disable=_QOpenGLFunctions_4_4_Core ' \
              '--disable=_QOpenGLFunctions_4_5_Compatibility ' \
              '--disable=_QOpenGLFunctions_4_5_Core ' \
              '--disable=_QOpenGLFunctions_ES2 ' \
              '--disable=pylupdate ' \
              '--disable=pyrcc ' \
              '--sip-incdir={1} ' \
              '--sip={2} ' \
              '{3} && {4} -j 8'.format(
            sys.executable,
            os.path.abspath('../sip-{0}/siplib/'.format(args.sipver)),
            os.path.abspath(
                '../sip-{0}/sipgen/sip{1}'.format(args.sipver,
                                                  '.exe' if args.platform == 'Windows' else '')),
            '--qmake={}'.format(args.qmake) if args.qmake and args.platform == 'Windows' else '',
            os.path.abspath(
                '../../tools/jom.exe') if args.platform == 'Windows' else 'make'
        )
        print('cmd:', cmd)
        retcode = subprocess.check_call(
            cmd,
            env=os.environ, shell=True,
            stderr=subprocess.STDOUT
        )
        print('retcode:', retcode)
        assert retcode == 0
        print('\nbuild PyQt5 ok\n')
    except subprocess.CalledProcessError as e:
        print(e)
        sys.exit(-1)

    ext = 'pyd' if args.platform == 'Windows' else 'so'

    # 复制pyd
    fsrc = 'QtScript/QtScript.{0}'.format(ext)
    fdst = '../../{0}/{1}/PyQt5/QtScript.{2}'.format(
        args.platform, args.arch, ext)
    if os.path.exists(fsrc):
        shutil.copyfile(fsrc, fdst)
    else:
        print('QtScript not found')
        sys.exit(-1)

    fsrc = 'QtScriptTools/QtScriptTools.{0}'.format(ext)
    fdst = '../../{0}/{1}/PyQt5/QtScriptTools.{2}'.format(
        args.platform, args.arch, ext)
    if os.path.exists(fsrc):
        shutil.copyfile(fsrc, fdst)
    else:
        print('QtScriptTools not found')
        sys.exit(-1)

    # 复制dll
    if args.platform == 'Windows':
        shutil.copyfile(
            os.path.join(os.path.dirname(args.qmake), 'Qt5Script.dll'),
            '../../{0}/{1}/PyQt5/Qt/bin/Qt5Script.dll'.format(args.platform, args.arch)
        )
        shutil.copyfile(
            os.path.join(os.path.dirname(args.qmake), 'Qt5ScriptTools.dll'),
            '../../{0}/{1}/PyQt5/Qt/bin/Qt5ScriptTools.dll'.format(args.platform, args.arch)
        )
    else:
        fsrc = os.path.join(os.path.dirname(os.path.dirname(args.qmake)), 'lib',
                            'libQt5Script.so.{0}'.format(args.pyqtver))
        fdst = '../../{0}/{1}/PyQt5/Qt/lib/libQt5Script.so.{2}'.format(args.platform, args.arch, args.pyqtver)
        print('copy {0} to {1}'.format(fsrc, fdst))
        shutil.copyfile(fsrc, fdst)

        fsrc = os.path.join(os.path.dirname(os.path.dirname(args.qmake)), 'lib',
                            'libQt5ScriptTools.so.{0}'.format(args.pyqtver))
        fdst = '../../{0}/{1}/PyQt5/Qt/lib/libQt5ScriptTools.so.{2}'.format(args.platform, args.arch, args.pyqtver)
        print('copy {0} to {1}'.format(fsrc, fdst))
        shutil.copyfile(fsrc, fdst)


if args.build == 'sip':
    buildSip()
if args.build == 'pyqt5':
    buildPyQt5()
