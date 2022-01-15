N = int(input())
S = set()
for i in range(N):
    x = list(map(int, input().split()))
    S.add(tuple(x))

print(len(S))