import math

N = int(input())
X = [0] * N
Y = [0] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())
ans = float('inf')
for i in range(N):
    for j in range(i+1, N):
        d = math.sqrt((X[j] - X[i]) ** 2 + (Y[j] - Y[i]) ** 2)
        ans = min(ans, d)
print(ans)