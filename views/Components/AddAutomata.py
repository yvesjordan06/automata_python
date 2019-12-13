from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from models.Automata import Automata, example
from views import Components


class HAddAutomata(QWidget):
    def __init__(self, automata: Automata = example):
        super().__init__()
        layout = QVBoxLayout()
        group = QGroupBox()
        label = QLabel("Create Automata")
        label.setStyleSheet('font-weight: 600; margin-bottom: 10px')
        layout.addWidget(label, alignment=Qt.AlignCenter)
        layout.addWidget(Components.HAddAlphabet(automata))
        layout.addWidget(Components.HAddState(automata))
        layout.addWidget(Components.HAddInitialState(automata))
        layout.addWidget(Components.HAddFinalState(automata))
        layout.addWidget(Components.HAddTransition(automata))
        self.setMaximumHeight(600)
        self.setLayout(layout)


if __name__ == '__main__':
    a = QApplication([])
    b = HAddAutomata()
    b.show()
    a.exec()
