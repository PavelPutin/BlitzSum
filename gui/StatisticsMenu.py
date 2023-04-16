# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\PycharmProjects\gameLogic\gui\StatisticsMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StaticsMenu(object):
    def setupUi(self, StaticsMenu):
        StaticsMenu.setObjectName("StaticsMenu")
        StaticsMenu.resize(890, 617)
        StaticsMenu.setStyleSheet("#rulesTextScrollArea {\n"
"    padding: 50px;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(StaticsMenu)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(StaticsMenu)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(55)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.widget, 0, QtCore.Qt.AlignTop)
        self.widget_2 = QtWidgets.QWidget(StaticsMenu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.closeButton = QtWidgets.QPushButton(self.widget_3)
        self.closeButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/vsu-theme/themes/vsu/interface-delete-vsu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_2.addWidget(self.closeButton, 0, QtCore.Qt.AlignLeft)
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.StaticsScrollArea = QtWidgets.QScrollArea(self.widget_2)
        self.StaticsScrollArea.setWidgetResizable(True)
        self.StaticsScrollArea.setObjectName("StaticsScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 852, 414))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_4 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget_4)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3, 0, QtCore.Qt.AlignLeft)
        self.totalGamesLabel = QtWidgets.QLabel(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.totalGamesLabel.sizePolicy().hasHeightForWidth())
        self.totalGamesLabel.setSizePolicy(sizePolicy)
        self.totalGamesLabel.setObjectName("totalGamesLabel")
        self.horizontalLayout_3.addWidget(self.totalGamesLabel, 0, QtCore.Qt.AlignLeft)
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4, 0, QtCore.Qt.AlignLeft)
        self.bestScoreLabel = QtWidgets.QLabel(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bestScoreLabel.sizePolicy().hasHeightForWidth())
        self.bestScoreLabel.setSizePolicy(sizePolicy)
        self.bestScoreLabel.setObjectName("bestScoreLabel")
        self.horizontalLayout_3.addWidget(self.bestScoreLabel, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_3.addWidget(self.widget_4)
        self.StaticsScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.StaticsScrollArea)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(StaticsMenu)
        QtCore.QMetaObject.connectSlotsByName(StaticsMenu)

    def retranslateUi(self, StaticsMenu):
        _translate = QtCore.QCoreApplication.translate
        StaticsMenu.setWindowTitle(_translate("StaticsMenu", "Form"))
        self.label.setText(_translate("StaticsMenu", "БлитцСессия"))
        self.label_2.setText(_translate("StaticsMenu", "Статистика"))
        self.label_3.setText(_translate("StaticsMenu", "Всего игр:"))
        self.totalGamesLabel.setText(_translate("StaticsMenu", "0"))
        self.label_4.setText(_translate("StaticsMenu", "Лучший счёт:"))
        self.bestScoreLabel.setText(_translate("StaticsMenu", "0"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StaticsMenu = QtWidgets.QWidget()
    ui = Ui_StaticsMenu()
    ui.setupUi(StaticsMenu)
    StaticsMenu.show()
    sys.exit(app.exec_())