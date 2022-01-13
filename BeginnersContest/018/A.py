A = []
B = []
for i in range(3):
    a = int(input())
    A.append(a)
    B.append(a)

B = sorted(B, reverse=True)

D = dict()
for i in range(3):
    D[B[i]] = i + 1

for i in range(3):
    print(D[A[i]])