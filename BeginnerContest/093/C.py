import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

A, B, C = na()
ans = 0
A, B, C = sorted([A, B, C])
ans += (C - B) // 2
ans += (C - A) // 2
B += 2 * ((C - B) // 2)
A += 2 * ((C - A) // 2)
A, B, C = sorted([A, B, C])
if A == B and B == C:
    pass
elif A == B:
    ans += 1
else:
    ans += 2
print(ans)