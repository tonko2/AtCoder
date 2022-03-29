W, H, N = map(int, input().split())
field = [[False] * W for _ in range(H)]

for _ in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        for i in range(H):
            for j in range(0, x):
                field[i][j] = True
    if a == 2:
        for i in range(H):
            for j in range(x, W):
                field[i][j] = True

    if a == 3:
        for i in range(H - y, H):
            for j in range(W):
                field[i][j] = True

    if a == 4:
        for i in range(0, H - y):
            for j in range(W):
                field[i][j] = True

ans = 0
for i in range(H):
    ans += field[i].count(False)
print(ans)