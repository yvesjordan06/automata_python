from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


def HHelpWindow() -> QWidget:
    # Vertical layout creation
    vBox = QVBoxLayout()

    # Components
    label = QLabel('Done By')
    label.setStyleSheet('font-size:24; font-weight:bold')
    label1 = QLabel('Nguejip Mukete Yves Jordan')
    label1.setStyleSheet('font-size:16; font-weight:bold')
    label2 = QLabel('17Q2742')
    label3 = QLabel('December 2019')
    label3.setStyleSheet('font-size:12')
    label.setAlignment(Qt.AlignCenter)
    label1.setAlignment(Qt.AlignCenter)
    label2.setAlignment(Qt.AlignCenter)
    label3.setAlignment(Qt.AlignCenter)
    # Adding Components to layout
    vBox.addWidget(label)
    vBox.addWidget(label1)
    vBox.addWidget(label2)
    vBox.addWidget(label3)

    # Main Widget Creation
    app = QWidget()
    app.setLayout(vBox)
    return app
