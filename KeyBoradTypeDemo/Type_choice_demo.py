# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Python\PythonProjects\hello\Type_choice.ui'
#
# Created: Sat Jul 15 21:30:20 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!


from PyQt4 import QtCore, QtGui
from Task import Task
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Type_compare import Type_compare

from PyQt4.QtCore import *

import time
import inspect
import ctypes
import os




import sys
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

def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


#选择任务类型
class Type_choice(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.task = Task()
        #self.initUi()

        self.ui=Type_welcome()

    def setTask(self, taskTemp):
        self.task = taskTemp

    def initUi(self):

        self.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.setStyleSheet(_fromUtf8("border-color: rgb(128, 128, 128);"))

        self.label = QtGui.QLabel("任务类型",self)


        #10
        self.radioButton10_1 = QtGui.QRadioButton(self)
        self.radioButton10_2 = QtGui.QRadioButton(self)
        self.radioButton10_3 = QtGui.QRadioButton(self)
        self.radioButton10_1 .setText("10ms×100ms")
        self.radioButton10_2 .setText("10ms×200ms")
        self.radioButton10_3 .setText("10ms×300ms")


        #15
        self.radioButton15_1 = QtGui.QRadioButton(self)
        self.radioButton15_2 = QtGui.QRadioButton(self )
        self.radioButton15_3 = QtGui.QRadioButton(self)
        self.radioButton15_1 .setText("15ms×100ms")
        self.radioButton15_2  .setText("15ms×200ms")
        self.radioButton15_3  .setText("15ms×300ms")

        # 20
        self.radioButton20_1 = QtGui.QRadioButton(self)
        self.radioButton20_2 = QtGui.QRadioButton(self)
        self.radioButton20_3 = QtGui.QRadioButton(self)
        self.radioButton20_1  .setText("20ms×100ms")
        self.radioButton20_2  .setText("20ms×200ms")
        self.radioButton20_3  .setText("20ms×300ms")




        #下一步

        self.pushButton = QtGui.QPushButton("下一步",self)

        self.pushButton.setStyleSheet(_fromUtf8("\n"
"\n"
"QPushButton:hover { background-color: rgb(139，137，137);border-color: rgb(226, 226, 226); }"))



        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.checkButton()                 #如果选中过的任务,则置为无效

        # 信号连接到指定槽
        self.pushButton.clicked.connect(self.on_pushButton_clicked)

    def retranslateUi(self ):

        #label
        self.label.move(self.task.screen_width * 0.20, (self.task.screen_height) * 0.10)
        self.label.setFixedSize(250, 140)

        #10
        self.radioButton10_1.move(self.task.screen_width * 0.26, (self.task.screen_height) * 0.18)
        self.radioButton10_1.setFixedSize(300, 140)

        self.radioButton10_2.move(self.task.screen_width * 0.45, (self.task.screen_height) * 0.18)
        self.radioButton10_2.setFixedSize(300, 140)

        self.radioButton10_3.move(self.task.screen_width * 0.64, (self.task.screen_height) * 0.18)
        self.radioButton10_3.setFixedSize(300, 140)

        #15
        self.radioButton15_1.move(self.task.screen_width * 0.26, (self.task.screen_height) * 0.3)
        self.radioButton15_1.setFixedSize(300, 140)

        self.radioButton15_2.move(self.task.screen_width * 0.45, (self.task.screen_height) * 0.3)
        self.radioButton15_2.setFixedSize(300, 140)

        self.radioButton15_3.move(self.task.screen_width * 0.64, (self.task.screen_height) * 0.3)
        self.radioButton15_3.setFixedSize(300, 140)

        #20
        self.radioButton20_1.move(self.task.screen_width * 0.26, (self.task.screen_height) * 0.42)
        self.radioButton20_1.setFixedSize(300, 140)

        self.radioButton20_2.move(self.task.screen_width * 0.45, (self.task.screen_height) * 0.42)
        self.radioButton20_2.setFixedSize(300, 140)

        self.radioButton20_3.move(self.task.screen_width * 0.64, (self.task.screen_height) * 0.42)
        self.radioButton20_3.setFixedSize(300, 140)

        #下一步
        self.pushButton.move(self.task.screen_width * 0.46, (self.task.screen_height) * 0.63)
        self.setFixedSize(200, 70)



        self.label.setStyleSheet(_fromUtf8("font: 28pt \"微软雅黑\";\n"
                                           ""))
        self.radioButton10_1.setStyleSheet(_fromUtf8("font: 18pt \"微软雅黑\";\n"""))
        self.radioButton10_2.setStyleSheet(_fromUtf8("font: 18pt \"微软雅黑\";\n"""))
        self.radioButton10_3.setStyleSheet(_fromUtf8("font: 18pt \"微软雅黑\";\n"""))
        self.radioButton15_3.setStyleSheet(_fromUtf8("font: 18pt \"微软雅黑\";\n"""))
        self.radioButton15_2.setStyleSheet(_fromUtf8("font: 18pt \"微软雅黑\";\n"""))
        self.radioButton15_1.setStyleSheet(_fromUtf8("font: 18pt \"微软雅黑\";\n"""))
        self.radioButton20_1.setStyleSheet(_fromUtf8("font: 18pt \"微软雅黑\";\n"""))
        self.radioButton20_2.setStyleSheet(_fromUtf8("font: 18pt \"微软雅黑\";\n"""))
        self.radioButton20_3.setStyleSheet(_fromUtf8("font: 18pt \"微软雅黑\";\n"""))
        self.pushButton.setStyleSheet(_fromUtf8("font: 20pt \"微软雅黑\";\n"""))

    def on_pushButton_clicked(self):
        # 判断选中的状态

        if (self.radioButton10_1.isChecked()):
            self.task.taskChoiceList.append("b10_1")
            self .task.taskType="10_1"
        if (self.radioButton10_2.isChecked()):
            self.task.taskChoiceList.append("b10_2")
            self.task.taskType = "10_2"
        if (self.radioButton10_3.isChecked()):
            self.task.taskChoiceList.append("b10_3")
            self.task.taskType = "10_3"

        if (self.radioButton15_1.isChecked()):
            self.task.taskChoiceList.append("b15_1")
            self.task.taskType = "15_1"
        if (self.radioButton15_2.isChecked()):
            self.task.taskChoiceList.append("b15_2")
            self.task.taskType = "15_2"
        if (self.radioButton15_3.isChecked()):
            self.task.taskChoiceList.append("b15_3")
            self.task.taskType = "15_3"

        if (self.radioButton20_1.isChecked()):
            self.task.taskChoiceList.append("b20_1")
            self.task.taskType = "20_1"
        if (self.radioButton20_2.isChecked()):
            self.task.taskChoiceList.append("b20_2")
            self.task.taskType = "20_2"
        if (self.radioButton20_3.isChecked()):
            self.task.taskChoiceList.append("b20_3")
            self.task.taskType = "20_3"

        #只要有一个按钮选中，就执行下一步
        if (self.radioButton10_1.isChecked() | self.radioButton10_2.isChecked()| self.radioButton10_3.isChecked()
                | self.radioButton20_1.isChecked() | self.radioButton20_2.isChecked()| self.radioButton20_3.isChecked()
                | self.radioButton15_1.isChecked() | self.radioButton15_2.isChecked() | self.radioButton15_3.isChecked()):



            self.ui.setTask(self.task)  # 传递任务对象
            self.close()

            self.ui.showFullScreen()

    # 键盘监听
    def keyPressEvent(self, event):
         key = event.key()

         if key == QtCore.Qt.Key_Escape:
                self.close()


    # 如果选中过的任务置为无效
    def checkButton(self):

        for type in self.task.taskChoiceList:
            if(type=="b10_1"):
                self.radioButton10_1.setCheckable(False)
                self.radioButton10_1.setStyleSheet(_fromUtf8("color: rgb(150, 150, 150);"))
            if (type == "b10_2"):
                self.radioButton10_2.setCheckable(False)
                self.radioButton10_2.setStyleSheet(_fromUtf8("color: rgb(150, 150, 150);"))
            if (type == "b10_3"):
                self.radioButton10_3.setCheckable(False)
                self.radioButton10_3.setStyleSheet(_fromUtf8("color: rgb(150, 150, 150);"))

            if (type == "b15_1"):
                self.radioButton15_1.setCheckable(False)
                self.radioButton15_1.setStyleSheet(_fromUtf8("color: rgb(150, 150, 150);"))
            if (type == "b15_2"):
                self.radioButton15_2.setCheckable(False)
                self.radioButton15_2.setStyleSheet(_fromUtf8("color: rgb(150, 150, 150);"))
            if (type == "b15_3"):
                self.radioButton15_3.setCheckable(False)
                self.radioButton15_3.setStyleSheet(_fromUtf8("color: rgb(150, 150, 150);"))

            if (type == "b20_1"):
                self.radioButton20_1.setCheckable(False)
                self.radioButton20_1.setStyleSheet(_fromUtf8("color: rgb(150, 150, 150);"))
            if (type == "b20_2"):
                self.radioButton20_2.setCheckable(False)
                self.radioButton20_2.setStyleSheet(_fromUtf8("color: rgb(150, 150, 150);"))
            if (type == "b20_3"):
                self.radioButton20_3.setCheckable(False)
                self.radioButton20_3.setStyleSheet(_fromUtf8("color: rgb(150, 150, 150);"))



#欢迎界面
class Type_welcome(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.task = Task()
        self.initUi()

        self.ui=Type_prepare5()
        self.ui2=openKeyBoard()

    def setTask(self,taskTemp):
        self.task=taskTemp


    def initUi(self):

        self.pushButton = QtGui.QPushButton("开始",self)

        self.pushButton.setStyleSheet(_fromUtf8("\n"
"\n"
"QPushButton:hover { background-color: rgb(139，137，137); }"))



        self.label = QtGui.QLabel("你好，欢迎参加实验!", self)


        self.label.setStyleSheet(_fromUtf8("font: 11pt \"微软雅黑\";"))

        self.label_2 = QtGui.QLabel("实验任务为用右手的",self)

        self.label_2.setStyleSheet(_fromUtf8("font: 11pt \"微软雅黑\";"))

        self.label_3 = QtGui.QLabel("食指",self)

        self.label_3.setStyleSheet(_fromUtf8("\n"
"font: 87 12pt \"Arial Black\";"))

        self.label_4 = QtGui.QLabel("和",self)

        self.label_4.setStyleSheet(_fromUtf8("font: 11pt \"微软雅黑\";"))

        self.label_5 = QtGui.QLabel("中指",self)

        self.label_5.setStyleSheet(_fromUtf8("\n"
"font: 87 12pt \"Arial Black\";"))

        self.label_6 = QtGui.QLabel("分别操作左右两个按键，按顺序输入给定的笔画。",self)

        self.label_6.setStyleSheet(_fromUtf8("font: 11pt \"微软雅黑\";"))

        self.label_7 = QtGui.QLabel("编码规则",self)

        self.label_7.setStyleSheet(_fromUtf8("\n"
"font: 87 12pt \"Arial Black\";"))

        self.label_8 = QtGui.QLabel("为：左键=丿，右键=丶，先左后右连续按键= 一，先右后左连续按",self)

        self.label_8.setStyleSheet(_fromUtf8("font: 11pt \"微软雅黑\";"))

        self.label_9 = QtGui.QLabel("键=丨，左右两键同时点击=乙",self)

        self.label_9.setStyleSheet(_fromUtf8("font: 11pt \"微软雅黑\";"))

        self.label_10 = QtGui.QLabel(" 如果输入错误，请",self)

        self.label_10.setStyleSheet(_fromUtf8("font: 11pt \"微软雅黑\";"))

        self.label_11 = QtGui.QLabel( "我们将记录你完成任务的用时和出错的次数来计算你的总分。",self)

        self.label_11.setStyleSheet(_fromUtf8("font: 11pt \"微软雅黑\";"))

        self.label_12 = QtGui.QLabel("如没有问题，请点击\"开始\"按钮进行练习；如有疑问，请联系主试。",self)

        self.label_12.setStyleSheet(_fromUtf8("font: 11pt \"微软雅黑\";"))

        self.label_13 = QtGui.QLabel("立即",self)

        self.label_13.setStyleSheet(_fromUtf8("\n"
"font: 87 12pt \"Arial Black\";"))

        self.label_14 = QtGui.QLabel("点击删除键删除并重新输入。",self)

        self.label_14.setStyleSheet(_fromUtf8("font: 11pt \"微软雅黑\";"))

        # 信号连接到指定槽
        self.pushButton.clicked.connect(self.on_pushButton_clicked)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.label.move(self.task.screen_width * 0.41, (self.task.screen_height) * 0.1)
        self.label.setFixedSize(500, 60)

        self.label_2.move(self.task.screen_width * 0.19, (self.task.screen_height) * 0.17)
        self.label_2.setFixedSize(400, 60)
        self.label_3.move(self.task.screen_width * 0.36, (self.task.screen_height) * 0.17)
        self.label_3.setFixedSize(300, 60)
        self.label_4.move(self.task.screen_width * 0.40, (self.task.screen_height) * 0.17)
        self.label_4.setFixedSize(300, 60)
        self.label_5.move(self.task.screen_width * 0.42, (self.task.screen_height) * 0.17)
        self.label_5.setFixedSize(300, 60)
        self.label_6.move(self.task.screen_width * 0.46, (self.task.screen_height) * 0.17)
        self.label_6.setFixedSize(900, 60)

        self.label_7.move(self.task.screen_width * 0.205, (self.task.screen_height) * 0.24)
        self.label_7.setFixedSize(300, 60)
        self.label_8.move(self.task.screen_width * 0.28, (self.task.screen_height) * 0.24)
        self.label_8.setFixedSize(1100, 60)

        self.label_9.move(self.task.screen_width * 0.38, (self.task.screen_height) * 0.31)
        self.label_9.setFixedSize(800, 60)
        self.label_10.move(self.task.screen_width * 0.29, (self.task.screen_height) * 0.38)
        self.label_10.setFixedSize(900, 60)

        self.label_11.move(self.task.screen_width * 0.27, (self.task.screen_height) * 0.45)
        self.label_11.setFixedSize(1100, 60)
        self.label_12.move(self.task.screen_width * 0.25, (self.task.screen_height) * 0.52)
        self.label_12.setFixedSize(1100, 60)

        self.label_13.move(self.task.screen_width * 0.45, (self.task.screen_height) * 0.38)
        self.label_13.setFixedSize( 800, 60)
        self.label_14.move(self.task.screen_width * 0.49, (self.task.screen_height) * 0.38)
        self.label_14.setFixedSize(800, 60)




        self.label.setStyleSheet(_fromUtf8("font: 18pt \"微软雅黑\";\n"
                                           ""))
        self.label_2.setStyleSheet(_fromUtf8("font: 18pt \"微软雅黑\";\n"
                                             ""))
        self.label_3.setStyleSheet(_fromUtf8("font: 18pt \"微软雅黑\";\n"
                                             ""))
        self.label_4.setStyleSheet(_fromUtf8("font: 18pt \"微软雅黑\";\n"
                                             ""))
        self.label_6.setStyleSheet(_fromUtf8("font: 18pt \"微软雅黑\";\n"
                                             ""))
        self.label_5.setStyleSheet(_fromUtf8("font: 18pt \"微软雅黑\";\n"
                                             ""))
        self.label_7.setStyleSheet(_fromUtf8("font: 18pt \"微软雅黑\";\n"
                                             ""))
        self.label_8.setStyleSheet(_fromUtf8("font: 18pt \"微软雅黑\";\n"
                                             ""))
        self.label_9.setStyleSheet(_fromUtf8("font: 18pt \"微软雅黑\";\n"
                                             ""))
        self.label_10.setStyleSheet(_fromUtf8("font: 18pt \"微软雅黑\";\n"
                                             ""))
        self.label_11.setStyleSheet(_fromUtf8("font: 18pt \"微软雅黑\";\n"
                                             ""))
        self.label_12.setStyleSheet(_fromUtf8("font: 18pt \"微软雅黑\";\n"
                                             ""))
        self.label_13.setStyleSheet(_fromUtf8("font: 18pt \"微软雅黑\";\n"
                                             ""))
        self.label_14.setStyleSheet(_fromUtf8("font: 18pt \"微软雅黑\";\n"
                                             ""))










        self.pushButton.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.46, (self.task.screen_height) * 0.65, 200, 80))
        self.label_12.setStyleSheet(_fromUtf8("font: 18pt \"微软雅黑\";\n"
                                              ""))


    def on_pushButton_clicked(self):

        self.ui2.setTask(self.task)
        self.close()

        self.ui.showFullScreen()

        self.ui.startCount()

        QTimer.singleShot(5000, self.ui.close)  # 设置5s后自动退出

        QTimer.singleShot(5000, self.ui2.showFullScreen)        # 设置5s后打开

        #QTimer.singleShot(5000, self.ui2.openKeyBoard)  # 设置5s后打开






    # 键盘监听
    def keyPressEvent(self, event):
            key = event.key()

            if key == QtCore.Qt.Key_Escape:
                self.close()






