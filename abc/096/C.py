import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

H, W = na()
canvas = []
for _ in range(H):
    canvas.append(ns())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(H):
    for j in range(W):
        if canvas[i][j] == '.':
            continue
        flag = False
        for k in range(4):
            x = j + dx[k]
            y = i + dy[k]
            if x >= 0 and y >= 0 and x < W and y < H and canvas[y][x] == '#':
                flag = True
        if flag == False:
            print("No")
            exit()
print("Yes")
