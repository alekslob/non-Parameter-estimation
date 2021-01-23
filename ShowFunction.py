import matplotlib.pyplot as plt

class ShowFunction(object):
    def __init__(self,
                fTeor,
                F,
                data,
                viewLimits):
        self.F = F
        self.fTeor = fTeor
        self.data = data
        width = viewLimits[1]-viewLimits[0]
        N = len(F)
        self.scopeOfView = [viewLimits[0] + i/(N-1)*width for i in range(N)]


    def  showFunction(self, chooseDistribution):
        labstr = self.getLable(chooseDistribution.current())
        plt.figure()
        plt.grid()
        plt.plot(self.scopeOfView, self.fTeor, linestyle = '--', linewidth = 2, color = 'black', label=labstr)
        plt.plot(self.scopeOfView, self.F, label = 'f(x)')
        plt.legend()
        plt.show()

    def getLable(self, chooseDistribution):
        if chooseDistribution == 0:
            return 'N('+str(self.data[0]) +','+str(self.data[1])+')'
        elif chooseDistribution == 1:
            return 'Exp('+str(self.data[2])+')'
        elif chooseDistribution == 2:
            return 'Г('+str(self.data[3])+','+str(self.data[4])+')'
