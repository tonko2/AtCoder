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
C = na()
cnt = 0
d = defaultdict(int)
for i in range(K):
    if d[C[i]] == 0:
        cnt += 1
    d[C[i]] += 1
ans = cnt
left = 0
right = K
while right < N:
    if d[C[left]] == 1:
        cnt -= 1
    d[C[left]] -= 1
    if d[C[right]] == 0:
        cnt += 1
    d[C[right]] += 1
    ans = max(ans, cnt)
    left += 1
    right += 1

print(ans)