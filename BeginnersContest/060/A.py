A, B, C = map(str, input().split())

A = list(map(str, A))
B = list(map(str, B))
C = list(map(str, C))

if A[len(A) - 1] == B[0] and B[len(B) - 1] == C[0]:
    print("YES")
else:
    print("NO")