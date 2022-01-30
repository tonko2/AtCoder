MOD = 100
N = int(input())
A = list(map(int, input().split()))
print(sum(A) % MOD)