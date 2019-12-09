from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


def HHelpWindow() -> QWidget:
    # Vertical layout creation
    vBox = QVBoxLayout()

    # Components
    button = QPushButton('Help page')
    label = QLabel('This is the Help page')
    label.setAlignment(Qt.AlignCenter)
    # Adding Components to layout
    vBox.addWidget(button)
    vBox.addWidget(label)

    # Main Widget Creation
    app = QWidget()
    app.setLayout(vBox)
    return app
