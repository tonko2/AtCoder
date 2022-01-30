N = int(input())
B = list(map(int, input().split()))
R = list(map(int, input().split()))
ans = 0
for i in range(N):
    ans += (1 / N) * B[i] + (1 / N) * R[i]
print(ans)