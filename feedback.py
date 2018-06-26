#!/usr/bin/python
import os
import xlrd
import xlwt
import xlutils

input_file = "/home/quocdai/Downloads/Overview.xls"
workbook_to_read = xlrd.open_workbook(input_file)
sheet = workbook_to_read.sheet_by_index(0)
print sheet.nrows
print sheet.ncols
print sheet.cell_value(3,1)
    
