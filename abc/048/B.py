a, b, x = map(int, input().split())
print(max(0, b // x - (a - 1) // x))