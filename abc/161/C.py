import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N, K = na()
N %= K
ans = N
S = set()
while not N in S:
    S.add(N)
    N = abs(N - K)
    ans = min(ans, N)
print(ans)