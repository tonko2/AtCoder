N = int(input())
T, X, Y = [], [], []
for i in range(N):
    t, x, y = map(int, input().split())
    T.append(t)
    X.append(x)
    Y.append(y)

x, y, t = 0, 0, 0
for i in range(N):
    dis = abs(x - X[i]) + abs(y - Y[i])
    if dis <= T[i] - t and (T[i] - t - dis) % 2 == 0:
        x = X[i]
        y = Y[i]
        t = T[i]
    else:
        print('No')
        exit()

print('Yes')