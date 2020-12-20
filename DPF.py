from tkinter import *
from tkinter.ttk import *
import math as mth
import random as rnd
import numpy as np
import matplotlib.pyplot as plt
# from scipy.stats import pearsonr  
import time

from threading import Thread
from multiprocessing import Queue

def clear(event):
    """ Clears entry form """
    caller = event.widget
    caller.delete("0", "end")

def insertval(value):
    output.insert("1.0", value)

def func(x, i):
    pi = mth.pi
    s = float(vs.get())
    m = float(vm.get())
    c = m - 4*s
    d = m + 4*s
    if i == 1:
        p = 1/mth.sqrt(d-c)
    elif mth.trunc(i/2) == i/2:
        p = mth.sqrt(2/(d-c))*mth.sin(pi*i/2*(x*2/(d-c) + (d + c)/(d-c)))
    else:
        p = mth.sqrt(2/(d-c))*mth.cos(pi*(i-1)/2*(x*2/(d-c) + (d + c)/(d-c)))
    return p

def X2(N, F_teor, F, m, s):
    k = int(1 + mth.log2(N))
    n = N/k
    X = []
    x = []
    for i in range(1,k+1):
        X.append((F_teor[int(n*i)-1] + F_teor[int(n*(i-1))])/2)
        summ = 0
        for j in range(int(n*(i-1)), int(n*i)):
            summ+=F[j]
        x.append(summ/n)
    return sum(((x[i] - X[i])**2)/X[i] for i in range(len(X)))
            

def func_teor(T, N,m,s):
    pi = mth.pi
    return [mth.exp(-((2*T*(i - N/2)/N)**2)/(2*s*s))/(s*mth.sqrt(2*pi)) for i in range(N+1)]

def creater():
    ident = comb_mod.current()
    N_point = int(vN.get())
    K_member = int(vK.get())
    N_wind = int(vNw.get())
    S_wind = int(vSw.get())
    pi = mth.pi

    s = float(vs.get())
    m = float(vm.get())
    x = [rnd.normalvariate(m,s) for i in range(N_point + 1)]
    X_nor = sorted(x)

    if ident == 0:
        DPF(X_nor, N_point, K_member, m, s)    
    elif ident ==1:
        BPF(X_nor, N_point, K_member, m, s)
    else:
        if N_wind > 0 and S_wind > 0:
            With_Wind(X_nor, N_point, K_member, N_wind, S_wind, ident, m, s)
        else:
            insertval("Необходимо установить параметры окна")

def proc(X_itog, X_nor, N_point, K_member, S_wind, t, ident, conn):
    conn.put(get_y(X_itog, X_nor, N_point, K_member, S_wind, t, ident))

def With_Wind(X_nor, N_point, K_member, N_wind, S_wind, ident, m, s):
    T = 4*s
    N = 100
    F_teor = func_teor(T, N, m, s)
    X_itog = [2*T*((i - N/2)/N) + m for i in range(N+1)]
    labstr = 'N('+str(m)+','+str(s)+')'
    plt.figure()
    plt.grid()
    plt.plot(X_itog, F_teor, linestyle = '--', linewidth = 2, color = 'black', label=labstr)

    for N_point in [100, 500, 1000]:
        x = [rnd.normalvariate(m,s) for i in range(N_point + 1)]
        X_nor = sorted(x)
        F = [0]*(N+1)
        T = 4*s
        N = 100
        F_teor = func_teor(T, N, m, s)
        X_itog = [2*T*((i - N/2)/N) + m for i in range(N+1)]
        start_itme = time.time()

        z = [get_y(X_itog, X_nor, N_point, K_member, S_wind, int(t*N/N_wind), ident) for t in range(N_wind)]
        # threads = []
        # Conn = Queue()
        # for t in range(N_wind):
        #     thread = Thread(target=proc, args=(X_itog, X_nor, N_point, K_member, S_wind, int(t*N/N_wind), ident, Conn))
        #     threads.append(thread)
        #     thread.start()
        # for thread in threads:
        #     z.append(Conn.get())
        #     thread.join()

        time_RES = time.time() - start_itme
        F = [z[0][i] for i in range(N+1)]
        k = 0
        for t in range(1, N_wind):
            for i in range(N+1):
                if F[i] < z[t][i]:
                    F[i] = z[t][i]
            k+=1
        
        q = mth.sqrt(sum(((F[i]-F_teor[i])**2)/N for i in range(N + 1)))
        insertval("\n")
        insertval("Среднеквадратичное отклонение = %3f \n" % q)
        insertval("X2 = %3f \n" % X2(N, F_teor, F, m, s))
        insertval("Время работы = %3f \n" % time_RES)
        labstr = 'N = ' + str(N_point) + ', K = ' + str(K_member)
        plt.plot(X_itog, F, label = labstr)
    plt.legend()
   
    # v, u = np.mgrid[0:N_wind:N_wind*1j, -4:4:(N+1)*1j]
    # x = v
    # y = u
    # z = np.array([np.array([1]*(N+1)) for t in z])*z
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    # ax.plot_surface(x, y, z, cmap='inferno')
    plt.show()
    return F

