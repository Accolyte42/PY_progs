import os
import xlrd, xlwt

# Текущая директория
cwd = os.getcwd()
print(cwd)

# Изменение текущей директории
os.chdir("C:\PY progs\diplom")
cwd = os.getcwd()
print(cwd)

# Изменение текущей директории
os.chdir("Ado")
cwd = os.getcwd()
print(cwd)

os.chdir("C:\PY progs\diplom")
cwd = os.getcwd()
print(os.listdir('.'))

rb = xlrd.open_workbook('123.xlsx')
print(rb)

sheet = rb.sheet_by_index(0)
print(sheet)

val = sheet.row_values(0)[0]
print(val)

vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
print(vals)

wb = xlwt.Workbook()
ws = wb.add_sheet('Test')

# в A1 записываем значение из ячейки A1 прошлого файла
ws.write(0, 0, 5)

# в столбец B запишем нашу последовательность из столбца A исходного файла
i = 0
for rec in vals:
    ws.write(i,1,rec[0])
    i =+ i

# сохраняем рабочую книгу
wb.save('xl_rec.xls')
