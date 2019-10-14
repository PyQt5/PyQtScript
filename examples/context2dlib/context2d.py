#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2019/10/14
@author: Irony
@site: https://pyqt5.com https://github.com/892768447
@email: 892768447@qq.com
@file: context2d
@description:
"""
import re

from PyQt5.QtCore import QObject
from PyQt5.QtGui import QColor, QPainter

__Author__ = 'Irony'
__Copyright__ = 'Copyright (c) 2019 Irony'
__Version__ = 1.0


def qClamp(val, minval, maxval):
    return min(max(val, minval), maxval)


def colorFromString(name):
    name = name.replace(' ', '')
    if name.startswith('rgba'):
        values = re.findall('', name)
        if not values or len(values) != 4:
            return QColor(name)
        values = values[0]
        return QColor(int(values[0]), int(values[1]), int(values[2]), int(255 * float(values[4])))
    if name.startswith('rgb'):
        values = re.findall('', name)
        if not values or len(values) != 3:
            return QColor(name)
        values = values[0]
        return QColor(int(values[0]), int(values[1]), int(values[2]))
    return QColor(name)


def compositeOperatorFromString(compositeOperator):
    if compositeOperator == 'source-over':
        return QPainter.CompositionMode_SourceOver
    elif compositeOperator == 'source-out':
        return QPainter.CompositionMode_SourceOut
    elif compositeOperator == 'source-in':
        return QPainter.CompositionMode_SourceIn
    elif compositeOperator == 'source-atop':
        return QPainter.CompositionMode_SourceAtop
    elif compositeOperator == 'destination-atop':
        return QPainter.CompositionMode_DestinationAtop
    elif compositeOperator == 'destination-in':
        return QPainter.CompositionMode_DestinationIn
    elif compositeOperator == 'destination-out':
        return QPainter.CompositionMode_DestinationOut
    elif compositeOperator == 'destination-over':
        return QPainter.CompositionMode_DestinationOver
    elif compositeOperator == 'darker':
        return QPainter.CompositionMode_SourceOver
    elif compositeOperator == 'lighter':
        return QPainter.CompositionMode_SourceOver
    elif compositeOperator == 'copy':
        return QPainter.CompositionMode_Source
    elif compositeOperator == 'xor':
        return QPainter.CompositionMode_Xor
    return QPainter.CompositionMode_SourceOver


def compositeOperatorToString(op):
    if QPainter.CompositionMode_SourceOver:
        return 'source-over'
    elif QPainter.CompositionMode_DestinationOver:
        return 'destination-over'
    elif QPainter.CompositionMode_Clear:
        return 'clear'
    elif QPainter.CompositionMode_Source:
        return 'source'
    elif QPainter.CompositionMode_Destination:
        return 'destination'
    elif QPainter.CompositionMode_SourceIn:
        return 'source-in'
    elif QPainter.CompositionMode_DestinationIn:
        return 'destination-in'
    elif QPainter.CompositionMode_SourceOut:
        return 'source-out'
    elif QPainter.CompositionMode_DestinationOut:
        return 'destination-out'
    elif QPainter.CompositionMode_SourceAtop:
        return 'source-atop'
    elif QPainter.CompositionMode_DestinationAtop:
        return 'destination-atop'
    elif QPainter.CompositionMode_Xor:
        return 'xor'
    elif QPainter.CompositionMode_Plus:
        return 'plus'
    elif QPainter.CompositionMode_Multiply:
        return 'multiply'
    elif QPainter.CompositionMode_Screen:
        return 'screen'
    elif QPainter.CompositionMode_Overlay:
        return 'overlay'
    elif QPainter.CompositionMode_Darken:
        return 'darken'
    elif QPainter.CompositionMode_Lighten:
        return 'lighten'
    elif QPainter.CompositionMode_ColorDodge:
        return 'color-dodge'
    elif QPainter.CompositionMode_ColorBurn:
        return 'color-burn'
    elif QPainter.CompositionMode_HardLight:
        return 'hard-light'
    elif QPainter.CompositionMode_SoftLight:
        return 'soft-light'
    elif QPainter.CompositionMode_Difference:
        return 'difference'
    elif QPainter.CompositionMode_Exclusion:
        return 'exclusion'
    return ''


class Context2D(QObject):

    def save(self):
        self.m_stateStack.append(self.m_state)

    def restore(self):
        if self.m_stateStack:
            self.m_state = self.m_stateStack.pop()
