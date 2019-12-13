from PyQt5.QtWidgets import *

from models.Automata import Automata, example


class HAddInitialState(QWidget):
    def __init__(self, automata: Automata = example):
        super().__init__()
        self.automata = automata
        self.automata.updated.connect(self.refresh)
        self._states = automata.get_states_string
        self.layout = QGridLayout()
        self.label = QLabel('Initial State')
        self.addButton = QPushButton('Set')
        self.addButton.setFixedWidth(100)
        self.addButton.clicked.connect(self.add_state)
        self.states = QComboBox()
        self.states.addItems(self._states())
        self.states.setLineEdit(QLineEdit())
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.states, 1, 0)
        self.layout.addWidget(self.addButton, 1, 1)
        self.setLayout(self.layout)

    def refresh(self):
        if self.automata.get_initial_state_string():
            self.states.setEditable(False)
            self.addButton.setEnabled(False)
        else:
            self.states.setEditable(True)
            self.addButton.setEnabled(True)
        _state = self.states.currentText()
        self.states.clear()
        self.states.addItems(sorted(self._states()))
        self.states.setCurrentText(_state)

    def add_state(self, *args):
        value = self.states.currentText()
        if value:
            self.automata.set_initial_state(value)
            self.refresh()
            self.states.setFocus()


if __name__ == '__main__':
    a = QApplication([])
    b = HAddInitialState()
    b.show()
    a.exec()
