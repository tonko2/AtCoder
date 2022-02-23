import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, X = na()
dp = [[0] * (X + 1) for _ in range(N + 1)]
A = [0] * (N + 1)
B = [0] * (N + 1)
for i in range(1, N + 1):
    A[i], B[i] = na()

dp[0][0] = 1

for i in range(1, N + 1):
    for j in range(X + 1):
        if j - A[i] >= 0 and dp[i - 1][j - A[i]] == 1:
            dp[i][j] = 1
        if j - B[i] >= 0 and dp[i - 1][j - B[i]] == 1:
            dp[i][j] = 1

if dp[N][X]:
    print("Yes")
else:
    print("No")
