from tkinter import *
from tkinter.ttk import *

from .labeles import *
from ..models import *
from ..non_parameter_estmation import NonParameterEstmation

class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.frame1()
        self.frame2()
        self.frame3()
    
    def frame1(self):
        frame = Labelframe(self)
        frame.grid(column=0, row=0)

        for i in range(len(frame1)):
            Label(frame, text=frame1[i]).grid(column=0, row=i,pady = (0, 0), padx=(30, 0))
        
        self.choose_model = Combobox(frame, values=values_model)
        self.choose_model.set(values_model[0])

        self.sample_size = StringVar()
        self.sample_size.set('100')
        frame_sample_size = Entry(frame, width = 23, textvariable = self.sample_size)

        self.members_of_row = StringVar()
        self.members_of_row.set('10')
        frame_members_of_row = Entry(frame, width=23, textvariable = self.members_of_row)

        self.choose_distribution = Combobox(frame, values = values_distribution)
        self.choose_distribution.set(values_distribution[0])

        self.choose_model.grid(          column=1, row=0, pady=(10, 0), padx=(5, 0))
        frame_sample_size.grid(           column=1, row=1, pady=(10, 0), padx=(5, 0))
        frame_members_of_row.grid(         column=1, row=2, pady=(10, 0), padx=(5, 0))
        self.choose_distribution.grid(   column=1, row=3, pady=(10, 0), padx=(5, 0))

    def frame2(self):
        frame = LabelFrame(self, text="Для ОПФ")
        frame.grid(column=0, row=1)

        Label(frame, text="Введите количество окон:").grid(column=0, row=0, pady = (0, 0), padx=(30, 0))
        Label(frame, text="Введите размер окон:"    ).grid(column=0, row=1, pady = (0, 0), padx=(30, 0))

        self.num_of_window = StringVar()
        self.num_of_window.set(0)
        frame_num_of_window = Entry(frame, width=23, textvariable = self.num_of_window)

        self.width_of_window = StringVar()
        self.width_of_window.set(0)
        frame_width_of_window = Entry(frame, width=23, textvariable = self.width_of_window)

        frame_num_of_window.grid(  column=1, row=0, pady=(10, 0), padx=(5, 0))
        frame_width_of_window.grid(column=1, row=1, pady=(10, 0), padx=(5, 0))
    
    def frame3(self):
        frame = LabelFrame(self)
        frame.grid(column=1, row=0, rowspan=2)

        self.output = Text(frame, bg="white", font="Arial 10", width = 50, height = 12)

        but_simple = Button(  frame, text="Решить", command=self.creater)
        self.output.grid(    column=0, row=0, columnspan=4)
        but_simple.grid(      column=0, row=1, padx=(40, 0), pady=(10, 0))

    def insertval(self, value):
        self.output.insert("1.0", value)
    
    def creater(self):
        text = "обычный 1 раз\n"
        sample_size = int(self.sample_size.get())
        members_of_row = int(self.members_of_row.get())
        choose_distribution = self.choose_distribution.current()
        choose_model = self.choose_model.current()
        
        npm = NonParameterEstmation(sample_size, members_of_row, choose_distribution, choose_model)
        npm.show()
        self.insertval(npm.message)