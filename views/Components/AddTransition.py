from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import *

from models.Automata import Automata, example


class HAddTransition(QWidget):
    def __init__(self, automata: Automata = example):
        self.automata = automata
        self.alphabet = automata.get_alphabet().get_alphabet()
        self.states = automata.get_states_string()
        super().__init__()
        layout = QGridLayout()
        start_label = QLabel('Start at')
        start_label.setMaximumWidth(100)
        on_label = QLabel('On reading')
        on_label.setMaximumWidth(100)
        end_label = QLabel('Go to')
        end_label.setMaximumWidth(100)
        addButton = QPushButton('Add')
        addButton.setMaximumWidth(160)
        start = QComboBox()
        start.addItems(sorted(self.states))
        start.setLineEdit(QLineEdit())
        self.on = QComboBox()
        self.on.addItems(sorted(self.alphabet))
        self.on.setLineEdit(QLineEdit())
        end = QComboBox()
        end.addItems(sorted(self.states))
        end.setLineEdit(QLineEdit())
        layout.addWidget(start_label, 0, 0, alignment=Qt.AlignCenter)
        layout.addWidget(on_label, 0, 1, alignment=Qt.AlignCenter)
        layout.addWidget(end_label, 0, 2, alignment=Qt.AlignCenter)
        layout.addWidget(start, 1, 0)
        layout.addWidget(self.on, 1, 1)
        layout.addWidget(end, 1, 2)
        layout.addWidget(addButton, 2, 0, 3, 3, Qt.AlignCenter)
        layout.setHorizontalSpacing(25)
        layout.setVerticalSpacing(10)
        self.setLayout(layout)
        self.on.installEventFilter(self)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.FocusIn:
            self.refresh()
        return False

    def refresh(self):
        print('im refreshing')
        alphabet = self.automata.get_alphabet().get_alphabet()
        print(alphabet)
        print(self.alphabet)
        self.states = self.automata.get_states_string()
        self.on.addItems(sorted(alphabet.difference(self.alphabet)))


if __name__ == '__main__':
    a = QApplication([])
    b = HAddTransition()
    b.show()
    a.exec()
