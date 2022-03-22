N, M, T = map(int, input().split())

max_N = N
time = 0
for i in range(M):
    s, t = map(int, input().split())
    N -= s - time
    time = t
    if N <= 0:
        print("No")
        exit()
    N = min(N + t - s, max_N)

N -= T - time

if N <= 0:
    print("No")
else:
    print("Yes")
