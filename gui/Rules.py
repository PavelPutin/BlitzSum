# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\PycharmProjects\gameLogic\gui\Rules.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RulesMenu(object):
    def setupUi(self, RulesMenu):
        RulesMenu.setObjectName("RulesMenu")
        RulesMenu.resize(890, 567)
        RulesMenu.setStyleSheet("#rulesTextScrollArea {\n"
"    padding: 50px;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(RulesMenu)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(RulesMenu)
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
        self.widget_2 = QtWidgets.QWidget(RulesMenu)
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
        self.closeRulesButton = QtWidgets.QPushButton(self.widget_3)
        self.closeRulesButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/vsu-theme/themes/vsu/interface-delete-vsu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeRulesButton.setIcon(icon)
        self.closeRulesButton.setObjectName("closeRulesButton")
        self.horizontalLayout_2.addWidget(self.closeRulesButton, 0, QtCore.Qt.AlignLeft)
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
        self.rulesTextScrollArea = QtWidgets.QScrollArea(self.widget_2)
        self.rulesTextScrollArea.setWidgetResizable(True)
        self.rulesTextScrollArea.setObjectName("rulesTextScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -1194, 735, 1655))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.rulesTextScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.rulesTextScrollArea)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(RulesMenu)
        QtCore.QMetaObject.connectSlotsByName(RulesMenu)

    def retranslateUi(self, RulesMenu):
        _translate = QtCore.QCoreApplication.translate
        RulesMenu.setWindowTitle(_translate("RulesMenu", "Form"))
        self.label.setText(_translate("RulesMenu", "БлитцСессия"))
        self.label_2.setText(_translate("RulesMenu", "Правила"))
        self.label_3.setText(_translate("RulesMenu", "<html><head/><body><p><span style=\" font-size:14pt;\">Четвёртый семестр в самом разгаре! Сможешь ли ты сдать сессию с наибольшим счётом!</span></p><p><span style=\" font-size:14pt;\">Твоя задача, выполняя аттестации, набрать как можно больше очков! Всего есть 10 предметов.</span></p><p><span style=\" font-size:18pt; font-weight:600;\">Экзамены:</span></p><p><img src=\":/rules-preview/rules-preview/PHILOSOPHY.png\"/><span style=\" font-size:14pt;\"> - философия</span></p><p><img src=\":/rules-preview/rules-preview/ENGLISH.jpg\"/><span style=\" font-size:14pt;\"> - английский</span></p><p><img src=\":/rules-preview/rules-preview/MATEQ.png\"/><span style=\" font-size:14pt;\"> - урмат</span></p><p><img src=\":/rules-preview/rules-preview/LANGUAGES.png\"/><span style=\" font-size:14pt;\"> - ЯиСП</span></p><p><span style=\" font-size:18pt; font-weight:600;\">Зачёты с оценкой:</span></p><p><img src=\":/rules-preview/rules-preview/HMI.png\"/><span style=\" font-size:14pt;\"> - ЧМИ</span></p><p><span style=\" font-size:18pt; font-weight:600;\">Обычные зачёты:</span></p><p><img src=\":/rules-preview/rules-preview/CALCULATION_METHODS.png\"/><span style=\" font-size:14pt;\"> - методы вычислений</span></p><p><img src=\":/rules-preview/rules-preview/TIPIS.png\"/><span style=\" font-size:14pt;\"> - ТИПиС</span></p><p><img src=\":/rules-preview/rules-preview/UNIX.png\"/><span style=\" font-size:14pt;\"> - ОС UNIX</span></p><p><img src=\":/rules-preview/rules-preview/ELECTRONICS.png\"/><span style=\" font-size:14pt;\"> - электроника</span></p><p><img src=\":/rules-preview/rules-preview/PE.png\"/><span style=\" font-size:14pt;\"> - физра</span></p><p><span style=\" font-size:14pt;\">иииииииииииииии...</span></p><p><span style=\" font-size:18pt; font-weight:600; color:#c8bc0d;\">- ХАЛЯВА!</span></p><p><span style=\" font-size:14pt;\">Очки за сданные аттестации начисляются, если суммарная оценка по ним равна 100 баллам.</span></p><p><span style=\" font-size:14pt;\">Если тебе удалось сдать аттестации только за счёт </span><span style=\" font-size:14pt; color:#c8bc0d;\">ХаЛяВы</span><span style=\" font-size:14pt;\">, то 100 баллов умножаются на 100!</span></p><p><span style=\" font-size:14pt;\">Если ты сдал аттестации по </span><span style=\" font-size:14pt; font-weight:600;\">одному предмету</span><span style=\" font-size:14pt;\">, то 100 баллов </span><span style=\" font-size:14pt; font-weight:600;\">умножаются</span><span style=\" font-size:14pt;\"> на множитель этого предмета:</span></p><p><span style=\" font-size:14pt;\">- для экзамена - </span><span style=\" font-size:14pt; font-style:italic;\">2х</span></p><p><span style=\" font-size:14pt;\">- для зачёта с оценкой - </span><span style=\" font-size:14pt; font-style:italic;\">1.5х</span></p><p><span style=\" font-size:14pt;\">- для обычного зачёта - </span><span style=\" font-size:14pt; font-style:italic;\">1х</span></p><p><span style=\" font-size:14pt;\">А если ты ещё и </span><span style=\" font-size:14pt; color:#c8bc0d;\">Х</span><span style=\" font-size:16pt; color:#c8bc0d;\">А</span><span style=\" font-size:18pt; color:#c8bc0d;\">Л</span><span style=\" font-size:20pt; color:#c8bc0d;\">Я</span><span style=\" font-size:18pt; color:#c8bc0d;\">В</span><span style=\" font-size:16pt; color:#c8bc0d;\">К</span><span style=\" font-size:14pt; color:#c8bc0d;\">У</span><span style=\" font-size:14pt;\"> залутал, то этот результат увеличивается в </span><span style=\" font-size:14pt; font-weight:600;\">10 раз</span><span style=\" font-size:14pt;\">!</span></p><p><span style=\" font-size:14pt;\">Если же аттестации сдавались по разным предметам, то... получишь </span><span style=\" font-size:14pt; font-weight:600;\">100 очков</span><span style=\" font-size:14pt;\">. Но не унывай! Ведь если среди этих предметов была </span><span style=\" font-size:14pt; color:#c8bc0d;\">ХАЛЯВА</span><span style=\" font-size:14pt; color:#000000;\">, то эти </span><span style=\" font-size:14pt; font-weight:600; color:#000000;\">100 очков</span><span style=\" font-size:14pt; color:#000000;\"> умножаться на </span><span style=\" font-size:14pt; font-weight:600; color:#000000;\">самый большой множитель</span><span style=\" font-size:14pt; color:#000000;\"> из сданных аттестаций.</span></p><p><span style=\" font-size:14pt;\">Также не забывай, что полученные очки </span><span style=\" font-size:14pt; font-weight:600;\">умножаются</span><span style=\" font-size:14pt;\"> на количество сданных аттестаций!</span><br/></p><p><span style=\" font-size:14pt; font-weight:600;\">Успешно сессии, студент!</span></p></body></html>"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RulesMenu = QtWidgets.QWidget()
    ui = Ui_RulesMenu()
    ui.setupUi(RulesMenu)
    RulesMenu.show()
    sys.exit(app.exec_())
