N = int(input())
A = [int(input()) for _ in range(N)]
S = set()
now = 1
cnt = 1
while now not in S:
    S.add(now)
    now = A[now-1]
    if now == 2:
        print(cnt)
        exit()
    cnt += 1
print(-1)