import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

S = ns()
S_black = []
S_white = []
for i in range(len(S)):
    if i % 2 == 0:
        S_black.append('0')
        S_white.append('1')
    else:
        S_black.append('1')
        S_white.append('0')

diff_1 = 0
diff_2 = 0
for i in range(len(S)):
    if S[i] != S_black[i]:
        diff_1 += 1
    if S[i] != S_white[i]:
        diff_2 += 1
print(min(diff_1, diff_2))