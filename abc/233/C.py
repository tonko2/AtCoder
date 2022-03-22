N, X = map(int, input().split())

lists = []
for i in range(N):
    a = list(map(int, input().split()))
    lists.append(a[1:])

ans = 0
def dfs(n, total):
    global ans
    if n == N and total == X:
       ans += 1
    if n >= N:
        return
    for x in lists[n]:
        dfs(n + 1, total * x)

for i in range(len(lists[0])):
    dfs(1, lists[0][i])

print(ans)

