from RandomVariables import RandomVariables
from FourierTransform import FourierTransform
from TeoreticalFunctions import TeoreticalFunctions
import CulcResults
import InterfacePE as ipe
from ShowFunction import ShowFunction 

def creater():
    evalution = getDensityFunction()
    ipe.insertval(outputOfResults(evalution))
    showDensityFunction(evalution)

def getDensityFunction():
    nPoint = int(ipe.sampleSize.get())
    kMember = int(ipe.membersOfRow.get())
    
    randomVariables = getRandomVariables()
    fourierTransform = FourierTransform(randomVariables,
                                        nPoint,
                                        kMember,
                                        ipe.viewLimits)
    return fourierTransform.getEstmation(ipe.chooseModel)
    

def getRandomVariables():
    nPoint = int(ipe.sampleSize.get())

    randomVariables = RandomVariables(nPoint, ipe.parametrs)
    return randomVariables.getFunction(ipe.chooseDistribution)

def outputOfResults(evalution):
    teoreticalFunctions = getTeoreticalFunction()

    deviation = CulcResults.culcDevation(teoreticalFunctions, evalution)
    X2 = CulcResults.culcX2(teoreticalFunctions, evalution)
    # insertval(" %3f |" % X2)
    # insertval(" %3f    |" % deviation)
    return '    {:3f}   | {:3f} \n'.format(X2, deviation)



def getTeoreticalFunction():
    teoreticalFunctions = TeoreticalFunctions(ipe.parametrs,
                                            ipe.viewLimits)
    return teoreticalFunctions.getFunction(ipe.chooseDistribution)
    

def showDensityFunction(evalution):
    showFunction = ShowFunction(getTeoreticalFunction(),
                                evalution,
                                ipe.parametrs,
                                ipe.viewLimits)
    showFunction.showFunction(ipe.chooseDistribution)