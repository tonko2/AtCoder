import math

N = int(input())
ans = 0
A = [int(input()) for _ in range(N)]
A.sort(reverse=True)
for i in range(N):
    if i % 2 == 1:
        ans -= A[i] ** 2
    else:
        ans += A[i] ** 2
print(ans * math.pi)