#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

"""
Automata 304

This is an assignment on Automata

Author: Yves Jordan Nguejip Mukete
email: yvesjordan06@gmail.com
Last edited: December 2019
"""

import random
import sys

from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
from .components.HiroComponents import TopMenu


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_UI()
        self.top_menu = TopMenu(self)

    def init_UI(self):
        """initiates application UI"""
        self.resize(600, 380)
        self.center()
        self.setWindowTitle('Automata 304')
        self.show()
        self.statusBar().showMessage('Ready')

    def center(self):
        """centers the window on the screen"""

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)
