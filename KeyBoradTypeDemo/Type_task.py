# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Python\PythonProjects\hello\Type_task.ui'
#
# Created: Sat Jul 15 21:30:24 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Type_choice_demo import Type_choice
from Task import Task
import sys

import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *

import locale
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


reload(sys)
sys.setdefaultencoding('utf8')


class Type_task(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.task = Task()

        self.initUi()

        self.ui=Type_choice()
        self.ui.initUi()


        #self.showFullScreen()

    def setTask(self, taskTemp):
        self.task = taskTemp



    def initUi(self):

        self.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.setStyleSheet(_fromUtf8("border-color: rgb(128, 128, 128);"))

        self.layoutWidget = QtGui.QWidget(self)


        self.layoutWidget.move(self.task.screen_width * 0.38, (self.task.screen_height) * 0.4)
        self.layoutWidget.setFixedSize(400, 120)

        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setMargin(0)
        #self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))

        self.radioButton_hanzi = QtGui.QRadioButton(self.layoutWidget)


        self.buttonGroup = QtGui.QButtonGroup(self)
        self.buttonGroup.addButton(self.radioButton_hanzi)

        self.horizontalLayout_2.addWidget(self.radioButton_hanzi)

        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setStyleSheet(_fromUtf8("\n"
"\n"
"font: 75 18pt \"Microsoft YaHei UI Light\";"))




        self.horizontalLayout_2.addWidget(self.label_5)

        self.layoutWidget_2 = QtGui.QWidget(self)


        self.layoutWidget_2.move(self.task.screen_width * 0.38, (self.task.screen_height) * 0.25)
        self.layoutWidget_2.setFixedSize(400, 120)


        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setMargin(0)

        self.radioButton_bihua = QtGui.QRadioButton(self.layoutWidget_2)


        self.buttonGroup.addButton(self.radioButton_bihua)
        self.horizontalLayout.addWidget(self.radioButton_bihua)
        self.label = QtGui.QLabel(self.layoutWidget_2)
        self.label.setStyleSheet(_fromUtf8("font: 75 18pt \"Microsoft YaHei UI Light\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)



        self.pushButton = QtGui.QPushButton(self)

        self.pushButton.setStyleSheet(_fromUtf8("\n"
"\n"
"QPushButton:hover { background-color: rgb(139，137，137);border-color: rgb(226, 226, 226); }"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        # 信号连接到指定槽
        self.pushButton.clicked.connect(self.on_pushButton_clicked)

    def retranslateUi(self):

        self.label_5.setText("汉字输入任务")
        self.label.setText("笔画输入任务")
        self.pushButton.setText("下一步")


        self.label.move(self.task.screen_width * 0.34, (self.task.screen_height) * 0.25)
        self.label.setFixedSize(400, 140)

        self.label.setStyleSheet(_fromUtf8("font: 28pt \"微软雅黑\";\n" ""))


        self.label_5.move(self.task.screen_width * 0.34, (self.task.screen_height) * 0.18)
        self.label_5.setFixedSize( 400, 140)

        self.label_5.setStyleSheet(_fromUtf8("font: 28pt \"微软雅黑\";\n" ""))


        self.pushButton.move(self.task.screen_width * 0.45, (self.task.screen_height) * 0.6)
        self.pushButton.setFixedSize(200, 80)

        self.pushButton.setStyleSheet(_fromUtf8("font: 20pt \"微软雅黑\";\n" ""))

    # 键盘监听
    def keyPressEvent(self, event):
            key = event.key()


            if key == QtCore.Qt.Key_Escape:

                self.close()


    def on_pushButton_clicked(self):
        if (self.radioButton_bihua.isChecked() or self.radioButton_hanzi.isChecked()):

            self.ui.setTask(self.task)  # 传递任务对象




            self.close()

            self.ui.showFullScreen()




if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)

    app.Encoding(QtGui.QApplication.UnicodeUTF8)
    utfcodec = QTextCodec.codecForName("UTF-8")
    QTextCodec.setCodecForTr(utfcodec)
    QTextCodec.setCodecForLocale(utfcodec)
    QTextCodec.setCodecForCStrings(utfcodec)

    ui = Type_task()
    ui.showFullScreen()

    sys.exit(app.exec_())