H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
for a in list(zip(*A)):
    print(*list(a))