from PyQt5.QtWidgets import *

from models.Automata import Automata


class HAddState(QWidget):
    def __init__(self, automata: Automata = None):
        super().__init__()
        layout = QGridLayout()
        label = QLabel('State')
        addButton = QPushButton('Add State')
        line_edit = QLineEdit()
        line_edit.setPlaceholderText('Input State here')
        layout.addWidget(label, 0, 0)
        layout.addWidget(line_edit, 0, 1)
        layout.addWidget(addButton, 0, 2)
        self.setLayout(layout)


if __name__ == '__main__':
    a = QApplication([])
    b = HAddState()
    b.show()
    a.exec()
