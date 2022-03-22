N = int(input())
d = dict()
for i in range(N - 1):
    a, b = map(int, input().split())
    d[a] = d.get(a, 0) + 1
    d[b] = d.get(b, 0) + 1

for i in range(N):
    if d[i + 1] == N - 1:
        print("Yes")
        exit()
print("No")