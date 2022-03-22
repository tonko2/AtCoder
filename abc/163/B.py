N, M = map(int, input().split())
A = list(map(int, input().split()))
days = N - sum(A)
if days < 0:
    print(-1)
else:
    print(days)