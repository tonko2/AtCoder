N = int(input())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())

res = 1e9
for i in range(N):
    for j in range(N):
        res = min(res, A[i] + B[j] if i == j else max(A[i], B[j]))
print(res)
