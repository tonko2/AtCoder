N, S = map(int, input().split())
A = list(map(int, input().split()))
cards = [False] * (S + 1)
cards[0] = True
for i in range(N):
    for j in range(S, -1, -1):
        if j - A[i] >= 0:
            if cards[j - A[i]]:
                cards[j] = True
if cards[S]:
    print("Yes")
else:
    print("No")