N, M, X = map(int, input().split())
A = list(map(int, input().split()))
grid = [0] * (N + 1)
for a in A:
    grid[a-1] = 1

print(min(sum(grid[:X]), sum(grid[X:])))