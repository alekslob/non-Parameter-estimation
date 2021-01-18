from tkinter import *
from tkinter.ttk import *

from FrameParametrEstmation import FrameParametrEstmation
from RandomVariables import RandomVariables
from FourierTransform import FourierTransform
from TeoreticalFunction import TeoreticalFunction

def main():
    frame = FrameParametrEstmation()
    

def creater():
    evalution = getDensityFunction()
    outputOfResults(evalution)
    showDensityFunction(evalution)

def getDensityFunction():
    chooseFourierTransform = comb_mod.current()
    
    N_point = int(vN.get())
    K_member = int(vK.get())
    N_wind = int(vNw.get())
    S_wind = int(vSw.get())
    expectation = 0
    variance = 1
    randomVariables = getRandomVariables()
    fourierTransform = FourierTransform(randomVariables,
                                        N_point,
                                        K_member,
                                        expectation,
                                        variance,
                                        start,
                                        end)
    if chooseFourierTransform == 0:
        return fourierTransform.discreteFourierTransform
    elif chooseFourierTransform == 1:
        return fourierTransform.fastFourierTransform
    elif chooseFourierTransform == 2:
        return fourierTransform.windowFourierTransform

def getRandomVariables():
    chooseDistribution = 1 #!!!!!
    N_point = int(vN.get())
    expectation = 0
    variance = 1

    randomVariables = RandomVariables(N_point, expectation, variance)
    if chooseDistribution == 0:
        return randomVariables.normal
    elif chooseDistribution == 1:
        return randomVariables.expectation
    elif chooseDistribution == 2:
        return randomVariables.gamma

def outputOfResults(evalution):
    teoreticalFunction = getTeoreticalFunction()
    expectation = 0
    variance = 1

    deviation = mth.sqrt(sum(((f - ft)**2)/len(evalution) for f,ft in zip(evalution, teoreticalFunction)))
    insertval(" %3f |" % X2(len(evalution), teoreticalFunction, evalution, expectation, variance))
    insertval(" %3f    |" % q)

def X2(N, F_teor, F, m, s):
    k = int(1 + mth.log2(N))
    insertval("\n %d\n" %k)
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

def getTeoreticalFunction():
    chooseDistribution = 1 #!!!!!
    N_point = int(vN.get())
    expectation = 0
    variance = 1
    
    teoreticalFunctions = TeoreticalFunction(start-end,
                                            N_point,
                                            expectation,
                                            variance)
    if chooseDistribution == 0:
        return teoreticalFunctions.normal
    elif chooseDistribution == 1:
        return teoreticalFunctions.expectation
    elif chooseDistribution == 2:
        return teoreticalFunctions.gamma
