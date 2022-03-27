import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
A = []
B = []
for _ in range(N):
    a, b = na()
    A.append(a)
    B.append(b)
A.reverse()
B.reverse()
ans = 0

for i in range(N):
    if ((A[i] + ans) % B[i]) != 0:
        ans += B[i] - ((A[i] + ans) % B[i])
print(ans)
