from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import *

from models.Automata import Automata, example
from models.Transition import Transition


class HAddTransition(QWidget):
    def __init__(self, automata: Automata = example):
        self.automata = automata
        self.alphabet = automata.get_alphabet().get_alphabet
        self.states = automata.get_states_string
        self.automata.updated.connect(self.refresh)
        super().__init__()
        self.layout = QGridLayout()
        self.start_label = QLabel('Start at')
        self.on_label = QLabel('On reading')
        self.end_label = QLabel('Go to')
        self.addButton = QPushButton('Add')
        self.addButton.setFixedWidth(100)
        self.addButton.clicked.connect(self.add_transition)
        self.start = QComboBox()
        self.start.setLineEdit(QLineEdit())
        self.on = QComboBox()
        self.on.setLineEdit(QLineEdit())
        self.end = QComboBox()
        self.end.setLineEdit(QLineEdit())
        self.refresh()
        self.layout.addWidget(self.start_label, 0, 0, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.on_label, 0, 1, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.end_label, 0, 2, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.start, 1, 0)
        self.layout.addWidget(self.on, 1, 1)
        self.layout.addWidget(self.end, 1, 2)
        self.layout.addWidget(self.addButton, 2, 0, 3, 3, Qt.AlignCenter)
        self.layout.setHorizontalSpacing(25)
        self.layout.setVerticalSpacing(10)
        self.setLayout(self.layout)

    def refresh(self):
        _on = self.on.currentText()
        _start = self.start.currentText()
        _end = self.end.currentText()
        self.on.clear()
        self.start.clear()
        self.end.clear()
        self.start.addItems(sorted(self.states()))
        self.end.addItems(sorted(self.states()))
        self.on.addItems(sorted(self.alphabet()))
        self.start.setCurrentText(_start)
        self.on.setCurrentText(_on)
        self.end.setCurrentText(_end)

    def add_transition(self):
        if self.on.currentText() and self.start.currentText() and self.end.currentText():
            a = Transition(self.start.currentText(), self.on.currentText(), self.end.currentText())
            self.automata.add_transition(a)
            self.refresh()


if __name__ == '__main__':
    a = QApplication([])
    b = HAddTransition()
    b.show()
    a.exec()
