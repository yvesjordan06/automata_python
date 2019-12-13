from PyQt5.QtWidgets import *

from models.Automata import Automata, example


class HAddFinalState(QWidget):
    def __init__(self, automata: Automata = example):
        super().__init__()
        self.automata = automata
        self.automata.updated.connect(self.refresh)
        self._states = automata.get_states_string
        self._finalStates = automata.get_final_states_string
        self.layout = QGridLayout()
        self.label = QLabel('Add Final State')
        self.addButton = QPushButton('Add')
        self.addButton.setFixedWidth(100)
        self.addButton.clicked.connect(self.add_state)
        self.states = QComboBox()
        self.refresh()
        self.states.setLineEdit(QLineEdit())
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.states, 1, 0)
        self.layout.addWidget(self.addButton, 1, 1)
        self.setLayout(self.layout)

    def refresh(self):
        self.states.clear()
        self.states.addItems(self._states().difference(self._finalStates()))

    def add_state(self, *args):
        value = self.states.currentText()
        if value:
            self.automata.add_final_state(value)
            self.refresh()
            self.states.setFocus()


if __name__ == '__main__':
    a = QApplication([])
    b = HAddFinalState()
    b.show()
    a.exec()
