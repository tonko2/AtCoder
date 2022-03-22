N, M = map(int, input().split())
P = []
for _ in range(N):
    a, b = map(int, input().split())
    P.append((a, b))
P2 = []
for _ in range(M):
    a, b = map(int, input().split())
    P2.append((a, b))

for i, (x, y) in enumerate(P):
    dis = 1e10
    ans = 1
    for j, (x2, y2) in enumerate(P2):
        new_dis = abs(x - x2) + abs(y2 - y)
        if dis > new_dis:
            dis = new_dis
            ans = j + 1
    print(ans)
