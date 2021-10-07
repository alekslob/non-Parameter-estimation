from RandomVariables import RandomVariables
from FourierTransform import FourierTransform
from TeoreticalFunctions import TeoreticalFunctions
import CulcResults
# import InterfacePE as ipe
from ShowFunction import ShowFunction 

valuesModel = [u"Дискретный", u"Быстрый", u"Прямоугольное окно", u"Окно Ханна", u"Окно Хемминга"]
valuesDistribution = [u"Нормальное распределение", u"Экспоненциальное распределение", u"Гамма-распределение"]

def creater(sampleSize, membersOfRow, chooseDistribution, chooseModel):
    evalution = getDensityFunction(sampleSize, membersOfRow, chooseDistribution, chooseModel)
    # ipe.insertval(outputOfResults(evalution))
    showDensityFunction(evalution, chooseDistribution)
    result = outputOfResults(evalution, chooseDistribution)
    return result

def createrArticleK(sampleSize, membersOfRow, chooseDistribution, chooseModel):
    evalutions = []
    # first
    result = ""
    i = 0
    for members in [6, 10, 15]:
    # membersOfRow = 6
        evalutions.append(getDensityFunction(sampleSize, members, chooseDistribution, chooseModel))
        result += "Параметр сглаживания = " + str(members) + "\n" + outputOfResults(evalutions[i], chooseDistribution)
        i+=1
    
    showDensityFunctionArticleK(evalutions, chooseDistribution)
    return result

def createrArticleN(sampleSize, membersOfRow, chooseDistribution, chooseModel):
    evalutions = []
    result = ""
    i=0
    # first
    for size in [100, 500, 1000]:
    # ipe.sampleSize.set('100')
        evalutions.append(getDensityFunction(size, membersOfRow, chooseDistribution, chooseModel))
        result += "Объем выборки = " + str(size) + "\n" + outputOfResults(evalutions[i], chooseDistribution)
        i+=1
    
    showDensityFunctionArticleN(evalutions, chooseDistribution)
    return result

def createrArticleСomparison(sampleSize, membersOfRow, chooseDistribution, chooseModel):
    evalutions = []
    result = ""
    # ipe.chooseModel.set(ipe.valuesModel[0])
    chm = 0
    evalutions.append(getDensityFunction(sampleSize, membersOfRow, chooseDistribution, chm))
    result += str(valuesModel[chm]) + ":\n" + outputOfResults(evalutions[0], chooseDistribution)

    # ipe.chooseModel.set(ipe.valuesModel[1])
    chm = 1
    evalutions.append(getDensityFunction(sampleSize, membersOfRow, chooseDistribution, chm))
    result += str(valuesModel[chm]) + ":\n" + outputOfResults(evalutions[1], chooseDistribution)

    showDensityFunctionArticleComparison(evalutions, chooseDistribution)
    return result


def getDensityFunction(sampleSize, membersOfRow, chooseDistribution, chooseModel):
    nPoint = sampleSize
    kMember = membersOfRow
    viewLimits = getViewLimits(chooseDistribution)

    randomVariables = getRandomVariables(nPoint, chooseDistribution)
    fourierTransform = FourierTransform(randomVariables,
                                        nPoint,
                                        kMember,
                                        viewLimits)
    return fourierTransform.getEstmation(chooseModel)

parametrs = [0,1,0.5,9,2]

def getViewLimits(chooseDistribution):
    m = parametrs[0]
    s = parametrs[1]
    if chooseDistribution == 0:
        return [m-4*s, m+4*s]
    elif chooseDistribution == 1:
        return [0, 4]
    elif chooseDistribution == 2:
        return [0, 4]

def getRandomVariables(nPoint, chooseDistribution):
    # nPoint = int(ipe.sampleSize.get())

    randomVariables = RandomVariables(nPoint, parametrs)
    return randomVariables.getFunction(chooseDistribution)

def outputOfResults(evalution, chooseDistribution):
    teoreticalFunctions = getTeoreticalFunction(chooseDistribution)

    deviation = CulcResults.culcDevation(teoreticalFunctions, evalution)
    X2 = CulcResults.culcX2(teoreticalFunctions, evalution)
    # insertval(" %3f |" % X2)
    # insertval(" %3f    |" % deviation)
    return 'X2 = {:3f}   | D = {:3f} \n'.format(X2, deviation)



def getTeoreticalFunction(chooseDistribution):
    viewLimits = getViewLimits(chooseDistribution)
    teoreticalFunctions = TeoreticalFunctions(parametrs,
                                            viewLimits)
    return teoreticalFunctions.getFunction(chooseDistribution)
    

def showDensityFunction(evalution, chooseDistribution):
    viewLimits = getViewLimits(chooseDistribution)
    showFunction = ShowFunction(getTeoreticalFunction(chooseDistribution),
                                evalution,
                                parametrs,
                                viewLimits)
    showFunction.showFunction(chooseDistribution)

def showDensityFunctionArticleN(evalutions, chooseDistribution):
    viewLimits = getViewLimits(chooseDistribution)
    showFunction = ShowFunction(getTeoreticalFunction(chooseDistribution),
                                evalutions,
                                parametrs,
                                viewLimits)
    showFunction.ShowFunctionArticleN(chooseDistribution)

def showDensityFunctionArticleK(evalutions, chooseDistribution):
    viewLimits = getViewLimits(chooseDistribution)
    showFunction = ShowFunction(getTeoreticalFunction(chooseDistribution),
                                evalutions,
                                parametrs,
                                viewLimits)
    showFunction.ShowFunctionArticleK(chooseDistribution)

def showDensityFunctionArticleComparison(evalutions, chooseDistribution):
    viewLimits = getViewLimits(chooseDistribution)
    showFunction = ShowFunction(getTeoreticalFunction(chooseDistribution),
                                evalutions,
                                parametrs,
                                viewLimits)
    showFunction.ShowFunctionArticleComparison(chooseDistribution)