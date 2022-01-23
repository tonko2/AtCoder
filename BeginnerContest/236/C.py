N, M = map(int, input().split())
S = list(map(str, input().split()))
T = set(list(map(str, input().split())))

for s in S:
    if s in T:
        print("Yes")
    else:
        print("No")