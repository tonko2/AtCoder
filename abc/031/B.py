L, H = map(int, input().split())
N = int(input())
for _ in range(N):
    a = int(input())
    if a < L:
        print(L - a)
    elif L <= a <= H:
        print(0)
    else:
        print(-1)