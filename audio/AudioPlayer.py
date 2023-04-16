from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from enum import Enum
import os


AUDIO_RESOURCE_PATH = os.path.join(os.getcwd(), "resources", "audio")


def _get_audio_path(filename):
    return QUrl.fromLocalFile(os.path.join(AUDIO_RESOURCE_PATH, filename))


class Sounds(Enum):
    BEST_SCORE_1 = _get_audio_path("sfx_best_score_1.wav")
    BEST_SCORE_2 = _get_audio_path("sfx_best_score_1.wav")
    CREDIT = _get_audio_path("sfx_credit.wav")
    CREDIT_WITH_MARK = _get_audio_path("sfx_credit_with_mark.wav")
    DENY_RESTART = _get_audio_path("sfx_deny_restart.wav")
    EXAM = _get_audio_path("sfx_exam.wav")
    EXIT_ATTENTION = _get_audio_path("sfx_exit_attention.wav")
    GAME_START = _get_audio_path("sfx_game_start.wav")
    HETEROGENEOUS = _get_audio_path("sfx_heterogenese.wav")
    NORMAL_SCORE = _get_audio_path("sfx_normal_score.wav")
    NORMAL_SELECT = _get_audio_path("sfx_normal_select.wav")
    SOUND_TEST = _get_audio_path("sfx_sound_test_1.wav")
    UNAVAILABLE_SELECTION = _get_audio_path("sfx_unavailable_selection.wav")
    UNSELECTION = _get_audio_path("sfx_unselection.wav")
    XALYBA = _get_audio_path("sfx_xalyba.wav")


class Player:
    def __init__(self):
        self.player = QMediaPlayer()
        self.set_volume(50)

    @property
    def volume(self):
        return self.player.volume()

    def set_volume(self, value: int):
        self.player.setVolume(value)

    def play(self, sound: Sounds):
        content = QMediaContent(sound.value)
        self.player.setMedia(content)
        self.player.play()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainGameMenu = QtWidgets.QWidget()
    p = Player()
    p.play(Sounds.SOUND_TEST)
    sys.exit(app.exec_())

