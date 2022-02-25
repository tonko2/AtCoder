import bisect
import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
D = na()
D.sort()

ans = 0
for k in range(1, 10 ** 5 + 1):
    index = bisect.bisect(D, k)
    if index == N // 2:
        ans += 1
print(ans)