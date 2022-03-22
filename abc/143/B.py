N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(0, N):
    for j in range(i+1, N):
       ans += A[i] * A[j]
print(ans)
