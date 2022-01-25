N = int(input())
T = list(map(int, input().split()))
M = int(input())
total = sum(T)
for i in range(M):
    p, x = map(int, input().split())
    print(total - T[p - 1] + x)