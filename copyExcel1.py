'''
import xlwings as xw
 
bookName = r'T:\1. ST CCTV & EES Upgrade Project\9. Engineering & Design\9.23 CROD\15. StationsDD\Arncliffe\DD\V2 - 20180727 -  FC - Release\0055001000006DD00 - Arncliffe - CRODD - Tables -20180727.xlsx'
sheetName = '2. Bill of Materials'
 
wb = xw.Book(bookName)
sht = wb.sheets[sheetName]
 
myCell = wb.sheets[sheetName].api.UsedRange.Find('*UPS*')
#print('---------------')
print (myCell.address)
#input()
print (myCell.address + 1)
'''

import xlsxwriter
import os
import xlrd    
import time 
from xlsxwriter.utility import xl_rowcol_to_cell
 
def findCell(sh, searchedValue):
    for row in range(sh.nrows):
        for col in range(sh.ncols):
            myCell = sh.cell(row, col)
            if myCell.value == searchedValue:
                return xl_rowcol_to_cell(row, col)
    return -1
 
myName = 'test1.xlsx'
wbk = xlsxwriter.Workbook(myName)
wks = wbk.add_worksheet()
i = -1
 
for x in range(1, 1000, 11):
    i+=1
    cella = xl_rowcol_to_cell(i, 0) #0,0 is A1!
    cellb = xl_rowcol_to_cell(i, 1)
    cellc = xl_rowcol_to_cell(i, 2)
    wks.write(cella,x)
    wks.write(cellb,x*3)
    wks.write(cellc,x*4.5)
myPath= r'C:\Users\pkongyang\Desktop\ExcelTest\test1.xlsx'
#myPath= os.getcwd()+"\\"+myName
 
searchedValue = 'Townhall'
print(searchedValue)
for sh in xlrd.open_workbook(myPath).sheets():  
    print(findCell(sh, searchedValue))
