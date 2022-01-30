N = int(input())
A = list(map(int, input().split()))
d = dict()
for a in A:
    d[a] = d.get(a, 0) + 1
print(d.get(100, 0) * d.get(400, 0) + d.get(200, 0) * d.get(300, 0))