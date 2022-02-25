import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
P = na()
ans = 0
min_v = float('inf')
for i in range(N):
    min_v = min(min_v, P[i])
    if min_v == P[i]:
        ans += 1
print(ans)