N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0

def dfs(n, costV, costC):
    global ans, V, C

    if n == N:
        ans = max(ans, costV - costC)
        return
    dfs(n + 1, costV, costC)
    dfs(n + 1, costV + V[n], costC + C[n])

dfs(0, 0, 0)

print(ans)