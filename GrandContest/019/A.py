import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

Q, H, S, D = na()
N = ni()
A = [4*Q, 2*H, S]
A.sort()
ans = 0
if D // 2 < A[0]:
    ans = (N // 2) * D
    N %= 2
ans += N * A[0]
print(ans)
