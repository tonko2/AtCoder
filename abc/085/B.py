import numpy as np

N = int(input())
d = []
for i in range(N):
    d.append(int(input()))

d = np.unique(d)
print(len(d))

'''
別解
    N = int(input())
    D = [int(input()) for _ in range(N)]
    d = list(set(D))
     
    print(len(d))
'''