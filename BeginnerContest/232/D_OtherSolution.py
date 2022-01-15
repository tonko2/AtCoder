import collections
import sys

input = lambda: sys.stdin.readline().rstrip()

h, w = map(int, input().split())

grid = [list(input()) for _ in range(h)]
q = collections.deque()
q.append((0,0))
grid[0][0] = 1
ans = 0

while q:
    y, x = q.popleft()
    dis = 0
    if 0 <= y+1 < h and grid[y+1][x] == '.':
        dis = 1
        grid[y+1][x] = grid[y][x] + 1
        q.append((y+1, x))
    if 0 <= x+1 < w and grid[y][x+1] == '.':
        dis = 1
        grid[y][x+1] = grid[y][x] + 1
        q.append((y, x+1))

    ans = max(ans, grid[y][x])

print(ans)