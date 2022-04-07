import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, M = na()
S = []
for _ in range(M):
    s = input().split()
    k = int(s[0])
    tmp = []
    for i in range(1, len(s)):
        tmp.append(int(s[i]))
    S.append(tmp)
P = na()
ans = 0
for i in range(1 << N):
    ok = 0
    for j in range(M):
        switch = 0
        for k in range(len(S[j])):
            if 1 << (S[j][k] - 1) & i:
                switch += 1
        if switch % 2 == P[j]:
            ok += 1
    if ok == M:
        ans += 1
print(ans)