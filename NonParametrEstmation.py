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

def createrArticleK():
    evalutions = []
    # first
    ipe.membersOfRow.set('6')
    evalutions.append(getDensityFunction())
    ipe.insertval(outputOfResults(evalutions[0]))
    
    # second
    ipe.membersOfRow.set('10')
    evalutions.append(getDensityFunction())
    ipe.insertval(outputOfResults(evalutions[1]))

    # third
    ipe.membersOfRow.set('15')
    evalutions.append(getDensityFunction())
    ipe.insertval(outputOfResults(evalutions[2]))

    showDensityFunctionArticle(evalutions)

def createrArticleN():
    evalutions = []
    # first
    ipe.sampleSize.set('100')
    evalutions.append(getDensityFunction())
    ipe.insertval(outputOfResults(evalutions[0]))
    
    # second
    ipe.sampleSize.set('500')
    evalutions.append(getDensityFunction())
    ipe.insertval(outputOfResults(evalutions[1]))

    # third
    ipe.sampleSize.set('1000')
    evalutions.append(getDensityFunction())
    ipe.insertval(outputOfResults(evalutions[2]))

    showDensityFunctionArticle(evalutions)

def createrArticleСomparison():
    evalutions = []
    ipe.chooseModel.set(ipe.valuesModel[0])
    evalutions.append(getDensityFunction())
    ipe.insertval(outputOfResults(evalutions[0]))

    ipe.chooseModel.set(ipe.valuesModel[1])
    evalutions.append(getDensityFunction())
    ipe.insertval(outputOfResults(evalutions[1]))

    showDensityFunctionArticleComparison(evalutions)


def getDensityFunction():
    nPoint = int(ipe.sampleSize.get())
    kMember = int(ipe.membersOfRow.get())
    viewLimits = getViewLimits(ipe.chooseDistribution.current())

    randomVariables = getRandomVariables()
    fourierTransform = FourierTransform(randomVariables,
                                        nPoint,
                                        kMember,
                                        viewLimits)
    return fourierTransform.getEstmation(ipe.chooseModel)
    
def getViewLimits(chooseDistribution):
    m = ipe.parametrs[0]
    s = ipe.parametrs[1]
    if chooseDistribution == 0:
        return [m-4*s, m+4*s]
    elif chooseDistribution == 1:
        return [0, 4]
    elif chooseDistribution == 2:
        return [0, 4]

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
    return '{:3f}   | {:3f} \n'.format(X2, deviation)



def getTeoreticalFunction():
    viewLimits = getViewLimits(ipe.chooseDistribution.current())
    teoreticalFunctions = TeoreticalFunctions(ipe.parametrs,
                                            viewLimits)
    return teoreticalFunctions.getFunction(ipe.chooseDistribution)
    

def showDensityFunction(evalution):
    viewLimits = getViewLimits(ipe.chooseDistribution.current())
    showFunction = ShowFunction(getTeoreticalFunction(),
                                evalution,
                                ipe.parametrs,
                                viewLimits)
    showFunction.showFunction(ipe.chooseDistribution)

def showDensityFunctionArticle(evalutions):
    viewLimits = getViewLimits(ipe.chooseDistribution.current())
    showFunction = ShowFunction(getTeoreticalFunction(),
                                evalutions,
                                ipe.parametrs,
                                viewLimits)
    showFunction.ShowFunctionArticle(ipe.chooseDistribution)

def showDensityFunctionArticleComparison(evalutions):
    viewLimits = getViewLimits(ipe.chooseDistribution.current())
    showFunction = ShowFunction(getTeoreticalFunction(),
                                evalutions,
                                ipe.parametrs,
                                viewLimits)
    showFunction.ShowFunctionArticleComparison(ipe.chooseDistribution)