import math

N = int(input())
X = [0] * N
Y = [0] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        x1, y1, x2, y2 = X[i], Y[i], X[j], Y[j]
        ans = max(ans, math.sqrt(abs(x1 - x2) ** 2  + abs(y1 - y2) ** 2))

print(ans)

