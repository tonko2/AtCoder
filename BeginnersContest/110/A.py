A = list(map(str, input().split()))
A = sorted(A, reverse=True)
print(int(A[0] + A[1]) + int(A[2]))
