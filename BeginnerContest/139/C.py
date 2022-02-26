import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
H = na()
l = 0
r = 1
ans = 0
while l < N:
    pos = l
    while r < N and H[l] >= H[r]:
        l += 1
        r += 1
    ans = max(ans, r - pos)
    l += 1
    r += 1

print(ans - 1)