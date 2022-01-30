N, W = map(int, input().split())
w = [0] * N
v = [0] * N
for i in range(N):
    w[i], v[i] = map(int, input().split())

dp = [0] * (W + 1)

for i in range(N):
    for j in range(W, 0, -1):
        if j - w[i] >= 0:
            dp[j] = max(dp[j], dp[j - w[i]] + v[i])

ans = 0
for i in range(1, W+1):
    ans = max(ans, dp[i])
print(ans)
