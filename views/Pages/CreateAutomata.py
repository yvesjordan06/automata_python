from PyQt5.QtWidgets import *

from models.Automata import Automata
from views.Components import HAddAutomata

automata = Automata(name='Mon Automate 2')


class HCreateAutomata(QDialog):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        create = HAddAutomata(automata)
        create.setMaximumWidth(500)
        self.setMaximumHeight(400)
        layout.addWidget(create)
        layout.addWidget(create)
        layout.addWidget(QPushButton('2'))

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication([])
    a = HCreateAutomata()
    a.show()
    app.exec()
