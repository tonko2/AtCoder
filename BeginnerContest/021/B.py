N = int(input())
a, b = map(int, input().split())
K = int(input())
S = {a, b}
P = list(map(int, input().split()))
for p in P:
    S.add(p)
if len(S) == 2 + K:
    print("YES")
else:
    print("NO")
