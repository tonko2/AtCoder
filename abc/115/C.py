import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, K = na()
H = [ni() for _ in range(N)]
H.sort()
ans = float('inf')
for i in range(N - K + 1):
    min_v = H[i]
    max_v = H[K + i - 1]
    ans = min(ans, max_v - min_v)
print(ans)