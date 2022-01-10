A, B, C = map(int, input().split())
C -= max(A - B, 0)
print(max([0, C]))