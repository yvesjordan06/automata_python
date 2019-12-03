from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QAction, QMainWindow, QToolBar


def TopMenu(app: QMainWindow):

    mainMenu = app.menuBar()
    mainMenu.size()
    fileMenu = mainMenu.addMenu('File')
    editMenu = mainMenu.addMenu('Edit')
    viewMenu = mainMenu.addMenu('View')
    searchMenu = mainMenu.addMenu('Search')
    toolsMenu = mainMenu.addMenu('Tools')
    helpMenu = mainMenu.addMenu('&Help')
    aboutButton = QAction('About', app)
    aboutButton.setShortcut('F1')
    aboutButton.setStatusTip('About me')
    helpMenu.addAction(aboutButton)
    exitButton = QAction(QIcon('../icons/exit.png'), 'Exit', app)
    exitButton.setShortcut('Ctrl+Q')
    exitButton.setStatusTip('Exit application')
    exitButton.triggered.connect(app.close)
    fileMenu.addAction(exitButton)
    toolbar = app.addToolBar('Exit')
    toolbar.addAction(exitButton)
