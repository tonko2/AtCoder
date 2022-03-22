A, B, C, D = map(int, input().split())

turn = 0
while A > 0 and C > 0:
    if turn == 0:
        C -= B
    else:
        A -= D
    turn = 1 - turn

if A <= 0:
    print("No")
else:
    print("Yes")