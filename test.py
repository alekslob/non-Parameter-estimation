import random as rnd
N_point = 100
x = [rnd.gammavariate(2, 2) for i in range(N_point + 1)]
print(max(x), min(x))
countx = [0]*10
for i in range(10):
    for xi in x:
        if(i*2 < xi <= (i*2+2)):
            countx[i]+=1
print(countx)

# print(x)

