N, M = map(int, input().split())
A = list(map(int, input().split()))
total = sum(A)
cnt = 0
for a in A:
    if -(-total // (4 * M)) <= a:
        cnt += 1

if cnt >= M:
    print("Yes")
else:
    print("No")