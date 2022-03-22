N = int(input())
S = [input() for _ in range(N)]
S_90 = (list(zip(*S)))
for i in range(N):
    print("".join(S_90[i][::-1]))