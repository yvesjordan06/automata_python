from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from models.Automata import Automata, example
from models.RegExp import RegularExpression
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
        layout.addWidget(HRegexInput(automata))
        # self.setMaximumHeight(600)
        #self.setMinimumWidth(300)
        self.setLayout(layout)


class HRegexInput(QWidget):
    def __init__(self, automata):
        super().__init__()
        self.automata = automata
        layout = QGridLayout()
        label = QLabel('Regular Expression')
        addButton = QPushButton('Generate Automata')
        #addButton.setFixedWidth(100)
        addButton.clicked.connect(self.create_regexp)
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText('Input Regular Expression Here')
        self.line_edit.returnPressed.connect(self.create_regexp)
        layout.addWidget(label, 0, 0)
        layout.addWidget(self.line_edit, 1, 0)
        layout.addWidget(addButton, 2, 0)
        self.setLayout(layout)

    def create_regexp(self, *args):
        value = self.line_edit.text()
        print(value)
        if value:
            temp = RegularExpression(value).Solve()
            print('alphabet')
            print(temp.get_alphabet().get_alphabet())
            self.automata.make(temp)
            #self.line_edit.clear()
            #self.line_edit.setFocus()

            # print(self.automata.get_alphabet().get_alphabet())


if __name__ == '__main__':
    a = QApplication([])
    b = HAddAutomata()
    b.show()
    a.exec()
