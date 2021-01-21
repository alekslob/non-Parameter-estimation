import math as mth

def culcDevation(fTeor, F):
    N =len(fTeor)
    return mth.sqrt(sum(((f - ft)**2)/N for ft, f in zip(fTeor, F)))

def culcX2(fTeor, F, m, s):
    N = len(F)
    k = int(1 + mth.log2(N))
    n = N/k
    X = []
    x = []
    for i in range(1,k+1):
        X.append((fTeor[int(n*i)-1] + fTeor[int(n*(i-1))])/2)
        summ = 0
        for j in range(int(n*(i-1)), int(n*i)):
            summ+=F[j]
        x.append(summ/n)
    return sum(((x[i] - X[i])**2)/X[i] for i in range(len(X)))