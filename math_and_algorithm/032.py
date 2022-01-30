from bisect import *

N, X = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
index = bisect_left(A, X)
if index < N and A[index] == X:
    print("Yes")
else:
    print("No")