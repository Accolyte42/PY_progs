import xlrd, xlwt, xlutils
import os

print(os.listdir())
workbook = xlrd.open_workbook("123.xlsx")

workbook = xlrd.open_workbook("123.xlsx", on_demand=True)
print(workbook)

worksheet = workbook.sheet_by_name("Sheet1")
print(worksheet)

print(worksheet.cell(0,0).value)

book = xlwt.Workbook()
sheet1 = book.add_sheet("Python sheet 1")

sheet1.write(1,0, "cell of First Sheet")

book.save("Signal.xls")

