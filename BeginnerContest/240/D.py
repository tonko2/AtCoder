import sys
from collections import deque
from collections import defaultdict


sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
A = na()

q = deque()
d = defaultdict(int)
for i in range(N):
    q.append(A[i])
    if d[A[i]] == 0:
        d = defaultdict(int)
    d[A[i]] += 1
    if d[A[i]] == A[i]:
        for j in range(A[i]):
            q.pop()
        if q:
            v = q.pop()
            cnt = 1
            while q:
                v2 = q.pop()
                if v2 != v:
                    q.append(v2)
                    break
                cnt += 1
            for j in range(cnt):
                q.append(v)
            d = defaultdict(int)
            d[v] = cnt
    print(len(q))
