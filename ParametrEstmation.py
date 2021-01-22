from RandomVariables import RandomVariables
from FourierTransform import FourierTransform
from TeoreticalFunctions import TeoreticalFunctions
import CulcResults
import InterfacePE as ipe

def creater():
    evalution = getDensityFunction()
    ipe.insertval(outputOfResults(evalution))
    # showDensityFunction(evalution)

def getDensityFunction():
    nPoint = int(ipe.sampleSize.get())
    kMember = int(ipe.membersOfRow.get())
    start = 0
    end = 4
    
    randomVariables = getRandomVariables()
    fourierTransform = FourierTransform(randomVariables,
                                        nPoint,
                                        kMember,
                                        start,
                                        end)
    return fourierTransform.getEstmation(ipe.chooseModel)
    

def getRandomVariables():
    nPoint = int(ipe.sampleSize.get())
    expectation = 0
    variance = 1

    randomVariables = RandomVariables(nPoint, expectation, variance)
    return randomVariables.getFunction(ipe.chooseDistribution)

def outputOfResults(evalution):
    teoreticalFunctions = getTeoreticalFunction()
    expectation = 0
    variance = 1

    deviation = CulcResults.culcDevation(teoreticalFunctions, evalution)
    X2 = CulcResults.culcX2(teoreticalFunctions, evalution, expectation, variance)
    # insertval(" %3f |" % X2)
    # insertval(" %3f    |" % deviation)
    return '    {:3f}   | {:3f} \n'.format(X2, deviation)



def getTeoreticalFunction():
    expectation = 0
    variance = 1
    start = -4
    end = 4

    teoreticalFunctions = TeoreticalFunctions(end-start,
                                            expectation,
                                            variance)
    return teoreticalFunctions.getFunction(ipe.chooseDistribution)
    

# def showDensityFunction(evalution):




