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

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from .components.index import HToolBar
from .Pages.index import HWindows


class App(QMainWindow):

    def __init__(self):
        super().__init__()

        # Register Tool Bars
        self.addToolBar(HToolBar('Toolbar 1', self))

        # Central Widget
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)

        # Register Windows Here
        self.used_pages = [
            HWindows.Main,
            HWindows.Help
        ]
        self.init_UI()

    def init_UI(self):

        """initiates application UI"""
        self.resize(600, 380)
        self.center()
        self.setWindowTitle('Automata 304')
        self.show()
        self.__register_window()
        self.setMainWindow(HWindows.Main)
        self.statusBar().showMessage('Ready')

    def center(self):
        """centers the window on the screen"""

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

    def setMainWindow(self, window):
        self.central_widget.setCurrentWidget(window)

    def __register_window(self):
        for window in self.used_pages:
            self.central_widget.addWidget(window)
