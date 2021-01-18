import math as mth

# todo:
#       - windowFourier
# 
class FourierTransform(object):
    def __init__(self, 
                randomVariables, 
                N_point, 
                K_member, 
                expectation, 
                variance, 
                c, 
                d):
        self.randomVariables = randomVariables
        self.N_point = N_point
        self.K_member = K_member
        self.expectation = expectation
        self.variance = variance
        self.c = c
        self.d = d
        
        self.scopeOfView = [c + i/(N_point)*d for i in range(N_point + 1)]

        self.N = 100
        self.F = [0]*(self.N + 1)

        self.discreteFourierTransform = self.dftFunction()
        self.fastFourierTransform = self.fftFunctoin()
        self.windowFourierTransform = self.wftFunction()

    def dftFunction(self):
        for xi in range(len(self.scopeOfView)):
            for i in range(self.K_member):
                coefficientOfDecomposition = self.coefficientOfDecompositionDFT(i)
                self.F[xi] += coefficientOfDecomposition * self.densityFunction(self.scopeOfView[xi], i)
        return self.F

    def coefficientOfDecompositionDFT(self, i):
        return sum(self.densityFunction(self.randomVariables[j], i)/self.N_point for j in range(self.N_point))

    def fftFunctoin(self):
        for xi in range(len(self.scopeOfView)):
            for i in range(self.K_member):
                coefficientOfDecomposition = self.coefficientOfDecompositionFFT(i)
                self.F[xi] += coefficientOfDecomposition * self.densityFunction(self.scopeOfView[xi], i)
        return self.F
    
    def coefficientOfDecompositionFFT(self, i):
        return sum(self.densityFunction(self.randomVariables[2*j], i)/self.N_point for j in range(int(self.N_point/2)))

    def densityFunction(self, x, smoothingFactor):
        pi = mth.pi
        if smoothingFactor == 1:
            return 1/mth.sqrt(self.d - self.c)
        elif (smoothingFactor % 2) == 0:
            return mth.sqrt(2/(self.d - self.c))*mth.sin(pi*smoothingFactor/2*(x*2/(self.d - self.c) + (self.d + self.c)/(self.d - self.c)))
        else:
            return mth.sqrt(2/(self.d - self.c))*mth.cos(pi*(smoothingFactor - 1)/2*(x*2/(self.d - self.c) + (self.d + self.c)/(self.d - self.c)))