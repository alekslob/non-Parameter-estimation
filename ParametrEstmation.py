from tkinter import *
from tkinter.ttk import *

# from FrameParametrEstmation import FrameParametrEstmation
from RandomVariables import RandomVariables
from FourierTransform import FourierTransform
from TeoreticalFunctions import TeoreticalFunctions
import CulcResults

# def main():
#     frame = FrameParametrEstmation()

def clear(event):
    """ Clears entry form """
    caller = event.widget
    caller.delete("0", "end")

def insertval(value):
    output.insert("1.0", value)

def creater():
    evalution = getDensityFunction()
    outputOfResults(evalution)
    # showDensityFunction(evalution)

def getDensityFunction():
    chooseFourierTransform = chooseModel.current()
    
    nPoint = int(sampleSize.get())
    kMember = int(membersOfRow.get())
    # N_wind = int(vNw.get())
    # S_wind = int(vSw.get())
    expectation = 0
    variance = 1
    start = -4
    end = 4
    
    randomVariables = getRandomVariables()
    fourierTransform = FourierTransform(randomVariables,
                                        nPoint,
                                        kMember,
                                        expectation,
                                        variance,
                                        start,
                                        end)
    if chooseFourierTransform == 0:
        return fourierTransform.discreteFourierTransform()
    elif chooseFourierTransform == 1:
        return fourierTransform.fastFourierTransform()
    elif chooseFourierTransform == 2:
        return fourierTransform.windowFourierTransform()

def getRandomVariables():
    chooseDistribution = 0 #!!!!!
    nPoint = int(sampleSize.get())
    expectation = 0
    variance = 1

    randomVariables = RandomVariables(nPoint, expectation, variance)
    if chooseDistribution == 0:
        return randomVariables.normal()
    elif chooseDistribution == 1:
        return randomVariables.expectation()
    elif chooseDistribution == 2:
        return randomVariables.gamma()

def outputOfResults(evalution):
    teoreticalFunctions = getTeoreticalFunction()
    expectation = 0
    variance = 1

    deviation = CulcResults.culcDevation(teoreticalFunctions, evalution)
    insertval(" %3f |" % CulcResults.culcX2(teoreticalFunctions, evalution, expectation, variance))
    insertval(" %3f    |" % deviation)



def getTeoreticalFunction():
    chooseDistribution = 0 #!!!!!
    nPoint = int(sampleSize.get())
    expectation = 0
    variance = 1
    start = -4
    end = 4

    teoreticalFunctions = TeoreticalFunctions(end-start,
                                            nPoint,
                                            expectation,
                                            variance)
    if chooseDistribution == 0:
        return teoreticalFunctions.normal
    elif chooseDistribution == 1:
        return teoreticalFunctions.expectation
    elif chooseDistribution == 2:
        return teoreticalFunctions.gamma

# def showDensityFunction(evalution):


root = Tk()

frame1 = LabelFrame()
frame1.grid(column = 1, row = 0, columnspan=1, padx=(10,10), pady=(10,10))

# выбор модели
Label(frame1, text = "Фурье:" ).grid( column = 1, row = 0, pady = (0, 0), padx=(30, 0))

chooseModel = Combobox(frame1, values=[u"Дискретный", u"Быстрый", u"Прямоугольное окно", u"Окно Ханна", u"Окно Хемминга"])
chooseModel.set(u"Дискретный")
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
frameMembersOfRow.grid(column = 2, row=2,  padx=(5, 0), pady=(10, 10))
# frameMembersOfRow.bind("<FocusIn>", clear)

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

button = Button(frame3, text="Решить", command = creater())
button.grid(column = 9,row = 1, padx=(40, 0), pady=(0, 0))


output = Text(frame3, bg="white", font="Arial 10", width = 50, height = 12)
output.grid(column=1, row = 0, columnspan = 10, rowspan=1, padx=(10, 10), pady=(10, 10))

root.mainloop()
