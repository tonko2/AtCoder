N = int(input())
K = int(input())
X = list(map(int, input().split()))

ans = 0
for x in X:
    ans += min(abs(K - x) * 2, x * 2)
print(ans)