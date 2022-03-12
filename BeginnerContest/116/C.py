import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
H = na()

left = 0
ans = 0
while left != N:
    while left < N and H[left] == 0:
        left += 1

    right = left
    while right < N and H[right] != 0:
        right += 1

    v = INF
    for i in range(left, right):
        v = min(v, H[i])
    for i in range(left, right):
        H[i] -= v

    if left != N:
        ans += v

    # print(left, right)
    # print(H)
print(ans)