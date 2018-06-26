#!/usr/bin/python
import os
import xlrd
import openpyxl

input_file = "/home/quocdai/Downloads/Overview.xls"
original_file = "/home/quocdai/Downloads/GV.xlsx"
workbook_to_read = xlrd.open_workbook(input_file,on_demand = True,formatting_info=True)
sheet = workbook_to_read.sheet_by_index(0)
print sheet.nrows
print sheet.ncols
print sheet.cell_value(1,5)
col_value = sheet.col_values(5, 1, sheet.nrows - 2)
col_value = [str(x)[0] for x in col_value]
print col_value.count('4')

write_workbook = openpyxl.load_workbook(original_file)
write_workbook.sheetnames
sheet1 = write_workbook['sheet1']


sheet1['F17'] = "mqdai"
img = openpyxl.drawing.image.Image("cusc.png")
sheet1.add_image(img, 'A1')
write_workbook.save('mqdai.xlsx')

