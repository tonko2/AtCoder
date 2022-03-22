N = int(input())

ans = 0
X = [None] * N
Y = [None] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())

for i in range(N-1):
    for j in range(i+1, N):
        x1, y1 = X[i], Y[i]
        x2, y2 = X[j], Y[j]
        if -1 <= (y2 - y1) / (x2 - x1) <= 1:
            ans += 1

print(ans)
