import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, M = na()
AB = []
for _ in range(N):
    a, b = na()
    AB.append((a, b))
AB.sort()

ans = 0
for (a, b) in AB:
    if M == 0:
        break
    ans += a * min(b, M)
    M -= min(b, M)
print(ans)