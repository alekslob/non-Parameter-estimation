import random as rnd

class RandomVariables(object):
    def __init__(self,
                numOfPoint,
                expectation, 
                variance):
        self.numOfPoint = numOfPoint
        self.expectation = expectation
        self.variance = variance

        self.normal = self.normalRandom()
        self.exponential = self.exponentialRandom()
        self.gamma = self.gammaRandom()
        self.beta = self.betaRandom()

    def normalRandom(self):
        return sorted([rnd.normalvariate(self.expectation,self.variance) for i in range(self.numOfPoint + 1)])

    def exponentialRandom(self):
        return sorted([rnd.expovariate(0.5) for i in range(self.numOfPoint + 1)])
    
    # todo: разобраться с k и alf
    def gammaRandom(self):
        alf = self.variance/self.expectation
        k = self.expectation*self.expectation/self.variance
        return sorted([rnd.gammavariate(k, alf) for i in range(self.numOfPoint + 1)])

    def betaRandom(self):
        return sorted([rnd.betavariate(2,2) for i in range(self.numOfPoint + 1)])