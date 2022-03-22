A, B, K = map(int, input().split())

s = set([A, B])

for i in range(1, K):
    if A <= A + i <= B:
        s.add(A + i)
    if A <= B - i <= B:
        s.add(B - i)

s = sorted(s)
for x in s:
    print(x)