import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
A = [ni() for _ in range(N)]
A.sort()
total = sum(A)
if total % 10 != 0:
    print(total)
    exit()
for a in A:
    if a % 10 != 0:
        print(total - a)
        exit()
print(0)