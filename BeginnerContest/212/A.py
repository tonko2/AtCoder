import sys
input = lambda: sys.stdin.readline().rstrip()

A, B = map(int, input().split())

if 0 < A and B == 0:
    print('Gold')
elif A == 0 and 0 < B:
    print('Silver')
else:
    print('Alloy')
