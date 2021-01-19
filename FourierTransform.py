import math as mth

# todo:
#       - windowFourier
# 
class FourierTransform(object):
    def __init__(self, 
                randomVariables, 
                nPoint, 
                kMember, 
                expectation, 
                variance, 
                c, 
                d):
        self.randomVariables = randomVariables
        self.nPoint = nPoint
        self.kMember = kMember
        self.expectation = expectation
        self.variance = variance
        self.c = c
        self.d = d
        
        self.scopeOfView = [c + i/(nPoint)*d for i in range(nPoint + 1)]

        self.N = 100
        self.F = [0]*(self.N + 1)

        # self.discreteFourierTransform = self.dftFunction()
        # self.fastFourierTransform = self.fftFunctoin()
        # self.windowFourierTransform = self.wftFunction()

    def discreteFourierTransform(self):
        for xi in range(len(self.scopeOfView)):
            for i in range(self.kMember):
                coefficientOfDecomposition = self.coefficientOfDecompositionDFT(i)
                self.F[xi] += coefficientOfDecomposition * self.densityFunction(self.scopeOfView[xi], i)
        return self.F

    def coefficientOfDecompositionDFT(self, i):
        return sum(self.densityFunction(self.randomVariables[j], i)/self.nPoint for j in range(self.nPoint))

    def fastFourierTransform(self):
        for xi in range(len(self.scopeOfView)):
            for i in range(self.kMember):
                coefficientOfDecomposition = self.coefficientOfDecompositionFFT(i)
                self.F[xi] += coefficientOfDecomposition * self.densityFunction(self.scopeOfView[xi], i)
        return self.F
    
    def coefficientOfDecompositionFFT(self, i):
        return sum(self.densityFunction(self.randomVariables[2*j], i)/self.nPoint for j in range(int(self.nPoint/2)))

    def densityFunction(self, x, smoothingFactor):
        pi = mth.pi
        if smoothingFactor == 1:
            return 1/mth.sqrt(self.d - self.c)
        elif (smoothingFactor % 2) == 0:
            return mth.sqrt(2/(self.d - self.c))*mth.sin(pi*smoothingFactor/2*(x*2/(self.d - self.c) + (self.d + self.c)/(self.d - self.c)))
        else:
            return mth.sqrt(2/(self.d - self.c))*mth.cos(pi*(smoothingFactor - 1)/2*(x*2/(self.d - self.c) + (self.d + self.c)/(self.d - self.c)))