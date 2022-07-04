import sys
import math
import heapq
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()


N, M = na()
G = [[] for _ in range(N)]
for _ in range(M):
    a, b, c, d = na()
    a -= 1
    b -= 1
    G[a].append((b, c, d))
    G[b].append((a, c, d))

# bitDP
# dp[bit][前の頂点] := 最短距離
dp = [[INF] * N for _ in range(1 << N)]
# dp2[bit][前の頂点] := 通り数
dp2 = [[0] * N for _ in range(1 << N)]
dp[0][0] = 0
dp2[0][0] = 1
for bit in range(1 << N):
    for u in range(N):
        for v, d, t in G[u]:
            if bit & (1 << v):
                continue
            if t < dp[bit][u] + d:
                continue
            if dp[bit][u] + d < dp[bit | (1 << v)][v]:
                dp[bit | (1 << v)][v] = dp[bit][u] + d
                dp2[bit | (1 << v)][v] = dp2[bit][u]
            elif dp[bit | (1 << v)][v] == dp[bit][u] + d:
                dp2[bit | (1 << v)][v] += dp2[bit][u]
if dp[(1 << N) - 1][0] == INF:
    print("IMPOSSIBLE")
else:
    print(dp[(1 << N) - 1][0], dp2[(1 << N) - 1][0])