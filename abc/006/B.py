MOD = 10007
n = int(input())
A = [0] * (n + 3)
A[1] = 0
A[2] = 0
A[3] = 1
for i in range(4, n+1):
    A[i] = int((A[i-1] + A[i-2] + A[i-3]) % MOD)
print(A[n])
