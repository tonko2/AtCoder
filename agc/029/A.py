import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

S = ns()
ans = 0
tmp = 0
for c in S:
    if c == 'B':
        tmp += 1
    else:
        ans += tmp
print(ans)


