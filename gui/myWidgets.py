import sys
from PyQt5.QtWidgets import QWidget, QApplication

import gameLogic.BlitzSum
from MainGameMenu import Ui_MainGameMenu
from Rules import Ui_RulesMenu
from GameField import Ui_GameScreen
from AttestationTile import Ui_AttestationTile
from SettingsMenu import Ui_SettingsMenu
from StatisticsMenu import Ui_StaticsMenu

from gameLogic.Subjects import Subjects


class MainGameMenu(QWidget, Ui_MainGameMenu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class RulesMenu(QWidget, Ui_RulesMenu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class GameScreen(QWidget, Ui_GameScreen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class SettingsMenu(QWidget, Ui_SettingsMenu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class StaticsMenu(QWidget, Ui_StaticsMenu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class AttestationTile(QWidget, Ui_AttestationTile):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.default_style_sheet = ""

    def set_view_attestation(self, attestation):
        self.valueButton.setText(str(attestation.mark))
        styles = ""
        if attestation.subject.title == "xalyba":
            styles = "background-color: gold;"
        else:
            styles = f"background-image: url(:/attestation-preview/attestation-preview/{attestation.subject.title.upper()}.png);"
            if attestation.subject.title == "hmi":
                styles += "color: white;"
        self.valueButton.setStyleSheet(styles)

    def select(self):
        self.valueButton.setStyleSheet("background-color: #880000")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainGameMenu()
    sys.exit(app.exec_())