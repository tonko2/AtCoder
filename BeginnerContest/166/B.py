N, K = map(int, input().split())
S = set()
for i in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    for a in A:
        S.add(a)
print(N - len(S))