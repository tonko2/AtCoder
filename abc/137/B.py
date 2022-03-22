K, X = map(int, input().split())

ans = []
for i in range(X-K+1, X+K):
    ans.append(i)
print(*ans)