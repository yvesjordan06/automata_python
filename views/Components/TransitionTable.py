from PyQt5 import Qt
from PyQt5.QtCore import QModelIndex
from PyQt5.QtWidgets import *

from models.Automata import example, convert_set_of_state_to_state
from models.Transition import Transition


class HTransitionTable(QTableWidget):
    def __init__(self, automata=example, *args):
        self.automata = automata
        self.alphabet = automata.get_alphabet().get_alphabet
        self.states = automata.get_states_string
        self.transitions = automata.get_transitions
        super().__init__(len(self.states()), len(self.alphabet()))

        automata.updated.connect(self.refresh)
        self.refresh()

    def refresh(self):
        print('Transitiopn')
        i = 0
        j = 0
        print(self.states())
        self.setRowCount(len(self.states()))
        self.setColumnCount(len(self.alphabet()))
        self.setHorizontalHeaderLabels(sorted(self.alphabet()))
        self.setVerticalHeaderLabels(sorted(self.states()))
        try:
            initial_index = sorted(self.states()).index(self.automata.get_initial_state_string())
            self.setVerticalHeaderItem(initial_index,
                                       QTableWidgetItem('-> ' + self.automata.get_initial_state_string()))
        except ValueError:
            pass

        try:
            for final in self.automata.get_final_states_string():
                index = sorted(self.states()).index(final)
                if final != self.automata.get_initial_state_string():
                    self.setVerticalHeaderItem(index,
                                               QTableWidgetItem('* ' + final))
                else:
                    self.setVerticalHeaderItem(index,
                                               QTableWidgetItem('*-> ' + final))
        except ValueError:
            pass

        for symbol in sorted(self.alphabet()):
            for state in sorted(self.states()):
                values = convert_set_of_state_to_state(self.automata.read(state, symbol))
                value = QTableWidgetItem(','.join(values).upper())
                hint = str(Transition(state, symbol, values))
                print(hint)
                value.setStatusTip(hint)
                value.setToolTip(hint)
                value.setWhatsThis(hint)
                self.setItem(i, j, value)
                i = i + 1
            j = j + 1
            i = 0


if __name__ == '__main__':
    b = QApplication([])
    a = HTransitionTable()
    a.show()
    b.exec()
