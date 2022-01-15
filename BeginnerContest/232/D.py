H, W = map(int, input().split())

grid = [input() for _ in range(H)]
grid_int = [[0] * (W + 1) for _ in range(H + 1)]

for h in range(H-1, -1, -1):
    for w in range(W-1, -1, -1):
        if grid[h][w] == '#':
            continue
        grid_int[h][w] = max(grid_int[h+1][w], grid_int[h][w+1]) + 1

print(grid_int[0][0])