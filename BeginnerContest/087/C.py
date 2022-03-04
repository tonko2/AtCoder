import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
A1 = na()
A2 = na()
A1_sum = [0] * (N + 1)
A2_sum = [0] * (N + 1)
for i in range(N):
    A1_sum[i + 1] = A1_sum[i] + A1[i]
    A2_sum[i + 1] = A2_sum[i] + A2[i]

ans = 0
for i in range(N):
    ans = max(ans, A1_sum[i + 1] + A2_sum[N] - A2_sum[i])
print(ans)