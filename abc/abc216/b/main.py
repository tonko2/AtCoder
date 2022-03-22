N = int(input())
C = set()
for _ in range(N):
    S, T = map(str, input().split())
    C.add(tuple([S, T]))

if len(C) == N:
    print("No")
else:
    print("Yes")