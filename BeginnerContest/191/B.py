N, X = map(int, input().split())
A = list(map(int, input().split()))
ans = []
for x in A:
    if x != X:
        ans.append(str(x))
print(" ".join(ans))

