import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
A = na()
ans = 0
for i in range(N):
    cnt = 0
    while A[i] % 2 == 0:
        A[i] //= 2
        cnt += 1
    ans += cnt
print(ans)