def Window(n, S_wind, ident):
    pi = mth.pi
    
    if ident == 2:
        # прямоугольное
        if n >= 0 and n < S_wind:
            return 1.
        else:
            return 0
    elif ident == 3:
        # Ханна
        return 0.5*(1 - mth.cos(2*pi*(n)/(S_wind-1)))
    elif ident == 4:
        # Хемминга
        return 0.53836 - 0.46164*mth.cos(2*pi*(n)/(S_wind-1))

def get_y(X_itog, X_nor, N_points, K_member, S_wind, t, ident):
    w2 = [Window(i-t, S_wind, ident) for i in range(len(X_itog))]
    F = [0]*len(X_itog)
    for xi in range(len(X_itog)):
        for i in range(K_member):
            Cn = 0
            for j in range(N_points):
                Cn += func(X_nor[j], i)/N_points
            F[xi] += Cn * func(X_itog[xi], i)*w2[xi]
    return F

def createrReturn(e): 
    creater()

root = Tk()
frame = LabelFrame()
frame.grid(column = 1, row = 0, columnspan=1, padx=(10,10), pady=(10,10))
frame2 = LabelFrame(text = "Для ОПФ")
frame2.grid(column = 1, row = 1, columnspan=1,  padx=(10,10), pady=(10,10))
frame3 = Frame()
frame3.grid(column = 2, row = 0, columnspan=1, rowspan=2,  padx=(10,10), pady=(10,10))

# выбор модели
lab_mod = Label(frame, text = "Фурье:" ).grid( column = 1, row = 0, pady = (0, 0), padx=(30, 0))
comb_mod = Combobox(frame, values=[u"Дискретный", u"Быстрый", u"Прямоугольное окно", u"Окно Ханна", u"Окно Хемминга"])
comb_mod.set(u"Дискретный")
comb_mod.grid( column = 2, row=0, pady=(10, 0), padx=(5, 0))

# N - количество точек
lab_N = Label(frame, text="Объем выборки:").grid( column = 1, row = 1, pady = (0, 0), padx = (30, 0))
vN = StringVar()
vN.set('100')
rN = Entry(frame, width = 23, textvariable = vN)
rN.grid(column = 2, row = 1, padx = (5, 0), pady=(10, 0))
rN.bind("<FocusIn>", clear)

# K - колличество членов ряда
lab_K = Label(frame, text="Количество членов ряда:").grid(column=1, row=2, pady=(0, 0), padx=(30, 0))
vK = StringVar()
vK.set('10')
rK = Entry(frame, width=23, textvariable=vK)
rK.grid(column = 2, row=2,  padx=(5, 0), pady=(10, 10))
rK.bind("<FocusIn>", clear)

# N_wind - количество окон
lab_Nw = Label(frame2, text="Введите количество окон:").grid(column=1, row=0, padx=(30, 0), pady=(10, 10))
vNw = StringVar()
vNw.set('0')
wN = Entry(frame2, width=23, textvariable=vNw)
wN.grid(column=2, row=0, padx=(10, 0), pady=(10, 0))
wN.bind("<FocusIn>", clear)

# S_wind - ширина окон
lab_Sw = Label(frame2, text="Введите размер окон:").grid(column=1, row=1, padx=(30, 0), pady=(10, 10))
vSw = StringVar()
vSw.set('0')
wS = Entry(frame2, width=23, textvariable=vSw)
wS.grid(column=2, row=1, padx=(10, 0), pady=(10, 0))
wS.bind("<FocusIn>", clear)

but = Button(frame3, text="Решить", command=creater)
but.grid(column = 9,row = 1, padx=(40, 0), pady=(0, 0))
root.bind('<Return>', createrReturn)

output = Text(frame3, bg="white", font="Arial 10", width = 50, height = 12)
output.grid(column=1, row = 0, columnspan = 10, rowspan=1, padx=(10, 10), pady=(10, 10))

vm = StringVar()
vm.set('0')
vs = StringVar()
vs.set('1')

root.mainloop()