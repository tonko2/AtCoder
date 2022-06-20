import sys
import heapq
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def topological_sort(inc, out):
    # 入次数が0のノード
    q = [i for i, c in enumerate(inc) if c == 0]
    res = []
    while q:
        v = heapq.heappop(q)
        res.append(v)
        for j in out[v]:
            inc[j] -= 1
            if inc[j] == 0:
                heapq.heappush(q, j)
    return res

N, M = na()
inc = [0] * N
out = [[] for _ in range(N)]

for _ in range(M):
    _ = ni()
    A = na()
    for i in range(len(A) - 1):
        inc[A[i + 1] - 1] += 1
        out[A[i] - 1].append(A[i + 1] - 1)
ans = topological_sort(inc, out)
if len(ans) == N:
    print("Yes")
else:
    print("No")