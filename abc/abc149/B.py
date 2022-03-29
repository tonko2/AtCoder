A, B, K = map(int, input().split())

A, K = max(A - A, A - K), max(0, K - A)
B = max(0, B - K)

print(f'{A} {B}')