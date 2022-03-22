N, M = map(int, input().split())
foods = [0] * 31
ans = 0
for i in range(N):
    A = list(map(int, input().split()))[1:]
    for a in A:
        foods[a] += 1
        if foods[a] == N:
            ans += 1
print(ans)
