N = int(input())
d = [0] * 100010
for i in range(N):
    l, r = map(int, input().split())
    d[l] += 1
    d[r+1] -= 1
cnt = 0

for i in range(1, 100010):
    d[i] += d[i-1]
    if d[i] > 0:
        cnt += 1
print(cnt)
