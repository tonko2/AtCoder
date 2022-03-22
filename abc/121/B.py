N, M, C = map(int, input().split())
B = list(map(int, input().split()))
ans = 0
for i in range(N):
    A = list(map(int, input().split()))
    total = 0
    for i, a in enumerate(A):
        total += A[i] * B[i]
    if total + C > 0:
        ans += 1
print(ans)