#练习开始前，准备5s
class Type_prepare5(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.ui=openKeyBoard()

        self.task = Task()

        self.initUi()

    def setTask(self, taskTemp):
        self.task = taskTemp

    def initUi(self):


        self.label = QtGui.QLabel("练习即将开始，请做好准备",self)
        self.label_2 = QtGui.QLabel( "5",self)

        self.label.move(self.task.screen_width * 0.3, (self.task.screen_height) * 0.33)
        self.label.setFixedSize( 800, 70)

        self.label_2.move(self.task.screen_width * 0.48, (self.task.screen_height) * 0.55)
        self.label_2.setFixedSize(800, 100)

        self.timer = QTimer(self)
        self.count = 4
        self.timer.timeout.connect(self.showNum)


        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self):


        self.label.setStyleSheet(_fromUtf8("font: 32pt \"微软雅黑\";\n"
                                           ""))
        self.label_2.setStyleSheet(_fromUtf8("font: 60pt \"微软雅黑\";\n"
                                             ""))

    def countSet(self,s):
            self.label_2.setText(s)

    def showNum(self):

        s=str(self.count)
        self.label_2.setText(s)
        self.count=self.count-1

    def startCount(self):
        self.timer.start(1000)


    # 键盘监听
    def keyPressEvent(self, event):
        key = event.key()

        if key == QtCore.Qt.Key_Escape:
            self.close()





#联系主试，开启软键盘
class openKeyBoard(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.task = Task()

        self.ui=Type_input()

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
        self.pushButton = QtGui.QPushButton("开始", self)

        self.pushButton.setStyleSheet(_fromUtf8("\n"
                                                "\n"
                                                "QPushButton:hover { background-color: rgb(139，137，137); }"))

        self.pushButton.clicked.connect(self.on_pushButton_clicked)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):

        self.label.setText("请联系主试，开启虚拟键盘")


        self.label.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.31, (self.task.screen_height) * 0.26, 800, 60))
        self.label.setStyleSheet(_fromUtf8("font: 30pt \"微软雅黑\";\n"
                                           ""))
        #self.pushButton.setGeometry(
            #QtCore.QRect(self.task.screen_width * 0.45, (self.task.screen_height) * 0.38, 200, 80))
        self.pushButton.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.45, (self.task.screen_height) * 0.38, 200, 80))
        self.pushButton.setStyleSheet(_fromUtf8("font: 22pt \"微软雅黑\";\n"
                                           ""))



    def on_pushButton_clicked(self):
        self.ui.setTask(self.task)
        self.ui.initUi()

        self.close()
        self.ui.showFullScreen()





