N = int(input())
K = int(input())

ans = 1e8
def dfs(total, n):
    global ans
    if n == N:
        ans = min(ans, total)
        return
    dfs(total * 2, n + 1)
    dfs(total + K, n + 1)

dfs(1, 0)

print(ans)