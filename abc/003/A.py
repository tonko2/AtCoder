N = int(input())

ans = 0
for i in range(N):
    ans += (10000 * (i + 1)) / N
print(int(ans))