#练习或者正式实验
class Type_input(QtGui.QWidget):
    def __init__(self, parent=None):

        QtGui.QMainWindow.__init__(self, parent)

        #self.ui = Type_formal()
        #self.ui2 = Type_input()  # 开始正式实验


        self.task = Task()

        self.timer = QTimer(self)

        #self.initUi()




    def setTask(self, taskTemp):
        self.task = taskTemp


    def initUi(self):


        self.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.setStyleSheet(_fromUtf8("border-color: rgb(128, 128, 128);"))

        #界面设计
        self.label = QtGui.QLabel(self)

        self.lineEdit = QtGui.QLineEdit(self)
        self.lineEdit.setEnabled(False)

        self.pushButton_left = QtGui.QPushButton("左键",self)

        self.pushButton_right = QtGui.QPushButton("右键",self)

        self.pushButton_delete = QtGui.QPushButton("delete",self)


        #错误笔画
        self.label_2 = QtGui.QLabel("一",self)
        #self.label_2.setGeometry(QtCore.QRect(90, 110, 21, 16))
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(245, 240, 250);"
                                             "font: 75 22pt \"微软雅黑\";\n"
                                            ))

        self.label_3 = QtGui.QLabel("一",self)
        #self.label_3.setGeometry(QtCore.QRect(140, 110, 21, 16))
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(245, 240, 250);"
                                             "font: 75 22pt \"微软雅黑\";\n"

                                             ))

        self.label_4 = QtGui.QLabel("一",self)
        #self.label_4.setGeometry(QtCore.QRect(170, 110, 21, 16))
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(245, 240, 250);"
                                             "font:  75 22pt \"微软雅黑\";\n"

                                             ))

        self.label_5 = QtGui.QLabel("一",self)

        #self.label_5.setGeometry(QtCore.QRect(210, 110, 21, 16))
        self.label_5.setStyleSheet(_fromUtf8("color: rgb(245, 240, 250);"
                                             "font: 75 22pt \"微软雅黑\";\n"
                                             ))

        self.label_6 = QtGui.QLabel("一",self)
        #self.label_6.setGeometry(QtCore.QRect(250, 110, 21, 16))
        self.label_6.setStyleSheet(_fromUtf8("color: rgb(245, 240, 250);"
                                             "font:75 22pt \"微软雅黑\";\n"

                                             ))

        self.label_7 = QtGui.QLabel("一",self)
        #self.label_7.setGeometry(QtCore.QRect(300, 110, 21, 16))
        self.label_7.setStyleSheet(_fromUtf8("color: rgb(245, 240, 250);"
                                             "font: 75 22pt \"微软雅黑\";\n"
                                             ))

        self.label_8 = QtGui.QLabel("一",self)
        #self.label_8.setGeometry(QtCore.QRect(340, 110, 21, 16))
        self.label_8.setStyleSheet(_fromUtf8("color: rgb(245, 240, 250);"
                                             "font: 75 22pt \"微软雅黑\";\n"

                                             ))

        self.label_9 =QtGui.QLabel("一",self)
        #self.label_9.setGeometry(QtCore.QRect(360, 120, 21, 16))
        self.label_9.setStyleSheet(_fromUtf8("color: rgb(245, 240, 250);"
                                             "font: 75 22pt \"微软雅黑\";\n"

                                             ))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel("一",self)
        #self.label_10.setGeometry(QtCore.QRect(410, 120, 21, 16))
        self.label_10.setStyleSheet(_fromUtf8("color: rgb(245, 240, 250);"
                                              "font: 75 22pt \"微软雅黑\";\n"

                                              ))

        self.label_11 = QtGui.QLabel("一",self)
        #self.label_11.setGeometry(QtCore.QRect(420, 140, 21, 16))
        self.label_11.setStyleSheet(_fromUtf8("color: rgb(245, 240, 250);"
                                              "font: 75 22pt \"微软雅黑\";\n"

                                              ))


        self.lineEdit.setMaxLength(32)



        # 信号连接到指定槽

        self.keyOrder=["1"]
        self.inputString=""

        self.bihua = ["  一  丨  乙  丿  丶  丶  丿  乙  丨  一",
                      "  丨  丿  一  丶  乙  乙  丶  一  丿  丨",
                      "  丿  丶  丨  乙  一  一  乙  丨  丶  丿",
                      "  丶  乙  丿  一  丨  丨  一  丿  乙  丶",
                      "  乙  一  丶  丨  丿  丿  丨  丶  一  乙"]
        self.bihuaIndex=[[4,5,3,1,2,2,1,3,5,4],[5,1,4,2,3,3,2,4,1,5],[1,2,5,3,4,4,3,5,2,1],[2,3,1,4,5,5,4,1,3,2],[3,4,2,5,1,1,5,2,4,3]]
        self.bihuaList=[]
        self.times=0                            #循环次数
        self.temptimes=0
        self .timetemp =-10
        self.timetemp = round(time.clock(),3)*1000
        self.timeleft = round(time.clock(),3)*1000
        self.timeright = round(time.clock(),3)*1000
        self.rowTimeList=[]
        self.errorList=[]

        self.tempTimes = 0

        self .bihuaError=0                                            #错误笔画数
        self.totalTime = round(time.clock(),3)                              #每一行输入用时
        self.formal=False                                               #判断是练习还是正式实验
        self.bihuaNum=0
        self.keyleft=False
        self.keyright=False
        self.keybihua=False
        self.timeout=False
        #self.thread = Thread_Timer()
        self.thread_left=Thread_Timer_left
        self.thread_right=Thread_Timer_right
        self.chulitag=True
        self.keylefttag=False
        self.keyrighttag=False
        self.t1=0
        self.t2=0

        self.tongshitag=False
        self.rownext=True

        self.pushButton_left.pressed.connect(self.keyLeft)
        self.pushButton_right.pressed.connect(self.keyRight)
        self.pushButton_delete.pressed.connect(self.deletePush)


        self.getTaskType()                  #获取任务类型，按键激活时间差

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        #self.showFullScreen()


    def retranslateUi(self):

        #错误笔画
        self.label_2.move(self.task.screen_width * 0.375, (self.task.screen_height) * 0.3)
        self.label_2.setFixedSize(20, 10)

        self.label_3.move(self.task.screen_width * 0.398, (self.task.screen_height) * 0.3)
        self.label_3.setFixedSize(20, 10)

        self.label_4.move(self.task.screen_width * 0.421, (self.task.screen_height) * 0.3)
        self.label_4.setFixedSize(20, 10)

        self.label_5.move(self.task.screen_width * 0.444, (self.task.screen_height) * 0.3)
        self.label_5.setFixedSize(20, 10)

        self.label_6.move(self.task.screen_width * 0.467, (self.task.screen_height) * 0.3)
        self.label_6.setFixedSize(20, 10)

        self.label_7.move(self.task.screen_width * 0.490, (self.task.screen_height) * 0.3)
        self.label_7.setFixedSize(20, 10)

        self.label_8.move(self.task.screen_width * 0.513, (self.task.screen_height) * 0.3)
        self.label_8.setFixedSize(20, 10)

        self.label_9.move(self.task.screen_width * 0.536, (self.task.screen_height) * 0.3)
        self.label_9.setFixedSize(20, 10)

        self.label_10.move(self.task.screen_width * 0.559, (self.task.screen_height) * 0.3)
        self.label_10.setFixedSize(20, 10)

        self.label_11.move(self.task.screen_width * 0.582, (self.task.screen_height) * 0.3)
        self.label_11.setFixedSize(20, 10)



        self.label.setText(self.bihua[self.times])

        # 笔画显示框
        self.label.move(700,220)
        self.label.setFixedSize(500,40)
        self.label.setStyleSheet(_fromUtf8("font: 14pt \"微软雅黑\";\n"
                                           ""))
        #笔画输入框
        self.lineEdit.setStyleSheet(_fromUtf8("font: 14pt \"微软雅黑\";\n"
                                              ""))
        self.lineEdit.move(700, 280)
        self.lineEdit.setFixedSize(520, 40)

        #左键
        self.pushButton_left.move(500, 800)
        self.pushButton_left.setFixedSize(82,82)

        # 右键
        self.pushButton_right.move(660, 800)
        self.pushButton_right.setFixedSize(82, 82)

        #删除键
        self.pushButton_delete.move(780, 800)
        self.pushButton_delete.setFixedSize(82, 82)




    def openKeyBoard(self):
        os.system("osk")

    #键盘监听
    def keyPressEvent(self, event):
        key1 = event.text()
        key2=event.key()


        if key1 == "k":

            self.keyLeft()

        if key1 == "l":

            self.keyRight()

        if key2 == QtCore.Qt.Key_Backspace:
            self.deletePush()

        if key2 == QtCore.Qt.Key_Escape:
            self.close()



    def setbihuaColor(self,num):
        if num==0:
            self.label_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
                                                  "font: 75 22pt \"微软雅黑\";\n"
                                                  "color: rgb(255, 0, 0);"))
            return;
        elif num==1:
            self.label_3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
                                                 "font: 75 22pt \"微软雅黑\";\n"
                                                 "color: rgb(255, 0, 0);"))
            return;
        elif num==2:
            self.label_4.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
                                                 "font: 75 22pt \"微软雅黑\";\n"
                                                 "color: rgb(255, 0, 0);"))
            return;
        elif num==3:
            self.label_5.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
                                                 "font: 75 22pt \"微软雅黑\";\n"
                                                 "color: rgb(255, 0, 0);"))
            return;
        elif num==4:
            self.label_6.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
                                                 "font: 75 22pt \"微软雅黑\";\n"
                                                 "color: rgb(255, 0, 0);"))
            return;
        elif num==5:
            self.label_7.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
                                                 "font: 75 22pt \"微软雅黑\";\n"
                                                 "color: rgb(255, 0, 0);"))
            return;
        elif num==6:
            self.label_8.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
                                                 "font: 75 22pt \"微软雅黑\";\n"
                                                 "color: rgb(255, 0, 0);"))
            return;
        elif num==7:
            self.label_9.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
                                                 "font: 75 22pt \"微软雅黑\";\n"
                                                 "color: rgb(255, 0, 0);"))
            return;
        elif num==8:
            self.label_10.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
                                                 "font: 75 22pt \"微软雅黑\";\n"
                                                 "color: rgb(255, 0, 0);"))
            return;
        elif num==9:
            self.label_11.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
                                                 "font: 75 22pt \"微软雅黑\";\n"
                                                 "color: rgb(255, 0, 0);"))
            return;


    def deletebihuaColor(self,num):
        if num==0:
            self.label_2.setStyleSheet(_fromUtf8("color: rgb(245, 240, 250);\n"
                                                  "font: 75 22pt \"微软雅黑\";\n"
                                                  ))
            return;
        elif num==1:
            self.label_3.setStyleSheet(_fromUtf8("color: rgb(245, 240, 250);\n"
                                                 "font: 75 22pt \"微软雅黑\";\n"
                                                 ))
            return;
        elif num==2:
            self.label_4.setStyleSheet(_fromUtf8("color: rgb(245, 240, 250);\n"
                                                 "font: 75 22pt \"微软雅黑\";\n"
                                                 ))
            return;
        elif num==3:
            self.label_5.setStyleSheet(_fromUtf8("color: rgb(245, 240, 250);\n"
                                                 "font: 75 22pt \"微软雅黑\";\n"
                                                 ))
            return;
        elif num==4:
            self.label_6.setStyleSheet(_fromUtf8("color: rgb(245, 240, 250);\n"
                                                 "font: 75 22pt \"微软雅黑\";\n"
                                                 ))
            return;
        elif num==5:
            self.label_7.setStyleSheet(_fromUtf8("color: rgb(245, 240, 250);\n"
                                                 "font: 75 22pt \"微软雅黑\";\n"
                                                 ))
            return;
        elif num==6:
            self.label_8.setStyleSheet(_fromUtf8("color: rgb(245, 240, 250);\n"
                                                 "font: 75 22pt \"微软雅黑\";\n"
                                                 ))
            return;
        elif num==7:
            self.label_9.setStyleSheet(_fromUtf8("color: rgb(245, 240, 250);\n"
                                                 "font: 75 22pt \"微软雅黑\";\n"
                                                 ))
            return;
        elif num==8:
            self.label_10.setStyleSheet(_fromUtf8("color: rgb(245, 240, 250);\n"
                                                 "font: 75 22pt \"微软雅黑\";\n"
                                                 ))
            return;
        elif num==9:
            self.label_11.setStyleSheet(_fromUtf8("color: rgb(245, 240, 250);\n"
                                                 "font: 75 22pt \"微软雅黑\";\n"
                                                 ))
            return;


    def resetbihuaColor(self):
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(245, 240, 250);"
                                              "font: 75 22pt \"微软雅黑\";\n"
                                              ))
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(245, 240, 250);"
                                             "font: 75 22pt \"微软雅黑\";\n"
                                             ))
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(245, 240, 250);"
                                             "font: 75 22pt \"微软雅黑\";\n"
                                             ))
        self.label_5.setStyleSheet(_fromUtf8("color: rgb(245, 240, 250);"
                                             "font: 75 22pt \"微软雅黑\";\n"
                                             ))
        self.label_6.setStyleSheet(_fromUtf8("color: rgb(245, 240, 250);"
                                             "font: 75 22pt \"微软雅黑\";\n"
                                             ))
        self.label_7.setStyleSheet(_fromUtf8("color: rgb(245, 240, 250);"
                                             "font: 75 22pt \"微软雅黑\";\n"
                                             ))
        self.label_8.setStyleSheet(_fromUtf8("color: rgb(245, 240, 250);"
                                             "font: 75 22pt \"微软雅黑\";\n"
                                             ))
        self.label_9.setStyleSheet(_fromUtf8("color: rgb(245, 240, 250);"
                                             "font: 75 22pt \"微软雅黑\";\n"
                                             ))
        self.label_10.setStyleSheet(_fromUtf8("color: rgb(245, 240, 250);"
                                             "font: 75 22pt \"微软雅黑\";\n"
                                             ))
        self.label_11.setStyleSheet(_fromUtf8("color: rgb(245, 240, 250);"
                                             "font: 75 22pt \"微软雅黑\";\n"
                                             ))




    def chuli(self,s):
        if self.chulitag and (len(self.bihuaList)<10):

            self.inputString = self.lineEdit.text() + s
            self.lineEdit.setText(self.inputString)
            self.chulitag=False


            if s=="  丿":
                self.keylefttag = False
                self.keyrighttag = False
                self.chulitag = False
                self.thread_right.ifdo = False
                self.thread_left.ifdo = False


                bihua = 1
                #self.thread.ifdo=False
                if (len(self.bihuaList) < 10):
                    self.bihuaList.append(1)
                num = len(self.bihuaList)
                if (len(self.bihuaList) <= 10):
                    if (not (bihua == self.bihuaIndex[self.times][num - 1])):
                        self.bihuaError = self.bihuaError + 1
                        self.setbihuaColor(num - 1)

            elif s=="  丶":

                self.keylefttag = False
                self.keyrighttag = False
                self.chulitag = False
                self.thread_right.ifdo = False
                self.thread_left.ifdo = False


                bihua = 2
                #self.thread.ifdo = False
                if (len(self.bihuaList) < 10):
                    self.bihuaList.append(2)
                num = len(self.bihuaList)
                if (len(self.bihuaList) <=10):
                    if (not (bihua == self.bihuaIndex[self.times][num - 1])):
                        self.bihuaError = self.bihuaError + 1
                        self.setbihuaColor(num - 1)

            self.rowEnd()


    #点击左键
    @QtCore.pyqtSlot()
    def keyLeft(self):
        #print "我是左键"
        if (len(self.bihuaList) >= 10):  # 输入够10个笔画
            return
        self.keylefttag=True

        self.timeleft=round(time.clock(),3)*1000
        t=self.timeleft -self .timetemp
        self.timetemp=self.timeleft


        self.t1=40
        self.t2=200



        if self.keyrighttag and (len(self.bihuaList)<10):
            if (t<=self.t1):
                self.inputString = self.lineEdit.text() + "  乙"
                self.lineEdit.setText(self.inputString)
                self.keylefttag = False
                self.keyrighttag = False
                self.chulitag = False
                self.thread_right.ifdo = False
                self.thread_left.ifdo=False


                bihua = 3
                if (len(self.bihuaList) < 10):
                    self.bihuaList.append(3)
                num = len(self.bihuaList)
                if (len(self.bihuaList) <= 10):
                    if (not (bihua == self.bihuaIndex[self.times][num - 1])):
                        self.bihuaError = self.bihuaError + 1
                        self.setbihuaColor(num-1)

            elif (t>self.t1 and t<=self.t2):
                self.inputString = self.lineEdit.text() + "   |"
                self.lineEdit.setText(self.inputString)
                self.keylefttag = False
                self.keyrighttag = False
                self.chulitag = False
                self.thread_right.ifdo = False
                self.thread_left.ifdo = False


                bihua = 5
                if (len(self.bihuaList) < 10):
                    self.bihuaList.append(5)
                num = len(self.bihuaList)
                if (len(self.bihuaList) <= 10):
                    if (not (bihua == self.bihuaIndex[self.times][num - 1])):
                        self.bihuaError = self.bihuaError + 1
                        self.setbihuaColor(num - 1)



        else:
            # 创建线程

            self.thread_left = Thread_Timer_left()

            self.thread_left.ifdo = True

            # 注册信号处理函数
            self.thread_left._signal.connect(self.chuli)

            self.thread_left.sett2(self.t2)

            self.thread_left.setSignalString("  丿")

            self.chulitag = True
            # 启动线程
            self.thread_left.start()




        self.keyrighttag = False

        #print  len(self.lineEdit.text())
        #print self.bihuaError

        self.rowEnd()


    #点击右键
    @QtCore.pyqtSlot()
    def keyRight(self):
        #print "我是右键"
        if (len(self.bihuaList) >= 10):  # 输入够10个笔画
            return

        self.keyrighttag=True

        self.timeright = round(time.clock(),3)*1000
        t = self.timeright -self .timetemp
        self.timetemp=self.timeright
        #print t

        self.t1 = 40
        self.t2 = 200

       #print self.keylefttag
        if self.keylefttag and (len(self.bihuaList)<10):
            if (t<=self.t1):
                self.inputString = self.lineEdit.text() + "  乙"
                self.lineEdit.setText(self.inputString)
                self.keylefttag = False
                self.keyrighttag = False
                self.chulitag = False
                self.thread_right.ifdo = False
                self.thread_left.ifdo = False


                bihua = 3
                if (len(self.bihuaList) < 10):
                    self.bihuaList.append(3)
                num = len(self.bihuaList)
                if (len(self.bihuaList) <= 10):
                    if (not (bihua == self.bihuaIndex[self.times][num - 1])):
                        self.bihuaError = self.bihuaError + 1
                        self.setbihuaColor(num - 1)

            elif (t>self.t1 and t<=self.t2):
                self.inputString = self.lineEdit.text() + "  一"
                self.lineEdit.setText(self.inputString)
                self.keylefttag = False
                self.keyrighttag = False
                self.chulitag = False
                self.thread_right.ifdo = False
                self.thread_left.ifdo = False


                bihua = 4
                if (len(self.bihuaList) < 10):
                    self.bihuaList.append(4)
                num = len(self.bihuaList)
                if (len(self.bihuaList) <= 10):
                    if (not (bihua == self.bihuaIndex[self.times][num - 1])):
                        self.bihuaError = self.bihuaError + 1
                        self.setbihuaColor(num - 1)



        else:
            # 创建线程
            self.thread_right = Thread_Timer_right()
            #thread = self.thread
            self.thread_right.ifdo = True

            # 注册信号处理函数
            self.thread_right._signal.connect(self.chuli)

            self.thread_right.sett2(self.t2)

            self.thread_right.setSignalString("  丶")

            self.chulitag = True
            # 启动线程
            self.thread_right.start()



        self.keylefttag=False
        #print  len(self.lineEdit.text())
        #print self.bihuaError

        self.rowEnd()



    def rowEnd(self):
        #print len(self.lineEdit.text())
        if (len(self.bihuaList) == 10):  # 输入够10个笔画
            tag = self.isRowCorrect()
            #tag=True

            if (tag == True):  # 如果这一行笔画完全正确,可以跳到下一行
                # time.sleep(1)

                totaltime = self.totalTime
                self.totalTime = round(time.clock(), 3)
                # print round(self.totalTime - totaltime, 3)

                if (self.formal == False):  # 如果是练习，把每一行的错误次数，用时记录好
                    self.addPracticeErrorList(self.bihuaError)
                    self.addPracticeTimeList(round(self.totalTime - totaltime, 3))

                else:  # 如果是正式实验，把每一行的错误次数，用时记录好
                    self.addFormalErrorList(self.bihuaError)
                    self.addFormalTimeList(round(self.totalTime - totaltime, 3))

                self.rowTimeList.append(round(self.totalTime - totaltime, 3))  # 记录这一行用时
                self.errorList.append(self.bihuaError)  # 记录这一行的笔画错误次数

                # 如果是正式实验，只要输入五次，就可以跳转界面
                if (self.times == 4 and self.formal == True):
                    self.ui3 = Type_evaluate1()  # 跳转到量表任务介绍界面
                    self.ui3.setTask(self.task)
                    self.toEvaluate1()
                    return

                # 否则，如果是练习



                #tag1 = True         self.tempTimes 哈哈哈哈哈
                self.rownext=True
                if (self.temptimes >= 6):
                  #self.tempTimes = self.tempTimes + 4



                  tag1 = self.isQualified()

                  #tag1=True

                  if (tag1 == True):
                        # 如果完成5次之后，有连续两行，并且每行时间少于13s,笔画错误次数少于1，跳转到正式实验，否则继续练习
                        self.ui = Type_formal()
                        self.ui2 = Type_input()
                        self.ui2.setTask(self.task)
                        self.ui2.initUi()
                        self.toFormal()  # 跳到练习和正式实验跳转界面
                        self.rownext=False
                        return
                    #else:
                     #   self.rowTimeList = []  # 否则下一次循环，每一行时间，错误次数重新记录
                      #  self.errorList = []

                # time.sleep(1)                                 #休息1s,跳转到下一行
                if(self.rownext):
                    self.times = self.times + 1
                    self.temptimes = self.temptimes + 1

                    if (self.times == 5):
                        self.times = 0  # 重新开始下一次循环

                    self.label.setText(self.bihua[self.times])
                    self.lineEdit.setText("")
                    self.inputString = ""
                    self.bihuaList = []
                    self.bihuaError = 0

                    self.resetbihuaColor()

                    self.totalTime = round(time.clock(), 3)  # 开始新的一行，重新计时


    #删除一个笔画
    @QtCore.pyqtSlot()
    def deletePush(self):
        if len(self.inputString)>=3:
            if self.inputString[-1] == "|":
                self.inputString = self.inputString[:-4]
            else:
                self.inputString = self.inputString[:-3]
        else:
            return
        self.lineEdit.setText(self.inputString)         #删除最后一个笔画
        self.bihuaError =self.bihuaError +1             #每删除一个元素，笔画错误数＋1

        self.keylefttag = False
        self.keyrighttag = False
        self.chulitag = False
        self.thread_right.ifdo = False
        self.thread_left.ifdo = False

        num=len(self.bihuaList)
        self.deletebihuaColor(num-1)


        if(len(self .bihuaList)>0 ):
            self.bihuaList.pop()        #删除最后一个元素


    #验证一行是否完全正确
    def isRowCorrect(self):

        for i in range(0,10 ):
            if(not(self .bihuaList [i]== self .bihuaIndex [self .times][i])):
                return False
        return True


    #验证是否合格，5行之后，是否有连续两行正确率达60%，
    def isQualified(self):
        CorrectRate=4              #正确率60%,即错误次数为4
        RowTime=99999999                 #无时间限制
        num=len(self.errorList)-1
        if self.errorList [num]<=CorrectRate  and self.errorList [num-1]<=CorrectRate:
            if self.rowTimeList[num] <= RowTime and self.rowTimeList[num- 1] <= RowTime:
                return True

        return False


    #获取任务类型，来设置按键时间差
    def getTaskType(self):

        if(self.task .taskType=="10_1"):   #10*100ms
            self.t1=80
            self.t2=150
            return
        if (self.task.taskType == "10_2"):  #10*200ms
            self.t1 = 80
            self.t2 = 200
            return
        if (self.task.taskType == "10_3"):  #10*300ms
            self.t1 = 80
            self.t2 = 250
            return

        if (self.task.taskType == "15_1"):  #15*100ms
            self.t1 = 100
            self.t2 = 150
            return
        if (self.task.taskType == "15_2"):  #15*200ms
            self.t1 = 100
            self.t2 = 200
            return
        if (self.task.taskType == "15_3"):  #15*300ms
            self.t1 = 100
            self.t2 = 250
            return

        if (self.task.taskType == "20_1"):  #20*100ms
            self.t1 = 120
            self.t2 = 150
            return
        if (self.task.taskType == "20_2"):  #20*200ms
            self.t1 = 120
            self.t2 = 200
            return
        if (self.task.taskType == "20_3"):  #20*300ms
            self.t1 = 120
            self.t2 = 250
            return


    def countSet(self,s):
        self .label_2 .setText(s)


    #练习，将每一行错误次数记录下来
    def addPracticeErrorList(self,e):
        for key in self .task .practiceErrorDic.keys():
            if(key == self.task .taskType ):
                self .task .practiceErrorDic [key].append(e)
                break

    # 正式实验，将每一行用时记录下来
    def addPracticeTimeList(self, e):
        for key in self.task.practiceTimeDic.keys():
            if (key == self.task.taskType):
                self.task.practiceTimeDic[key].append(e)
                break

    # 正式实验，将每一行错误次数记录下来
    def addFormalErrorList(self, e):
        for key in self.task.formalErrorDic.keys():
            if (key == self.task.taskType):
                self.task.formalErrorDic[key].append(e)
                break

    # 正式实验，将每一行用时记录下来
    def addFormalTimeList(self, e):
        for key in self.task.formalTimeDic.keys():
            if (key == self.task.taskType):
                self.task.formalTimeDic[key].append(e)
                break

    def newFormal(self):
        self.ui=Type_formal()

    def newInput(self):
        self.ui2=Type_input()

    #跳转到正式实验界面,练习结束
    def toFormal(self):

        # 关闭练习界面
        QTimer.singleShot(1000, self.close)  # 设置1s后自动退出
        QTimer.singleShot(1000, self.ui.showFullScreen) #练习和正式实验之间的跳转界面




        self.ui2.formal = True  # 设置正式实验标志为真



        QTimer.singleShot(6000, self.ui.close)  # 设置5s后自动退出
        self.ui.startCount()
        QTimer.singleShot(6000, self.ui2.showFullScreen)  # 设置5s后自动显示






    #跳转到任务评价价绍界面
    def toEvaluate1(self):

        self.close()
        #QTimer.singleShot(500, self.close)  # 设置2s后自动退出

        #结束正式试验
        #self.close()
        self.ui3.showFullScreen()
        #QTimer.singleShot(500, self.ui3.showFullScreen)  # 设置2s后自动显示






#练习结束，练习和正式实验之间的跳转界面
class Type_formal(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        self.task = Task()

        self.initUi()



    def setTask(self, taskTemp):
        self.task = taskTemp



    def initUi(self):

        self.label = QtGui.QLabel("正式实验即将开始，请做好准备",self)
        self.label_2 = QtGui.QLabel("练习结束", self)
        self.label_4 = QtGui.QLabel("5",self)


        self.label.move(self.task.screen_width * 0.3, (self.task.screen_height) * 0.21)
        self.label.setFixedSize(800, 200)

        self.label_2.move(self.task.screen_width * 0.44, (self.task.screen_height) * 0.13)
        self.label_2.setFixedSize(300, 200)

        self.label_4.move(self.task.screen_width * 0.48, (self.task.screen_height) * 0.35)
        self.label_4.setFixedSize( 200, 140)

        self.timer = QTimer(self)
        self.count = 5
        self.timer.timeout.connect(self.showNum)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self):


        self.label.setStyleSheet(_fromUtf8("font: 28pt \"微软雅黑\";\n"
                                             ""))
        self.label_2.setStyleSheet(_fromUtf8("font: 28pt \"微软雅黑\";\n"
                                             ""))
        self.label_4.setStyleSheet(_fromUtf8("font: 60pt \"微软雅黑\";\n"
                                             ""))

    # 键盘监听
    def keyPressEvent(self, event):

            key= event.key()

            if key == QtCore.Qt.Key_Escape:
                self.close()

    def startCount(self):
        self.timer.start(1000)

    def showNum(self):

        s=str(self.count)
        self.label_4.setText(s)
        self.count=self.count-1




