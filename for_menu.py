# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 15:37
# @Author  : Alessia
# @Email   : baoming1221@126.com
# @File    : for_menu.py
# @Software: PyCharm
#
import xlwt
import xlrd
import pandas as pd
import numpy as np

#xlrd读取
f = xlrd.open_workbook('E:\python_study\menu\menu_1.xls')
sheet = f.sheet_by_index(0)


#xlwt 写入
file_name = 'E:\python_study\menu\menu_2.xls'
f1 = xlwt.Workbook(encoding = 'utf-8')
sheet1 = f1.add_sheet('new1')


#行转列
for i in range(sheet.nrows):
    sheet_data = sheet.cell(i, 0).value
    if sheet_data != ' ':
        for j in range(len(sheet.row(i))):
            menu_item = sheet.cell(i,j).value
            sheet1.write(j,i,menu_item)
            f1.save(file_name)
    else:
        pass

# f_menu = pd.read_excel('D:\Personal\menu_1.xls')
#
# bd = pd.DataFrame(f_menu)
# bd = bd.transpose()
# print(bd)
# print(bd.to_excel('D:\Personal\menu_2.xls',index=False))


