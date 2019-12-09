from PyQt5.QtWidgets import *


def text_edited(s):
    print(s)


class HMainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # Vertical layout creation
        self.vBox = QVBoxLayout()

        # Components
        self.button = QPushButton('Click me')
        self.widget = QLineEdit()
        self.widget.setMaxLength(10)
        self.widget.setPlaceholderText("Enter your text")

        # self.widget.setReadOnly(True) # uncomment this to make readonly

        self.widget.returnPressed.connect(text_edited)
        self.widget.selectionChanged.connect(text_edited)
        self.widget.textChanged.connect(text_edited)
        self.widget.textEdited.connect(text_edited)

        # Adding Components to layout
        self.vBox.addWidget(self.button)
        self.vBox.addWidget(self.widget)

        # Main Widget Creation
        self.setLayout(self.vBox)
