# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Python\PythonProjects\Type_over.ui'
#
# Created: Wed Jul 19 17:03:31 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Task import Task

import sys
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


class Type_over(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.task = Task()
        self.initUi()

    def setTask(self, taskTemp):
        self.task = taskTemp

        # 键盘监听

    def keyPressEvent(self, event):
        key = event.key()

        if key == QtCore.Qt.Key_Escape:
            self.close()
    def initUi(self):

        self.label = QtGui.QLabel(self)

        self.label.setStyleSheet(_fromUtf8("font: 22pt \"微软雅黑\";\n"
                                           ""))

        self.label_2 = QtGui.QLabel(self)

        self.label_2.setStyleSheet(_fromUtf8("font: 22pt \"微软雅黑\";"))


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):

        self.label.setText("实验结束")
        self.label_2.setText("感谢您的参与")

        self.label.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.42, (self.task.screen_height) * 0.33, 800, 60))
        self.label.setStyleSheet(_fromUtf8("font: 32pt \"微软雅黑\";\n"
                                           ""))

        self.label_2.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.39, (self.task.screen_height) * 0.5, 800, 100))
        self.label_2.setStyleSheet(_fromUtf8("font: 32pt \"微软雅黑\";\n"
                                             ""))

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)

    app.Encoding(QtGui.QApplication.UnicodeUTF8)
    utfcodec = QTextCodec.codecForName("UTF-8")
    QTextCodec.setCodecForTr(utfcodec)
    QTextCodec.setCodecForLocale(utfcodec)
    QTextCodec.setCodecForCStrings(utfcodec)


    ui = Type_over ()

    ui.showFullScreen()
    sys.exit(app.exec_())