from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from models.Automata import Automata
from views.Components import HAddAutomata, HTransitionTable

automata = Automata(name='Mon Automate 2')


class HCreateAutomata(QDialog):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        create = HAddAutomata(automata)
        line = QFrame()
        line.setFrameShape(QFrame.VLine)
        line.setFrameShadow(QFrame.Sunken)
        layout.addWidget(create, 0, 0)
        layout.addWidget(line, 0, 1)

        button = QPushButton('View')
        button.clicked.connect(lambda: automata.view())
        layout.addWidget(HTransitionTable(automata), 1, 0, 3, 3)
        layout.addWidget(HAutomataDetail(automata), 0, 2)
        self.setMinimumWidth(400)
        self.setLayout(layout)


class HAutomataDetail(QWidget):
    def __init__(self, _automata):
        self.states = list()
        self.state_index = -1
        super().__init__()
        self.automata = _automata
        self.automata.updated.connect(self.refresh)
        self.text = QLabel()
        self.text.setText(automata.check_type())
        self.text1 = QLabel()
        self.text1.setText(f'Nombre Etats: {len(automata.get_states())}')
        self.text2 = QLabel()
        self.text2.setText(f'Nombre Transition: {len(automata.get_transitions())}')
        self.text3 = QLabel()
        self.text3.setText(f'Nombre Symbole: {len(automata.get_alphabet().get_alphabet())}')
        self.text4 = QLabel()
        self.text4.setText(f"Alphabet : [ {', '.join(automata.get_alphabet().get_alphabet())} ]")
        self.text5 = QLabel()
        self.text6 = QLabel()
        self.text7 = QLabel()
        self.layout = QVBoxLayout()
        # self.layout.addStretch(1)
        self.setMinimumWidth(600)
        button = QPushButton('View')
        button.clicked.connect(lambda: automata.view())
        next = QPushButton('Next')
        next.clicked.connect(lambda: self.go_next())
        previous = QPushButton('Previous')
        previous.clicked.connect(lambda: self.go_back())
        temp = QHBoxLayout()
        temp.addWidget(previous)
        temp.addWidget(next)

        minimize = QPushButton('Minimize')
        minimize.clicked.connect(lambda: automata.make(automata.minimize()))
        convert = QPushButton('Determinize')
        convert.clicked.connect(lambda: automata.make(automata.convert_to_dfa()))
        buttonReset = QPushButton('Reset')
        buttonReset.clicked.connect(lambda: automata.reset())
        self.layout.addWidget(button)
        # self.layout.addLayout(temp)
        # self.layout.addWidget(temp, alignment=Qt.AlignCenter)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.text1)
        self.layout.addWidget(self.text2)
        self.layout.addWidget(self.text3)
        self.layout.addWidget(self.text4)
        self.layout.addWidget(self.text5)
        self.layout.addWidget(self.text6)
        self.layout.addWidget(self.text7)
        self.layout.addWidget(minimize)
        self.layout.addWidget(convert)
        self.layout.addWidget(buttonReset)
        self.setLayout(self.layout)

    def refresh(self):
        if self.state_index == len(self.states) - 1:
            self.state_index = len(self.states)
            self.states.append(self.automata)
        self.text1.setText(f'Nombre Etats: {len(automata.get_states())}')
        self.text2.setText(f'Nombre Transition: {len(automata.get_transitions())}')
        self.text3.setText(f'Nombre Symbole: {len(automata.get_alphabet().get_alphabet())}')
        self.text4.setText(f"Alphabet : [ {', '.join(automata.get_alphabet().get_alphabet())} ]")
        self.text5.setText(f"Etat : [ {', '.join(automata.get_states_string())} ]")
        self.text6.setText(f"Etat Initiale : {automata.get_initial_state_string()}")
        self.text7.setText(f"Etat Finale : [ {', '.join(automata.get_final_states_string())} ]")
        self.text.setText(self.automata.check_type())

    def go_next(self):
        if self.state_index < len(self.states) - 1:
            self.state_index += 1
            self.automata.make(self.states[self.state_index])

    def go_back(self):
        print(self.state_index)
        print(self.states)
        if self.state_index > 0:
            self.state_index -= 1
            self.automata.make(self.states[self.state_index])


if __name__ == '__main__':
    app = QApplication([])
    a = HCreateAutomata()
    a.show()
    app.exec()
