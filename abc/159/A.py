N, M = map(int, input().split())
n, m = 0, 0

if N >= 2:
    n = N * (N-1) / 2
if M >= 2:
    m = M * (M-1) / 2

print(int(n + m))