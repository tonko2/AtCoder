import sys
import math
from collections import defaultdict, deque, Counter

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, K = na()
S = []
for _ in range(N):
    S.append(ns())

ans = 0
for bit in range(1 << N):
    d = defaultdict(int)
    alpha = []
    for i in range(N):
        if bit & 1 << i:
            for c in S[i]:
                alpha.append(c)
    counter = Counter(alpha)
    cnt = 0
    for k, v in counter.most_common():
        if v == K:
            cnt += 1
    ans = max(ans, cnt)
print(ans)