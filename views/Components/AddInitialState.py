from PyQt5.QtWidgets import *

from models.Automata import Automata, example


class HAddInitialState(QWidget):
    def __init__(self, automata: Automata = example):
        super().__init__()
        layout = QGridLayout()
        label = QLabel('Initial State')
        label.setMaximumWidth(100)
        addButton = QPushButton('Set Initial State')
        addButton.setMaximumWidth(160)
        states = QComboBox()
        states.addItems(sorted(automata.get_states_string()))
        states.setLineEdit(QLineEdit())
        states.setMinimumWidth(200)
        layout.addWidget(label, 0, 0)
        layout.addWidget(states, 0, 1)
        layout.addWidget(addButton, 0, 2)
        self.setLayout(layout)


if __name__ == '__main__':
    a = QApplication([])
    b = HAddInitialState()
    b.show()
    a.exec()
