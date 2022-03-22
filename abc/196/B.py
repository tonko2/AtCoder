import sys

input = sys.stdin.readline()

S = input
if S.count(".") == 0:
    print(S)
else:
    print(S.split(".")[0])
