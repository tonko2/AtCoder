N, M = map(int, input().split())
A = []
for i in range(M):
    a, b = map(int, input().split())
    A.append(a)
    A.append(b)
for i in range(1, N+1):
    print(A.count(i))