A, B = map(int, input().split())

print(max(A - 1, B) + max(A, B - 1))