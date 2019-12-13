from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from models.Automata import Automata


class HAddState(QWidget):
    def __init__(self, automata: Automata = None):
        super().__init__()
        self.automata = automata
        self.layout = QGridLayout()
        self.label = QLabel('State')
        self.addButton = QPushButton('Add State')
        self.addButton.setFixedWidth(100)
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText('Input State here')
        self.addButton.clicked.connect(self.add_state)
        self.line_edit.returnPressed.connect(self.add_state)
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.line_edit, 1, 0)
        self.layout.addWidget(self.addButton, 1, 1)
        self.setLayout(self.layout)

    def add_state(self, *args):
        value = self.line_edit.text()
        if value:
            self.automata.add_state(value)
            self.line_edit.clear()
            self.line_edit.setFocus()

if __name__ == '__main__':
    a = QApplication([])
    b = HAddState()
    b.show()
    a.exec()
