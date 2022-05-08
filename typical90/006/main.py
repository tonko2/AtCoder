import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, K = na()
S = ns()

nex = [[INF] * 26 for _ in range(N + 1)]

for i in range(len(S) - 1, -1, -1):
    for j in range(26):
        if ord(S[i]) - ord('a') == j:
            nex[i][j] = i
        else:
            nex[i][j] = nex[i + 1][j]

ans = ""
cur = 0
for i in range(K):
    for j in range(26):
        pos = nex[cur][j]
        l = (len(S) - pos) + i
        if l >= K:
            ans += chr(ord('a') + j)
            cur = pos + 1
            break
print(ans)