from tkinter import *
from tkinter.ttk import *

class FrameParametrEstmation(object):
    def __init__(self):
        self.root = Tk()
        self.frame1()
        self.frame2()
        self.frame3()

        # vm = StringVar()
        # vm.set('0')
        # vs = StringVar()
        # vs.set('1')
        # insertval("     | отклонение |     X2     |   время\n")
        # root.bind('<Return>', self.createrReturn)
        self.root.mainloop()

    def frame1(self):
        frame = LabelFrame()
        frame.grid(column = 1, row = 0, columnspan=1, padx=(10,10), pady=(10,10))
        
        # выбор модели
        Label(frame, text = "Фурье:" ).grid( column = 1, row = 0, pady = (0, 0), padx=(30, 0))
        self.chooseModel = Combobox(frame, values=[u"Дискретный", u"Быстрый", u"Прямоугольное окно", u"Окно Ханна", u"Окно Хемминга"])
        self.chooseModel.set(u"Дискретный")
        self.chooseModel.grid( column = 2, row=0, pady=(10, 0), padx=(5, 0))

        # N - количество точек
        
        Label(frame, text="Объем выборки:").grid( column = 1, row = 1, pady = (0, 0), padx = (30, 0))
        self.numOfPoint = StringVar()
        self.numOfPoint.set('100')
        frameNumOfPoint = Entry(frame, width = 23, textvariable = self.numOfPoint)
        frameNumOfPoint.grid(column = 2, row = 1, padx = (5, 0), pady=(10, 0))
        # frameNumOfPoint.bind("<FocusIn>", clear)

        # K - колличество членов ряда
        Label(frame, text="Количество членов ряда:").grid(column=1, row=2, pady=(0, 0), padx=(30, 0))
        self.membersOfRow = StringVar()
        self.membersOfRow.set('10')
        frameMembersOfRow = Entry(frame, width=23, textvariable = self.membersOfRow)
        frameMembersOfRow.grid(column = 2, row=2,  padx=(5, 0), pady=(10, 10))
        # frameMembersOfRow.bind("<FocusIn>", clear)

    def frame2(self):
        frame = LabelFrame(text = "Для ОПФ")
        frame.grid(column = 1, row = 1, columnspan=1,  padx=(10,10), pady=(10,10))

        # N_wind - количество окон
        Label(frame, text="Введите количество окон:").grid(column=1, row=0, padx=(30, 0), pady=(10, 10))
        self.numOfWindow = StringVar()
        self.numOfWindow.set('0')
        frameNumOfWindow = Entry(frame, width=23, textvariable = self.numOfWindow)
        frameNumOfWindow.grid(column=2, row=0, padx=(10, 0), pady=(10, 0))
        # frameNumOfWindow.bind("<FocusIn>", clear)

        # S_wind - ширина окон
        Label(frame, text="Введите размер окон:").grid(column=1, row=1, padx=(30, 0), pady=(10, 10))
        self.widthOfWindow = StringVar()
        self.widthOfWindow.set('0')
        frameWidthOfWindow = Entry(frame, width=23, textvariable = self.widthOfWindow)
        frameWidthOfWindow.grid(column=2, row=1, padx=(10, 0), pady=(10, 0))
        # frameWidthOfWindow.bind("<FocusIn>", clear)

    def frame3(self):
        frame = Frame()
        frame.grid(column = 2, row = 0, columnspan=1, rowspan=2,  padx=(10,10), pady=(10,10))

        self.button = Button(frame, text="Решить", command = self.start())
        self.button.grid(column = 9,row = 1, padx=(40, 0), pady=(0, 0))
        

        self.output = Text(frame, bg="white", font="Arial 10", width = 50, height = 12)
        self.output.grid(column=1, row = 0, columnspan = 10, rowspan=1, padx=(10, 10), pady=(10, 10))

    # def createrReturn(e): 
    #     self.start()

    def start(self):
        self.canCulc = True

    def clear(self, event):
        self.caller = event.widget
        self.caller.delete("0", "end")
    
    def insertval(self, value):
        self.output.insert("1.0", value) 


test = FrameParametrEstmation()
while test.start == True:
    test = FrameParametrEstmation()
    test.insertval("Работает")

test.insertval("не понимаю")