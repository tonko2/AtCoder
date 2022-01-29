x1, y1, x2, y2 = map(int, input().split())
dx = x2 - x1
dy = y2 - y1
ans = []
for i in range(2):
    dx, dy = -dy, dx
    x2 += dx
    y2 += dy
    ans.append(x2)
    ans.append(y2)
print(*ans)
