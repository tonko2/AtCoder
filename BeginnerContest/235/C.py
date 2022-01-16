from collections import defaultdict

N, Q = map(int, input().split())
A = list(map(str, input().split()))

B = defaultdict(list)
for i in range(len(A)):
    B[int(A[i])].append(i + 1)

for i in range(Q):
    x, k = map(int, input().split())
    if len(B[x]) >= k:
        print(B[x][k - 1])
    else:
        print(-1)
