N = int(input())
A = list(map(int, input().split()))
print(-(-sum(A) // (N - A.count(0))))