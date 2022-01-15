N = int(input())
A = list(map(int, input().split()))
ranking = [[A[i], i + 1] for i in range(N)]
ranking.sort()

print(ranking[-2][1])
