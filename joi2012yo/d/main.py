import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')
MOD = 10000

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, M = na()
pasta = [0] * N
for _ in range(M):
    a, b = na()
    pasta[a - 1] = b

# dp[N日目][1日前][2日前]
dp = [[[0] * 4 for _ in range(4)] for _ in range(N + 1)]
dp[0][0][0] = 1
for i in range(N):
    for j in range(4):
        for k in range(4):
            for l in range(1, 4):
                # パスタが指定されている場合(pasta[i] != 0), 次食べるパスタはpasta[i]じゃないといけない
                if pasta[i] != 0 and pasta[i] != l:
                    continue
                # 1日前(j), 2日前(k), 今日(l)
                if j != k or k != l:
                    dp[i + 1][l][j] += dp[i][j][k]
                    dp[i + 1][l][j] %= MOD

ans = 0
for i in range(4):
    for j in range(4):
        ans = (ans + dp[N][i][j]) % MOD
print(ans)
