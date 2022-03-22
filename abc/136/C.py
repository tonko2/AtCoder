import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
H = na()
max_v = 0
for i in range(N):
    max_v = max(max_v, H[i])
    if max_v - H[i] > 1:
        print("No")
        exit()
print("Yes")