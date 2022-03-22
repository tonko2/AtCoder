import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

C = []
for i in range(3):
    C.append(na())

for i in range(2):
    for j in range(2):
        if C[i][j] - C[i][j + 1] != C[i + 1][j] - C[i + 1][j + 1]:
            print("No")
            exit()
print("Yes")

