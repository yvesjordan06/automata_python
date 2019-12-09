import functools

from PyQt5.QtGui import QIcon, QTextLine
from PyQt5.QtWidgets import QWidget, QAction, QMainWindow, QToolBar, QMenuBar

from ..Pages.index import HHelpWindow


class HToolBar(QToolBar):
    def __init__(self, title: str, parent: QMainWindow):
        super().__init__(title)
        self.parent = parent
        self.add_actions()

    def add_actions(self):
        # Creating Actions
        actions = {
            'About Us': QAction('About'),
            'Quit Application': QAction('Exit')
        }
        # Register Icons
        for x, y in actions.items():
            y.setParent(self.parent)
            print(x)
            print(type(y))
            y.setStatusTip(x)
            self.addAction(y)


def TopMenu(app):
    mainMenu: QMenuBar = app.menuBar()
    # mainMenu.setStyleSheet("background-color: red; padding: 5px")
    mainMenu.size()
    fileMenu = mainMenu.addMenu('&File')
    editMenu = mainMenu.addMenu('&Edit')
    viewMenu = mainMenu.addMenu('&View')
    searchMenu = mainMenu.addMenu('&Search')
    toolsMenu = mainMenu.addMenu('&Tools')
    helpMenu = mainMenu.addMenu('&Help')
    aboutButton = QAction('About', app)
    aboutButton.setShortcut('F1')
    aboutButton.setStatusTip('About me')
    aboutButton.triggered.connect(functools.partial(app.setMainWindow, HHelpWindow()))
    helpMenu.addAction(aboutButton)
    exitButton = QAction(QIcon('icons/exit.png'), 'Exit')
    exitButton.setShortcut('Ctrl+Q')
    exitButton.setStatusTip('Exit application')
    exitButton.triggered.connect(app.close)
    fileMenu.addAction(exitButton)
    toolbar = QToolBar('Menu Bar')
    app.addToolBar(toolbar)

    toolbar.addAction(exitButton)
