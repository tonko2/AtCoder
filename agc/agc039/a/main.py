import collections
import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

S = ns()
K = ni()
N = len(S)
i = 0
cnt = 0
while i < N:
    while i + 1 < N and S[i] == S[i + 1]:
        i += 2
        cnt += 1
    i += 1
if S[0] != S[-1]:
    print(cnt * K)
else:
    counter = collections.Counter(S)
    key, value = counter.most_common()[0]
    if value == N:
        print(N * K // 2)
        exit()
    a = 0
    b = 0
    c = S[0]
    for i in range(N):
        if c == S[i]:
            a += 1
        else:
            break
    for i in range(N - 1, -1, -1):
        if c == S[i]:
            b += 1
        else:
            break
    print(cnt * K - ((a // 2 + b // 2 - ((a + b) // 2))) * (K - 1))