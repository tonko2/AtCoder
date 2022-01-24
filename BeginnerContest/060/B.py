A, B, C = map(int, input().split())
S = set()
tmp_A = A
while A % B not in S:
    if A % B == C:
        print("YES")
        exit()
    S.add(A % B)
    A += tmp_A
print("NO")