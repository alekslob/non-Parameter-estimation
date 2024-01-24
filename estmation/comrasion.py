import math as mth
from typing import List

class Comprasion:
    def __init__(self, teoretical: List[float], F: List[float]) -> None:
        self.teoretical = teoretical
        self.F = F
    
    @property
    def deviation(self) -> float:
        N =len(self.teoretical)
        return mth.sqrt(sum(((f - ft)**2)/N for ft, f in zip(self.teoretical, self.F)))
    
    @property
    def X2(self) -> float:
        N = len(self.F)
        k = int(1 + mth.log2(N))
        n = N/k
        X = []
        x = []
        for i in range(1,k+1):
            X.append((self.teoretical[int(n*i)-1] + self.teoretical[int(n*(i-1))])/2)
            summ = 0
            for j in range(int(n*(i-1)), int(n*i)):
                summ+=self.F[j]
            x.append(summ/n)
        return sum(((x[i] - X[i])**2)/X[i] for i in range(len(X)))
