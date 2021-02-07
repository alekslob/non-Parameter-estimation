import matplotlib.pyplot as plt

class ShowFunction(object):
    def __init__(self,
                fTeor,
                F,
                data,
                viewLimits
                ):
        self.F = F
        self.fTeor = fTeor
        self.data = data
        width = viewLimits[1]-viewLimits[0]
        N = 101
        self.scopeOfView = [viewLimits[0] + i/(N-1)*width for i in range(N)]


    def  showFunction(self, chooseDistribution):
        
        labstr = self.getLable(chooseDistribution.current())
        plt.figure()
        plt.grid()
        plt.plot(self.scopeOfView, self.fTeor, linestyle = '--', linewidth = 2, color = 'black', label=labstr)
        plt.plot(self.scopeOfView, self.F, label = 'f(x)')
        plt.legend()
        plt.show()

    def  ShowFunctionArticle(self, chooseDistribution):
        labstr = self.getLable(chooseDistribution.current())
        plt.figure()
        plt.grid()
        plt.plot(self.scopeOfView, self.fTeor, linestyle = 'solid', color = 'black', label='$\it{N(0,1)}$')
        plt.plot(self.scopeOfView, self.F[0], linestyle = 'dashed', label = '$\it{f(x), N=100}$')
        plt.plot(self.scopeOfView, self.F[1], linestyle = 'dashdot', label = '$\it{f(x), N=500}$')
        plt.plot(self.scopeOfView, self.F[2], linestyle = 'dotted', label = '$\it{f(x), N=1000}$')
        plt.legend()
        plt.show()
    
    def ShowFunctionArticleComparison(self, chooseDistribution):
        labstr = self.getLable(chooseDistribution.current())
        plt.figure()
        plt.grid()
        plt.plot(self.scopeOfView, self.fTeor, linestyle = 'solid', color = 'black', label='$\it{N(0,1)}$')
        plt.plot(self.scopeOfView, self.F[0], linestyle = 'dashed', label = '$\it{ f_N (t), ДПФ}$')
        plt.plot(self.scopeOfView, self.F[1], linestyle = 'dashdot', label = '$\it{f_N (t), БПФ}$')
        plt.legend()
        plt.show()

    def getLable(self, chooseDistribution):
        if chooseDistribution == 0:
            return 'N('+str(self.data[0]) +','+str(self.data[1])+')'
        elif chooseDistribution == 1:
            return 'Exp('+str(self.data[2])+')'
        elif chooseDistribution == 2:
            return 'Г('+str(self.data[3])+','+str(self.data[4])+')'
