N = int(input())
L = [2 ** i for i in range(10)]
for i,l in enumerate(L):
    if l > N:
        print(L[i-1])
        exit()