S, T = map(str, input().split())
A, B = map(int, input().split())
U = input()
if S == U:
    A -= 1
else:
    B -= 1
print(f'{A} {B}')