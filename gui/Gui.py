import math
import sys

from PyQt5 import QtGui

from Game import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtCore import QTimer, pyqtSignal
from myWidgets import MainGameMenu, RulesMenu, GameScreen, AttestationTile, SettingsMenu, StaticsMenu
from gameLogic.BlitzSum import BlitzSum
from gameLogic.Field import Field

from audio.AudioPlayer import *

from Statistics.StatisticHandler import StatisticHandler

from random import choice
import webbrowser

class MyWindow(QMainWindow, Ui_MainWindow):
    TEXT_BY_COLOR_THEMES = {
        "csf": "ФКН",
        "vsu": "ВГУ"
    }

    COLOR_THEMES_BY_TEXT = {v: k for k, v in TEXT_BY_COLOR_THEMES.items()}

    game_start = pyqtSignal()
    game_stop = pyqtSignal()
    game_over = pyqtSignal()
    color_theme_changed = pyqtSignal()
    statistics_changed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.main_menu = MainGameMenu()
        self.rules_menu = RulesMenu()
        self.rules_predecessor = None
        self.settings_menu = SettingsMenu()
        self.statistics_menu = StaticsMenu()
        self.game_screen = GameScreen()
        self.game = None
        self.game_timer = None
        self.attestations_tiles = []

        self.theme = "vsu"

        statistics_data = StatisticHandler.get_data()
        self.total_games = statistics_data["total_games"]
        self.best_score = statistics_data["best_score"]

        self.audio_player = Player()

        self.init_component()
        self.show()

    def init_component(self):
        self.setWindowTitle("БлитцСессия")
        self.game_start.connect(self.on_game_start)
        self.game_stop.connect(self.on_game_stop)
        self.game_over.connect(self.on_game_over)
        self.color_theme_changed.connect(self.on_color_theme_change)
        self.statistics_changed.connect(self.on_statistics_changed)
        self.statistics_changed.emit()

        self.game_timer = QTimer(self)
        self.game_timer.setInterval(1000)  # 1 сек
        self.game_timer.timeout.connect(self.timer_tick)

        # инициализация главного меню
        self.mainBodyLayout.addWidget(self.main_menu)
        self.main_menu.playButton.clicked.connect(self.start_game)
        self.main_menu.settingsButton.clicked.connect(self.main_menu_to_settings)
        self.main_menu.rulesButton.clicked.connect(self.main_menu_to_rules)
        self.main_menu.statisticsButton.clicked.connect(self.main_menu_to_statistics)
        self.main_menu.exitButton.clicked.connect(self.exit_clicked)

        # инициализация меню правил
        self.mainBodyLayout.addWidget(self.rules_menu)
        self.rules_menu.hide()
        self.rules_menu.closeRulesButton.clicked.connect(self.close_rules)

        # инициализация экрана игры
        self.mainBodyLayout.addWidget(self.game_screen)
        self.game_screen.hide()
        self.game_screen.returnBackButton.clicked.connect(self.hot_game_exit)
        self.game_screen.rulesButton.clicked.connect(self.game_screen_to_rules)

        # инициализация меню настроеек
        self.mainBodyLayout.addWidget(self.settings_menu)
        self.settings_menu.hide()
        self.settings_menu.closeButton.clicked.connect(self.settings_to_main)
        self.settings_menu.volumeButton.clicked.connect(self.mute)
        self.settings_menu.horizontalSlider.setValue(self.audio_player.volume)
        self.settings_menu.horizontalSlider.valueChanged.connect(self.on_volume_change)
        self.settings_menu.themeComboBox.addItems(self.TEXT_BY_COLOR_THEMES.values())
        self.settings_menu.themeComboBox.setCurrentText(self.TEXT_BY_COLOR_THEMES[self.theme])
        self.settings_menu.themeComboBox.activated.connect(self.on_theme_combobox_activated)
        self.settings_menu.resetSettingsButton.clicked.connect(self.on_reset_settings)
        self.settings_menu.resetStatisticsButton.clicked.connect(self.on_reset_statistics)
        self.settings_menu.starButton.clicked.connect(self.on_github_star)

        # инициализация меню статистики
        self.mainBodyLayout.addWidget(self.statistics_menu)
        self.statistics_menu.hide()
        self.statistics_menu.closeButton.clicked.connect(self.statistics_to_main)

    def update_current_score_label(self):
        self.game_screen.currentScoreLabel.setText("Текущий счёт: " + str(self.game.score))

    def update_game_field(self):
        for ri, row in enumerate(self.attestations_tiles):
            for ci, item in enumerate(row):
                item.set_view_attestation(self.game.field[ri][ci])
                if self.game.field.is_select(ri, ci):
                    item.select()

    def toggle_select(self, ri, ci):
        def returnee():
            is_select, event = self.game.select(ri, ci)
            if not is_select:
                self.game.unselect(ri, ci)

            match event:
                case "exam":
                    self.audio_player.play(Sounds.EXAM)
                case "credit with mark":
                    self.audio_player.play(Sounds.CREDIT_WITH_MARK)
                case "credit":
                    self.audio_player.play(Sounds.CREDIT)
                case "xalyba":
                    self.audio_player.play(Sounds.XALYBA)
                case "unavailable select":
                    self.audio_player.play(Sounds.UNAVAILABLE_SELECTION)
                case "normal selection":
                    self.audio_player.play(Sounds.NORMAL_SELECT)
                case "unselection":
                    self.audio_player.play(Sounds.UNSELECTION)
                case "heterogeneous":
                    self.audio_player.play(Sounds.HETEROGENEOUS)
                case _:
                    self.audio_player.play(Sounds.SOUND_TEST)

            self.update_game_field()
            self.update_current_score_label()
        return returnee

    def start_game(self):
        """
        Срабатывает при нажатии кнопки "Играть" в главном меню
        :return:
        """
        self.main_menu.hide()
        self.game_screen.show()
        self.game = BlitzSum()

        self.attestations_tiles = [[AttestationTile() for i in range(Field.DEFAULT_SIZE)] for row in range(Field.DEFAULT_SIZE)]
        for ri, row in enumerate(self.attestations_tiles):
            for ci, item in enumerate(row):
                item.set_view_attestation(self.game.field[ri][ci])
                item.valueButton.clicked.connect(self.toggle_select(ri, ci))

        for ri, row in enumerate(self.game.field):
            for ci, item in enumerate(row):
                self.game_screen.gridLayout.addWidget(self.attestations_tiles[ri][ci], ri, ci)

        self.game_screen.daysLeftLabel.setText(f"Дней до конца семестра: {self.game.current_day}")

        self.game_screen.timeLeftProgressBar.setValue(100)
        self.audio_player.play(Sounds.GAME_START)
        self.game_start.emit()

    def on_game_start(self):
        self.audio_player.play(Sounds.GAME_START)
        self.game.start()
        self.game_timer.start()

    def on_game_stop(self):
        self.game.stop()
        self.game_timer.stop()

    def timer_tick(self):
        self.game.decrease_tick()
        value = self.game.current_day / self.game.DAYS_LEFT * 100
        value = math.floor(value)
        self.game_screen.timeLeftProgressBar.setValue(value)
        self.game_screen.daysLeftLabel.setText(f"До конца семестра осталось {self.game.current_day} из {self.game.DAYS_LEFT}")
        if not self.game.is_running:
            self.game_stop.emit()
            self.game_over.emit()

    def on_game_over(self):
        """
        Срабатывает по истечении времени игры
        :return:
        """
        if self.game.score > self.best_score:
            track = choice((Sounds.BEST_SCORE_1, Sounds.BEST_SCORE_2))
            self.audio_player.play(track)
            info = f"Ваш счёт {self.game.score} и он на {self.game.score - self.best_score} больше лучшего результата!\nПоздравляю!"
            self.best_score = self.game.score
        else:
            info =  f"Ваш счёт {self.game.score}"
            self.audio_player.play(Sounds.NORMAL_SCORE)
        info += "\nХотите ещё раз сыграть?"

        message_box = QMessageBox.question(self, "Игра окончена", info, QMessageBox.Yes | QMessageBox.No)
        self.total_games += 1
        self.statistics_changed.emit()

        if message_box == QMessageBox.Yes:
            self.start_game()
        elif message_box == QMessageBox.No:
            self.audio_player.play(Sounds.DENY_RESTART)
            self.game_screen_to_main_menu()

    def hot_game_exit(self):
        """
        Срабатывает при нажатии кнопки "Стрелка влево" на игровом экране.
        Завершает без сохранения текущую игру и возвращает на главный экран
        :return:
        """
        self.game_stop.emit()
        self.audio_player.play(Sounds.EXIT_ATTENTION)
        message_box = QMessageBox.question(self, "Выход из игры!",
                                           "Внимание! Если вы выйдете до завершения таймера, текущий счёт будет потерян!\nВернуться в главное меню?",
                                           QMessageBox.Yes | QMessageBox.No)
        if message_box == QMessageBox.Yes:
            self.game_screen_to_main_menu()
        else:
            self.game_start.emit()

    def game_screen_to_main_menu(self):
        """
        Срабатывает при нажатии кнопки "Стрелка влево" на игровом экране.
        Завершает без сохранения текущую игру и возвращает на главный экран
        :return:
        """
        self.game_stop.emit()
        self.game_screen.hide()
        self.main_menu.show()


    def game_screen_to_rules(self):
        """
        Срабатывает при нажатии кнопки "Вопросительный знак" на игровом экране.
        Приостанавливает с сохранением текущую игру и открывает меню правил
        :return:
        """
        self.game_stop.emit()
        self.game_screen.hide()
        self.rules_predecessor = self.game_screen
        self.rules_menu.show()

    def main_menu_to_settings(self):
        """
        Срабатывает при нажатии кнопки "Настройки" в главном меню
        :return:
        """
        self.main_menu.hide()
        self.settings_menu.show()

    def main_menu_to_rules(self):
        """
        Срабатывает при нажатии кнопки "Правила" в главном меню
        :return:
        """
        self.main_menu.hide()
        self.rules_predecessor = self.main_menu
        self.rules_menu.show()

    def main_menu_to_statistics(self):
        """
        Срабатывает при нажатии кнопки "Статистика" в главном меню
        :return:
        """
        self.statistics_menu.show()
        self.main_menu.hide()

    def exit_clicked(self):
        """
        Срабатывает при нажатии кнопки "Выход" в главном меню
        :return:
        """
        self.close()

    def close_rules(self):
        """
        Срабатывает при нажатии кнопки "Выход" в меню правил.
        Возвращает к виджету, указанному в self.rules_predecessor
        :return:
        """
        self.rules_menu.hide()
        if self.rules_predecessor is not None:
            if self.rules_predecessor is self.game_screen:
                self.game_start.emit()

            self.rules_predecessor.show()
            self.rules_predecessor = None
        else:
            self.main_menu.show()

    def statistics_to_main(self):
        """
        Срабатывает при нажатии кнопки "Выход" в меню статистики
        :return:
        """
        self.main_menu.show()
        self.statistics_menu.hide()

    def settings_to_main(self):
        """
        Срабатывает при нажатии кнопки "Выход" в меню настроеек
        :return:
        """
        self.settings_menu.hide()
        self.main_menu.show()

    def on_theme_combobox_activated(self):
        text = self.settings_menu.themeComboBox.currentText()
        activated_theme = self.COLOR_THEMES_BY_TEXT[text]
        if self.theme != activated_theme:
            self.theme = activated_theme
            self.color_theme_changed.emit()

    def on_color_theme_change(self):
        """
        closeButton (setting)
        volumeButton (setting)
        returnBackButton (game field)
        rulesButton (game field)
        closeRulesButton (rules)
        closeButton (statistic)
        """
        self.settings_menu.closeButton.setIcon(self.get_icon("interface-delete"))
        self.game_screen.returnBackButton.setIcon(self.get_icon("interface-arrows-left"))
        self.game_screen.rulesButton.setIcon(self.get_icon("interface-help-question-circle"))
        self.rules_menu.closeRulesButton.setIcon(self.get_icon("interface-delete"))
        self.statistics_menu.closeButton.setIcon(self.get_icon("interface-delete"))
        self.update_volume_button()

    def on_volume_change(self):
        volume = self.settings_menu.horizontalSlider.value()
        self.audio_player.set_volume(volume)
        self.audio_player.play(Sounds.SOUND_TEST)
        self.update_volume_button()

    def mute(self):
        self.settings_menu.horizontalSlider.setValue(0)

    def update_volume_button(self):
        volume = self.settings_menu.horizontalSlider.value()
        if 50 <= volume:
            icon = self.get_icon("entertainment-volume-high")
        elif 0 < volume < 50:
            icon = self.get_icon("entertainment-volume-low")
        else:
            icon = self.get_icon("entertainment-volume-off")
        self.settings_menu.volumeButton.setIcon(icon)

    def on_reset_settings(self):
        self.settings_menu.horizontalSlider.setValue(50)
        self.theme = "vsu"
        self.color_theme_changed.emit()

    def on_statistics_changed(self):
        self.game_screen.bestScoreLabel.setText("Лучший счёт: " + str(self.best_score))
        self.statistics_menu.totalGamesLabel.setText(str(self.total_games))
        self.statistics_menu.bestScoreLabel.setText(str(self.best_score))
        StatisticHandler.write_data(self.total_games, self.best_score)

    def on_reset_statistics(self):
        message_box = QMessageBox.question(self, "Сброс статистики", "Внимание! Это действие нельзя будет отменить!\nСбросить статистику?",
                                  QMessageBox.Yes | QMessageBox.No)
        if message_box == QMessageBox.Yes:
            self.total_games = 0
            self.best_score = 0
            self.statistics_changed.emit()

    def on_github_star(self):
        webbrowser.open("https://github.com/PavelPutin/BlitzSum", new=2)

    def get_icon(self, icon_name):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f":/{self.theme}-theme/themes/{self.theme}/{icon_name}-{self.theme}.png"),
                       QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        return icon


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
