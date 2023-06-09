# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\PycharmProjects\gameLogic\gui\GameField.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GameScreen(object):
    def setupUi(self, GameScreen):
        GameScreen.setObjectName("GameScreen")
        GameScreen.resize(823, 566)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(GameScreen)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_6 = QtWidgets.QWidget(GameScreen)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.returnBackButton = QtWidgets.QPushButton(self.widget_6)
        self.returnBackButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/vsu-theme/themes/vsu/interface-arrows-left-vsu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.returnBackButton.setIcon(icon)
        self.returnBackButton.setObjectName("returnBackButton")
        self.horizontalLayout.addWidget(self.returnBackButton, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_7.addWidget(self.widget_6, 0, QtCore.Qt.AlignTop)
        self.widget_4 = QtWidgets.QWidget(GameScreen)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtWidgets.QWidget(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.GameFieldWidget = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.GameFieldWidget.sizePolicy().hasHeightForWidth())
        self.GameFieldWidget.setSizePolicy(sizePolicy)
        self.GameFieldWidget.setObjectName("GameFieldWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.GameFieldWidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_6.addLayout(self.gridLayout)
        self.verticalLayout_2.addWidget(self.GameFieldWidget)
        self.widget_7 = QtWidgets.QWidget(self.widget)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.timeLeftProgressBar = QtWidgets.QProgressBar(self.widget_7)
        self.timeLeftProgressBar.setProperty("value", 24)
        self.timeLeftProgressBar.setObjectName("timeLeftProgressBar")
        self.verticalLayout_5.addWidget(self.timeLeftProgressBar)
        self.daysLeftLabel = QtWidgets.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.daysLeftLabel.setFont(font)
        self.daysLeftLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.daysLeftLabel.setObjectName("daysLeftLabel")
        self.verticalLayout_5.addWidget(self.daysLeftLabel)
        self.verticalLayout_2.addWidget(self.widget_7, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_2.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.widget_4)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.currentScoreLabel = QtWidgets.QLabel(self.widget_3)
        self.currentScoreLabel.setObjectName("currentScoreLabel")
        self.verticalLayout_3.addWidget(self.currentScoreLabel)
        self.bestScoreLabel = QtWidgets.QLabel(self.widget_3)
        self.bestScoreLabel.setObjectName("bestScoreLabel")
        self.verticalLayout_3.addWidget(self.bestScoreLabel)
        self.verticalLayout.addWidget(self.widget_3, 0, QtCore.Qt.AlignTop)
        self.widget_5 = QtWidgets.QWidget(self.widget_2)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.rulesButton = QtWidgets.QPushButton(self.widget_5)
        self.rulesButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/vsu-theme/themes/vsu/interface-help-question-circle-vsu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rulesButton.setIcon(icon1)
        self.rulesButton.setIconSize(QtCore.QSize(20, 20))
        self.rulesButton.setObjectName("rulesButton")
        self.verticalLayout_4.addWidget(self.rulesButton, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.widget_5, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.verticalLayout_7.addWidget(self.widget_4)

        self.retranslateUi(GameScreen)
        QtCore.QMetaObject.connectSlotsByName(GameScreen)

    def retranslateUi(self, GameScreen):
        _translate = QtCore.QCoreApplication.translate
        GameScreen.setWindowTitle(_translate("GameScreen", "Form"))
        self.returnBackButton.setToolTip(_translate("GameScreen", "Вернуться в главное меню (игра не сохранится!)"))
        self.daysLeftLabel.setText(_translate("GameScreen", "TextLabel"))
        self.currentScoreLabel.setText(_translate("GameScreen", "Текущий счёт: 0"))
        self.bestScoreLabel.setText(_translate("GameScreen", "Лучший счёт: 0"))
        self.rulesButton.setToolTip(_translate("GameScreen", "Открыть страницу правил (игра приостановится)"))
        self.rulesButton.setShortcut(_translate("GameScreen", "Ctrl+R"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GameScreen = QtWidgets.QWidget()
    ui = Ui_GameScreen()
    ui.setupUi(GameScreen)
    GameScreen.show()
    sys.exit(app.exec_())
