# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Python\PythonProjects\hello\Type_choice.ui'
#
# Created: Sat Jul 15 21:30:20 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Task(object ):
    def __init__(self):
        self.screen_width=1920             #设置屏幕分辨率
        self .screen_height=1080


        self.times=1                 #判断第几次任务选择
        self.testID=""
        self.testName=""
        self.bornDate=""
        self.Sex=""
        self.Hand=""
        self.equimentID=""
        self.signUpTime=""


        self.taskChoiceList=[]       #任务类型记录
        self.taskType=""             #每一次的任务类型
        self.practiceTimeList=[]       #练习的单行用时记录
        self.practiceErrorList = []     #单行错误次数

        self.formalTimeList=[]          #正式实验单行用时记录
        self.formalErrorList = []       #单行错误次数

        self.practiceErrorDic={"10_1":[], "15_1": [],"20_1": [],
                               "10_2":[], "15_2": [],"20_2": [],
                               "10_3":[],"15_3": [],"20_3": []}         #记录不同任务类型错误次数
        self.practiceTimeDic = {"10_1":[],"15_1": [],"20_1": [],
                                "10_2":[],"15_2": [], "20_2": [],
                                "10_3":[],"15_3": [],"20_3": []}         #记录不同任务类型用时

        self.formalTimeDic = {"10_1":[],"15_1": [], "20_1": [],
                              "10_2":[],"15_2": [],"20_2": [],
                              "10_3":[],"15_3": [],"20_3": []}         #记录不同任务类型错误次数

        self.formalErrorDic = {"10_1":[],"15_1": [], "20_1": [],
                               "10_2":[],"15_2": [],"20_2": [],
                               "10_3":[],"15_3": [],"20_3": []}         #记录不同任务类型错误次数



        self.scoreDic={"10_1":[],"15_1": [],"20_1": [],
                       "10_2":[], "15_2": [], "20_2": [],
                       "10_3":[],"15_3": [],"20_3": []}         #记录不同任务类型分数

        self.weightList=[]          #权重

