import math as mth

def culcDevation(F_teor, F):
    N =len(F)
    return mth.sqrt(sum(((f - ft)**2)/N for ft, f in zip(F_teor, F)))

def culcX2(F_teor, F, m, s):
    N = len(F)
    k = int(1 + mth.log2(N))
    insertval("\n %d\n" %k)
    n = N/k
    X = []
    x = []
    for i in range(1,k+1):
        X.append((F_teor[int(n*i)-1] + F_teor[int(n*(i-1))])/2)
        summ = 0
        for j in range(int(n*(i-1)), int(n*i)):
            summ+=F[j]
        x.append(summ/n)
    return sum(((x[i] - X[i])**2)/X[i] for i in range(len(X)))