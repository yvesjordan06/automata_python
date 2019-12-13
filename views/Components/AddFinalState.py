from PyQt5.QtWidgets import *

from models.Automata import Automata, example


class HAddFinalState(QWidget):
    def __init__(self, automata: Automata = example):
        super().__init__()
        layout = QGridLayout()
        label = QLabel('Final State')
        label.setMaximumWidth(100)
        addButton = QPushButton('Add')
        addButton.setMaximumWidth(160)
        states = QComboBox()
        states.addItems(sorted(automata.get_states_string().difference(automata.get_final_states_string())))
        states.setLineEdit(QLineEdit())
        states.setMinimumWidth(200)
        layout.addWidget(label, 0, 0)
        layout.addWidget(states, 0, 1)
        layout.addWidget(addButton, 0, 2)
        self.setLayout(layout)


if __name__ == '__main__':
    a = QApplication([])
    b = HAddFinalState()
    b.show()
    a.exec()
