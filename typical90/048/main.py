import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, K = na()
A = []
for i in range(N):
    a, b = na()
    A.append(b)
    A.append(a - b)
A.sort(reverse=True)

ans = 0
for i in range(K):
    ans += A[i]
print(ans)