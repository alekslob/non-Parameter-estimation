import math as mth

# todo:
#       - windowFourier
# 
class FourierTransform(object):
    def __init__(self, 
                randomVariables, 
                nPoint, 
                kMember, 
                c, 
                d):
        self.randomVariables = randomVariables
        self.nPoint = nPoint
        self.kMember = kMember

        self.c = c
        self.d = d

        self.N = 100
        self.scopeOfView = [self.c + i/(self.N)*self.d for i in range(self.N + 1)]
        self.randomVariablesFFT = [self.randomVariables[2*i] for i in range(int(len(self.randomVariables)/2))]

    def discreteFourierTransform(self):
        F = [0]*(self.N + 1)
        for f, sV in zip(F, self.scopeOfView):
            for i in range(self.kMember):
                coefficientOfDecomposition = self.coefficientOfDecompositionDFT(i)
                f += coefficientOfDecomposition * self.densityFunction(sV, i)
        return F

    def coefficientOfDecompositionDFT(self, i):
        return sum(self.densityFunction(rv, i)/self.nPoint for rv in self.randomVariables)

    def fastFourierTransform(self):
        F = [0]*(self.N + 1)
        for f, sv in zip(F, self.scopeOfView):
            for i in range(self.kMember):
                coefficientOfDecomposition = self.coefficientOfDecompositionFFT(i)
                f += 2*coefficientOfDecomposition*self.densityFunction(sv, i)
        return F
    
    def coefficientOfDecompositionFFT(self, i):
        return sum(self.densityFunction(rv, i)/self.nPoint for rv in self.randomVariablesFFT)

    def densityFunction(self, x, smoothingFactor):
        pi = mth.pi
        if smoothingFactor == 1:
            return 1/mth.sqrt(self.d - self.c)
        elif (smoothingFactor % 2) == 0:
            return mth.sqrt(2/(self.d - self.c))*mth.sin(pi*smoothingFactor/2*(x*2/(self.d - self.c) + (self.d + self.c)/(self.d - self.c)))
        else:
            return mth.sqrt(2/(self.d - self.c))*mth.cos(pi*(smoothingFactor - 1)/2*(x*2/(self.d - self.c) + (self.d + self.c)/(self.d - self.c)))