N = int(input())
A = [list(map(int, input().split())) for _ in range(2 * N - 1)]
used = [False] * (2 * N)

ans = 0
def dfs(n, total):
    if n == N:
        global ans
        ans = max(ans, total)
        return

    for i in range(2 * N):
        if not used[i]:
            used[i] = True
            break
    for j in range(i + 1, 2 * N):
        if not used[j]:
            used[j] = True
            dfs(n + 1, total ^ A[i][j - i - 1])
            used[j] = False
    used[i] = False

dfs(0, 0)
print(ans)
