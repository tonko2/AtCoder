N, X = map(int, input().split())
d = dict()
d[X] = 1
ans = 1

A = list(map(int, input().split()))

flag = True
while flag:
    flag = False
    if d.get(A[X-1], 0) == 0:
        d[A[X-1]] = 1
        X = A[X-1]
        ans += 1
        flag = True

print(ans)
