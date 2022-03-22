H, W, Y, X = map(int, input().split())
X -= 1
Y -= 1
field = []
for i in range(H):
    field.append(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = 1
for i in range(4):
    nx = X + dx[i]
    ny = Y + dy[i]
    while 0 <= nx < W and 0 <= ny < H and field[ny][nx] == '.':
        nx += dx[i]
        ny += dy[i]
        ans += 1

print(ans)