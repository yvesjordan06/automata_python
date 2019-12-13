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
        layout.addWidget(create,0,0)
        layout.addWidget(line,0,1)

        button = QPushButton('View')
        button.clicked.connect(lambda: automata.view())
        layout.addWidget(HTransitionTable(automata),1,0,3,3)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication([])
    a = HCreateAutomata()
    a.show()
    app.exec()


def determinisation(self):
    new_etats = [self.__etat_initial]
    new_transition = set()
    new_etat_finaux = list()
    traité = []

    for etat_actuel in new_etats:
        if etat_actuel in traité:
            continue
        for symbol_actuel in self.__alphabet:
            etat_resultat = self.f_transition(etat_actuel, symbol_actuel)
            if etat_resultat:
                new_etats.append(etat_resultat)
                new_transition.add((etat_actuel, symbol_actuel, etat_resultat))
        traité.append(etat_actuel)

    for etat in new_etats:
        if isinstance(etat, str) and etat in self.__etat_finaux:
            new_etat_finaux.append(etat)
        elif isinstance(etat, set) and etat.intersection(self.__etat_finaux):
            new_etat_finaux.append(etat)

    return Automate(self.__alphabet, new_etats, self.__etat_initial, new_etat_finaux, new_transition)

def f_transition(self, etat, symbol):
    if isinstance(symbol, str):
        resultat = set()
        for transition_actuel in self.__transition:
            if isinstance(etat, str):
                if transition_actuel[0] == etat and transition_actuel[1] == symbol:
                    resultat.add(transition_actuel[2])
            elif isinstance(etat, (list, tuple, set)):
                for sous_etat in etat:
                    if transition_actuel[0] == sous_etat and transition_actuel[1] == symbol:
                        resultat.add(transition_actuel[2])
            else:
                print("Erreur le type de l'état non pris en charge")
        if resultat:
            return resultat
    else:
        print("Erreur le type du symbole non pris en charge")