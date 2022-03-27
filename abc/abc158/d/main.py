import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

S = ns()
d = deque(S)
Q = ni()
cur = 0
for _ in range(Q):
    q = list(map(str, input().split()))
    t = int(q[0])
    if t == 1:
        cur = 1 - cur
    if t == 2:
        f, c = int(q[1]), q[2]
        if f == 1:
            if cur == 0:
                d.appendleft(c)
            else:
                d.append(c)
        else:
            if cur == 0:
                d.append(c)
            else:
                d.appendleft(c)
if not cur:
    d.reverse()
ans = []
while d:
    ans.append(d.pop())
print("".join(ans))
