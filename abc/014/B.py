n, X = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
ans = 0
while X and cnt < n:
    if X & 1:
       ans += A[cnt]
    cnt += 1
    X >>= 1
print(ans)