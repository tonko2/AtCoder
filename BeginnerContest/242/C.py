import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

MOD = 998244353

N = ni()

dp = [[0] * 10 for _ in range(N + 1)]
for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N + 1):
    for j in range(2, 9):
        dp[i][j] = (dp[i][j] + dp[i - 1][j] + dp[i - 1][j - 1] + dp[i - 1][j + 1]) % MOD
    dp[i][1] = (dp[i][1] + dp[i - 1][1] + dp[i - 1][2]) % MOD
    dp[i][9] = (dp[i][9] + dp[i - 1][9] + dp[i - 1][8]) % MOD

ans = 0
for i in range(1, 10):
    ans = (ans + dp[N][i]) % MOD
print(ans)