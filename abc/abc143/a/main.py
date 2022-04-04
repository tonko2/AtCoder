import sys
import math
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
L = na()
def judge(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return True
    return False

ans = 0
L.sort()
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if judge(L[i], L[j], L[k]):
                ans += 1
print(ans)
