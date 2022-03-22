import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
A = na()
if A.count(1) == 0:
    print(-1)
    exit()
l = 0
ans = float('inf')
while l < N:
    if A[l] != 1:
        l += 1
        continue
    r = l + 1
    cnt = 1
    while r < N and A[r] != 1:
        if A[r] == cnt + 1:
            cnt += 1
        r += 1
    l = r
    ans = min(ans, N - cnt)
print(ans)