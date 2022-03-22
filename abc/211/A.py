import sys
input = lambda: sys.stdin.readline().rstrip()

A, B = map(int, input().split())
C = (A - B) / 3 + B

print(C)