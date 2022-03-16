import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
ans = []
cur = 1
bit = 0
while N != 0:
    ans.append('B')
    if N & 1:
        ans.append('A')
    N >>= 1
print("".join(reversed(ans))[0:-1])