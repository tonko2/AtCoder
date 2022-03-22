import sys
input = lambda: sys.stdin.readline().rstrip()

S, T = map(str, input().split())

if S < T:
    print('Yes')
else:
    print('No')