from tkinter import *
from tkinter.ttk import *
import NonParametrEstmation as pe

parametrs = [0,1,0.5,9,2]
# viewLimits = [-4, 4]

def clear(event):
    """ Clears entry form """
    caller = event.widget
    caller.delete("0", "end")

def insertval(value):
    output.insert("1.0", value)

root = Tk()

frame1 = LabelFrame()
frame1.grid(column = 1, row = 0, columnspan=1, padx=(10,10), pady=(10,10))


# выбор модели
valuesModel = [u"Дискретный", u"Быстрый", u"Прямоугольное окно", u"Окно Ханна", u"Окно Хемминга"]
Label(frame1, text = "Фурье:" ).grid( column = 1, row = 0, pady = (0, 0), padx=(30, 0))
chooseModel = Combobox(frame1, values = valuesModel)
chooseModel.set(valuesModel[0])
chooseModel.grid( column = 2, row=0, pady=(10, 0), padx=(5, 0))

# N - количество точек

Label(frame1, text="Объем выборки:").grid( column = 1, row = 1, pady = (0, 0), padx = (30, 0))
sampleSize = StringVar()
sampleSize.set('100')
frameSampleSize = Entry(frame1, width = 23, textvariable = sampleSize)
frameSampleSize.grid(column = 2, row = 1, padx = (5, 0), pady=(10, 0))
# frameSampleSize.bind("<FocusIn>", clear)

# K - колличество членов ряда
Label(frame1, text="Количество членов ряда:").grid(column=1, row=2, pady=(0, 0), padx=(30, 0))
membersOfRow = StringVar()
membersOfRow.set('10')
frameMembersOfRow = Entry(frame1, width=23, textvariable = membersOfRow)
frameMembersOfRow.grid(column = 2, row=2,  padx=(5, 0), pady=(10, 0))
# frameMembersOfRow.bind("<FocusIn>", clear)

# распределение
valuesDistribution = [u"Нормальное распределение", u"Экспоненциальное распределение", u"Гамма-распределение"]
Label(frame1, text = "Функция распределения: ").grid(column = 1, row = 3, pady = (0, 0), padx = (30, 0))
chooseDistribution = Combobox(frame1, values = valuesDistribution)
chooseDistribution.set(valuesDistribution[0])
chooseDistribution.grid( column = 2, row=3, pady=(10, 0), padx=(5, 0))

frame2 = LabelFrame(text = "Для ОПФ")
frame2.grid(column = 1, row = 1, columnspan=1,  padx=(10,10), pady=(10,10))

# N_wind - количество окон
Label(frame2, text="Введите количество окон:").grid(column=1, row=0, padx=(30, 0), pady=(10, 10))
numOfWindow = StringVar()
numOfWindow.set('0')
frameNumOfWindow = Entry(frame2, width=23, textvariable = numOfWindow)
frameNumOfWindow.grid(column=2, row=0, padx=(10, 0), pady=(10, 0))
# frameNumOfWindow.bind("<FocusIn>", clear)

# S_wind - ширина окон
Label(frame2, text="Введите размер окон:").grid(column=1, row=1, padx=(30, 0), pady=(10, 10))
widthOfWindow = StringVar()
widthOfWindow.set('0')
frameWidthOfWindow = Entry(frame2, width=23, textvariable = widthOfWindow)
frameWidthOfWindow.grid(column=2, row=1, padx=(10, 0), pady=(10, 0))
# frameWidthOfWindow.bind("<FocusIn>", clear)

frame3 = Frame()
frame3.grid(column = 2, row = 0, columnspan=1, rowspan=2,  padx=(10,10), pady=(10,10))

output = Text(frame3, bg="white", font="Arial 10", width = 50, height = 12)
output.grid(column=1, row = 0, columnspan = 10, rowspan=1, padx=(10, 10), pady=(10, 10))

butSimple = Button(frame3, text="Решить", command = pe.creater)
butSimple.grid(column = 7,row = 1, padx=(40, 0), pady=(0, 0))

butArticleK = Button(frame3, text="СреднийN", command = pe.createrArticleK)
butArticleK.grid(column = 8,row = 1, padx=(40, 0), pady=(0, 0))

butArticleN = Button(frame3, text="СреднийK", command = pe.createrArticleN)
butArticleN.grid(column = 9,row = 1, padx=(40, 0), pady=(0, 0))

butArticleСomparison = Button(frame3, text="Сравнение", command = pe.createrArticleСomparison)
butArticleСomparison.grid(column = 10,row = 1, padx=(40, 0), pady=(0, 0))
# root.bind('<Return>', createrReturn)

root.mainloop()