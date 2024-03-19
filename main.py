from openpyxl import *

wb = load_workbook('test.xlsx')
ws = wb["Лист1"]
test = ws['c4']
week = 1
for i in range(4, 75):
    if (i == 4):
        print("Понедельник")
    elif (i == 16):
        print("\nВторник")
    elif (i == 28):
        print("\nСреда")
    elif (i == 40):
        print("\nЧетверг")
    elif (i == 52):
        print("\nПятница")
    elif (i == 64):
        print("\nСуббота")
    if (i % 2 == 0):
        time = ws['b' + str(i)]
        print(time.value)
    name = ws['c' + str(i)]
    if (i % 2 == week):
        if (name.value != None):
            print(name.value)
