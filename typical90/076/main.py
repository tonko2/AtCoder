import sys
from collections import defaultdict
import bisect

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
A = na()

if sum(A) % 10 != 0:
    print("No")
    exit()

B = [0] * (2 * N + 1)
for i in range(N):
    B[i + 1] = B[i] + A[i]
for i in range(N):
    B[i + N + 1] = B[i + N] + A[i]

for i in range(N):
    goal = B[i] + B[N] // 10
    pos1 = bisect.bisect(B, goal) - 1
    if B[pos1] == goal:
        print("Yes")
        exit()
print("No")


