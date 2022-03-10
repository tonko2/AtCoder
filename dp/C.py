import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
A, B, C = [], [], []
for _ in range(N):
    a, b, c = na()
    A.append(a)
    B.append(b)
    C.append(c)

dp = [[0] * 3 for _ in range(N + 1)]

for i in range(N):
     dp[i + 1][0] = max(dp[i + 1][0], max(dp[i][1] + A[i], dp[i][2] + A[i]))
     dp[i + 1][1] = max(dp[i + 1][1], max(dp[i][0] + B[i], dp[i][2] + B[i]))
     dp[i + 1][2] = max(dp[i + 1][2], max(dp[i][0] + C[i], dp[i][1] + C[i]))

ans = 0
for i in range(3):
    ans = max(ans, dp[N][i])
print(ans)
