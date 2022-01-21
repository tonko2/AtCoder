N = int(input())
W = list(map(int, input().split()))
ans = 1e7

for t in range(0, N):
    left = 0
    right = 0
    for i, x in enumerate(W):
        if i <= t:
            left += x
        else:
            right += x
    ans = min(ans, abs(left - right))

print(ans)
