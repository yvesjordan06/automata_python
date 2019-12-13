from PyQt5.QtWidgets import *

from models.Automata import Automata


class HAddAlphabet(QWidget):
    def __init__(self, automata: Automata = None):
        super().__init__()
        self.automata = automata
        layout = QGridLayout()
        label = QLabel('Add symbol to alphabet')
        addButton = QPushButton('Add Symbol')
        addButton.setFixedWidth(100)
        addButton.clicked.connect(self.add_alphabet)
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText('Input Symbol here')
        self.line_edit.returnPressed.connect(self.add_alphabet)
        layout.addWidget(label, 0, 0)
        layout.addWidget(self.line_edit, 1, 0)
        layout.addWidget(addButton, 1, 1)
        self.setLayout(layout)

    def add_alphabet(self, *args):
        value = self.line_edit.text()
        if value:
            self.automata.add_symbol(value)
            self.line_edit.clear()
            self.line_edit.setFocus()
            self.automata = self.automata
            print(self.automata.get_alphabet().get_alphabet())


if __name__ == '__main__':
    a = QApplication([])
    b = HAddAlphabet()
    b.show()
    a.exec()
