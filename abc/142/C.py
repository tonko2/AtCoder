import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
A = na()
d = dict()
for i in range(N):
    d[A[i]] = i + 1
ans = []
for i in range(1, N + 1):
    ans.append(d[i])
print(*ans)