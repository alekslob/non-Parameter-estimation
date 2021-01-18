import math as mth

# todo:
#       - убрать T, N и тд
#       
class TeoreticalFunctions(object):
    def __init__(self,
                width, 
                numOfPoint, 
                expectation, 
                variance):
        self.width = width
        self.numOfPoint = numOfPoint
        self.expectation = expectation
        self.variance = variance
        self.lambd = 0.5 

        self.normal = self.normalFunction()
        self.exponential = self.exponentialFunction()
        self.gamma = self.gammaFunction()
        self.beta = self.betaFunction()
    
    def normalFunction(self):
        pi = mth.pi
        T = self.width
        N = self.numOfPoint
        m = self.expectation
        s = self.variance
        return [mth.exp(-((2*T*(i - N/2)/N)**2)/(2*s*s))/(s*mth.sqrt(2*pi)) for i in range(N+1)]

    def exponentialFunction(self):
        pi = mth.pi
        T = self.width
        N = self.numOfPoint
        m = self.expectation
        s = self.variance
        return [self.lambd*mth.exp(-self.lambd*(2*T*(i)/N)) for i in range(N+1)]
    
    def gammaFunction(self):
        pi = mth.pi
        T = self.width
        N = self.numOfPoint
        m = self.expectation
        s = self.variance
        alf = m/s
        k = m*m/s
        return [((2*T*i/N)**(k-1))*mth.exp(-(2*T*i/N)*alf)*(alf**k)/mth.gamma(k) for i in range(N+1)]

    def betaFunction(self):
        T = self.width
        N = self.numOfPoint
        m = self.expectation
        s = self.variance
        alf = 2
        bet = 2
        return [((2*T*i/N)**(alf-1))*((1-(2*T*i/N))**(bet-1))/mth.beta(alf, bet) for i in range(N+1)]
        