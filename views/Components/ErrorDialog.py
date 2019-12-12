from PyQt5.QtWidgets import QMessageBox


class HErrorDialog(QMessageBox):
    def __init__(self, title, message, extra):
        super().__init__()
        self.setIcon(QMessageBox.Critical)
        self.setText(message)
        self.setInformativeText(extra)
        self.setWindowTitle(title)
