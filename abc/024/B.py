N, T = map(int, input().split())
A = [int(input()) for _ in range(N)]
start = A[0]
open = 0
index = 0
ans = 0
for i in range(0, N - 1):
    if start + open + T <= A[i + 1]:
        ans += open + T
        start = A[i + 1]
        open = 0
    else:
        open = A[i + 1] - start
ans += open + T
print(ans)