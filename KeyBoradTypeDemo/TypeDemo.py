# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Python\PythonProjects\TypeDemo.ui'
#
# Created: Mon Jul 24 19:24:38 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!



from PyQt4 import QtCore, QtGui
from Type_task import Type_task
from Task import Task


import sys
from PyQt4.QtCore import *


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


class Type_Demo(QtGui.QWidget):
    def __init__(self, parent=None):

        QtGui.QWidget.__init__(self, parent)
        self.task = Task()


        self.initUi()
        self.nextui = Type_task()

        self.showFullScreen()





    def setTask(self, taskTemp):
        self.task = taskTemp


    def initUi(self):

        self.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.setStyleSheet(_fromUtf8("border-color: rgb(128, 128, 128);"))

        self.radioButton_left = QtGui.QRadioButton("左",self)
        self.radioButton_left.move(self.task.screen_width*0.48 ,(self.task.screen_height )*0.57)
        self.radioButton_left.setFixedSize(200, 60)

        self.radioButton_right = QtGui.QRadioButton("右", self)
        self.radioButton_right.move(self.task.screen_width * 0.55, (self.task.screen_height) * 0.57)
        self.radioButton_right.setFixedSize(200, 60)


        self.buttonGroup2 = QtGui.QButtonGroup(self)
        self.buttonGroup2.addButton(self.radioButton_left)
        self.buttonGroup2.addButton(self.radioButton_right)

        self.label_1 = QtGui.QLabel("设备编号", self)
        self.label_1.move(self.task.screen_width * 0.34, (self.task.screen_height) * 0.18)
        self.label_1.setFixedSize(200, 140)

        self.label_2 = QtGui.QLabel("被试编号",self)
        self.label_2.move(self.task.screen_width * 0.34, (self.task.screen_height) * 0.25)
        self.label_2.setFixedSize(200, 140)

        self.label_3 = QtGui.QLabel("出生日期", self)
        self.label_3.move(self.task.screen_width * 0.34, (self.task.screen_height) * 0.32)
        self.label_3.setFixedSize(200, 140)

        self.label_4 = QtGui.QLabel("姓名", self)
        self.label_4.move(self.task.screen_width * 0.34, (self.task.screen_height) * 0.39)
        self.label_4.setFixedSize(200, 140)

        self.label_5 = QtGui.QLabel("性别", self)
        self.label_5.move(self.task.screen_width * 0.34, (self.task.screen_height) * 0.46)
        self.label_5.setFixedSize(200, 140)

        self.label_6 = QtGui.QLabel("利手", self)
        self.label_6.move(self.task.screen_width * 0.34, (self.task.screen_height) * 0.53)
        self.label_6.setFixedSize(200, 140)




        self.lineEdit_1 = QtGui.QLineEdit(self)
        self.lineEdit_2 = QtGui.QLineEdit(self)
        self.lineEdit_3 = QtGui.QLineEdit(self)
        self.lineEdit_4 = QtGui.QLineEdit(self)

        self.lineEdit_1.move(self.task.screen_width * 0.47, (self.task.screen_height) * 0.23)
        self.lineEdit_1.setFixedSize( 200, 40)
        self.lineEdit_2.move(self.task.screen_width * 0.47, (self.task.screen_height) * 0.3)
        self.lineEdit_2.setFixedSize(200, 40)
        self.lineEdit_3.move(self.task.screen_width * 0.47, (self.task.screen_height) * 0.37)
        self.lineEdit_3.setFixedSize(200, 40)
        self.lineEdit_4.move(self.task.screen_width * 0.47, (self.task.screen_height) * 0.44)
        self.lineEdit_4.setFixedSize(200, 40)



        self.pushButton = QtGui.QPushButton("下一步",self)
        #self.pushButton.setGeometry(QtCore.QRect(170, 230, 200, 50))
        self.pushButton.setStyleSheet(_fromUtf8("\n"
"\n"
"QPushButton:hover { background-color: rgb(139，137，137); }"))

        self.pushButton.move(self.task.screen_width * 0.45, (self.task.screen_height) * 0.68)
        self.pushButton.setFixedSize( 200, 70)



        self.radioButton_man = QtGui.QRadioButton("男",self)
        self.radioButton_man.move(self.task.screen_width * 0.48, (self.task.screen_height) * 0.51)
        self.setFixedSize( 200, 200)

        self.radioButton_woman = QtGui.QRadioButton("女", self)
        self.radioButton_woman.move(self.task.screen_width * 0.55, (self.task.screen_height) * 0.51)
        self.setFixedSize(200, 200)

        self.buttonGroup1 = QtGui.QButtonGroup(self)

        self.buttonGroup1.addButton(self.radioButton_man)
        self.buttonGroup1.addButton(self.radioButton_woman)


        self .lineEdit_1.setMaxLength(2)
        self.lineEdit_2.setMaxLength(3)
        self.lineEdit_3.setMaxLength(10)
        self.lineEdit_4.setMaxLength(20)




        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)



        # 信号连接到指定槽
        self.pushButton.clicked.connect(self.on_pushButton_clicked)



    def retranslateUi(self):


        self.label_1.setStyleSheet(_fromUtf8("font: 24pt \"微软雅黑\";\n"
                                           ""))
        self.label_2.setStyleSheet(_fromUtf8("font: 24pt \"微软雅黑\";\n"
                                             ""))
        self.label_3.setStyleSheet(_fromUtf8("font: 24pt \"微软雅黑\";\n"
                                             ""))
        self.label_4.setStyleSheet(_fromUtf8("font: 24pt \"微软雅黑\";\n"
                                             ""))
        self.label_5.setStyleSheet(_fromUtf8("font: 24pt \"微软雅黑\";\n"
                                             ""))
        self.label_6.setStyleSheet(_fromUtf8("font: 24pt \"微软雅黑\";\n"
                                             ""))



        self.lineEdit_1.setStyleSheet(_fromUtf8("font: 14pt \"微软雅黑\";\n"
                                             ""))
        self.lineEdit_2.setStyleSheet(_fromUtf8("font: 14pt \"微软雅黑\";\n"
                                                ""))
        self.lineEdit_3.setStyleSheet(_fromUtf8("font: 14pt \"微软雅黑\";\n"
                                                ""))
        self.lineEdit_4.setStyleSheet(_fromUtf8("font: 14pt \"微软雅黑\";\n"
                                                ""))





        self.pushButton.setStyleSheet(_fromUtf8("font: 14pt \"微软雅黑\";\n"""))




    def on_pushButton_clicked(self):
        tag=self .checkButton()
        if ( ( self .radioButton_left .isChecked() or self .radioButton_right  .isChecked() )
            and (self.radioButton_man.isChecked() or self .radioButton_woman  .isChecked() )
                        and tag      ) :
            #获取登录信息
            self.task.equimentID = self.lineEdit_1.text()
            self.task.testID = self.lineEdit_2.text()
            self.task.bornDate = self.lineEdit_3.text()
            self.task.testName=self.lineEdit_4.text()

            if self.radioButton_left.isChecked():
                self.task.Hand="左"
            if self.radioButton_right.isChecked():
                self.task.Hand = "右"
            if self.radioButton_man.isChecked():
                self.task.Sex="男"
            if self.radioButton_woman.isChecked():
                self.task.Sex = "女"

            #print self.task.testName
            #print self.task.equimentID
            #print self.task.testID
            #print self.task.bornDate
            #print self.task.Sex
            #print self.task.Hand


            self.nextui.setTask(self.task)

            self.close()


            self.nextui.showFullScreen()




    def checkButton(self):
        if(self .lineEdit_1 .text() ==""):
            return False
        if (self.lineEdit_2.text() == ""):
            return False
        if (self.lineEdit_3.text() == ""):
            return False
        if (self.lineEdit_4.text() == ""):
            return False
        return True



    def keyPressEvent(self, event):
        key = event.key()

        if key == QtCore.Qt.Key_Escape:
            self.close()


if __name__ == "__main__":
    import sys


    app = QtGui.QApplication(sys.argv)

    app.Encoding(QtGui.QApplication.UnicodeUTF8)
    utfcodec = QTextCodec.codecForName("UTF-8")
    QTextCodec.setCodecForTr(utfcodec)
    QTextCodec.setCodecForLocale(utfcodec)
    QTextCodec.setCodecForCStrings(utfcodec)

    ui = Type_Demo()






    sys.exit(app.exec_())

