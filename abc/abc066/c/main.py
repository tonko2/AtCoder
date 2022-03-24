import sys
from collections import defaultdict, deque


sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
A = na()
d = deque([])
for i in range(N):
    if i % 2 == 0:
        d.append(A[i])
    else:
        d.appendleft(A[i])
ans = []
while d:
    ans.append(d.pop())
if N % 2 == 0:
    ans = reversed(ans)
    print(*ans)
else:
    print(*ans)
