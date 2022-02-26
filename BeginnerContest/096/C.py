import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

A, B, C, X, Y = na()
ans = 0
if (A + B) // 2 >= C:
    ans += min(X, Y) * C * 2
    if X > Y:
        ans += min((X - Y) * C * 2, (X - Y) * A)
    if X < Y:
        ans += min((Y - X) * C * 2, (Y - X) * B)
else:
    ans += X * A + Y * B

print(ans)