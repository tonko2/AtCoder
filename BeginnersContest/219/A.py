import sys
input = lambda: sys.stdin.readline().rstrip()

X = int(input())

if X >= 90:
    print('expert')
elif 0 <= X < 40:
    print(40 - X)
elif 40 <= X < 70:
    print(70 - X)
else:
    print(90 - X)