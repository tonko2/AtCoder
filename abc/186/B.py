H, W = map(int, input().split())

grid = []
min_value = 1e9
for i in range(H):
    l = list(map(int, input().split()))
    grid.append(l)
    min_value = min(min_value, min(l))

ans = 0
for i in range(H):
    for j in range(W):
       ans += grid[i][j] - min_value

print(ans)