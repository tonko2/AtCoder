import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')
MOD = 998244353

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, K = na()
cnt = [0] * N
ans = 0
for i in range(K):
    tmp = ns().split()
    c = tmp[0]
    k = int(tmp[1]) - 1
    cnt[k] = -1
    if c == 'R':
        for j in range(0, k):
            if cnt[j] != -1:
                cnt[j] += 1
    else:
        for j in range(k, N):
            if cnt[j] != -1:
                cnt[j] += 1
ans = 1
for i in range(N):
    if cnt[i] != -1:
        ans = (ans * cnt[i]) % MOD
print(ans)

