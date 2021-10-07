
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb

import NonParametrEstmation as npe


def sendErrMes(text):
    mb.showerror(
            "Message", 
            text)
def sendInfMes(text):
    mb.showinfo(
            "Message", 
            text)

class App(Tk):
    def __init__(self, valuesModel, valuesDistribution):
        super().__init__()
        self.valuesModel = valuesModel
        self.valuesDistribution = valuesDistribution
        self.frame1()
        self.frame2()
        self.frame3()
    
    def frame1(self):
        frame = LabelFrame(self)
        frame.grid(column=0, row=0)

        Label(frame, text = "Фурье: "               ).grid(column=0, row=0,pady = (0, 0), padx=(30, 0))
        Label(frame, text="Объем выборки: "         ).grid(column=0, row=1,pady = (0, 0), padx=(30, 0))
        Label(frame, text="Количество членов ряда:" ).grid(column=0, row=2,pady = (0, 0), padx=(30, 0))
        Label(frame, text = "Функция распределения:").grid(column=0, row=3,pady = (0, 0), padx=(30, 0))

        self.chooseModel = Combobox(frame, values=self.valuesModel)
        self.chooseModel.set(self.valuesModel[0])

        self.sampleSize = StringVar()
        self.sampleSize.set('100')
        frameSampleSize = Entry(frame, width = 23, textvariable = self.sampleSize)

        self.membersOfRow = StringVar()
        self.membersOfRow.set('10')
        frameMembersOfRow = Entry(frame, width=23, textvariable = self.membersOfRow)

        self.chooseDistribution = Combobox(frame, values = self.valuesDistribution)
        self.chooseDistribution.set(self.valuesDistribution[0])
        


        self.chooseModel.grid(          column=1, row=0, pady=(10, 0), padx=(5, 0))
        frameSampleSize.grid(           column=1, row=1, pady=(10, 0), padx=(5, 0))
        frameMembersOfRow.grid(         column=1, row=2, pady=(10, 0), padx=(5, 0))
        self.chooseDistribution.grid(   column=1, row=3, pady=(10, 0), padx=(5, 0))

    
    def frame2(self):
        frame = LabelFrame(self, text="Для ОПФ")
        frame.grid(column=0, row=1)

        Label(frame, text="Введите количество окон:").grid(column=0, row=0, pady = (0, 0), padx=(30, 0))
        Label(frame, text="Введите размер окон:"    ).grid(column=0, row=1, pady = (0, 0), padx=(30, 0))

        self.numOfWindow = StringVar()
        self.numOfWindow.set(0)
        frameNumOfWindow = Entry(frame, width=23, textvariable = self.numOfWindow)

        self.widthOfWindow = StringVar()
        self.widthOfWindow.set(0)
        frameWidthOfWindow = Entry(frame, width=23, textvariable = self.widthOfWindow)

        frameNumOfWindow.grid(  column=1, row=0, pady=(10, 0), padx=(5, 0))
        frameWidthOfWindow.grid(column=1, row=1, pady=(10, 0), padx=(5, 0))



    def frame3(self):
        frame = LabelFrame(self)
        frame.grid(column=1, row=0, rowspan=2)

        self.output = Text(frame, bg="white", font="Arial 10", width = 50, height = 12)
        
        butSimple = Button(  frame, text="Решить", command=self.creater)
        butArticleK = Button(frame, text="СреднийN", command=self.createrArticleK)
        butArticleN = Button(frame, text="СреднийK", command=self.createrArticleN)
        butArticleСomparison = Button(frame, text="Сравнение", command = self.createrArticleС)

        self.output.grid(    column=0, row=0, columnspan=4)
        butSimple.grid(      column=0, row=1, padx=(40, 0), pady=(10, 0))
        butArticleK.grid(    column=1, row=1, padx=(40, 0), pady=(10, 0))
        butArticleN.grid(    column=2, row=1, padx=(40, 0), pady=(10, 0))
        butArticleСomparison.grid(column=3, row=1, padx=(40, 40), pady=(10, 0))

    def insertval(self, value):
        self.output.insert("1.0", value)

    def creater(self):
        text = "обычный 1 раз\n"
        sampleSize = int(self.sampleSize.get())
        membersOfRow = int(self.membersOfRow.get())
        chooseDistribution = self.chooseDistribution.current()
        chooseModel = self.chooseModel.current()
        text = npe.creater(sampleSize, membersOfRow, chooseDistribution, chooseModel)
        self.insertval(text)

    def createrArticleK(self):
        text = "средний по N\n"
        sampleSize = int(self.sampleSize.get())
        membersOfRow = int(self.membersOfRow.get())
        chooseDistribution = self.chooseDistribution.current()
        chooseModel = self.chooseModel.current()
        text = npe.createrArticleK(sampleSize, membersOfRow, chooseDistribution, chooseModel)
        self.insertval(text)

    def createrArticleN(self):
        text = "средний по K\n"
        sampleSize = int(self.sampleSize.get())
        membersOfRow = int(self.membersOfRow.get())
        chooseDistribution = self.chooseDistribution.current()
        chooseModel = self.chooseModel.current()
        text = npe.createrArticleN(sampleSize, membersOfRow, chooseDistribution, chooseModel)
        self.insertval(text)

    def createrArticleС(self):
        text = "сравнение\n"
        sampleSize = int(self.sampleSize.get())
        membersOfRow = int(self.membersOfRow.get())
        chooseDistribution = self.chooseDistribution.current()
        chooseModel = self.chooseModel.current()
        text = npe.createrArticleСomparison(sampleSize, membersOfRow, chooseDistribution, chooseModel)
        self.insertval(text)
    

if __name__ == "__main__":
    app = App(npe.valuesModel, npe.valuesDistribution)
    app.mainloop()