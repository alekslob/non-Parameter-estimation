import math as mth

# todo:
#       - windowFourier
# 
class FourierTransform(object):
    def __init__(self, 
                randomVariables, 
                nPoint, 
                kMember, 
                viewLimits):
        self.randomVariables = randomVariables
        self.nPoint = nPoint
        self.kMember = kMember

        self.c = viewLimits[0]
        self.d = viewLimits[1]
        width = viewLimits[1] - viewLimits[0]

        self.N = 101
        self.scopeOfView = [viewLimits[0] + i/(self.N - 1)*width for i in range(self.N)]
        self.randomVariablesFFT = [self.randomVariables[2*i] for i in range(int(len(self.randomVariables)/2))]

    def getEstmation(self, chooseModel):
        if chooseModel == 0:
            return self.discreteFourierTransform()
        elif chooseModel == 1:
            return self.fastFourierTransform()
        elif chooseModel == 2:
            return self.windowFourierTransform()
            
    def discreteFourierTransform(self):
        F = [0]*(self.N)
        for j in range(self.N):
        # for f, sV in zip(F, self.scopeOfView):
            for i in range(self.kMember + 1):
                coefficientOfDecomposition = self.coefficientOfDecompositionDFT(i)
                F[j] += coefficientOfDecomposition * self.densityFunction(self.scopeOfView[j], i)
        return F

    def coefficientOfDecompositionDFT(self, i):
        return sum(self.densityFunction(rv, i)/self.nPoint for rv in self.randomVariables)

    def fastFourierTransform(self):
        F = [0]*(self.N)
        for j in range(self.N):
        # for f, sv in zip(F, self.scopeOfView):
            for i in range(self.kMember):
                coefficientOfDecomposition = self.coefficientOfDecompositionFFT(i)
                F[j] += 2*coefficientOfDecomposition * self.densityFunction(self.scopeOfView[j], i)
        return F
    
    def coefficientOfDecompositionFFT(self, i):
        return sum(self.densityFunction(rv, i)/self.nPoint for rv in self.randomVariablesFFT)

    def windowFourierTransform(self):
        F = [0]*(self.N )
        return F
        
    def densityFunction(self, x, smoothingFactor):
        pi = mth.pi
        if smoothingFactor == 1:
            return 1/mth.sqrt(self.d - self.c)
        elif (smoothingFactor % 2) == 0:
            return mth.sqrt(2/(self.d - self.c))*mth.sin(pi*smoothingFactor/2*(x*2/(self.d - self.c) + (self.d + self.c)/(self.d - self.c)))
        else:
            return mth.sqrt(2/(self.d - self.c))*mth.cos(pi*(smoothingFactor - 1)/2*(x*2/(self.d - self.c) + (self.d + self.c)/(self.d - self.c)))
    
    