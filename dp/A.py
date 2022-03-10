import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
H = na()
INF = float('inf')
dp = [INF] * (N + 1)
dp[0] = 0
for i in range(N - 1):
    dp[i + 1] = min(dp[i + 1], dp[i] + abs(H[i + 1] - H[i]))
    if i + 2 < N:
        dp[i + 2] = min(dp[i + 2], dp[i] + abs(H[i + 2] - H[i]))
print(dp[N - 1])