#任务评价介绍
class Type_evaluate1(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        self.ui = Type_evaluate2()


        self.task = Task()

        self.initUi()

    def setTask(self, taskTemp):
        self.task = taskTemp

    def initUi(self):

            self.label = QtGui.QLabel(self)

            self.label_4 = QtGui.QLabel(self)
            self.label_5 = QtGui.QLabel(self)
            self.label_6 = QtGui.QLabel(self)
            self.label_7 = QtGui.QLabel(self)
            self.label_8 = QtGui.QLabel(self)
            self.label_9 = QtGui.QLabel(self)
            self.label_10 = QtGui.QLabel(self)
            self.label_11 = QtGui.QLabel(self)
            self.label_12 = QtGui.QLabel(self)

            self.layoutWidget_2 = QtGui.QWidget(self)

            self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget_2)
            self.verticalLayout_4.setMargin(0)

            self.label_26 = QtGui.QLabel(self.layoutWidget_2)

            self.verticalLayout_4.addWidget(self.label_26)

            self.label_27 = QtGui.QLabel(self.layoutWidget_2)

            self.verticalLayout_4.addWidget(self.label_27)
            self.label_28 = QtGui.QLabel(self.layoutWidget_2)

            self.verticalLayout_4.addWidget(self.label_28)
            self.label_29 = QtGui.QLabel(self.layoutWidget_2)

            self.verticalLayout_4.addWidget(self.label_29)
            self.layoutWidget = QtGui.QWidget(self)

            self.verticalLayout_5 = QtGui.QVBoxLayout(self.layoutWidget)
            self.verticalLayout_5.setMargin(0)

            self.label_21 = QtGui.QLabel(self.layoutWidget)

            self.verticalLayout_5.addWidget(self.label_21)
            self.label_30 = QtGui.QLabel(self.layoutWidget)

            self.verticalLayout_5.addWidget(self.label_30)
            self.layoutWidget_3 = QtGui.QWidget(self)

            self.verticalLayout_6 = QtGui.QVBoxLayout(self.layoutWidget_3)
            self.verticalLayout_6.setMargin(0)

            self.label_22 = QtGui.QLabel(self.layoutWidget_3)
            self.verticalLayout_6.addWidget(self.label_22)

            self.label_31 = QtGui.QLabel(self.layoutWidget_3)
            self.verticalLayout_6.addWidget(self.label_31)

            self.label_24 = QtGui.QLabel(self)

            self.label_17 = QtGui.QLabel(self)
            self.label_18 = QtGui.QLabel(self)
            self.label_15 = QtGui.QLabel(self)
            self.label_16 = QtGui.QLabel(self)
            self.label_14 = QtGui.QLabel(self)
            self.label_23 = QtGui.QLabel(self)

            self.pushButton = QtGui.QPushButton(self)
            self.pushButton.setStyleSheet(_fromUtf8("\n"
                                                    "\n"
                                                    "QPushButton:hover { background-color: rgb(139，137，137); }"))



            self.layoutWidget1 = QtGui.QWidget(self)


            self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget1)
            self.verticalLayout_3.setMargin(0)

            self.label_19 = QtGui.QLabel(self.layoutWidget1)

            self.verticalLayout_3.addWidget(self.label_19)
            self.label_25 = QtGui.QLabel(self.layoutWidget1)

            self.verticalLayout_3.addWidget(self.label_25)
            self.label_20 = QtGui.QLabel(self.layoutWidget1)

            self.verticalLayout_3.addWidget(self.label_20)
            self.label_13 = QtGui.QLabel(self)



            self.line = QtGui.QFrame(self)
            self.line.setGeometry(QtCore.QRect(self.task.screen_width * 0.15, (self.task.screen_height) * 0.09, 1400, 60))
            self.line.setStyleSheet(_fromUtf8("color: rgb(0, 255, 255);"))
            self.line.setFrameShape(QtGui.QFrame.HLine)
            self.line.setFrameShadow(QtGui.QFrame.Sunken)

            self.line_2 = QtGui.QFrame(self)
            self.line_2.setGeometry(QtCore.QRect(self.task.screen_width * 0.15, (self.task.screen_height) * 0.13, 1400, 60))
            self.line_2.setFrameShape(QtGui.QFrame.HLine)
            self.line_2.setFrameShadow(QtGui.QFrame.Sunken)


            # 信号连接到指定槽
            self.pushButton.pressed.connect(self.next_Button_clicked)

            self.retranslateUi()
            QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):


            self.label.move(self.task.screen_width * 0.15, (self.task.screen_height) * 0.05)
            self.setFixedSize(1600, 60)

            #条目名称
            self.label_4.setGeometry(QtCore.QRect(self.task.screen_width * 0.17, (self.task.screen_height) * 0.125, 130, 30))
            # 端点
            self.label_5.setGeometry(
                QtCore.QRect(self.task.screen_width * 0.30, (self.task.screen_height) * 0.125, 120, 30))
            # 条目说明
            self.label_6.setGeometry(
                QtCore.QRect(self.task.screen_width * 0.60, (self.task.screen_height) * 0.125, 150, 30))

            # 脑力需求
            self.label_7.setGeometry(
                QtCore.QRect(self.task.screen_width * 0.16, (self.task.screen_height) * 0.2, 200, 40))

            self.label_13.setGeometry(
                QtCore.QRect(self.task.screen_width * 0.295, (self.task.screen_height) * 0.2, 80, 40))


            self.layoutWidget1.move(self.task.screen_width * 0.40, (self.task.screen_height) * 0.19)
            self.layoutWidget1.setFixedSize(1000, 150)


            #体力需求
            self.label_8.setGeometry(
                QtCore.QRect(self.task.screen_width * 0.16, (self.task.screen_height) * 0.35, 200, 40))

            self.label_14.setGeometry(
                QtCore.QRect(self.task.screen_width * 0.295, (self.task.screen_height) * 0.35, 80,40))

            self.layoutWidget_2.setGeometry(
                QtCore.QRect(self.task.screen_width * 0.40, (self.task.screen_height) * 0.34,  1000, 150))

            #时间需求
            self.label_9.setGeometry(
                QtCore.QRect(self.task.screen_width * 0.16, (self.task.screen_height) * 0.52,200, 40))

            self.label_15.setGeometry(
                QtCore.QRect(self.task.screen_width * 0.295, (self.task.screen_height) * 0.52, 80, 40))

            self.layoutWidget.setGeometry(
                QtCore.QRect(self.task.screen_width * 0.40, (self.task.screen_height) * 0.51,  1000, 70))

            # 业绩水平
            self.label_10.setGeometry(
                QtCore.QRect(self.task.screen_width * 0.16, (self.task.screen_height) * 0.618, 200, 40))

            self.label_16.setGeometry(
                QtCore.QRect(self.task.screen_width * 0.295, (self.task.screen_height) * 0.618, 80, 40))

            self.layoutWidget_3.setGeometry(
                QtCore.QRect(self.task.screen_width * 0.40, (self.task.screen_height) * 0.61,  1000, 70))

            # 努力程度
            self.label_11.setGeometry(
                QtCore.QRect(self.task.screen_width * 0.16, (self.task.screen_height) * 0.72, 200, 40))

            self.label_17.setGeometry(
                QtCore.QRect(self.task.screen_width * 0.295, (self.task.screen_height) * 0.72, 80, 40))

            self.label_23.setGeometry(QtCore.QRect(self.task.screen_width * 0.40, (self.task.screen_height) * 0.72, 1000, 40))

            # 受挫程度
            self.label_12.setGeometry(
                QtCore.QRect(self.task.screen_width * 0.16, (self.task.screen_height) * 0.8, 200, 40))

            self.label_18.setGeometry(
                QtCore.QRect(self.task.screen_width * 0.295, (self.task.screen_height) * 0.8, 80, 40))

            self.label_24.setGeometry(
                QtCore.QRect(self.task.screen_width * 0.40, (self.task.screen_height) * 0.8,  1000, 40))

            self.pushButton.setGeometry(
                QtCore.QRect(self.task.screen_width * 0.45, (self.task.screen_height) * 0.5, 200, 80))
            #self.pushButton.setGeometry(QtCore.QRect(self.task.screen_width * 0.45, (self.task.screen_height) * 0.87, 200, 80))


            self.label.setText("请对刚刚完成的拖动任务从以下6个方面进行主观评价，请先仔细阅读以下说明：")

            self.label_4.setText("条目名称")
            self.label_5.setText("端点")
            self.label_6.setText("条目说明")
            self.label_7.setText("1.脑力需求")
            self.label_8.setText("2.体力需求")
            self.label_9.setText("3.时间需求")
            self.label_10.setText("4.业绩水平")
            self.label_11.setText("5.努力程度")
            self.label_12.setText("6.受挫程度")

            self.label_26.setText("体力需求指完成工作过程中需要付出多大的体力劳动（如：推，拉，")
            self.label_27.setText("转身，动作控制，进行活动的程度等等）？该任务从体力方面对你而")
            self.label_28.setText("言是容易还是困难？是缓慢还是快速？肌肉感到松弛还是紧张？动作")
            self.label_29.setText("轻松还是费力？")
            self.label_21.setText("时间需求指定完成任务是的速率或节奏，器节奏是缓慢还是快速？是")
            self.label_30.setText("使人感到从容不迫，还是令人感到慌乱呢？")
            self.label_22.setText("业绩水平指对完成目标取得的成绩怎么样？对取得的成绩，您的满意")
            self.label_31.setText("程度有多大？")
            self.label_24.setText("受挫程度指在工作中，您感到沮丧感，烦恼程度是小还是大？")
            self.pushButton.setText("下一步")
            self.label_17.setText("低/高")
            self.label_18.setText("低/高")
            self.label_15.setText("低/高")
            self.label_16.setText("好/差")
            self.label_14.setText("低/高")
            self.label_23.setText("努力程度指完成您的工作需付出的努力是小还是大？（脑力及体力）")
            self.label_19.setText("脑力需求指完成工作过程中需付出多大的脑力活动（如：思考，下")
            self.label_25.setText("决定，计算，记忆，观察，搜查等等）？该工作从脑力方面对你而言")
            self.label_20.setText("是容易还是困难？是简单还是复杂？要求严格还是不严格？")
            self.label_13.setText("低/高")

            self.label.setStyleSheet(_fromUtf8("font: 20pt \"微软雅黑\";"))
            self.label_4.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                 ""))
            self.label_5.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                 ""))
            self.label_6.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                 ""))
            self.label_7.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                 ""))
            self.label_13.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                  ""))
            self.label_19.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                  ""))
            self.label_20.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                  ""))
            self.label_25.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                  ""))
            self.label_8.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                 ""))
            self.label_14.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                  ""))
            self.label_26.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                  ""))
            self.label_27.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                  ""))
            self.label_28.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                  ""))
            self.label_29.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                  ""))
            self.label_9.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                 ""))
            self.label_15.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                  ""))
            self.label_21.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                  ""))
            self.label_30.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                  ""))
            self.label_10.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                  ""))
            self.label_16.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                  ""))
            self.label_22.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                  ""))
            self.label_31.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                  ""))
            self.label_11.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                  ""))
            self.label_17.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                  ""))
            self.label_23.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                  ""))
            self.label_12.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                  ""))
            self.label_18.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                  ""))
            self.label_24.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                  ""))


    def next_Button_clicked(self):

        self.ui.setTask(self.task)  # 传递任务对象
        self.close()

        self.ui.showFullScreen()




    # 键盘监听
    def keyPressEvent(self, event):
            key = event.key()

            if key == QtCore.Qt.Key_Escape:
                self.close()



