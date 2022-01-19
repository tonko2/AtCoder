N = 10
cost = [[float('inf')] * N] * N

for k in range(N):
    for i in range(N):
        for j in range(N):
            if cost[i][k] != float('inf') and cost[k][j] != float('inf'):
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

