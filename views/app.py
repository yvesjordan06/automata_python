#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

"""
Automata 304

This is an assignment on Automata

Author: Yves Jordan Nguejip Mukete
email: yvesjordan06@gmail.com
Last edited: December 2019
"""

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

from views import Pages
from views.Components import HErrorDialog, HAction


def show_automata():
    a = Pages.HCreateAutomata()
    a.exec()


class MainWindow(QMainWindow):

    def __init__(self, flags=None, *args, **kwargs):
        super().__init__(flags, *args, **kwargs)

        self.AppPages = {
            'main': Pages.HMainWindow(),
            'help': Pages.HHelpWindow(),
            'new': Pages.HCreateAutomata()
        }

        self.AppActions = {
            'exit': HAction(
                name='Exit',
                shortcut='Ctrl+Q',
                status_tip='Quit Application',
                slot=self.close,
                icon=QIcon('icons/exit.png')
            ),
            'help': HAction(
                name='About',
                shortcut='Ctrl+F1',
                slot=[self.change_page, 'help']
            ),
            'new': HAction(
                name='New',
                shortcut='Ctrl+N',
                slot=[self.change_page, 'new'],
                status_tip='Create a new Automata'
            )
        }

        self.windows = list()
        self.stack = QStackedWidget()
        try:
            self.title = kwargs['title']
        except KeyError:
            self.title = 'Hiro Automata'

        self.create_menu()

        # Initialise et Demarre la vue
        self.initUI()

    def initUI(self):
        self.register_pages()

        self.setWindowTitle(self.title)
        self.statusBar().showMessage('Prêt')
        self.resize(400, 400)
        self.setCentralWidget(self.stack)

    def register_pages(self):
        for name, page in self.AppPages.items():
            self.stack.addWidget(page)

    def change_page(self, page):
        try:
            self.stack.setCurrentWidget(self.AppPages[page])
        except KeyError:
            HErrorDialog('Page Not Found', f'The page {page} is not found', 'Did you register the page ?').exec()

    def pop_page(self, page):
        try:
            self.AppPages[page].exec()
        except KeyError:
            HErrorDialog('Page Not Found', f'The page {page} is not found', 'Did you register the page ?').exec()

    def create_menu(self):

        mainMenu = self.menuBar()
        # Sub menu
        fileMenu = mainMenu.addMenu('&File')
        helpMenu = mainMenu.addMenu('&Help')

        # Actions to sub Menu
        fileMenu.addAction(self.AppActions['new'])
        fileMenu.addAction(self.AppActions['exit'])
        helpMenu.addAction(self.AppActions['help'])


def start_app():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    start_app()
