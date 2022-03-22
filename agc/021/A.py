import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

S = ns()
ans = 0
for s in S:
    ans += ord(s) - ord('0')
ans2 = 9 * (len(S) - 1) + ord(S[0]) - ord('0') - 1
print(max(ans, ans2))
