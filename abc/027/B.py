N = int(input())
A = list(map(int, input().split()))

if sum(A) % N != 0:
    print(-1)
    exit()

total = 0
ans = 0
land = 1
for a in A:
    total += a
    if total % land == 0 and total // land == sum(A) // N:
        total = 0
        land = 1
    else:
        ans += 1
        land += 1
print(ans)
