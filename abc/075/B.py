H, W = map(int, input().split())
field = [input() for _ in range(H)]
cnt = [[0] * W for _ in range(H)]

dx = [1, -1, 0, 0, 1, -1, -1, 1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]

for i in range(H):
    for j in range(W):
        for k in range(8):
            if field[i][j] == '.':
                continue
            nx = j + dx[k]
            ny = i + dy[k]
            if nx >= 0 and ny >= 0 and nx < W and ny < H:
                cnt[ny][nx] += 1

for i in range(H):
    out = ''
    for j in range(W):
        if field[i][j] == '#':
            out += '#'
        else:
            out += str(cnt[i][j])
    print(out)
