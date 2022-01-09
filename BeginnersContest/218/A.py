import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
S = input()

if S[N-1] == 'o':
    print('Yes')
else:
    print('No')