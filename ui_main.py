# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import res_rc
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(788, 600)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(11, 0, 200, 15), stop:0.127447 rgba(71,91, 132, 135), stop:1 rgba(55, 79, 165,255));\n"
"font-family: Microsoft Sans Serif")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.text = QLabel(self.centralwidget)
        self.text.setObjectName(u"text")
        self.text.setGeometry(QRect(310, 30, 211, 31))
        self.text.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 30pt;\n"
"background-color: none;\n"
"border: none")
        self.bt_add_task = QPushButton(self.centralwidget)
        self.bt_add_task.setObjectName(u"bt_add_task")
        self.bt_add_task.setGeometry(QRect(360, 460, 100, 32))
        self.bt_add_task.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 18pt;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1 px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setGeometry(QRect(150, 80, 521, 331))
        self.widget = QWidget(self.main_frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 40, 501, 231))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.task_1 = QFrame(self.widget)
        self.task_1.setObjectName(u"task_1")
        self.task_1.setStyleSheet(u"background-color: none;\n"
"border: 1 px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.horizontalLayout_4 = QHBoxLayout(self.task_1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.checkBox_1 = QCheckBox(self.task_1)
        self.checkBox_1.setObjectName(u"checkBox_1")
        self.checkBox_1.setMaximumSize(QSize(24, 24))
        self.checkBox_1.setStyleSheet(u"background-color: none;\n"
"border: 1 px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.checkBox_1.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.checkBox_1)

        self.lineEdit_1 = QLineEdit(self.task_1)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.setMaximumSize(QSize(16777215, 34))
        self.lineEdit_1.setStyleSheet(u"color: white;\n"
"font-size: 15pt;\n"
"background-color: rgba(250, 236, 255, 0.3);\n"
"border: none;\n"
"border-radius: 7px;")
        self.lineEdit_1.setMaxLength(32772)

        self.horizontalLayout_4.addWidget(self.lineEdit_1)

        self.bt_delete1 = QPushButton(self.task_1)
        self.bt_delete1.setObjectName(u"bt_delete1")
        self.bt_delete1.setMaximumSize(QSize(24, 27))
        self.bt_delete1.setStyleSheet(u"background-color: none;\n"
"border: 1 px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        icon = QIcon()
        icon.addFile(u":/icons/icons/delete_white_24dp.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bt_delete1.setIcon(icon)
        self.bt_delete1.setIconSize(QSize(24, 24))
        self.bt_delete1.setAutoDefault(False)

        self.horizontalLayout_4.addWidget(self.bt_delete1)


        self.verticalLayout.addWidget(self.task_1)

        self.task_2 = QFrame(self.widget)
        self.task_2.setObjectName(u"task_2")
        self.task_2.setStyleSheet(u"background-color: none;\n"
"border: 1 px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.horizontalLayout_2 = QHBoxLayout(self.task_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkBox_2 = QCheckBox(self.task_2)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setMaximumSize(QSize(24, 24))
        self.checkBox_2.setStyleSheet(u"background-color: none;\n"
"border: 1 px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.checkBox_2.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.checkBox_2)

        self.le_text2_2 = QLineEdit(self.task_2)
        self.le_text2_2.setObjectName(u"le_text2_2")
        self.le_text2_2.setMaximumSize(QSize(16777215, 34))
        self.le_text2_2.setStyleSheet(u"color: white;\n"
"font-size: 15pt;\n"
"background-color: rgba(250, 236, 255, 0.3);\n"
"border: none;\n"
"border-radius: 7px;")
        self.le_text2_2.setMaxLength(32772)

        self.horizontalLayout_2.addWidget(self.le_text2_2)

        self.bt_delete2 = QPushButton(self.task_2)
        self.bt_delete2.setObjectName(u"bt_delete2")
        self.bt_delete2.setMaximumSize(QSize(24, 27))
        self.bt_delete2.setStyleSheet(u"background-color: none;\n"
"border: 1 px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.bt_delete2.setIcon(icon)
        self.bt_delete2.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.bt_delete2)


        self.verticalLayout.addWidget(self.task_2)

        self.task_3 = QFrame(self.widget)
        self.task_3.setObjectName(u"task_3")
        self.task_3.setStyleSheet(u"background-color: none;\n"
"border: 1 px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.horizontalLayout_3 = QHBoxLayout(self.task_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.checkBox_3 = QCheckBox(self.task_3)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setMaximumSize(QSize(24, 24))
        self.checkBox_3.setStyleSheet(u"background-color: none;\n"
"border: 1 px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.checkBox_3.setIconSize(QSize(24, 24))
        self.checkBox_3.setChecked(False)

        self.horizontalLayout_3.addWidget(self.checkBox_3)

        self.le_text3 = QLineEdit(self.task_3)
        self.le_text3.setObjectName(u"le_text3")
        self.le_text3.setMaximumSize(QSize(16777215, 34))
        self.le_text3.setStyleSheet(u"color: white;\n"
"font-size: 15pt;\n"
"background-color: rgba(250, 236, 255, 0.3);\n"
"border: none;\n"
"border-radius: 7px;")
        self.le_text3.setMaxLength(32772)

        self.horizontalLayout_3.addWidget(self.le_text3)

        self.bt_delete_3 = QPushButton(self.task_3)
        self.bt_delete_3.setObjectName(u"bt_delete_3")
        self.bt_delete_3.setMaximumSize(QSize(24, 27))
        self.bt_delete_3.setStyleSheet(u"background-color: none;\n"
"border: 1 px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.bt_delete_3.setIcon(icon)
        self.bt_delete_3.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.bt_delete_3)


        self.verticalLayout.addWidget(self.task_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ToDoList", None))
        self.text.setText(QCoreApplication.translate("MainWindow", u"Your Daily Plan", None))
        self.bt_add_task.setText(QCoreApplication.translate("MainWindow", u"Add Task", None))
        self.checkBox_1.setText("")
        self.checkBox_2.setText("")
        self.checkBox_3.setText("")
    # retranslateUi

