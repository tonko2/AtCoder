import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

R, G, B, N = na()
ans = 0
for r in range(3001):
    if R * r > N:
        continue
    for g in range(3001):
        if R * r + G * g > N:
            continue
        if (N - (R * r + G * g)) % B == 0:
            ans += 1
print(ans)

