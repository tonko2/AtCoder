N = int(input())
P = list(map(int, input().split()))
sorted_P = sorted(P)
cnt = 0
for i in range(N):
    if P[i] != sorted_P[i]:
       cnt += 1
if cnt <= 2:
    print("YES")
else:
    print("NO")
