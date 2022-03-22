import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, K = na()
A = na()
d = defaultdict(int)
for a in A:
    d[a] += 1

arr = []
for key in d.keys():
    arr.append((d[key], key))
arr.sort()
ans = 0
for i in range(len(arr)):
    if K >= len(d.keys()):
        break
    ans += arr[i][0]
    K += 1

print(ans)

