N = int(input())
A = list(map(int, input().split()))
ans = 0

def dfs(n, total, pos):
    global ans
    if n == 5:
        if total == 1000:
            ans += 1
        return
    if total > 1000 or pos >= N:
        return
    dfs(n + 1, total + A[pos], pos + 1)
    dfs(n, total, pos + 1)
dfs(0, 0, 0)
print(ans)