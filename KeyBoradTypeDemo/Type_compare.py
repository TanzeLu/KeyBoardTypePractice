# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Python\PythonProjects\Type_compare.ui'
#
# Created: Wed Jul 19 17:03:44 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Task import Task
from Type_over import Type_over
from excelGenerate import excelDemo
from PyQt4.QtCore import *

import  sys
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

class Type_compare(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.task = Task()
        self.ui = Type_over()  # 打字练习结束界面
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

        self.label.setStyleSheet(_fromUtf8("font: 12pt \"微软雅黑\";"))

        self.label_2 = QtGui.QLabel(self)

        self.label_2.setStyleSheet(_fromUtf8("font: 12pt \"微软雅黑\";"))

        self.checkBox_1 = QtGui.QCheckBox(self)

        self.buttonGroup = QtGui.QButtonGroup(self)

        self.buttonGroup.addButton(self.checkBox_1)
        self.checkBox_2 = QtGui.QCheckBox(self)

        self.buttonGroup_2 = QtGui.QButtonGroup(self)

        self.buttonGroup_2.addButton(self.checkBox_2)
        self.checkBox_3 = QtGui.QCheckBox(self)

        self.buttonGroup_3 = QtGui.QButtonGroup(self)

        self.buttonGroup_3.addButton(self.checkBox_3)
        self.checkBox_4 = QtGui.QCheckBox(self)

        self.buttonGroup_4 = QtGui.QButtonGroup(self)

        self.buttonGroup_4.addButton(self.checkBox_4)
        self.pushButton = QtGui.QPushButton(self)

        self.pushButton.setStyleSheet(_fromUtf8("\n"
                                                "\n"
                                                "QPushButton:hover { background-color: rgb(139，137，137); }"))

        self.checkBox_5 = QtGui.QCheckBox(self)

        self.buttonGroup_5 = QtGui.QButtonGroup(self)

        self.buttonGroup_5.addButton(self.checkBox_5)
        self.checkBox_6 = QtGui.QCheckBox(self)

        self.buttonGroup_3.addButton(self.checkBox_6)
        self.checkBox_7 = QtGui.QCheckBox(self)

        self.buttonGroup_2.addButton(self.checkBox_7)
        self.checkBox_8 = QtGui.QCheckBox(self)

        self.buttonGroup.addButton(self.checkBox_8)
        self.checkBox_9 = QtGui.QCheckBox(self)

        self.buttonGroup_4.addButton(self.checkBox_9)
        self.checkBox_10 = QtGui.QCheckBox(self)

        self.buttonGroup_5.addButton(self.checkBox_10)
        self.checkBox_11 = QtGui.QCheckBox(self)

        self.buttonGroup_8 = QtGui.QButtonGroup(self)

        self.buttonGroup_8.addButton(self.checkBox_11)
        self.checkBox_12 = QtGui.QCheckBox(self)

        self.buttonGroup_7 = QtGui.QButtonGroup(self)

        self.buttonGroup_7.addButton(self.checkBox_12)
        self.checkBox_13 = QtGui.QCheckBox(self)

        self.buttonGroup_6 = QtGui.QButtonGroup(self)

        self.buttonGroup_6.addButton(self.checkBox_13)
        self.checkBox_14 = QtGui.QCheckBox(self)

        self.buttonGroup_9 = QtGui.QButtonGroup(self)

        self.buttonGroup_9.addButton(self.checkBox_14)
        self.checkBox_15 = QtGui.QCheckBox(self)

        self.buttonGroup_10 = QtGui.QButtonGroup(self)

        self.buttonGroup_10.addButton(self.checkBox_15)
        self.checkBox_16 = QtGui.QCheckBox(self)

        self.buttonGroup_8.addButton(self.checkBox_16)
        self.checkBox_17 = QtGui.QCheckBox(self)

        self.buttonGroup_7.addButton(self.checkBox_17)
        self.checkBox_18 = QtGui.QCheckBox(self)

        self.buttonGroup_6.addButton(self.checkBox_18)
        self.checkBox_19 = QtGui.QCheckBox(self)

        self.buttonGroup_10.addButton(self.checkBox_19)

        self.checkBox_20 = QtGui.QCheckBox(self)

        self.buttonGroup_9.addButton(self.checkBox_20)

        self.checkBox_21 = QtGui.QCheckBox(self)

        self.buttonGroup_13 = QtGui.QButtonGroup(self)

        self.checkBox_22 = QtGui.QCheckBox(self)

        self.buttonGroup_11 = QtGui.QButtonGroup(self)

        self.buttonGroup_11.addButton(self.checkBox_22)
        self.checkBox_23 = QtGui.QCheckBox(self)

        self.buttonGroup_12 = QtGui.QButtonGroup(self)

        self.buttonGroup_12.addButton(self.checkBox_23)
        self.checkBox_24 = QtGui.QCheckBox(self)

        self.buttonGroup_15 = QtGui.QButtonGroup(self)

        self.buttonGroup_15.addButton(self.checkBox_24)
        self.checkBox_25 = QtGui.QCheckBox(self)

        self.buttonGroup_12.addButton(self.checkBox_25)
        self.checkBox_26 = QtGui.QCheckBox(self)

        self.buttonGroup_11.addButton(self.checkBox_26)
        self.checkBox_27 = QtGui.QCheckBox(self)

        self.buttonGroup_15.addButton(self.checkBox_27)
        self.checkBox_28 = QtGui.QCheckBox(self)

        self.buttonGroup_14 = QtGui.QButtonGroup(self)

        self.buttonGroup_14.addButton(self.checkBox_28)
        self.checkBox_29 = QtGui.QCheckBox(self)

        self.buttonGroup_14.addButton(self.checkBox_29)
        self.checkBox_30 = QtGui.QCheckBox(self)

        self.buttonGroup_13.addButton(self.checkBox_30)
        self.line = QtGui.QFrame(self)

        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)

        self.line_2 = QtGui.QFrame(self)

        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)

        self.line_3 = QtGui.QFrame(self)

        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)

        self.line_4 = QtGui.QFrame(self)
        # self.line_4.setGeometry(QtCore.QRect(320, 110, 20, 211))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)

        self.line_5 = QtGui.QFrame(self)
        # self.line_5.setGeometry(QtCore.QRect(410, 110, 20, 221))
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)

        self.line_6 = QtGui.QFrame(self)

        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)

        self.line_7 = QtGui.QFrame(self)

        self.line_7.setStyleSheet(_fromUtf8("\n"
                                            "color: rgb(0, 255, 127);"))
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)

        self.line_8 = QtGui.QFrame(self)

        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)

        self.line_9 = QtGui.QFrame(self)

        self.line_9.setStyleSheet(_fromUtf8("color: rgb(0, 255, 127);"))
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)

        self.line_10 = QtGui.QFrame(self)

        self.line_10.setFrameShape(QtGui.QFrame.HLine)
        self.line_10.setFrameShadow(QtGui.QFrame.Sunken)


        # 信号连接到指定槽
        self.pushButton.clicked.connect(self.on_pushButton_clicked)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)



    def retranslateUi(self, Form):

        self.label.setText("在下面15组中，每2项进行相互比较，请选出每组2项中你认为对工作")
        self.label_2.setText("成绩影响最大的那一条目，点击相应项目前的方框做标记")
        self.checkBox_1.setText("脑力需求")
        self.checkBox_2.setText("时间需求")
        self.checkBox_3.setText("努力程度")
        self.checkBox_4.setText("努力程度")
        self.pushButton.setText("完成")
        self.checkBox_5.setText("脑力需求")
        self.checkBox_6.setText("业绩水平")
        self.checkBox_7.setText("受挫程度")
        self.checkBox_8.setText("体力需求")
        self.checkBox_9.setText("体力需求")
        self.checkBox_10.setText("受挫程度")
        self.checkBox_11.setText("脑力需求")
        self.checkBox_12.setText("业绩水平")
        self.checkBox_13.setText("体力需求")
        self.checkBox_14.setText("受挫程度")
        self.checkBox_15.setText("时间需求")
        self.checkBox_16.setText("努力程度")
        self.checkBox_17.setText("体力需求")
        self.checkBox_18.setText( "时间需求")
        self.checkBox_19.setText("体力需求")
        self.checkBox_20.setText("业绩水平")
        self.checkBox_21.setText("脑力需求")
        self.checkBox_22.setText("努力程度")
        self.checkBox_23.setText("时间需求")
        self.checkBox_24.setText("努力程度")
        self.checkBox_25.setText("脑力需求")
        self.checkBox_26.setText("时间需求")
        self.checkBox_27.setText("受挫程度")
        self.checkBox_28.setText("业绩水平")
        self.checkBox_29.setText("受挫程度")
        self.checkBox_30.setText("业绩水平")

        self.label.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.19, (self.task.screen_height) * 0.08, 1300, 40))
        self.label.setStyleSheet(_fromUtf8("font: 20pt \"微软雅黑\";\n"
                                           ""))
        self.label_2.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.24, (self.task.screen_height) * 0.13, 1100, 40))
        self.label_2.setStyleSheet(_fromUtf8("font: 20pt \"微软雅黑\";\n"
                                           ""))

        self.line_7.setGeometry(QtCore.QRect(self.task.screen_width * 0.19, (self.task.screen_height) * 0.2, 1210, 20))
        self.line_9.setGeometry(QtCore.QRect(self.task.screen_width * 0.19, (self.task.screen_height) * 0.38, 1210, 20))
        self.line_10.setGeometry(QtCore.QRect(self.task.screen_width * 0.19, (self.task.screen_height) * 0.56, 1210, 20))
        self.line_8.setGeometry(QtCore.QRect(self.task.screen_width * 0.19, (self.task.screen_height) * 0.74, 1210, 20))

        self.line.setGeometry(QtCore.QRect(self.task.screen_width * 0.185, (self.task.screen_height) * 0.21, 20, 585))
        self.line_2.setGeometry(QtCore.QRect(self.task.screen_width * 0.311, (self.task.screen_height) * 0.21, 20, 585))
        self.line_3.setGeometry(QtCore.QRect(self.task.screen_width * 0.437, (self.task.screen_height) * 0.21, 20, 585))
        self.line_4.setGeometry(QtCore.QRect(self.task.screen_width * 0.563, (self.task.screen_height) * 0.21, 20, 585))
        self.line_5.setGeometry(QtCore.QRect(self.task.screen_width * 0.689, (self.task.screen_height) * 0.21, 20, 585))
        self.line_6.setGeometry(QtCore.QRect(self.task.screen_width * 0.815, (self.task.screen_height) * 0.21, 20, 585))


        self.checkBox_1.setGeometry(QtCore.QRect(self.task.screen_width * 0.21, (self.task.screen_height) * 0.24, 160, 60))
        self.checkBox_1.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                           ""))
        self.checkBox_8.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.21, (self.task.screen_height) * 0.3,  160, 60))
        self.checkBox_8.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                ""))

        self.checkBox_2.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.336, (self.task.screen_height) * 0.24,  160, 60))
        self.checkBox_2.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                ""))
        self.checkBox_7.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.336, (self.task.screen_height) * 0.3,  160, 60))
        self.checkBox_7.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                ""))

        self.checkBox_3.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.462, (self.task.screen_height) * 0.24, 160, 60))
        self.checkBox_3.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                ""))
        self.checkBox_6.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.462, (self.task.screen_height) * 0.3,  160, 60))
        self.checkBox_6.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                ""))

        self.checkBox_4.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.588, (self.task.screen_height) * 0.24, 160, 60))
        self.checkBox_4.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                ""))
        self.checkBox_9.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.588, (self.task.screen_height) * 0.3,  160, 60))
        self.checkBox_9.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                ""))

        #self.checkBox_5.setGeometry(
         #   QtCore.QRect(self.task.screen_width * 0.714, (self.task.screen_height) * 0.24,  160, 60))
        #self.checkBox_5.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
         #                                       ""))
        #self.checkBox_10.setGeometry(
         #   QtCore.QRect(self.task.screen_width * 0.714, (self.task.screen_height) * 0.3,  160, 60))
        #self.checkBox_10.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
         #                                       ""))

        self.checkBox_5.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.514, (self.task.screen_height) * 0.24, 160, 60))
        self.checkBox_5.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                ""))
        self.checkBox_10.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.514, (self.task.screen_height) * 0.3, 160, 60))
        self.checkBox_10.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                 ""))

        self.checkBox_13.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.21, (self.task.screen_height) * 0.42,  160, 60))
        self.checkBox_13.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                ""))
        self.checkBox_18.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.21, (self.task.screen_height) * 0.48, 160, 60))
        self.checkBox_18.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                ""))

        self.checkBox_12.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.336, (self.task.screen_height) * 0.42,  160, 60))
        self.checkBox_12.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                ""))
        self.checkBox_17.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.336, (self.task.screen_height) * 0.48,  160, 60))
        self.checkBox_17.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                ""))

        self.checkBox_11.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.462, (self.task.screen_height) * 0.42,  160, 60))
        self.checkBox_11.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                ""))
        self.checkBox_16.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.462, (self.task.screen_height) * 0.48,  160, 60))
        self.checkBox_16.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                ""))

        self.checkBox_14.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.588, (self.task.screen_height) * 0.42, 160, 60))
        self.checkBox_14.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                ""))
        self.checkBox_20.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.588, (self.task.screen_height) * 0.48,  160, 60))
        self.checkBox_20.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                ""))

        #self.checkBox_15.setGeometry(
         #   QtCore.QRect(self.task.screen_width * 0.714, (self.task.screen_height) * 0.42, 160, 60))
        #self.checkBox_15.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
         #                                       ""))
        #self.checkBox_19.setGeometry(
         #   QtCore.QRect(self.task.screen_width * 0.714, (self.task.screen_height) * 0.48,  160, 60))
        #self.checkBox_19.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
         #                                        ""))

        self.checkBox_15.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.514, (self.task.screen_height) * 0.42, 160, 60))
        self.checkBox_15.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                 ""))
        self.checkBox_19.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.514, (self.task.screen_height) * 0.48, 160, 60))
        self.checkBox_19.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                 ""))

        self.checkBox_22.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.21, (self.task.screen_height) * 0.60,  160, 60))
        self.checkBox_22.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                 ""))
        self.checkBox_26.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.21, (self.task.screen_height) * 0.66,  160, 60))
        self.checkBox_26.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                 ""))

        self.checkBox_23.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.336, (self.task.screen_height) * 0.60,  160, 60))
        self.checkBox_23.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                 ""))
        self.checkBox_25.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.336, (self.task.screen_height) * 0.66,  160, 60))
        self.checkBox_25.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                 ""))

        self.checkBox_30.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.462, (self.task.screen_height) * 0.60,  160, 60))
        self.checkBox_30.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                 ""))
        self.checkBox_21.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.462, (self.task.screen_height) * 0.66,  160, 60))
        self.checkBox_21.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                 ""))

        self.checkBox_29.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.588, (self.task.screen_height) * 0.60,  160, 60))
        self.checkBox_29.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                 ""))
        self.checkBox_28.setGeometry(
            QtCore.QRect(self.task.screen_width * 0.588, (self.task.screen_height) * 0.66,  160, 60))
        self.checkBox_28.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                 ""))

        #self.checkBox_24.setGeometry(
         #   QtCore.QRect(self.task.screen_width * 0.714, (self.task.screen_height) * 0.60,  160, 60))
        #self.checkBox_24.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
         #                                        ""))
        #self.checkBox_27.setGeometry(
         #   QtCore.QRect(self.task.screen_width * 0.714, (self.task.screen_height) * 0.66,  160, 60))
        #self.checkBox_27.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                             #    ""))
        self.checkBox_24.setGeometry(
           QtCore.QRect(self.task.screen_width * 0.514, (self.task.screen_height) * 0.60,  160, 60))
        self.checkBox_24.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
                                                ""))
        self.checkBox_27.setGeometry(
           QtCore.QRect(self.task.screen_width * 0.514, (self.task.screen_height) * 0.66,  160, 60))
        self.checkBox_27.setStyleSheet(_fromUtf8("font: 16pt \"微软雅黑\";\n"
            ""))

        #self.pushButton.setGeometry(
         #   QtCore.QRect(self.task.screen_width * 0.45, (self.task.screen_height) * 0.82, 200, 80))
        self.pushButton.setGeometry(QtCore.QRect(self.task.screen_width * 0.45, (self.task.screen_height) * 0.5, 200, 80))





        self.brain=0.00
        self.strength=0.00
        self.time=0.00
        self .achievement=0.00
        self .effort=0.00
        self .disappoint=0.00


    def on_pushButton_clicked(self):
        if((self.checkBox_1.isChecked()  or self.checkBox_8.isChecked() ) and (self.checkBox_2.isChecked()  or self.checkBox_7.isChecked() )and (
            self.checkBox_3.isChecked()  or self.checkBox_6.isChecked() )and (self.checkBox_4.isChecked()  or self.checkBox_9.isChecked() )and(
             self.checkBox_5.isChecked()  or self.checkBox_10.isChecked() ) and (self.checkBox_13.isChecked()  or self.checkBox_18.isChecked() ) and (
             self.checkBox_12 or self.checkBox_17.isChecked() )and (self.checkBox_11.isChecked()  or self.checkBox_16.isChecked() ) and (
             self.checkBox_14 or self.checkBox_20.isChecked()) and (self.checkBox_15.isChecked() or self.checkBox_19.isChecked()) and (
            self.checkBox_22 or self.checkBox_26.isChecked()) and (self.checkBox_23.isChecked() or self.checkBox_25.isChecked()) and (
            self.checkBox_30 or self.checkBox_21.isChecked()) and (self.checkBox_29.isChecked() or self.checkBox_28.isChecked()) and (
            self.checkBox_24 or self.checkBox_27.isChecked())):


                self.setWeight()

                self.close()


                print "practiceerrordic"
                print self.task.practiceErrorDic
                print "practicetimedic"
                print self.task.practiceTimeDic
                print "formalerrordic"
                print self.task.formalErrorDic
                print "formaltimedic"
                print self.task.formalTimeDic


                # 生成数据收集表，NASA表
                exceldemo = excelDemo()
                exceldemo.setTask(self.task)
                exceldemo.write_dataCollect()
                exceldemo.write_dataNASA()



                self.ui.showFullScreen()





    def setWeight(self):                    #设置权重分数

        #脑力权重
        if (self.checkBox_1.isChecked()):
            self.brain = self.brain + 1
        if(self.checkBox_5.isChecked()):
            self.brain = self.brain + 1
        if (self.checkBox_11.isChecked()):
            self.brain = self.brain + 1
        if (self.checkBox_21.isChecked()):
            self.brain = self.brain + 1
        if (self.checkBox_25.isChecked()):
            self.brain = self.brain + 1



        #体力权重
        if (self.checkBox_8.isChecked()):
            self.strength = self.strength + 1
        if (self.checkBox_9.isChecked()):
            self.strength = self.strength + 1
        if (self.checkBox_13.isChecked()):
            self.strength = self.strength + 1
        if (self.checkBox_17.isChecked()):
            self.strength = self.strength + 1
        if (self.checkBox_19.isChecked()):
            self.strength = self.strength + 1


        # 时间权重
        if (self.checkBox_2.isChecked()):
            self.time = self.time + 1
        if (self.checkBox_15.isChecked()):
            self.time = self.time + 1
        if (self.checkBox_18.isChecked()):
            self.time = self.time + 1
        if (self.checkBox_23.isChecked()):
            self.time = self.time + 1
        if (self.checkBox_26.isChecked()):
            self.time = self.time + 1


        # 业绩权重
        if (self.checkBox_6.isChecked()):
            self.achievement = self.achievement + 1
        if (self.checkBox_12.isChecked()):
            self.achievement = self.achievement + 1
        if (self.checkBox_20.isChecked()):
            self.achievement = self.achievement + 1
        if (self.checkBox_28.isChecked()):
            self.achievement = self.achievement + 1
        if (self.checkBox_30.isChecked()):
            self.achievement = self.achievement + 1



        # 努力权重
        if (self.checkBox_3.isChecked()):
            self.effort = self.effort + 1
        if (self.checkBox_4.isChecked()):
            self.effort = self.effort + 1
        if (self.checkBox_16.isChecked()):
            self.effort = self.effort + 1
        if (self.checkBox_22.isChecked()):
            self.effort = self.effort + 1
        if (self.checkBox_24.isChecked()):
            self.effort = self.effort + 1



        # 受挫权重
        if (self.checkBox_7.isChecked()):
            self.disappoint = self.disappoint + 1
        if (self.checkBox_10.isChecked()):
            self.disappoint = self.disappoint + 1
        if (self.checkBox_14.isChecked()):
            self.disappoint = self.disappoint + 1
        if (self.checkBox_27.isChecked()):
            self.disappoint = self.disappoint + 1
        if (self.checkBox_29.isChecked()):
            self.disappoint = self.disappoint + 1


        #将所有权重分数记录下来，权重分数除去15
        self.task .weightList.append(round(self .brain/15,2)   )
        self.task.weightList.append(round(self .strength/15,2) )
        self.task.weightList.append(round(self.time/15,2))
        self.task.weightList.append(round(self.achievement/15,2) )
        self.task.weightList.append(round(self .effort/15,2) )
        self.task.weightList.append(round(self.disappoint/15,2) )




if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)

    app.Encoding(QtGui.QApplication.UnicodeUTF8)
    utfcodec = QTextCodec.codecForName("UTF-8")
    QTextCodec.setCodecForTr(utfcodec)
    QTextCodec.setCodecForLocale(utfcodec)
    QTextCodec.setCodecForCStrings(utfcodec)


    ui = Type_compare()
    ui.showFullScreen()

    sys.exit(app.exec_())












