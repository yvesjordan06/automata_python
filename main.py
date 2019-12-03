import sys

from PyQt5.QtWidgets import QApplication

from models.Alphabet import Alphabet
from models.Automata import Automata
from models.Transition import Transition
from views.app import App

if __name__ == '__main__':
    app = QApplication([])
    ex = App()
    sys.exit(app.exec_())

    print('Welcome to 304'.capitalize().center(10, '#'))
    size = int(input('What is the length of the alphabet : '))
    local_alphabet = []
    for i in range(size):
        local_alphabet.append(input('Enter alphabet : '))
    alphabet = Alphabet(local_alphabet)
    size = int(input('What is the length of all states : '))
    states = []
    for i in range(size):
        states.append(input('Enter state : '))
    initial_state = input('What is the initial state: ')
    size = int(input('What is the length of final states : '))
    final_states = []
    for i in range(size):
        final_states.append(input('Enter state : '))
    size = int(input('What is the length of transitions : '))
    transitions = []
    for i in range(size):
        transitions.append(tuple(input('Enter state (format: 1,a,c)').split(',')))
    automata = Automata(alphabet, states, initial_state, final_states, transitions)
