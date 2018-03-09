# -*- coding: utf-8 -*-
import xlwt
from datetime import datetime
from Task import Task

class excelDemo(object ):

    def __init__(self):
        self .task=Task ()

    def setTask(self,task):
        self.task =task

    # 数据收集表
    def write_dataCollect(self):
        style0 = xlwt.easyxf('font: name Times New Roman', num_format_str='#,##0.00')


        wb = xlwt.Workbook()
        ws = wb.add_sheet('A Test Sheet', cell_overwrite_ok=True)


        Row0=[u'设备编号', u'被试编号', u'出生日期', u'被试姓名', u'被试性别', u'利手', u'登录时间', u'测试条件'
            , u'练习或正式实验', u'行数序号', u'单行用时', u'单行错误次数', u'总用时', u'总错误次数']

        #设置第一行
        for i in range(len(Row0 ) ) :
            ws.write(0, i,Row0 [i], style0)

        #设置被试编号
        testID=unicode (self.task .testID)
        equimentID=unicode (self.task.equimentID )
        bornDate=unicode(self.task.bornDate)
        testName=unicode(self.task.testName)
        Sex=unicode(self.task.Sex)
        Hand=unicode(self.task.Hand)
        signupTime=unicode(self.task.signUpTime)

        ws.write(1, 0, equimentID , style0)
        ws.write(1, 1, testID, style0)
        ws.write(1, 2, bornDate, style0)
        ws.write(1, 3, testName, style0)
        ws.write(1, 4, Sex, style0)
        ws.write(1, 5, Hand, style0)
        ws.write(1, 6,signupTime, style0)

        #任务类型
        typeList=["10ms*100ms","15ms*100ms","20ms*100ms",
                  "10ms*200ms","15ms*200ms","20ms*200ms",
                  "10ms*300ms", "15ms*300ms", "20ms*300ms"]
        typeListTemp=["10_1","15_1","20_1",
                      "10_2", "15_2", "20_2",
                      "10_3", "15_3", "20_3"]

        #每一种任务类型的长度
        typeLengthList=[]

        typeLengthList .append(len(self .task .practiceTimeDic["10_1"]) +5)
        typeLengthList.append(len(self.task.practiceTimeDic["15_1"]) + 5)
        typeLengthList.append(len(self.task.practiceTimeDic["20_1"]) + 5)

        typeLengthList.append(len(self.task.practiceTimeDic["10_2"]) + 5)
        typeLengthList.append(len(self.task.practiceTimeDic["15_2"]) + 5)
        typeLengthList.append(len(self.task.practiceTimeDic["20_2"]) + 5)

        typeLengthList.append(len(self.task.practiceTimeDic["10_3"]) + 5)
        typeLengthList.append(len(self.task.practiceTimeDic["15_3"]) + 5)
        typeLengthList.append(len(self.task.practiceTimeDic["20_3"]) + 5)




        #打印各种任务类型
        j = 1
        for i in range(0,9):
            ws.write(j, 7, typeList[i], style0)
            j=j+typeLengthList [i]


        #打印练习或正式实验，打印行数序号,单行用时，单行错误次数
        length=1
        for i in range(0,9):
            lop=typeLengthList [i]-5
            lof=1

            for k in range(typeLengthList [i]) :
                if(k<lop):
                    tem =  (k+1)

                    ptime =  (self.task.practiceTimeDic[typeListTemp[i]][k])
                    perror= (self .task .practiceErrorDic[typeListTemp[i]][k])
                    ws.write(length , 8, u'练习', style0)
                    ws.write(length,9, tem, style0)
                    ws.write(length, 10, ptime, style0)
                    ws.write(length, 11, perror, style0)
                else:
                    tem= lof
                    ftime = (self.task.formalTimeDic[typeListTemp[i]][lof-1])
                    ferror =  (self.task.formalErrorDic[typeListTemp[i]][lof-1])

                    ws.write(length, 8, u'正式实验', style0)
                    ws.write(length, 9, tem, style0)
                    ws.write(length, 10, ftime, style0)
                    ws.write(length, 11,ferror , style0)
                    lof=lof+1

                length=length+1

        #计算练习，正式实验总用时，总错误次数
        length1=0
        for k in range(0,9):
            #计算练习用时
            sum1=0
            length1=length1 +len(self .task .practiceTimeDic[typeListTemp  [k]])
            for i in range(len(self .task .practiceTimeDic[typeListTemp  [k]]) ):
                sum1=sum1+self .task .practiceTimeDic[typeListTemp  [k]][i]

            # 计算练习错误次数
            sum2 = 0
            for i in range(len(self.task.practiceErrorDic[typeListTemp [k]])):
                sum2 = sum2 + self.task.practiceErrorDic[typeListTemp [k]][i]


            ws.write(length1 , 12, sum1, style0)
            ws.write(length1, 13, sum2, style0)

            #计算正式实验用时
            sum1=0

            for i in range(5 ):
                sum1=sum1+self .task .practiceTimeDic[typeListTemp  [k]][length1+i]

            length1 = length1 + 5
            # 计算正式实验错误次数
            sum2 = 0
            for i in range(5):
                sum2 = sum2 + self.task.formalErrorDic[typeListTemp[k]][i]

            ws.write(length1 , 12, sum1, style0)
            ws.write(length1, 13, sum2, style0)

        testID = unicode(self.task.testID)
        testName=unicode (self.task.testName)


        #练习和正式实验数据表格，存放路径D盘
        str = "d:\\" + testID + "_" + testName + ".xls"
        wb.save(str)  # 保存文件


    #写NASA表
    def write_dataNASA(self):
        style0 = xlwt.easyxf('font: name Times New Roman', num_format_str='#,##0.00')


        wb = xlwt.Workbook()
        ws = wb.add_sheet('A Test Sheet', cell_overwrite_ok=True)

        Row0 = [u'第一步得分', u'脑力需求', u'体力需求', u'时间需求', u'业绩水平', u'努力程度', u'受挫程度', u'   '
            , u'加权得分', u'脑力需求', u'体力需求', u'时间需求', u'业绩水平', u'努力程度', u'受挫程度',u'总分']
        Colum0=["10ms*100ms","15ms*100ms","20ms*100ms",
                  "10ms*200ms","15ms*200ms","20ms*200ms",
                  "10ms*300ms", "15ms*300ms", "20ms*300ms"]
        typeListTemp = ["10_1", "15_1", "20_1",
                        "10_2", "15_2", "20_2",
                        "10_3", "15_3", "20_3"]

        # 设置第一行
        for i in range(len(Row0)):
            ws.write(0, i, Row0[i], style0)
        for i in range(len(Colum0 ) ):
            ws.write(i+1, 0, Colum0[i], style0)

        ws.write(11, 0, u'第二步权值', style0)

        for i in range(0,9):
            sum=0
            for j in range(0,6):
                l=self.task.scoreDic[typeListTemp[i]][j]*self.task.weightList [j]
                sum=sum+l

                ws.write(i+1, j+1, self.task .scoreDic [typeListTemp [i]][j], style0)
                ws.write(i + 1, j + 9,l , style0)

            ws.write(i + 1,15, sum, style0)

        for j in range(0, 6):
            ws.write(11, j + 1, self.task.weightList [j], style0)

        testID =  unicode(self.task.testID)
        testName = unicode (self.task.testName)

        #NASA表格存放路径，D盘
        str = "d:\\NASA_" + testID + "_" + testName + ".xls"
        wb.save(str)  # 保存文件


if __name__ == '__main__':

    demo=excelDemo ()
    demo.write_dataCollect()
    demo.write_dataNASA()