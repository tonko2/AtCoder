N = int(input())
A = set([int(input()) for _ in range(N)])
A = sorted(A)
print(A[-2])