#开始任务评价
class Type_evaluate2(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        self.ui=Type_break15()
        self.ui1 = Type_choice()

        self.ui2=Type_compare()

        self.task = Task()

        self.initUi()

    # 键盘监听
    def keyPressEvent(self, event):
            key = event.key()

            if key == QtCore.Qt.Key_Escape:
                self.close()

    def setTask(self, taskTemp):
        self.task = taskTemp


    def initUi(self):


        self.pushButton = QtGui.QPushButton(self)

        self.pushButton.setStyleSheet(_fromUtf8("\n"
"\n"
"QPushButton:hover { background-color: rgb(139，137，137); }"))

        self.label = QtGui.QLabel(self)
        self.label_2 = QtGui.QLabel(self)
        self.label_3 = QtGui.QLabel(self)
        self.label_4 = QtGui.QLabel(self)
        self.label_5 = QtGui.QLabel(self)
        self.label_6 = QtGui.QLabel(self)
        self.label_7 = QtGui.QLabel(self)
        self.label_8 = QtGui.QLabel(self)
        self.label_9 = QtGui.QLabel(self)



        self.label_0 = QtGui.QLabel(self)
        self.label_25 = QtGui.QLabel(self)
        self.label_50 = QtGui.QLabel(self)
        self.label_75 = QtGui.QLabel(self)
        self.label_100 = QtGui.QLabel(self)

        self.layoutWidget = QtGui.QWidget(self)

        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setMargin(0)

        self.label_12 = QtGui.QLabel(self.layoutWidget)

        self.horizontalLayout_2.addWidget(self.label_12)


        self.label_17 = QtGui.QLabel(self.layoutWidget)

        self.horizontalLayout_2.addWidget(self.label_17)
        self.layoutWidget_2 = QtGui.QWidget(self)


        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setMargin(0)

        self.label_13 = QtGui.QLabel(self.layoutWidget_2)

        self.horizontalLayout_3.addWidget(self.label_13)


        self.label_18 = QtGui.QLabel(self.layoutWidget_2)

        self.horizontalLayout_3.addWidget(self.label_18)
        self.layoutWidget_3 = QtGui.QWidget(self)


        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_4.setMargin(0)

        self.label_14 = QtGui.QLabel(self.layoutWidget_3)

        self.horizontalLayout_4.addWidget(self.label_14)

        self.label_19 = QtGui.QLabel(self.layoutWidget_3)

        self.horizontalLayout_4.addWidget(self.label_19)
        self.layoutWidget_4 = QtGui.QWidget(self)


        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_5.setMargin(0)

        self.label_15 = QtGui.QLabel(self.layoutWidget_4)

        self.horizontalLayout_5.addWidget(self.label_15)


        self.label_20 = QtGui.QLabel(self.layoutWidget_4)

        self.horizontalLayout_5.addWidget(self.label_20)
        self.layoutWidget_5 = QtGui.QWidget(self)


        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_6.setMargin(0)

        self.label_16 = QtGui.QLabel(self.layoutWidget_5)

        self.horizontalLayout_6.addWidget(self.label_16)



        self.label_21 = QtGui.QLabel(self.layoutWidget_5)

        self.horizontalLayout_6.addWidget(self.label_21)
        self.widget = QtGui.QWidget(self)


        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)

        self.label_10 = QtGui.QLabel(self.widget)

        self.horizontalLayout.addWidget(self.label_10)

        self.label_11 = QtGui.QLabel(self.widget)

        self.horizontalLayout.addWidget(self.label_11)

        self.Button_ui()
        self.setTags()

        # 信号连接到指定槽
        self.pushButton.clicked.connect(self.on_pushButton_clicked)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):

        self.label.setText("在认真阅读上述各条目地详细说明后，")
        self.label_2.setText("根据自己所执行的任务实际情况，分别点击直线上的相应位置做标记")
        self.label_3.setText("除业绩水平外，其余五条目从左至右均为逐渐增加；业绩水平从左至右为好到差")
        self.pushButton.setText( "下一步")
        self.label_4.setText("脑力需求")
        self.label_5.setText( "体力需求")
        self.label_6.setText("时间需求")
        self.label_7.setText("业绩水平")
        self.label_8.setText("努力程度")
        self.label_9.setText( "受挫程度")

        self.label_0.setText("0")
        self.label_25.setText("25")
        self.label_50 .setText("50")
        self.label_75 .setText("75")
        self.label_100 .setText("100")

        self.label_0.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.37, (self.task.screen_height) * 0.26, 200, 40))
        self.label_0.setStyleSheet(_fromUtf8("font: 15pt \"微软雅黑\";\n"
                                           ""))
        self.label_25.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.455, (self.task.screen_height) * 0.26, 300, 40))
        self.label_25.setStyleSheet(_fromUtf8("font: 15pt \"微软雅黑\";\n"
                                             ""))
        self.label_50.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.54, (self.task.screen_height) * 0.26, 300, 40))
        self.label_50.setStyleSheet(_fromUtf8("font: 15pt \"微软雅黑\";\n"
                                             ""))
        self.label_75.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.625, (self.task.screen_height) * 0.26, 300, 40))
        self.label_75.setStyleSheet(_fromUtf8("font: 15pt \"微软雅黑\";\n"
                                             ""))
        self.label_100.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.71, (self.task.screen_height) * 0.26, 300, 40))
        self.label_100.setStyleSheet(_fromUtf8("font: 15pt \"微软雅黑\";\n"
                                             ""))

        self.label.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.35, (self.task.screen_height) * 0.08, 700, 40))
        self.label.setStyleSheet(_fromUtf8("font: 20pt \"微软雅黑\";\n"
                                             ""))
        self.label_2.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.23, (self.task.screen_height) * 0.13, 1200, 40))
        self.label_2.setStyleSheet(_fromUtf8("font: 20pt \"微软雅黑\";\n"
                                           ""))
        self.label_3.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.175, (self.task.screen_height) * 0.18, 1800, 40))
        self.label_3.setStyleSheet(_fromUtf8("font: 20pt \"微软雅黑\";\n"
                                             ""))

        self.label_4.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.2, (self.task.screen_height) * 0.3, 150, 40))
        self.label_4.setStyleSheet(_fromUtf8("font: 18pt \"微软雅黑\";\n"
                                             ""))
        self.widget.setGeometry(QtCore.QRect(self.task.screen_width * 0.37, (self.task.screen_height) * 0.305, 700, 40))


        self.label_5.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.2, (self.task.screen_height) * 0.38, 150, 40))
        self.label_5.setStyleSheet(_fromUtf8("font: 18pt \"微软雅黑\";\n"
                                             ""))
        self.layoutWidget.setGeometry(QtCore.QRect(self.task.screen_width * 0.334, (self.task.screen_height) * 0.385, 772, 40))


        self.label_6.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.2, (self.task.screen_height) * 0.46, 150, 40))
        self.label_6.setStyleSheet(_fromUtf8("font: 18pt \"微软雅黑\";\n"
                                             ""))
        self.layoutWidget_2.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.37, (self.task.screen_height) * 0.465, 700, 40))

        self.label_7.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.2, (self.task.screen_height) * 0.54, 150, 40))
        self.label_7.setStyleSheet(_fromUtf8("font: 18pt \"微软雅黑\";\n"
                                             ""))
        self.layoutWidget_3.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.37, (self.task.screen_height) * 0.545, 700, 40))

        self.label_8.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.2, (self.task.screen_height) * 0.62, 150, 40))
        self.label_8.setStyleSheet(_fromUtf8("font: 18pt \"微软雅黑\";\n"
                                             ""))
        self.layoutWidget_4.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.37, (self.task.screen_height) * 0.625, 700, 40))

        self.label_9.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.2, (self.task.screen_height) * 0.7, 150, 40))
        self.label_9.setStyleSheet(_fromUtf8("font: 18pt \"微软雅黑\";\n"
                                             ""))
        self.layoutWidget_5.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.37, (self.task.screen_height) * 0.505, 700, 40))

        #self.layoutWidget_5.setGeometry(
          #  QtCore.QRect(self.task.screen_width * 0.37, (self.task.screen_height) * 0.705, 700, 40))

        #self.pushButton.setGeometry(
           # QtCore.QRect(self.task.screen_width * 0.45, (self.task.screen_height) * 0.8, 200, 80))
        self.pushButton.setGeometry(QtCore.QRect(self.task.screen_width * 0.45, (self.task.screen_height) * 0.5, 200, 80))



        self.brain = 0  # 脑力水平
        self.strength = 0  # 体力水平
        self.time = 0  # 时间
        self.achivement = 0  # 业绩
        self.effort = 0  # 努力
        self.disappoint = 0  # 受挫

    #设置高低好差标识
    def setTags(self):
        # 设置高低好差，标识
        self.label_s_1 = QtGui.QLabel(self)
        self.label_s_2 = QtGui.QLabel(self)
        self.label_s_3 = QtGui.QLabel(self)
        self.label_s_4 = QtGui.QLabel(self)
        self.label_s_5 = QtGui.QLabel(self)
        self.label_s_6 = QtGui.QLabel(self)
        self.label_s_7 = QtGui.QLabel(self)
        self.label_s_8 = QtGui.QLabel(self)
        self.label_s_9 = QtGui.QLabel(self)
        self.label_s_10 = QtGui.QLabel(self)
        self.label_s_11 = QtGui.QLabel(self)
        self.label_s_12 = QtGui.QLabel(self)
        # 脑力
        self.label_s_1.setText("低")
        self.label_s_2.setText("高")
        self.label_s_1.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.34, (self.task.screen_height) * 0.30, 40, 40))
        self.label_s_2.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.75, (self.task.screen_height) * 0.30, 40, 40))


        # 体力
        self.label_s_3.setText("低")
        self.label_s_4.setText("高")
        self.label_s_3.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.34, (self.task.screen_height) * 0.38, 40, 40))
        self.label_s_4.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.75, (self.task.screen_height) * 0.38, 40, 40))

        # 时间
        self.label_s_5.setText("低")
        self.label_s_6.setText("高")
        self.label_s_5.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.34, (self.task.screen_height) * 0.465, 40, 40))
        self.label_s_6.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.75, (self.task.screen_height) * 0.465, 40, 40))

        # 业绩
        self.label_s_7.setText("好")
        self.label_s_8.setText("差")
        self.label_s_7.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.34, (self.task.screen_height) * 0.54, 40, 40))
        self.label_s_8.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.75, (self.task.screen_height) * 0.54, 40, 40))

        # 努力
        self.label_s_9.setText("低")
        self.label_s_10.setText("高")
        self.label_s_9.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.34, (self.task.screen_height) * 0.62, 40, 40))
        self.label_s_10.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.75, (self.task.screen_height) * 0.62, 40, 40))

        # 受挫
        self.label_s_11.setText("低")
        self.label_s_12.setText("高")
        self.label_s_11.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.34, (self.task.screen_height) * 0.70, 40, 40))
        self.label_s_12.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.75, (self.task.screen_height) * 0.70, 40, 40))


        self.label_s_1.setStyleSheet(_fromUtf8("font: 14pt \"微软雅黑\";\n"
                                               ""))
        self.label_s_2.setStyleSheet(_fromUtf8("font: 14pt \"微软雅黑\";\n"
                                               ""))
        self.label_s_3.setStyleSheet(_fromUtf8("font: 14pt \"微软雅黑\";\n"
                                               ""))
        self.label_s_4.setStyleSheet(_fromUtf8("font: 14pt \"微软雅黑\";\n"
                                               ""))
        self.label_s_5.setStyleSheet(_fromUtf8("font: 14pt \"微软雅黑\";\n"
                                               ""))
        self.label_s_6.setStyleSheet(_fromUtf8("font: 14pt \"微软雅黑\";\n"
                                               ""))
        self.label_s_7.setStyleSheet(_fromUtf8("font: 14pt \"微软雅黑\";\n"
                                               ""))
        self.label_s_8.setStyleSheet(_fromUtf8("font: 14pt \"微软雅黑\";\n"
                                               ""))
        self.label_s_9.setStyleSheet(_fromUtf8("font: 14pt \"微软雅黑\";\n"
                                               ""))
        self.label_s_10.setStyleSheet(_fromUtf8("font: 14pt \"微软雅黑\";\n"
                                               ""))
        self.label_s_11.setStyleSheet(_fromUtf8("font: 14pt \"微软雅黑\";\n"
                                               ""))
        self.label_s_12.setStyleSheet(_fromUtf8("font: 14pt \"微软雅黑\";\n"
                                               ""))


    def Button_ui(self):
        self.radioButton_22 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton_22.setText(_fromUtf8(""))
        self.radioButton_22.setObjectName(_fromUtf8("radioButton_22"))
        self.horizontalLayout_2.addWidget(self.radioButton_22)
        self.radioButton_23 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton_23.setText(_fromUtf8(""))
        self.radioButton_23.setObjectName(_fromUtf8("radioButton_23"))
        self.horizontalLayout_2.addWidget(self.radioButton_23)
        self.radioButton_24 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton_24.setText(_fromUtf8(""))
        self.radioButton_24.setObjectName(_fromUtf8("radioButton_24"))
        self.horizontalLayout_2.addWidget(self.radioButton_24)
        self.radioButton_25 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton_25.setText(_fromUtf8(""))
        self.radioButton_25.setObjectName(_fromUtf8("radioButton_25"))
        self.horizontalLayout_2.addWidget(self.radioButton_25)
        self.radioButton_26 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton_26.setText(_fromUtf8(""))
        self.radioButton_26.setObjectName(_fromUtf8("radioButton_26"))
        self.horizontalLayout_2.addWidget(self.radioButton_26)
        self.radioButton_27 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton_27.setText(_fromUtf8(""))
        self.radioButton_27.setObjectName(_fromUtf8("radioButton_27"))
        self.horizontalLayout_2.addWidget(self.radioButton_27)
        self.radioButton_28 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton_28.setText(_fromUtf8(""))
        self.radioButton_28.setObjectName(_fromUtf8("radioButton_28"))
        self.horizontalLayout_2.addWidget(self.radioButton_28)
        self.radioButton_29 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton_29.setText(_fromUtf8(""))
        self.radioButton_29.setObjectName(_fromUtf8("radioButton_29"))
        self.horizontalLayout_2.addWidget(self.radioButton_29)
        self.radioButton_30 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton_30.setText(_fromUtf8(""))
        self.radioButton_30.setObjectName(_fromUtf8("radioButton_30"))
        self.horizontalLayout_2.addWidget(self.radioButton_30)
        self.radioButton_31 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton_31.setText(_fromUtf8(""))
        self.radioButton_31.setObjectName(_fromUtf8("radioButton_31"))
        self.horizontalLayout_2.addWidget(self.radioButton_31)
        self.radioButton_32 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton_32.setText(_fromUtf8(""))
        self.radioButton_32.setObjectName(_fromUtf8("radioButton_32"))
        self.horizontalLayout_2.addWidget(self.radioButton_32)
        self.radioButton_33 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton_33.setText(_fromUtf8(""))
        self.radioButton_33.setObjectName(_fromUtf8("radioButton_33"))
        self.horizontalLayout_2.addWidget(self.radioButton_33)
        self.radioButton_34 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton_34.setText(_fromUtf8(""))
        self.radioButton_34.setObjectName(_fromUtf8("radioButton_34"))
        self.horizontalLayout_2.addWidget(self.radioButton_34)
        self.radioButton_35 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton_35.setText(_fromUtf8(""))
        self.radioButton_35.setObjectName(_fromUtf8("radioButton_35"))
        self.horizontalLayout_2.addWidget(self.radioButton_35)
        self.radioButton_36 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton_36.setText(_fromUtf8(""))
        self.radioButton_36.setObjectName(_fromUtf8("radioButton_36"))
        self.horizontalLayout_2.addWidget(self.radioButton_36)
        self.radioButton_37 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton_37.setText(_fromUtf8(""))
        self.radioButton_37.setObjectName(_fromUtf8("radioButton_37"))
        self.horizontalLayout_2.addWidget(self.radioButton_37)
        self.radioButton_38 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton_38.setText(_fromUtf8(""))
        self.radioButton_38.setObjectName(_fromUtf8("radioButton_38"))
        self.horizontalLayout_2.addWidget(self.radioButton_38)
        self.radioButton_39 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton_39.setText(_fromUtf8(""))
        self.radioButton_39.setObjectName(_fromUtf8("radioButton_39"))
        self.horizontalLayout_2.addWidget(self.radioButton_39)
        self.radioButton_40 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton_40.setText(_fromUtf8(""))
        self.radioButton_40.setObjectName(_fromUtf8("radioButton_40"))
        self.horizontalLayout_2.addWidget(self.radioButton_40)
        self.radioButton_41 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton_41.setText(_fromUtf8(""))
        self.radioButton_41.setObjectName(_fromUtf8("radioButton_41"))
        self.horizontalLayout_2.addWidget(self.radioButton_41)
        self.radioButton_42 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton_42.setText(_fromUtf8(""))
        self.radioButton_42.setObjectName(_fromUtf8("radioButton_42"))
        self.horizontalLayout_2.addWidget(self.radioButton_42)
        self.layoutWidget_2 = QtGui.QWidget(self)
        self.layoutWidget_2.setGeometry(QtCore.QRect(70, 190, 611, 16))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.radioButton_43 = QtGui.QRadioButton(self.layoutWidget_2)
        self.radioButton_43.setText(_fromUtf8(""))
        self.radioButton_43.setObjectName(_fromUtf8("radioButton_43"))
        self.horizontalLayout_3.addWidget(self.radioButton_43)
        self.radioButton_44 = QtGui.QRadioButton(self.layoutWidget_2)
        self.radioButton_44.setText(_fromUtf8(""))
        self.radioButton_44.setObjectName(_fromUtf8("radioButton_44"))
        self.horizontalLayout_3.addWidget(self.radioButton_44)
        self.radioButton_45 = QtGui.QRadioButton(self.layoutWidget_2)
        self.radioButton_45.setText(_fromUtf8(""))
        self.radioButton_45.setObjectName(_fromUtf8("radioButton_45"))
        self.horizontalLayout_3.addWidget(self.radioButton_45)
        self.radioButton_46 = QtGui.QRadioButton(self.layoutWidget_2)
        self.radioButton_46.setText(_fromUtf8(""))
        self.radioButton_46.setObjectName(_fromUtf8("radioButton_46"))
        self.horizontalLayout_3.addWidget(self.radioButton_46)
        self.radioButton_47 = QtGui.QRadioButton(self.layoutWidget_2)
        self.radioButton_47.setText(_fromUtf8(""))
        self.radioButton_47.setObjectName(_fromUtf8("radioButton_47"))
        self.horizontalLayout_3.addWidget(self.radioButton_47)
        self.radioButton_48 = QtGui.QRadioButton(self.layoutWidget_2)
        self.radioButton_48.setText(_fromUtf8(""))
        self.radioButton_48.setObjectName(_fromUtf8("radioButton_48"))
        self.horizontalLayout_3.addWidget(self.radioButton_48)
        self.radioButton_49 = QtGui.QRadioButton(self.layoutWidget_2)
        self.radioButton_49.setText(_fromUtf8(""))
        self.radioButton_49.setObjectName(_fromUtf8("radioButton_49"))
        self.horizontalLayout_3.addWidget(self.radioButton_49)
        self.radioButton_50 = QtGui.QRadioButton(self.layoutWidget_2)
        self.radioButton_50.setText(_fromUtf8(""))
        self.radioButton_50.setObjectName(_fromUtf8("radioButton_50"))
        self.horizontalLayout_3.addWidget(self.radioButton_50)
        self.radioButton_51 = QtGui.QRadioButton(self.layoutWidget_2)
        self.radioButton_51.setText(_fromUtf8(""))
        self.radioButton_51.setObjectName(_fromUtf8("radioButton_51"))
        self.horizontalLayout_3.addWidget(self.radioButton_51)
        self.radioButton_52 = QtGui.QRadioButton(self.layoutWidget_2)
        self.radioButton_52.setText(_fromUtf8(""))
        self.radioButton_52.setObjectName(_fromUtf8("radioButton_52"))
        self.horizontalLayout_3.addWidget(self.radioButton_52)
        self.radioButton_53 = QtGui.QRadioButton(self.layoutWidget_2)
        self.radioButton_53.setText(_fromUtf8(""))
        self.radioButton_53.setObjectName(_fromUtf8("radioButton_53"))
        self.horizontalLayout_3.addWidget(self.radioButton_53)
        self.radioButton_54 = QtGui.QRadioButton(self.layoutWidget_2)
        self.radioButton_54.setText(_fromUtf8(""))
        self.radioButton_54.setObjectName(_fromUtf8("radioButton_54"))
        self.horizontalLayout_3.addWidget(self.radioButton_54)
        self.radioButton_55 = QtGui.QRadioButton(self.layoutWidget_2)
        self.radioButton_55.setText(_fromUtf8(""))
        self.radioButton_55.setObjectName(_fromUtf8("radioButton_55"))
        self.horizontalLayout_3.addWidget(self.radioButton_55)
        self.radioButton_56 = QtGui.QRadioButton(self.layoutWidget_2)
        self.radioButton_56.setText(_fromUtf8(""))
        self.radioButton_56.setObjectName(_fromUtf8("radioButton_56"))
        self.horizontalLayout_3.addWidget(self.radioButton_56)
        self.radioButton_57 = QtGui.QRadioButton(self.layoutWidget_2)
        self.radioButton_57.setText(_fromUtf8(""))
        self.radioButton_57.setObjectName(_fromUtf8("radioButton_57"))
        self.horizontalLayout_3.addWidget(self.radioButton_57)
        self.radioButton_58 = QtGui.QRadioButton(self.layoutWidget_2)
        self.radioButton_58.setText(_fromUtf8(""))
        self.radioButton_58.setObjectName(_fromUtf8("radioButton_58"))
        self.horizontalLayout_3.addWidget(self.radioButton_58)
        self.radioButton_59 = QtGui.QRadioButton(self.layoutWidget_2)
        self.radioButton_59.setText(_fromUtf8(""))
        self.radioButton_59.setObjectName(_fromUtf8("radioButton_59"))
        self.horizontalLayout_3.addWidget(self.radioButton_59)
        self.radioButton_60 = QtGui.QRadioButton(self.layoutWidget_2)
        self.radioButton_60.setText(_fromUtf8(""))
        self.radioButton_60.setObjectName(_fromUtf8("radioButton_60"))
        self.horizontalLayout_3.addWidget(self.radioButton_60)
        self.radioButton_61 = QtGui.QRadioButton(self.layoutWidget_2)
        self.radioButton_61.setText(_fromUtf8(""))
        self.radioButton_61.setObjectName(_fromUtf8("radioButton_61"))
        self.horizontalLayout_3.addWidget(self.radioButton_61)
        self.radioButton_62 = QtGui.QRadioButton(self.layoutWidget_2)
        self.radioButton_62.setText(_fromUtf8(""))
        self.radioButton_62.setObjectName(_fromUtf8("radioButton_62"))
        self.horizontalLayout_3.addWidget(self.radioButton_62)
        self.radioButton_63 = QtGui.QRadioButton(self.layoutWidget_2)
        self.radioButton_63.setText(_fromUtf8(""))
        self.radioButton_63.setObjectName(_fromUtf8("radioButton_63"))
        self.horizontalLayout_3.addWidget(self.radioButton_63)
        self.layoutWidget_3 = QtGui.QWidget(self)
        self.layoutWidget_3.setGeometry(QtCore.QRect(70, 240, 611, 16))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.radioButton_64 = QtGui.QRadioButton(self.layoutWidget_3)
        self.radioButton_64.setText(_fromUtf8(""))
        self.radioButton_64.setObjectName(_fromUtf8("radioButton_64"))
        self.horizontalLayout_4.addWidget(self.radioButton_64)
        self.radioButton_65 = QtGui.QRadioButton(self.layoutWidget_3)
        self.radioButton_65.setText(_fromUtf8(""))
        self.radioButton_65.setObjectName(_fromUtf8("radioButton_65"))
        self.horizontalLayout_4.addWidget(self.radioButton_65)
        self.radioButton_66 = QtGui.QRadioButton(self.layoutWidget_3)
        self.radioButton_66.setText(_fromUtf8(""))
        self.radioButton_66.setObjectName(_fromUtf8("radioButton_66"))
        self.horizontalLayout_4.addWidget(self.radioButton_66)
        self.radioButton_67 = QtGui.QRadioButton(self.layoutWidget_3)
        self.radioButton_67.setText(_fromUtf8(""))
        self.radioButton_67.setObjectName(_fromUtf8("radioButton_67"))
        self.horizontalLayout_4.addWidget(self.radioButton_67)
        self.radioButton_68 = QtGui.QRadioButton(self.layoutWidget_3)
        self.radioButton_68.setText(_fromUtf8(""))
        self.radioButton_68.setObjectName(_fromUtf8("radioButton_68"))
        self.horizontalLayout_4.addWidget(self.radioButton_68)
        self.radioButton_69 = QtGui.QRadioButton(self.layoutWidget_3)
        self.radioButton_69.setText(_fromUtf8(""))
        self.radioButton_69.setObjectName(_fromUtf8("radioButton_69"))
        self.horizontalLayout_4.addWidget(self.radioButton_69)
        self.radioButton_70 = QtGui.QRadioButton(self.layoutWidget_3)
        self.radioButton_70.setText(_fromUtf8(""))
        self.radioButton_70.setObjectName(_fromUtf8("radioButton_70"))
        self.horizontalLayout_4.addWidget(self.radioButton_70)
        self.radioButton_71 = QtGui.QRadioButton(self.layoutWidget_3)
        self.radioButton_71.setText(_fromUtf8(""))
        self.radioButton_71.setObjectName(_fromUtf8("radioButton_71"))
        self.horizontalLayout_4.addWidget(self.radioButton_71)
        self.radioButton_72 = QtGui.QRadioButton(self.layoutWidget_3)
        self.radioButton_72.setText(_fromUtf8(""))
        self.radioButton_72.setObjectName(_fromUtf8("radioButton_72"))
        self.horizontalLayout_4.addWidget(self.radioButton_72)
        self.radioButton_73 = QtGui.QRadioButton(self.layoutWidget_3)
        self.radioButton_73.setText(_fromUtf8(""))
        self.radioButton_73.setObjectName(_fromUtf8("radioButton_73"))
        self.horizontalLayout_4.addWidget(self.radioButton_73)
        self.radioButton_74 = QtGui.QRadioButton(self.layoutWidget_3)
        self.radioButton_74.setText(_fromUtf8(""))
        self.radioButton_74.setObjectName(_fromUtf8("radioButton_74"))
        self.horizontalLayout_4.addWidget(self.radioButton_74)
        self.radioButton_75 = QtGui.QRadioButton(self.layoutWidget_3)
        self.radioButton_75.setText(_fromUtf8(""))
        self.radioButton_75.setObjectName(_fromUtf8("radioButton_75"))
        self.horizontalLayout_4.addWidget(self.radioButton_75)
        self.radioButton_76 = QtGui.QRadioButton(self.layoutWidget_3)
        self.radioButton_76.setText(_fromUtf8(""))
        self.radioButton_76.setObjectName(_fromUtf8("radioButton_76"))
        self.horizontalLayout_4.addWidget(self.radioButton_76)
        self.radioButton_77 = QtGui.QRadioButton(self.layoutWidget_3)
        self.radioButton_77.setText(_fromUtf8(""))
        self.radioButton_77.setObjectName(_fromUtf8("radioButton_77"))
        self.horizontalLayout_4.addWidget(self.radioButton_77)
        self.radioButton_78 = QtGui.QRadioButton(self.layoutWidget_3)
        self.radioButton_78.setText(_fromUtf8(""))
        self.radioButton_78.setObjectName(_fromUtf8("radioButton_78"))
        self.horizontalLayout_4.addWidget(self.radioButton_78)
        self.radioButton_79 = QtGui.QRadioButton(self.layoutWidget_3)
        self.radioButton_79.setText(_fromUtf8(""))
        self.radioButton_79.setObjectName(_fromUtf8("radioButton_79"))
        self.horizontalLayout_4.addWidget(self.radioButton_79)
        self.radioButton_80 = QtGui.QRadioButton(self.layoutWidget_3)
        self.radioButton_80.setText(_fromUtf8(""))
        self.radioButton_80.setObjectName(_fromUtf8("radioButton_80"))
        self.horizontalLayout_4.addWidget(self.radioButton_80)
        self.radioButton_81 = QtGui.QRadioButton(self.layoutWidget_3)
        self.radioButton_81.setText(_fromUtf8(""))
        self.radioButton_81.setObjectName(_fromUtf8("radioButton_81"))
        self.horizontalLayout_4.addWidget(self.radioButton_81)
        self.radioButton_82 = QtGui.QRadioButton(self.layoutWidget_3)
        self.radioButton_82.setText(_fromUtf8(""))
        self.radioButton_82.setObjectName(_fromUtf8("radioButton_82"))
        self.horizontalLayout_4.addWidget(self.radioButton_82)
        self.radioButton_83 = QtGui.QRadioButton(self.layoutWidget_3)
        self.radioButton_83.setText(_fromUtf8(""))
        self.radioButton_83.setObjectName(_fromUtf8("radioButton_83"))
        self.horizontalLayout_4.addWidget(self.radioButton_83)
        self.radioButton_84 = QtGui.QRadioButton(self.layoutWidget_3)
        self.radioButton_84.setText(_fromUtf8(""))
        self.radioButton_84.setObjectName(_fromUtf8("radioButton_84"))
        self.horizontalLayout_4.addWidget(self.radioButton_84)
        self.layoutWidget_4 = QtGui.QWidget(self)
        self.layoutWidget_4.setGeometry(QtCore.QRect(70, 300, 611, 16))
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.radioButton_85 = QtGui.QRadioButton(self.layoutWidget_4)
        self.radioButton_85.setText(_fromUtf8(""))
        self.radioButton_85.setObjectName(_fromUtf8("radioButton_85"))
        self.horizontalLayout_5.addWidget(self.radioButton_85)
        self.radioButton_86 = QtGui.QRadioButton(self.layoutWidget_4)
        self.radioButton_86.setText(_fromUtf8(""))
        self.radioButton_86.setObjectName(_fromUtf8("radioButton_86"))
        self.horizontalLayout_5.addWidget(self.radioButton_86)
        self.radioButton_87 = QtGui.QRadioButton(self.layoutWidget_4)
        self.radioButton_87.setText(_fromUtf8(""))
        self.radioButton_87.setObjectName(_fromUtf8("radioButton_87"))
        self.horizontalLayout_5.addWidget(self.radioButton_87)
        self.radioButton_88 = QtGui.QRadioButton(self.layoutWidget_4)
        self.radioButton_88.setText(_fromUtf8(""))
        self.radioButton_88.setObjectName(_fromUtf8("radioButton_88"))
        self.horizontalLayout_5.addWidget(self.radioButton_88)
        self.radioButton_89 = QtGui.QRadioButton(self.layoutWidget_4)
        self.radioButton_89.setText(_fromUtf8(""))
        self.radioButton_89.setObjectName(_fromUtf8("radioButton_89"))
        self.horizontalLayout_5.addWidget(self.radioButton_89)
        self.radioButton_90 = QtGui.QRadioButton(self.layoutWidget_4)
        self.radioButton_90.setText(_fromUtf8(""))
        self.radioButton_90.setObjectName(_fromUtf8("radioButton_90"))
        self.horizontalLayout_5.addWidget(self.radioButton_90)
        self.radioButton_91 = QtGui.QRadioButton(self.layoutWidget_4)
        self.radioButton_91.setText(_fromUtf8(""))
        self.radioButton_91.setObjectName(_fromUtf8("radioButton_91"))
        self.horizontalLayout_5.addWidget(self.radioButton_91)
        self.radioButton_92 = QtGui.QRadioButton(self.layoutWidget_4)
        self.radioButton_92.setText(_fromUtf8(""))
        self.radioButton_92.setObjectName(_fromUtf8("radioButton_92"))
        self.horizontalLayout_5.addWidget(self.radioButton_92)
        self.radioButton_93 = QtGui.QRadioButton(self.layoutWidget_4)
        self.radioButton_93.setText(_fromUtf8(""))
        self.radioButton_93.setObjectName(_fromUtf8("radioButton_93"))
        self.horizontalLayout_5.addWidget(self.radioButton_93)
        self.radioButton_94 = QtGui.QRadioButton(self.layoutWidget_4)
        self.radioButton_94.setText(_fromUtf8(""))
        self.radioButton_94.setObjectName(_fromUtf8("radioButton_94"))
        self.horizontalLayout_5.addWidget(self.radioButton_94)
        self.radioButton_95 = QtGui.QRadioButton(self.layoutWidget_4)
        self.radioButton_95.setText(_fromUtf8(""))
        self.radioButton_95.setObjectName(_fromUtf8("radioButton_95"))
        self.horizontalLayout_5.addWidget(self.radioButton_95)
        self.radioButton_96 = QtGui.QRadioButton(self.layoutWidget_4)
        self.radioButton_96.setText(_fromUtf8(""))
        self.radioButton_96.setObjectName(_fromUtf8("radioButton_96"))
        self.horizontalLayout_5.addWidget(self.radioButton_96)
        self.radioButton_97 = QtGui.QRadioButton(self.layoutWidget_4)
        self.radioButton_97.setText(_fromUtf8(""))
        self.radioButton_97.setObjectName(_fromUtf8("radioButton_97"))
        self.horizontalLayout_5.addWidget(self.radioButton_97)
        self.radioButton_98 = QtGui.QRadioButton(self.layoutWidget_4)
        self.radioButton_98.setText(_fromUtf8(""))
        self.radioButton_98.setObjectName(_fromUtf8("radioButton_98"))
        self.horizontalLayout_5.addWidget(self.radioButton_98)
        self.radioButton_99 = QtGui.QRadioButton(self.layoutWidget_4)
        self.radioButton_99.setText(_fromUtf8(""))
        self.radioButton_99.setObjectName(_fromUtf8("radioButton_99"))
        self.horizontalLayout_5.addWidget(self.radioButton_99)
        self.radioButton_100 = QtGui.QRadioButton(self.layoutWidget_4)
        self.radioButton_100.setText(_fromUtf8(""))
        self.radioButton_100.setObjectName(_fromUtf8("radioButton_100"))
        self.horizontalLayout_5.addWidget(self.radioButton_100)
        self.radioButton_101 = QtGui.QRadioButton(self.layoutWidget_4)
        self.radioButton_101.setText(_fromUtf8(""))
        self.radioButton_101.setObjectName(_fromUtf8("radioButton_101"))
        self.horizontalLayout_5.addWidget(self.radioButton_101)
        self.radioButton_102 = QtGui.QRadioButton(self.layoutWidget_4)
        self.radioButton_102.setText(_fromUtf8(""))
        self.radioButton_102.setObjectName(_fromUtf8("radioButton_102"))
        self.horizontalLayout_5.addWidget(self.radioButton_102)
        self.radioButton_103 = QtGui.QRadioButton(self.layoutWidget_4)
        self.radioButton_103.setText(_fromUtf8(""))
        self.radioButton_103.setObjectName(_fromUtf8("radioButton_103"))
        self.horizontalLayout_5.addWidget(self.radioButton_103)
        self.radioButton_104 = QtGui.QRadioButton(self.layoutWidget_4)
        self.radioButton_104.setText(_fromUtf8(""))
        self.radioButton_104.setObjectName(_fromUtf8("radioButton_104"))
        self.horizontalLayout_5.addWidget(self.radioButton_104)
        self.radioButton_105 = QtGui.QRadioButton(self.layoutWidget_4)
        self.radioButton_105.setText(_fromUtf8(""))
        self.radioButton_105.setObjectName(_fromUtf8("radioButton_105"))
        self.horizontalLayout_5.addWidget(self.radioButton_105)
        self.layoutWidget_5 = QtGui.QWidget(self)
        self.layoutWidget_5.setGeometry(QtCore.QRect(70, 340, 611, 16))

        self.layoutWidget_5.setObjectName(_fromUtf8("layoutWidget_5"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.radioButton_106 = QtGui.QRadioButton(self.layoutWidget_5)
        self.radioButton_106.setText(_fromUtf8(""))
        self.radioButton_106.setObjectName(_fromUtf8("radioButton_106"))
        self.horizontalLayout_6.addWidget(self.radioButton_106)
        self.radioButton_107 = QtGui.QRadioButton(self.layoutWidget_5)
        self.radioButton_107.setText(_fromUtf8(""))
        self.radioButton_107.setObjectName(_fromUtf8("radioButton_107"))
        self.horizontalLayout_6.addWidget(self.radioButton_107)
        self.radioButton_108 = QtGui.QRadioButton(self.layoutWidget_5)
        self.radioButton_108.setText(_fromUtf8(""))
        self.radioButton_108.setObjectName(_fromUtf8("radioButton_108"))
        self.horizontalLayout_6.addWidget(self.radioButton_108)
        self.radioButton_109 = QtGui.QRadioButton(self.layoutWidget_5)
        self.radioButton_109.setText(_fromUtf8(""))
        self.radioButton_109.setObjectName(_fromUtf8("radioButton_109"))
        self.horizontalLayout_6.addWidget(self.radioButton_109)
        self.radioButton_110 = QtGui.QRadioButton(self.layoutWidget_5)
        self.radioButton_110.setText(_fromUtf8(""))
        self.radioButton_110.setObjectName(_fromUtf8("radioButton_110"))
        self.horizontalLayout_6.addWidget(self.radioButton_110)
        self.radioButton_111 = QtGui.QRadioButton(self.layoutWidget_5)
        self.radioButton_111.setText(_fromUtf8(""))
        self.radioButton_111.setObjectName(_fromUtf8("radioButton_111"))
        self.horizontalLayout_6.addWidget(self.radioButton_111)
        self.radioButton_112 = QtGui.QRadioButton(self.layoutWidget_5)
        self.radioButton_112.setText(_fromUtf8(""))
        self.radioButton_112.setObjectName(_fromUtf8("radioButton_112"))
        self.horizontalLayout_6.addWidget(self.radioButton_112)
        self.radioButton_113 = QtGui.QRadioButton(self.layoutWidget_5)
        self.radioButton_113.setText(_fromUtf8(""))
        self.radioButton_113.setObjectName(_fromUtf8("radioButton_113"))
        self.horizontalLayout_6.addWidget(self.radioButton_113)
        self.radioButton_114 = QtGui.QRadioButton(self.layoutWidget_5)
        self.radioButton_114.setText(_fromUtf8(""))
        self.radioButton_114.setObjectName(_fromUtf8("radioButton_114"))
        self.horizontalLayout_6.addWidget(self.radioButton_114)
        self.radioButton_115 = QtGui.QRadioButton(self.layoutWidget_5)
        self.radioButton_115.setText(_fromUtf8(""))
        self.radioButton_115.setObjectName(_fromUtf8("radioButton_115"))
        self.horizontalLayout_6.addWidget(self.radioButton_115)
        self.radioButton_116 = QtGui.QRadioButton(self.layoutWidget_5)
        self.radioButton_116.setText(_fromUtf8(""))
        self.radioButton_116.setObjectName(_fromUtf8("radioButton_116"))
        self.horizontalLayout_6.addWidget(self.radioButton_116)
        self.radioButton_117 = QtGui.QRadioButton(self.layoutWidget_5)
        self.radioButton_117.setText(_fromUtf8(""))
        self.radioButton_117.setObjectName(_fromUtf8("radioButton_117"))
        self.horizontalLayout_6.addWidget(self.radioButton_117)
        self.radioButton_118 = QtGui.QRadioButton(self.layoutWidget_5)
        self.radioButton_118.setText(_fromUtf8(""))
        self.radioButton_118.setObjectName(_fromUtf8("radioButton_118"))
        self.horizontalLayout_6.addWidget(self.radioButton_118)
        self.radioButton_119 = QtGui.QRadioButton(self.layoutWidget_5)
        self.radioButton_119.setText(_fromUtf8(""))
        self.radioButton_119.setObjectName(_fromUtf8("radioButton_119"))
        self.horizontalLayout_6.addWidget(self.radioButton_119)
        self.radioButton_120 = QtGui.QRadioButton(self.layoutWidget_5)
        self.radioButton_120.setText(_fromUtf8(""))
        self.radioButton_120.setObjectName(_fromUtf8("radioButton_120"))
        self.horizontalLayout_6.addWidget(self.radioButton_120)
        self.radioButton_121 = QtGui.QRadioButton(self.layoutWidget_5)
        self.radioButton_121.setText(_fromUtf8(""))
        self.radioButton_121.setObjectName(_fromUtf8("radioButton_121"))
        self.horizontalLayout_6.addWidget(self.radioButton_121)
        self.radioButton_122 = QtGui.QRadioButton(self.layoutWidget_5)
        self.radioButton_122.setText(_fromUtf8(""))
        self.radioButton_122.setObjectName(_fromUtf8("radioButton_122"))
        self.horizontalLayout_6.addWidget(self.radioButton_122)
        self.radioButton_123 = QtGui.QRadioButton(self.layoutWidget_5)
        self.radioButton_123.setText(_fromUtf8(""))
        self.radioButton_123.setObjectName(_fromUtf8("radioButton_123"))
        self.horizontalLayout_6.addWidget(self.radioButton_123)
        self.radioButton_124 = QtGui.QRadioButton(self.layoutWidget_5)
        self.radioButton_124.setText(_fromUtf8(""))
        self.radioButton_124.setObjectName(_fromUtf8("radioButton_124"))
        self.horizontalLayout_6.addWidget(self.radioButton_124)
        self.radioButton_125 = QtGui.QRadioButton(self.layoutWidget_5)
        self.radioButton_125.setText(_fromUtf8(""))
        self.radioButton_125.setObjectName(_fromUtf8("radioButton_125"))
        self.horizontalLayout_6.addWidget(self.radioButton_125)
        self.radioButton_126 = QtGui.QRadioButton(self.layoutWidget_5)
        self.radioButton_126.setText(_fromUtf8(""))
        self.radioButton_126.setObjectName(_fromUtf8("radioButton_126"))
        self.horizontalLayout_6.addWidget(self.radioButton_126)
        self.widget = QtGui.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(71, 90, 611, 16))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        self.radioButton_1 = QtGui.QRadioButton(self.widget)
        self.radioButton_1.setText(_fromUtf8(""))
        self.radioButton_1.setObjectName(_fromUtf8("radioButton_1"))
        self.horizontalLayout.addWidget(self.radioButton_1)

        self.radioButton_2 = QtGui.QRadioButton(self.widget)
        self.radioButton_2.setText(_fromUtf8(""))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtGui.QRadioButton(self.widget)
        self.radioButton_3.setText(_fromUtf8(""))
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.horizontalLayout.addWidget(self.radioButton_3)
        self.radioButton_4 = QtGui.QRadioButton(self.widget)
        self.radioButton_4.setText(_fromUtf8(""))
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.horizontalLayout.addWidget(self.radioButton_4)

        self.radioButton_5 = QtGui.QRadioButton(self.widget)
        self.radioButton_5.setText(_fromUtf8(""))
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        self.horizontalLayout.addWidget(self.radioButton_5)

        self.radioButton_6 = QtGui.QRadioButton(self.widget)
        self.radioButton_6.setText(_fromUtf8(""))
        self.radioButton_6.setObjectName(_fromUtf8("radioButton_6"))
        self.horizontalLayout.addWidget(self.radioButton_6)

        self.radioButton_7 = QtGui.QRadioButton(self.widget)
        self.radioButton_7.setText(_fromUtf8(""))
        self.radioButton_7.setObjectName(_fromUtf8("radioButton_7"))
        self.horizontalLayout.addWidget(self.radioButton_7)
        self.radioButton_8 = QtGui.QRadioButton(self.widget)
        self.radioButton_8.setText(_fromUtf8(""))
        self.radioButton_8.setObjectName(_fromUtf8("radioButton_8"))
        self.horizontalLayout.addWidget(self.radioButton_8)
        self.radioButton_9 = QtGui.QRadioButton(self.widget)
        self.radioButton_9.setText(_fromUtf8(""))
        self.radioButton_9.setObjectName(_fromUtf8("radioButton_9"))
        self.horizontalLayout.addWidget(self.radioButton_9)
        self.radioButton_10 = QtGui.QRadioButton(self.widget)
        self.radioButton_10.setText(_fromUtf8(""))
        self.radioButton_10.setObjectName(_fromUtf8("radioButton_10"))
        self.horizontalLayout.addWidget(self.radioButton_10)
        self.radioButton_11 = QtGui.QRadioButton(self.widget)
        self.radioButton_11.setText(_fromUtf8(""))
        self.radioButton_11.setObjectName(_fromUtf8("radioButton_11"))
        self.horizontalLayout.addWidget(self.radioButton_11)
        self.radioButton_12 = QtGui.QRadioButton(self.widget)
        self.radioButton_12.setText(_fromUtf8(""))
        self.radioButton_12.setObjectName(_fromUtf8("radioButton_12"))
        self.horizontalLayout.addWidget(self.radioButton_12)
        self.radioButton_13 = QtGui.QRadioButton(self.widget)
        self.radioButton_13.setText(_fromUtf8(""))
        self.radioButton_13.setObjectName(_fromUtf8("radioButton_13"))
        self.horizontalLayout.addWidget(self.radioButton_13)
        self.radioButton_14 = QtGui.QRadioButton(self.widget)
        self.radioButton_14.setText(_fromUtf8(""))
        self.radioButton_14.setObjectName(_fromUtf8("radioButton_14"))
        self.horizontalLayout.addWidget(self.radioButton_14)
        self.radioButton_15 = QtGui.QRadioButton(self.widget)
        self.radioButton_15.setText(_fromUtf8(""))
        self.radioButton_15.setObjectName(_fromUtf8("radioButton_15"))
        self.horizontalLayout.addWidget(self.radioButton_15)
        self.radioButton_16 = QtGui.QRadioButton(self.widget)
        self.radioButton_16.setText(_fromUtf8(""))
        self.radioButton_16.setObjectName(_fromUtf8("radioButton_16"))
        self.horizontalLayout.addWidget(self.radioButton_16)
        self.radioButton_17 = QtGui.QRadioButton(self.widget)
        self.radioButton_17.setText(_fromUtf8(""))
        self.radioButton_17.setObjectName(_fromUtf8("radioButton_17"))
        self.horizontalLayout.addWidget(self.radioButton_17)
        self.radioButton_18 = QtGui.QRadioButton(self.widget)
        self.radioButton_18.setText(_fromUtf8(""))
        self.radioButton_18.setObjectName(_fromUtf8("radioButton_18"))
        self.horizontalLayout.addWidget(self.radioButton_18)
        self.radioButton_19 = QtGui.QRadioButton(self.widget)
        self.radioButton_19.setText(_fromUtf8(""))
        self.radioButton_19.setObjectName(_fromUtf8("radioButton_19"))
        self.horizontalLayout.addWidget(self.radioButton_19)
        self.radioButton_20 = QtGui.QRadioButton(self.widget)
        self.radioButton_20.setText(_fromUtf8(""))
        self.radioButton_20.setObjectName(_fromUtf8("radioButton_20"))
        self.horizontalLayout.addWidget(self.radioButton_20)
        self.radioButton_21 = QtGui.QRadioButton(self.widget)
        self.radioButton_21.setText(_fromUtf8(""))
        self.radioButton_21.setObjectName(_fromUtf8("radioButton_21"))
        self.horizontalLayout.addWidget(self.radioButton_21)



    def on_pushButton_clicked(self):

        tag=self .checkButton()

        if(tag==True ):


            self.setScore()                     #获取分数

            self.task.times = self.task.times + 1

            print  self.task.times
            print "practiceerrordic"
            print self.task.practiceErrorDic
            print "practicetimedic"
            print self.task.practiceTimeDic
            print "formalerrordic"
            print self.task.formalErrorDic
            print "formaltimedic"
            print self.task.formalTimeDic


            self.ui1.setTask(self.task)

            self.ui1.initUi()

            self.ui2.setTask(self.task)

            self.close()

            self.ui.showFullScreen()

            self.ui.startCount()



            QTimer.singleShot(15000, self.ui.close)  # 设置15s后自动退出




            if(self.task .times <=9):               #如果9种任务类型都选过了，那么跳到最后的界面，否则，继续循环
                                       # 传递任务对象
                QTimer.singleShot(15000, self.ui1.showFullScreen)  # 设置15s后自动显示
            else:
                                        # 传递任务对象
                QTimer.singleShot(15000, self.ui2.showFullScreen)  # 设置15s后自动显示




    #根据不同按钮，来设定分数，并将分数加入到相应的任务类型
    def setScore(self):
        score = 0
        if(self .radioButton_1.isChecked() ):        #脑力
            self.brain = 0
        elif (self.radioButton_2.isChecked()):
            self.brain = 1 *5
        elif (self.radioButton_3.isChecked()):
            self.brain = 2*5
        elif (self.radioButton_4.isChecked()):
            self.brain = 3*5
        elif (self.radioButton_5.isChecked()):
            self.brain = 4*5
        elif (self.radioButton_6.isChecked()):
            self.brain = 5*5
        elif (self.radioButton_7.isChecked()):
            self.brain = 6*5
        elif (self.radioButton_8.isChecked()):
            self.brain = 7*5
        elif (self.radioButton_9.isChecked()):
            self.brain = 8*5
        elif (self.radioButton_10.isChecked()):
            self.brain = 9*5

        elif (self.radioButton_11.isChecked()):
            self.brain = 10*5
        elif (self.radioButton_12.isChecked()):
            self.brain = 11*5
        elif (self.radioButton_13.isChecked()):
            self.brain = 12*5
        elif (self.radioButton_14.isChecked()):
            self.brain = 13*5
        elif (self.radioButton_15.isChecked()):
            self.brain = 14*5
        elif (self.radioButton_16.isChecked()):
            self.brain = 15*5
        elif (self.radioButton_17.isChecked()):
            self.brain = 16*5
        elif (self.radioButton_18.isChecked()):
            self.brain = 17*5
        elif (self.radioButton_19.isChecked()):
            self.brain = 18*5
        elif (self.radioButton_20.isChecked()):
            self.brain = 19*5
        elif (self.radioButton_21.isChecked()):
            self.brain = 20*5

        if (self.radioButton_22.isChecked()):  # 体力
            self.strength = 0
        elif (self.radioButton_23.isChecked()):
            self.strength = 1 * 5
        elif (self.radioButton_24.isChecked()):
            self.strength = 2 * 5
        elif (self.radioButton_25.isChecked()):
            self.strength = 3 * 5
        elif (self.radioButton_26.isChecked()):
            self.strength = 4 * 5
        elif (self.radioButton_27.isChecked()):
            self.strength = 5 * 5
        elif (self.radioButton_28.isChecked()):
            self.strength = 6 * 5
        elif (self.radioButton_29.isChecked()):
            self.strength = 7 * 5
        elif (self.radioButton_30.isChecked()):
            self.strength = 8 * 5
        elif (self.radioButton_31.isChecked()):
            self.strength = 9 * 5

        elif (self.radioButton_32.isChecked()):
            self.strength = 10 * 5
        elif (self.radioButton_33.isChecked()):
            self.strength = 11 * 5
        elif (self.radioButton_34.isChecked()):
            self.strength = 12 * 5
        elif (self.radioButton_35.isChecked()):
            self.strength = 13 * 5
        elif (self.radioButton_36.isChecked()):
            self.strength = 14 * 5
        elif (self.radioButton_37.isChecked()):
            self.strength = 15 * 5
        elif (self.radioButton_38.isChecked()):
            self.strength = 16 * 5
        elif (self.radioButton_39.isChecked()):
            self.strength = 17 * 5
        elif (self.radioButton_40.isChecked()):
            self.strength = 18 * 5
        elif (self.radioButton_41.isChecked()):
            self.strength = 19 * 5
        elif (self.radioButton_42.isChecked()):
            self.strength = 20 * 5

        if (self.radioButton_43.isChecked()):  # 时间
            self.time = 0
        elif (self.radioButton_44.isChecked()):
            self.time = 1 * 5
        elif (self.radioButton_45.isChecked()):
            self.time = 2 * 5
        elif (self.radioButton_46.isChecked()):
            self.time = 3 * 5
        elif (self.radioButton_47.isChecked()):
            self.time = 4 * 5
        elif (self.radioButton_48.isChecked()):
            self.time = 5 * 5
        elif (self.radioButton_49.isChecked()):
            self.time = 6 * 5
        elif (self.radioButton_50.isChecked()):
            self.time = 7 * 5
        elif (self.radioButton_51.isChecked()):
            self.time = 8 * 5
        elif (self.radioButton_52.isChecked()):
            self.time = 9 * 5

        elif (self.radioButton_53.isChecked()):
            self.time = 10 * 5
        elif (self.radioButton_54.isChecked()):
            self.time = 11 * 5
        elif (self.radioButton_55.isChecked()):
            self.time = 12 * 5
        elif (self.radioButton_56.isChecked()):
            self.time = 13 * 5
        elif (self.radioButton_57.isChecked()):
            self.time = 14 * 5
        elif (self.radioButton_58.isChecked()):
            self.time = 15 * 5
        elif (self.radioButton_59.isChecked()):
            self.time = 16 * 5
        elif (self.radioButton_60.isChecked()):
            self.time = 17 * 5
        elif (self.radioButton_61.isChecked()):
            self.time = 18 * 5
        elif (self.radioButton_62.isChecked()):
            self.time = 19 * 5
        elif (self.radioButton_63.isChecked()):
            self.time = 20 * 5

        if (self.radioButton_64.isChecked()):  # 业绩
            self.achivement = 0
        elif (self.radioButton_65.isChecked()):
            self.achivement = 1* 5
        elif (self.radioButton_66.isChecked()):
            self.achivement = 2 * 5
        elif (self.radioButton_67.isChecked()):
            self.achivement = 3 * 5
        elif (self.radioButton_68.isChecked()):
            self.achivement = 4 * 5
        elif (self.radioButton_69.isChecked()):
            self.achivement = 5 * 5
        elif (self.radioButton_70.isChecked()):
            self.achivement = 6 * 5
        elif (self.radioButton_71.isChecked()):
            self.achivement = 7 * 5
        elif (self.radioButton_72.isChecked()):
            self.achivement = 8 * 5
        elif (self.radioButton_73.isChecked()):
            self.achivement = 9 * 5

        elif (self.radioButton_74.isChecked()):
            self.achivement = 10 * 5
        elif (self.radioButton_75.isChecked()):
            self.achivement = 11 * 5
        elif (self.radioButton_76.isChecked()):
            self.achivement = 12 * 5
        elif (self.radioButton_77.isChecked()):
            self.achivement = 13 * 5
        elif (self.radioButton_78.isChecked()):
            self.achivement = 14 * 5
        elif (self.radioButton_79.isChecked()):
            self.achivement = 15 * 5
        elif (self.radioButton_80.isChecked()):
            self.achivement = 16 * 5
        elif (self.radioButton_81.isChecked()):
            self.achivement = 17 * 5
        elif (self.radioButton_82.isChecked()):
            self.achivement = 18 * 5
        elif (self.radioButton_83.isChecked()):
            self.achivement = 19 * 5
        elif (self.radioButton_84.isChecked()):
            self.achivement = 20*5

        if (self.radioButton_85.isChecked()):  # 努力
            self.effort = 0
        elif (self.radioButton_86.isChecked()):
            self.effort = 1 * 5
        elif (self.radioButton_87.isChecked()):
            self.effort = 2 * 5
        elif (self.radioButton_88.isChecked()):
            self.effort = 3 * 5
        elif (self.radioButton_89.isChecked()):
            self.effort = 4 * 5
        elif (self.radioButton_90.isChecked()):
            self.effort = 5 * 5
        elif (self.radioButton_91.isChecked()):
            self.effort = 6 * 5
        elif (self.radioButton_92.isChecked()):
            self.effort = 7 * 5
        elif (self.radioButton_93.isChecked()):
            self.effort = 8 * 5
        elif (self.radioButton_94.isChecked()):
            self.effort = 9 * 5

        elif (self.radioButton_95.isChecked()):
            self.effort = 10 * 5
        elif (self.radioButton_96.isChecked()):
            self.effort = 11 * 5
        elif (self.radioButton_97.isChecked()):
            self.effort = 12 * 5
        elif (self.radioButton_98.isChecked()):
            self.effort = 13 * 5
        elif (self.radioButton_99.isChecked()):
            self.effort = 14 * 5
        elif (self.radioButton_100.isChecked()):
            self.effort = 15 * 5
        elif (self.radioButton_101.isChecked()):
            self.effort = 16 * 5
        elif (self.radioButton_102.isChecked()):
            self.effort = 17 * 5
        elif (self.radioButton_103.isChecked()):
            self.effort = 18 * 5
        elif (self.radioButton_104.isChecked()):
            self.effort = 19 * 5
        elif (self.radioButton_105.isChecked()):
            self.effort = 20 * 5


        if (self.radioButton_106.isChecked()):  # 受挫
            self.disappoint = 0
        elif (self.radioButton_107.isChecked()):
            self.disappoint = 1 * 5
        elif (self.radioButton_108.isChecked()):
            self.disappoint = 2 * 5
        elif (self.radioButton_109.isChecked()):
            self.disappoint = 3 * 5
        elif (self.radioButton_110.isChecked()):
            self.disappoint = 4 * 5
        elif (self.radioButton_111.isChecked()):
            self.disappoint = 5 * 5
        elif (self.radioButton_112.isChecked()):
            self.disappoint = 6 * 5
        elif (self.radioButton_113.isChecked()):
            self.disappoint = 7 * 5
        elif (self.radioButton_114.isChecked()):
            self.disappoint = 8 * 5
        elif (self.radioButton_115.isChecked()):
            self.disappoint = 9 * 5

        elif (self.radioButton_116.isChecked()):
            self.disappoint = 10 * 5
        elif (self.radioButton_117.isChecked()):
            self.disappoint = 11 * 5
        elif (self.radioButton_118.isChecked()):
            self.disappoint = 12 * 5
        elif (self.radioButton_119.isChecked()):
            self.disappoint = 13 * 5
        elif (self.radioButton_120.isChecked()):
            self.disappoint = 14 * 5
        elif (self.radioButton_121.isChecked()):
            self.disappoint = 15 * 5
        elif (self.radioButton_122.isChecked()):
            self.disappoint = 16 * 5
        elif (self.radioButton_123.isChecked()):
            self.disappoint = 17 * 5
        elif (self.radioButton_124.isChecked()):
            self.disappoint = 18 * 5
        elif (self.radioButton_125.isChecked()):
            self.disappoint = 19 * 5
        elif (self.radioButton_126.isChecked()):
            self.disappoint = 20 * 5



        #判断任务类型，并将相应分数加入
        if(self.task.taskType=="10_1"):
            self.task.scoreDic ["10_1"].append(self.brain)
            self.task.scoreDic["10_1"].append(self .strength)
            self.task.scoreDic["10_1"].append(self.time )
            self.task.scoreDic["10_1"].append(self.achivement )
            self.task.scoreDic["10_1"].append(self.effort )
            self.task.scoreDic["10_1"].append(self.disappoint )

        elif (self.task.taskType == "10_2"):
            self.task.scoreDic["10_2"].append(self.brain)
            self.task.scoreDic["10_2"].append(self.strength)
            self.task.scoreDic["10_2"].append(self.time)
            self.task.scoreDic["10_2"].append(self.achivement)
            self.task.scoreDic["10_2"].append(self.effort)
            self.task.scoreDic["10_2"].append(self.disappoint)

        elif (self.task.taskType == "10_3"):
            self.task.scoreDic["10_3"].append(self.brain)
            self.task.scoreDic["10_3"].append(self.strength)
            self.task.scoreDic["10_3"].append(self.time)
            self.task.scoreDic["10_3"].append(self.achivement)
            self.task.scoreDic["10_3"].append(self.effort)
            self.task.scoreDic["10_3"].append(self.disappoint)


        elif (self.task.taskType == "15_1"):
            self.task.scoreDic["15_1"].append(self.brain)
            self.task.scoreDic["15_1"].append(self.strength)
            self.task.scoreDic["15_1"].append(self.time)
            self.task.scoreDic["15_1"].append(self.achivement)
            self.task.scoreDic["15_1"].append(self.effort)
            self.task.scoreDic["15_1"].append(self.disappoint)

        elif (self.task.taskType == "15_2"):
            self.task.scoreDic["15_2"].append(self.brain)
            self.task.scoreDic["15_2"].append(self.strength)
            self.task.scoreDic["15_2"].append(self.time)
            self.task.scoreDic["15_2"].append(self.achivement)
            self.task.scoreDic["15_2"].append(self.effort)
            self.task.scoreDic["15_2"].append(self.disappoint)

        elif (self.task.taskType == "15_3"):
            self.task.scoreDic["15_3"].append(self.brain)
            self.task.scoreDic["15_3"].append(self.strength)
            self.task.scoreDic["15_3"].append(self.time)
            self.task.scoreDic["15_3"].append(self.achivement)
            self.task.scoreDic["15_3"].append(self.effort)
            self.task.scoreDic["15_3"].append(self.disappoint)


        elif (self.task.taskType == "20_1"):
            self.task.scoreDic["20_1"].append(self.brain)
            self.task.scoreDic["20_1"].append(self.strength)
            self.task.scoreDic["20_1"].append(self.time)
            self.task.scoreDic["20_1"].append(self.achivement)
            self.task.scoreDic["20_1"].append(self.effort)
            self.task.scoreDic["20_1"].append(self.disappoint)

        elif (self.task.taskType == "20_2"):
            self.task.scoreDic["20_2"].append(self.brain)
            self.task.scoreDic["20_2"].append(self.strength)
            self.task.scoreDic["20_2"].append(self.time)
            self.task.scoreDic["20_2"].append(self.achivement)
            self.task.scoreDic["20_2"].append(self.effort)
            self.task.scoreDic["20_2"].append(self.disappoint)

        elif (self.task.taskType == "20_3"):
            self.task.scoreDic["20_3"].append(self.brain)
            self.task.scoreDic["20_3"].append(self.strength)
            self.task.scoreDic["20_3"].append(self.time)
            self.task.scoreDic["20_3"].append(self.achivement)
            self.task.scoreDic["20_3"].append(self.effort)
            self.task.scoreDic["20_3"].append(self.disappoint)


    #检查是否各类按钮已选中
    def checkButton(self):

        if(self.radioButton_1.isChecked() or self.radioButton_2.isChecked()or self.radioButton_3.isChecked()or self.radioButton_4.isChecked() or self.radioButton_5.isChecked()
           or self.radioButton_6.isChecked() or self.radioButton_7.isChecked()or self.radioButton_8.isChecked()or self.radioButton_9.isChecked() or self.radioButton_10.isChecked()
             or self.radioButton_11.isChecked() or self.radioButton_12.isChecked()or self.radioButton_13.isChecked()or self.radioButton_14.isChecked()or self.radioButton_15.isChecked()
                or self.radioButton_16.isChecked() or self.radioButton_17.isChecked() or self.radioButton_18.isChecked() or self.radioButton_11.isChecked() or self.radioButton_19.isChecked()
                    or self.radioButton_20.isChecked()or self.radioButton_21.isChecked()):
            if (self.radioButton_22.isChecked() or self.radioButton_23.isChecked() or self.radioButton_24.isChecked() or self.radioButton_25.isChecked() or self.radioButton_26.isChecked()
                or self.radioButton_27.isChecked() or self.radioButton_28.isChecked() or self.radioButton_29.isChecked() or self.radioButton_30.isChecked() or self.radioButton_31.isChecked()
                 or self.radioButton_32.isChecked() or self.radioButton_33.isChecked() or self.radioButton_34.isChecked()or self.radioButton_35.isChecked() or self.radioButton_36.isChecked()
                  or self.radioButton_37.isChecked() or self.radioButton_38.isChecked() or self.radioButton_39.isChecked()or self.radioButton_40.isChecked() or self.radioButton_41.isChecked()or self.radioButton_42.isChecked()):
                if (self.radioButton_43.isChecked() or self.radioButton_44.isChecked() or self.radioButton_45.isChecked() or self.radioButton_46.isChecked() or self.radioButton_47.isChecked()
                    or self.radioButton_48.isChecked() or self.radioButton_49.isChecked() or self.radioButton_50.isChecked() or self.radioButton_51.isChecked() or self.radioButton_52.isChecked()
                    or self.radioButton_53.isChecked() or self.radioButton_54.isChecked() or self.radioButton_55.isChecked() or self.radioButton_56.isChecked() or self.radioButton_57.isChecked() or self.radioButton_58.isChecked()
                    or self.radioButton_59.isChecked() or self.radioButton_60.isChecked() or self.radioButton_61.isChecked() or self.radioButton_62.isChecked() or self.radioButton_63.isChecked() or self.radioButton_64.isChecked()):
                    if (self.radioButton_64.isChecked() or self.radioButton_65.isChecked() or self.radioButton_66.isChecked() or self.radioButton_67.isChecked() or self.radioButton_68.isChecked()or self.radioButton_69.isChecked()
                        or self.radioButton_70.isChecked() or self.radioButton_71.isChecked() or self.radioButton_72.isChecked() or self.radioButton_73.isChecked() or self.radioButton_74.isChecked()or self.radioButton_75.isChecked()
                         or self.radioButton_76.isChecked() or self.radioButton_77.isChecked()or self.radioButton_78.isChecked()or self.radioButton_79.isChecked()or self.radioButton_80.isChecked()or self.radioButton_81.isChecked()
                          or self.radioButton_81.isChecked() or self.radioButton_82.isChecked()or self.radioButton_83.isChecked()or self.radioButton_84.isChecked()):
                        if (self.radioButton_85.isChecked() or self.radioButton_86.isChecked() or self.radioButton_87.isChecked() or self.radioButton_88.isChecked() or self.radioButton_89.isChecked()
                            or self.radioButton_90.isChecked() or self.radioButton_91.isChecked() or self.radioButton_92.isChecked() or self.radioButton_93.isChecked() or self.radioButton_94.isChecked()
                            or self.radioButton_95.isChecked() or self.radioButton_96.isChecked()or self.radioButton_97.isChecked() or self.radioButton_98.isChecked()or self.radioButton_99.isChecked() or self.radioButton_100.isChecked()
                            or self.radioButton_101.isChecked() or self.radioButton_102.isChecked()or self.radioButton_103.isChecked() or self.radioButton_104.isChecked()or self.radioButton_105.isChecked() ):
                            if (self.radioButton_106.isChecked() or self.radioButton_107.isChecked() or self.radioButton_108.isChecked() or self.radioButton_109.isChecked() or self.radioButton_110.isChecked()
                                or self.radioButton_111.isChecked() or self.radioButton_112.isChecked() or self.radioButton_113.isChecked() or self.radioButton_114.isChecked() or self.radioButton_115.isChecked()
                                or self.radioButton_116.isChecked() or self.radioButton_117.isChecked()or self.radioButton_118.isChecked() or self.radioButton_119.isChecked()or self.radioButton_120.isChecked() or self.radioButton_121.isChecked()
                                or self.radioButton_122.isChecked() or self.radioButton_123.isChecked()or self.radioButton_124.isChecked() or self.radioButton_125.isChecked()or self.radioButton_126.isChecked()):
                                return True

        return False




#短暂休息15s,重新开始选择任务类型
class Type_break15(QtGui.QWidget):
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


        self.label_4 = QtGui.QLabel(self)


        self.timer = QTimer(self)
        self.count = 14
        self.timer.timeout.connect(self.showNum)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):

        self.label.setText("请做短暂休息")
        self.label_4.setText("15")

        self.label.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.4, (self.task.screen_height) * 0.33, 800, 70))
        self.label.setStyleSheet(_fromUtf8("font: 32pt \"微软雅黑\";\n"
                                           ""))

        self.label_4.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.455, (self.task.screen_height) * 0.55, 800, 100))
        self.label_4.setStyleSheet(_fromUtf8("font: 60pt \"微软雅黑\";\n"
                                             ""))

    def countSet(self,s):
        self .label_4 .setText(s)

    def startCount(self):
        self.timer.start(1000)

    def showNum(self):

        s=str(self.count)
        self.label_4.setText(s)
        self.count=self.count-1




