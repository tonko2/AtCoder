import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, K = na()
H = na()
INF = float('inf')
dp = [INF] * N
dp[0] = 0
for i in range(N - 1):
    for k in range(1, K + 1):
        if i + k < N:
            dp[i + k] = min(dp[i + k], dp[i] + abs(H[i] - H[i + k]))
print(dp[N - 1])