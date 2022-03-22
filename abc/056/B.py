W, a, b = map(int, input().split())
print(max(0, max(b - (a + W), a - (b + W))))