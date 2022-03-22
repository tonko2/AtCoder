K, S = map(int, input().split())
ans = 0
for i in range(0, K + 1):
    for j in range(0, K + 1):
        if 0 <= S - (i + j) <= K:
            ans += 1
print(ans)