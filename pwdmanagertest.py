from __future__ import  print_function
import csv
import codecs
import join
from os.path import join , dirname , abspath
import xlrd
from xlrd.sheet import ctype_text
sitedict = {}
#fileReader = csv.reader(codecs.open('usercred.csv','r', 'utf-16'))

fileName = join(dirname(dirname(abspath(__file__))),
                'password-manager-','usercred.xlsx')

workBookOne = xlrd.open_workbook(fileName)

workbookSheetNames = workBookOne.sheet_names()
print('Sheet names: ', workbookSheetNames)

categoryWorkBookOne = workBookOne.sheet_by_name(workbookSheetNames[0])

categoryWorkBookOne = workBookOne.sheet_by_index(0)
print('Sheet name: {}'.format(categoryWorkBookOne.name))

#getting the first row
rowOne = categoryWorkBookOne.row(0)
