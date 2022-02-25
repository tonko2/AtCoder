import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, M = na()
imos = [0] * (N + 2)
for _ in range(M):
    l, r = na()
    imos[l] += 1
    imos[r + 1] -= 1

for i in range(N):
    imos[i + 1] += imos[i]

print(imos.count(M))
