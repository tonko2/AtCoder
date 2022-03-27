import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, M = na()
A = na()
C = na()
A.reverse()
C.reverse()
ans = []

for i in range(M + 1):
    n = C[i] // A[0]
    ans.append(n)
    for j in range(N):
        C[i + j + 1] -= n * A[j + 1]
ans.reverse()
print(*ans)