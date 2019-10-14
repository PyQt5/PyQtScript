#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2019/10/14
@author: Irony
@site: https://pyqt5.com https://github.com/PyQt5
@email: 892768447@qq.com
@file: Environment
@description: 
"""
import re
from enum import Enum

from PyQt5.QtCore import Qt, QObject, pyqtSlot, QTimerEvent, QEvent, QDateTime
from PyQt5.QtGui import QGradient, QColor
from PyQt5.QtScript import QScriptEngine, QScriptValueIterator, QScriptValue, QScriptable

__Author__ = 'Irony'
__Copyright__ = 'Copyright (c) 2019'
__Version__ = 'Version 1.0'


class KeyCodes(Enum):
    DOM_VK_UNDEFINED = 0x0
    DOM_VK_RIGHT_ALT = 0x12
    DOM_VK_LEFT_ALT = 0x12
    DOM_VK_LEFT_CONTROL = 0x11
    DOM_VK_RIGHT_CONTROL = 0x11
    DOM_VK_LEFT_SHIFT = 0x10
    DOM_VK_RIGHT_SHIFT = 0x10
    DOM_VK_META = 0x9D
    DOM_VK_BACK_SPACE = 0x08
    DOM_VK_CAPS_LOCK = 0x14
    DOM_VK_DELETE = 0x7F
    DOM_VK_END = 0x23
    DOM_VK_ENTER = 0x0D
    DOM_VK_ESCAPE = 0x1B
    DOM_VK_HOME = 0x24
    DOM_VK_NUM_LOCK = 0x90
    DOM_VK_PAUSE = 0x13
    DOM_VK_PRINTSCREEN = 0x9A
    DOM_VK_SCROLL_LOCK = 0x91
    DOM_VK_SPACE = 0x20
    DOM_VK_TAB = 0x09
    DOM_VK_LEFT = 0x25
    DOM_VK_RIGHT = 0x27
    DOM_VK_UP = 0x26
    DOM_VK_DOWN = 0x28
    DOM_VK_PAGE_DOWN = 0x22
    DOM_VK_PAGE_UP = 0x21
    DOM_VK_F1 = 0x70
    DOM_VK_F2 = 0x71
    DOM_VK_F3 = 0x72
    DOM_VK_F4 = 0x73
    DOM_VK_F5 = 0x74
    DOM_VK_F6 = 0x75
    DOM_VK_F7 = 0x76
    DOM_VK_F8 = 0x77
    DOM_VK_F9 = 0x78
    DOM_VK_F10 = 0x79
    DOM_VK_F11 = 0x7A
    DOM_VK_F12 = 0x7B
    DOM_VK_F13 = 0xF000
    DOM_VK_F14 = 0xF001
    DOM_VK_F15 = 0xF002
    DOM_VK_F16 = 0xF003
    DOM_VK_F17 = 0xF004
    DOM_VK_F18 = 0xF005
    DOM_VK_F19 = 0xF006
    DOM_VK_F20 = 0xF007
    DOM_VK_F21 = 0xF008
    DOM_VK_F22 = 0xF009
    DOM_VK_F23 = 0xF00A
    DOM_VK_F24 = 0xF00B


def qtToDomKey(keyCode):
    if keyCode == Qt.Key_Backspace:
        return KeyCodes.DOM_VK_BACK_SPACE
    elif keyCode == Qt.Key_Enter:
        return KeyCodes.DOM_VK_ENTER
    elif keyCode == Qt.Key_Return:
        return KeyCodes.DOM_VK_ENTER
    elif keyCode == Qt.Key_NumLock:
        return KeyCodes.DOM_VK_NUM_LOCK
    elif keyCode == Qt.Key_Alt:
        return KeyCodes.DOM_VK_RIGHT_ALT
    elif keyCode == Qt.Key_Control:
        return KeyCodes.DOM_VK_LEFT_CONTROL
    elif keyCode == Qt.Key_Shift:
        return KeyCodes.DOM_VK_LEFT_SHIFT
    elif keyCode == Qt.Key_Meta:
        return KeyCodes.DOM_VK_META
    elif keyCode == Qt.Key_CapsLock:
        return KeyCodes.DOM_VK_CAPS_LOCK
    elif keyCode == Qt.Key_Delete:
        return KeyCodes.DOM_VK_DELETE
    elif keyCode == Qt.Key_End:
        return KeyCodes.DOM_VK_END
    elif keyCode == Qt.Key_Escape:
        return KeyCodes.DOM_VK_ESCAPE
    elif keyCode == Qt.Key_Home:
        return KeyCodes.DOM_VK_HOME
    elif keyCode == Qt.Key_Pause:
        return KeyCodes.DOM_VK_PAUSE
    elif keyCode == Qt.Key_Print:
        return KeyCodes.DOM_VK_PRINTSCREEN
    elif keyCode == Qt.Key_ScrollLock:
        return KeyCodes.DOM_VK_SCROLL_LOCK
    elif keyCode == Qt.Key_Left:
        return KeyCodes.DOM_VK_LEFT
    elif keyCode == Qt.Key_Right:
        return KeyCodes.DOM_VK_RIGHT
    elif keyCode == Qt.Key_Up:
        return KeyCodes.DOM_VK_UP
    elif keyCode == Qt.Key_Down:
        return KeyCodes.DOM_VK_DOWN
    elif keyCode == Qt.Key_PageDown:
        return KeyCodes.DOM_VK_PAGE_DOWN
    elif keyCode == Qt.Key_PageUp:
        return KeyCodes.DOM_VK_PAGE_UP
    elif keyCode == Qt.Key_F1:
        return KeyCodes.DOM_VK_F1
    elif keyCode == Qt.Key_F2:
        return KeyCodes.DOM_VK_F2
    elif keyCode == Qt.Key_F3:
        return KeyCodes.DOM_VK_F3
    elif keyCode == Qt.Key_F4:
        return KeyCodes.DOM_VK_F4
    elif keyCode == Qt.Key_F5:
        return KeyCodes.DOM_VK_F5
    elif keyCode == Qt.Key_F6:
        return KeyCodes.DOM_VK_F6
    elif keyCode == Qt.Key_F7:
        return KeyCodes.DOM_VK_F7
    elif keyCode == Qt.Key_F8:
        return KeyCodes.DOM_VK_F8
    elif keyCode == Qt.Key_F9:
        return KeyCodes.DOM_VK_F9
    elif keyCode == Qt.Key_F10:
        return KeyCodes.DOM_VK_F10
    elif keyCode == Qt.Key_F11:
        return KeyCodes.DOM_VK_F11
    elif keyCode == Qt.Key_F12:
        return KeyCodes.DOM_VK_F12
    elif keyCode == Qt.Key_F13:
        return KeyCodes.DOM_VK_F13
    elif keyCode == Qt.Key_F14:
        return KeyCodes.DOM_VK_F14
    elif keyCode == Qt.Key_F15:
        return KeyCodes.DOM_VK_F15
    elif keyCode == Qt.Key_F16:
        return KeyCodes.DOM_VK_F16
    elif keyCode == Qt.Key_F17:
        return KeyCodes.DOM_VK_F17
    elif keyCode == Qt.Key_F18:
        return KeyCodes.DOM_VK_F18
    elif keyCode == Qt.Key_F19:
        return KeyCodes.DOM_VK_F19
    elif keyCode == Qt.Key_F20:
        return KeyCodes.DOM_VK_F20
    elif keyCode == Qt.Key_F21:
        return KeyCodes.DOM_VK_F21
    elif keyCode == Qt.Key_F22:
        return KeyCodes.DOM_VK_F22
    elif keyCode == Qt.Key_F23:
        return KeyCodes.DOM_VK_F23
    elif keyCode == Qt.Key_F24:
        return KeyCodes.DOM_VK_F24
    return keyCode


class Document(QObject):

    @pyqtSlot(str)
    def getElementById(self, eid):
        env = self.parent()
        canvas = env.canvasByName(eid)
        if not canvas:
            return QScriptValue()
        return env.toWrapper(canvas)

    @pyqtSlot(str)
    def getElementsByTagName(self, name):
        if name != 'canvas':
            return QScriptValue()
        env = self.parent()
        canvases = env.canvases()
        result = env.engine().newArray(len(canvases))
        for i, v in enumerate(canvases):
            result.setProperty(i, env.toWrapper(v))
        return result

    @pyqtSlot(str, object, bool)
    def addEventListener(self, _type, listener, useCapture):
        if listener.isFunction():
            env = self.parent()
            that = env.toWrapper(self)
            that.setProperty('on' + str(_type), listener)


class CanvasGradientPrototype(QObject, QScriptable):

    def addColorStop(self, offset, color):
        that = self.thisObject()
        if not that or that.value.type() == QGradient.NoGradient:
            return
        that.value.setColorAt(offset, colorFromString(color))

    def setup(self, engine):
        proto = CanvasGradientPrototype()
        engine.setDefaultPrototype(1, engine.newQObject(
            proto, QScriptEngine.ScriptOwnership, QScriptEngine.ExcludeSuperClassContents))


class Environment(QObject):

    def __init__(self, *args, **kwargs):
        super(Environment, self).__init__(*args, **kwargs)
        self.m_engine = QScriptEngine(self)
        self.m_document = self.m_engine.newObject(
            Document(self), QScriptEngine.QtOwnership, QScriptEngine.ExcludeSuperClassContents)

        CanvasGradientPrototype.setup(self.m_engine)
        self.m_originalGlobalObject = self.m_engine.globalObject()
        self.reset()

    def engine(self):
        return self.m_engine

    def document(self):
        return self.m_document

    def setTimeout(self, expression, delay):
        if expression.isString() or expression.isFunction():
            timerId = self.startTimer(delay)
            self.m_timeoutHash[timerId] = expression
            return timerId
        return -1

    def clearTimeout(self, timerId):
        self.killTimer(timerId)
        self.m_timeoutHash.pop(timerId, None)

    def setInterval(self, expression, delay):
        if expression.isString() or expression.isFunction():
            timerId = self.startTimer(delay)
            self.m_intervalHash[timerId] = expression
            return timerId
        return -1

    def clearInterval(self, timerId):
        self.killTimer(timerId)
        self.m_intervalHash.pop(timerId, None)

    def timerEvent(self, event):
        timerId = event.timerId()
        expression = self.m_intervalHash[timerId]
        if not expression.isValid():
            expression = self.m_timeoutHash[timerId]
            if expression.isValid():
                self.killTimer(timerId)
        if expression.isString():
            self.evaluate(expression.isString())
        elif expression.isFunction():
            expression.call()
        self.maybeEmitScriptError()

    def addCanvas(self, canvas):
        self.m_canvases.append(canvas)

    def canvasByName(self, name):
        for canvas in self.m_canvases:
            if canvas.objectName() == name:
                return canvas
        return 0

    def canvases(self):
        return self.m_canvases

    def reset(self):
        if self.m_engine.isEvaluating():
            self.m_engine.abortEvaluation()
        for timerId in self.m_intervalHash.keys():
            self.killTimer(timerId)
        self.m_intervalHash.clear()
        for timerId in self.m_timeoutHash.keys():
            self.killTimer(timerId)
        self.m_timeoutHash.clear()

        for canvas in self.m_canvases:
            canvas.reset()

        that = self.m_engine.newQObject(self, QScriptEngine.QtOwnership, QScriptEngine.ExcludeSuperClassContents)
        it = QScriptValueIterator(self.m_originalGlobalObject)
        while it.hasNext():
            it.next()
            that.setProperty(it.scriptName(), it.value(), it.flags())

        that.setProperty('self', that)
        that.setProperty('window', that)

        navigator = self.m_engine.newObject()
        navigator.setProperty('appCodeName', 'context2d')
        navigator.setProperty('appMinorVersion', 1)
        navigator.setProperty('appVersion', 1)
        navigator.setProperty('browserLanguage', 'en_US')
        navigator.setProperty('cookieEnabled', False)
        navigator.setProperty('cpuClass', 'i686')
        navigator.setProperty('onLine', False)
        navigator.setProperty('platform', 'bogus OS')
        navigator.setProperty('systemLanguage', 'en_US')
        navigator.setProperty('userAgent', 'Context2D/1.1')
        navigator.setProperty('userLanguage', 'en_US')
        that.setProperty('navigator', navigator)

        self.m_engine.setGlobalObject(that)
        self.m_engine.collectGarbage()

    def evaluate(self, code, fileName=''):
        return self.m_engine.evaluate(code, fileName)

    def hasIntervalTimers(self):
        return len(self.m_intervalHash) != 0

    def triggerTimers(self):
        for v in self.self.m_intervalHash.values():
            self.timerEvent(QTimerEvent(v))
        for v in self.self.m_timeoutHash.values():
            self.timerEvent(QTimerEvent(v))

    def toWrapper(self, obj):
        return self.m_engine.newQObject(
            obj, QScriptEngine.QtOwnership,
            QScriptEngine.PreferExistingWrapperObject | QScriptEngine.ExcludeSuperClassContents)

    def handleMouseEvent(self, canvas, e):
        _type = ''
        if e.type() == QEvent.MouseButtonPress:
            _type = 'mousedown'
        elif e.type() == QEvent.MouseButtonRelease:
            _type = 'mouseup'
        elif e.type() == QEvent.MouseMove:
            _type = 'mousemove'
        if not _type:
            return

        handler, handlerObject = self.eventHandler(canvas, _type)
        if not handler.isFunction():
            return

        scriptEvent = self.newFakeDomEvent(_type, self.toWrapper(canvas))
        # MouseEvent
        scriptEvent.setProperty('screenX', e.globalX(), QScriptValue.ReadOnly)
        scriptEvent.setProperty('screenY', e.globalY(), QScriptValue.ReadOnly)
        scriptEvent.setProperty('clientX', e.x(), QScriptValue.ReadOnly)
        scriptEvent.setProperty('clientY', e.y(), QScriptValue.ReadOnly)
        scriptEvent.setProperty('layerX', e.x(), QScriptValue.ReadOnly)
        scriptEvent.setProperty('layerY', e.y(), QScriptValue.ReadOnly)
        scriptEvent.setProperty('pageX', e.x(), QScriptValue.ReadOnly)
        scriptEvent.setProperty('pageY', e.y(), QScriptValue.ReadOnly)
        scriptEvent.setProperty('altKey', (e.modifiers() & Qt.AltModifier) != 0,
                                QScriptValue.ReadOnly)
        scriptEvent.setProperty('ctrlKey', (e.modifiers() & Qt.ControlModifier) != 0,
                                QScriptValue.ReadOnly)
        scriptEvent.setProperty('metaKey', (e.modifiers() & Qt.MetaModifier) != 0,
                                QScriptValue.ReadOnly)
        scriptEvent.setProperty('shiftKey', (e.modifiers() & Qt.ShiftModifier) != 0,
                                QScriptValue.ReadOnly)

        button = 0
        if e.button() == Qt.RightButton:
            button = 2
        elif e.button() == Qt.MidButton:
            button = 1
        scriptEvent.setProperty('button', button)
        scriptEvent.setProperty('relatedTarget', self.m_engine.nullValue(), QScriptValue.ReadOnly)
        handler.call(handlerObject, [scriptEvent])
        self.maybeEmitScriptError()

    def handleKeyEvent(self, canvas, e):
        _type = ''
        if e.type() == QEvent.KeyPress:
            _type = 'keydown'
        elif e.type() == QEvent.KeyRelease:
            _type = 'keyup'
        if not _type:
            return

        handler, handlerObject = self.eventHandler(canvas, _type)
        if not handler.isFunction():
            return

        scriptEvent = self.newFakeDomEvent(_type, self.toWrapper(canvas))
        # KeyEvent
        scriptEvent.setProperty('isChar', not e.text().isEmpty())
        scriptEvent.setProperty('charCode', e.text())
        scriptEvent.setProperty('keyCode', qtToDomKey(e.key()))
        scriptEvent.setProperty('which', e.key())
        handler.call(handlerObject, [scriptEvent])
        self.maybeEmitScriptError()

    def eventHandler(self, canvas, _type):
        handlerName = 'on' + str(_type)
        obj = self.toWrapper(canvas)
        handler = obj.property(handlerName)
        if not handler.isValid():
            obj = self.m_document
            handler = obj.property(handlerName)
        if handler.isFunction():
            who = obj
        else:
            who = QScriptValue()
        return handler, who

    def newFakeDomEvent(self, _type, target):
        e = self.m_engine.newObject()
        # Event
        e.setProperty('type', _type, QScriptValue.ReadOnly)
        e.setProperty('bubbles', True, QScriptValue.ReadOnly)
        e.setProperty('cancelable', False, QScriptValue.ReadOnly)
        e.setProperty('target', target, QScriptValue.ReadOnly)
        e.setProperty('currentTarget', target, QScriptValue.ReadOnly)
        e.setProperty('eventPhase', 3)  # bubbling
        e.setProperty('timeStamp', QDateTime.currentDateTime().toTime_t())
        # UIEvent
        e.setProperty('detail', 0, QScriptValue.ReadOnly)
        e.setProperty('view', self.m_engine.globalObject(), QScriptValue.ReadOnly)
        return e

    def maybeEmitScriptError(self):
        if self.m_engine.hasUncaughtException():
            self.scriptError.emit(self.m_engine.uncaughtException())