#线程1，倒计时5s
class Mythread(QThread):
    # 定义信号,定义参数为str类型
    _signal = pyqtSignal(str)

    def __init__(self):
        super(Mythread, self).__init__()


    def run(self):
        t=5
        for i in range(5):
            # 发出信号

            tem = '%d' % t
            self._signal.emit(tem)
            # 让程序休眠
            time.sleep(1)

            t=t-1


#线程2，倒计时15s
class Mythread2(QThread):
    # 定义信号,定义参数为str类型
    _signal = pyqtSignal(str)

    def __init__(self):
        super(Mythread2, self).__init__()


    def run(self):
        t=15
        for i in range(15):
            # 发出信号
            tem = '%d' % t
            self._signal.emit(tem)
            # 让程序休眠
            time.sleep(1)
            t=t-1



class Thread_Timer_left(QThread):
    # 定义信号,定义参数为str类型
    _signal = pyqtSignal(str)

    def __init__(self):
        super(Thread_Timer_left, self).__init__()
        self.ifdo = True
        self.singnalstring=""
        self.interval=0
        self.t2=0


    def run(self):
               # 发出信号
            time.sleep(self.t2)
            if self.ifdo:
                self._signal.emit(self.singnalstring)
                self.ifdo=False
                return

    def sett2(self,t2):

        self.t2=round(t2/1000.000,3)


    def setSignalString(self,s):    #获取笔画信号
        self.singnalstring=s

    def getInterval(self):          #返回时间间隔
        return self.interval


class Thread_Timer_right(QThread):
    # 定义信号,定义参数为str类型
    _signal = pyqtSignal(str)

    def __init__(self):
        super(Thread_Timer_right,self).__init__()
        self.ifdo = True
        self.singnalstring=""
        self.interval=0
        self.t2=0.000


    def run(self):
               # 发出信号
            time.sleep(self.t2)
            if self.ifdo:
                self._signal.emit(self.singnalstring)
                self.ifdo=False
            return


    def sett2(self,t2):

        self.t2=round(t2/1000.000,3)


    def setSignalString(self,s):    #获取笔画信号
        self.singnalstring=s

    def getInterval(self):          #返回时间间隔
        return self.interval





if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)

    app.Encoding(QtGui.QApplication.UnicodeUTF8)
    utfcodec = QTextCodec.codecForName("UTF-8")
    QTextCodec.setCodecForTr(utfcodec)
    QTextCodec.setCodecForLocale(utfcodec)
    QTextCodec.setCodecForCStrings(utfcodec)



    ui = Type_input()

    #ui.initUi()

    ui.showFullScreen()



    sys.exit(app.exec_())

