A = list(map(int, input().split()))
K = int(input())

A.sort()
for _ in range(K):
    A[2] *= 2
print(sum(A))

