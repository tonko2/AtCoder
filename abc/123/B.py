def dfs(used, total):
    global ans, A
    if False not in used:
        ans = min(ans, total)
        return
    for i in range(5):
        if used[i] == False:
            used[i] = True
            if False not in used:
                dfs(used, total + A[i])
            else:
                dfs(used, total + A[i] + (10 - A[i] % 10) % 10)
            used[i] = False

A = [int(input()) for i in range(5)]
ans = 10000
used = [False] * 5
dfs(used, 0)
print(ans)
