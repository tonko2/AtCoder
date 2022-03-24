import math

N, D = map(int, input().split())
X = []

def get_dis(a, b):
    n = len(a)
    res = 0
    for i in range(n):
        res += abs(a[i] - b[i]) ** 2
    return res ** 0.5

for i in range(N):
    X.append(list(map(int, input().split())))

ans = 0
for i in range(N):
    for j in range(i+1, N):
        dis = get_dis(X[i], X[j])
        if dis == math.ceil(dis):
            ans += 1
print(ans)

